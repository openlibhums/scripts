// @ts-check
/**
 * Build a markdown summary report from axe-general teardown output.
 * One section per rule: heading, help text, tags, then a URL × browser violations table.
 */

/** Wrap angle-bracket tag-like text in backticks so markdown previewers don't treat it as HTML. */
function mdAngleBrackets(str) {
  if (typeof str !== 'string') return '';
  return str.replace(/<([^>]+)>/g, '`<$1>`');
}

/**
 * Find the longest common URL prefix that ends at a path boundary (/)
 * so table cells show only the distinctive path segment.
 */
function commonUrlRoot(urls) {
  if (urls.length === 0) return '';
  let prefix = urls[0];
  for (let i = 1; i < urls.length; i++) {
    while (!urls[i].startsWith(prefix) && prefix.length) prefix = prefix.slice(0, -1);
  }
  const lastSlash = prefix.lastIndexOf('/');
  return lastSlash >= 0 ? prefix.slice(0, lastSlash + 1) : prefix;
}

/** Return the path segment of url after root; use '/' when it is the root itself. */
function shortUrl(root, url) {
  const suffix = root && url.startsWith(root) ? url.slice(root.length) : url;
  return suffix || '/';
}

/** Generate a stable anchor ID from a short URL path. */
function urlAnchor(short) {
  return 'url-' + short.replace(/[^a-z0-9]+/gi, '-').replace(/^-+|-+$/g, '').toLowerCase() || 'url-root';
}

/** Violation count cell: checkmark for zero, number otherwise. */
function cell(n) {
  return n === 0 ? ':white_check_mark:' : String(n);
}

/** Extract the test_date from the first browser entry found in the output. */
function extractTestDate(output) {
  for (const rule of output) {
    for (const urlEntry of rule.urls) {
      for (const browserData of Object.values(urlEntry.browsers)) {
        if (browserData.test_date) return browserData.test_date;
      }
    }
  }
  return '';
}

/** Sum all violations across all URLs and browsers for a rule. */
function totalViolations(rule) {
  return rule.urls.reduce(
    (sum, urlEntry) =>
      sum + Object.values(urlEntry.browsers).reduce((s, b) => s + b.violations, 0),
    0
  );
}

/**
 * Build the markdown report from axe-general teardown output.
 * @param {Array<{id: string, help: string, tags: string[], urls: Array<{url: string, browsers: Record<string, {test_date: string, violations: number}>}>}>} output
 * @returns {string}
 */
function buildGeneralMarkdown(output) {
  const testDate = extractTestDate(output);
  const allUrls = [...new Set(output.flatMap((r) => r.urls.map((u) => u.url)))].sort();
  const urlRoot = commonUrlRoot(allUrls);

  const lines = [
    '# Axe general accessibility report',
    '',
    `**Test date:** ${testDate}`,
    '',
    '| Rule | Description | Tags | Results |',
    '| --- | --- | --- | --- |',
  ];

  for (const rule of output) {
    const total = totalViolations(rule);
    const desc = mdAngleBrackets(rule.help).replace(/\|/g, '\\|');
    const tags = rule.tags.map((t) => `\`${t}\``).join(', ');
    const results = total === 0 ? ':white_check_mark:' : `[${total}](#${rule.id})`;
    lines.push(`| ${rule.id} | ${desc} | ${tags} | ${results} |`);
  }

  lines.push('');

  // Second summary: URLs × browsers
  const allBrowsers = [...new Set(
    output.flatMap((r) => r.urls.flatMap((u) => Object.keys(u.browsers)))
  )].sort();

  // Build a map: url → browser → total violations across all rules
  /** @type {Map<string, Map<string, number>>} */
  const urlBrowserTotals = new Map();
  for (const rule of output) {
    for (const urlEntry of rule.urls) {
      if (!urlBrowserTotals.has(urlEntry.url)) urlBrowserTotals.set(urlEntry.url, new Map());
      const browserMap = urlBrowserTotals.get(urlEntry.url);
      for (const [browser, data] of Object.entries(urlEntry.browsers)) {
        browserMap.set(browser, (browserMap.get(browser) || 0) + data.violations);
      }
    }
  }

  lines.push(`| URL | ${allBrowsers.join(' | ')} |`, `| --- |${allBrowsers.map(() => ' --- |').join('')}`);
  for (const url of allUrls) {
    const browserMap = urlBrowserTotals.get(url) || new Map();
    const short = shortUrl(urlRoot, url);
    const hasViolations = [...(browserMap.values())].some((n) => n > 0);
    const urlCell = hasViolations ? `[${short}](#${urlAnchor(short)})` : short;
    const cells = allBrowsers.map((b) => cell(browserMap.get(b) || 0));
    lines.push(`| ${urlCell} | ${cells.join(' | ')} |`);
  }

  lines.push('');

  // Detail tables only for rules with at least one violation
  for (const rule of output.filter((r) => totalViolations(r) > 0)) {
    const browsers = rule.urls.length > 0 ? Object.keys(rule.urls[0].browsers).sort() : [];

    lines.push(`## ${rule.id}`, '');
    lines.push(mdAngleBrackets(rule.help), '');
    lines.push(`Tags: ${rule.tags.map((t) => `\`${t}\``).join(', ')}`, '');

    const header = `| URL | ${browsers.join(' | ')} | Total |`;
    const sep = `| --- |${browsers.map(() => ' --- |').join('')} --- |`;
    lines.push(header, sep);

    for (const urlEntry of rule.urls) {
      const counts = browsers.map((b) => urlEntry.browsers[b]?.violations ?? 0);
      const rowTotal = counts.reduce((s, n) => s + n, 0);
      if (rowTotal === 0) continue;
      const urlLabel = shortUrl(urlRoot, urlEntry.url);
      const cells = counts.map((n) => cell(n));
      lines.push(`| ${urlLabel} | ${cells.join(' | ')} | ${cell(rowTotal)} |`);
    }

    lines.push('');
  }

  // Second detail set: one section per URL, rows are rules
  // Build url → rule → browsers map (only where violations exist)
  /** @type {Map<string, Map<string, Record<string, {violations: number}>>>} */
  const urlRuleMap = new Map();
  for (const rule of output) {
    for (const urlEntry of rule.urls) {
      const urlTotal = Object.values(urlEntry.browsers).reduce((s, b) => s + b.violations, 0);
      if (urlTotal === 0) continue;
      if (!urlRuleMap.has(urlEntry.url)) urlRuleMap.set(urlEntry.url, new Map());
      urlRuleMap.get(urlEntry.url).set(rule.id, urlEntry.browsers);
    }
  }

  for (const url of allUrls) {
    const ruleMap = urlRuleMap.get(url);
    if (!ruleMap) continue;

    const short = shortUrl(urlRoot, url);
    lines.push(`<span id="${urlAnchor(short)}"></span>`, `## ${short}`, '');

    const header = `| Rule | ${allBrowsers.join(' | ')} | Total |`;
    const sep = `| --- |${allBrowsers.map(() => ' --- |').join('')} --- |`;
    lines.push(header, sep);

    for (const [ruleId, browsers] of [...ruleMap.entries()].sort(([a], [b]) => a.localeCompare(b))) {
      const counts = allBrowsers.map((b) => browsers[b]?.violations ?? 0);
      const rowTotal = counts.reduce((s, n) => s + n, 0);
      const cells = counts.map((n) => cell(n));
      lines.push(`| ${ruleId} | ${cells.join(' | ')} | ${cell(rowTotal)} |`);
    }

    lines.push('');
  }

  return lines.join('\n');
}

module.exports = { buildGeneralMarkdown };
