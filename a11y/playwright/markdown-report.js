// @ts-check
/**
 * Build a markdown accessibility report from merged axe results.
 */

/** Wrap angle-bracket tag-like text in backticks so markdown previewers don't treat it as HTML. */
function mdAngleBrackets(str) {
  if (typeof str !== 'string') return '';
  return str.replace(/<([^>]+)>/g, '`<$1>`');
}

/** Empty string for 0, so table cells are blank where there are no violations. */
function cell(n) {
  return n === 0 ? '' : String(n);
}

/**
 * Find the longest common URL prefix that ends at a path boundary (/) so headings
 * use only the part beyond the root and are not full URLs (avoids linkification and TOC issues).
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

/** Return the part of url after root for use as a heading; use "Results" when the path is the root. */
function shortUrlHeading(root, url) {
  const suffix = root && url.startsWith(root) ? url.slice(root.length) : url;
  const pathPart = suffix || '/';
  return pathPart === '/' ? 'Results' : pathPart;
}

function summaryByUrlAndSeverity(allResults) {
  const lines = ['## Summary by URL', '', '| URL | Errors | Status |', '| --- | --- | --- |'];
  for (const { url, violations } of allResults) {
    const total = (violations || []).reduce((sum, v) => sum + (v.nodes || []).length, 0);
    const status = total > 0 ? ':x: fail' : ':white_check_mark: pass';
    lines.push(`| ${url} | ${cell(total)} | ${status} |`);
  }
  return lines.join('\n');
}

function buildByRule(allViolationsByUrl) {
  const byRule = {};
  const bySeverity = { critical: 0, serious: 0, moderate: 0, minor: 0 };
  for (const { violations } of allViolationsByUrl) {
    for (const v of violations) {
      if (!byRule[v.id]) byRule[v.id] = { critical: 0, serious: 0, moderate: 0, minor: 0 };
      const impact = v.impact && byRule[v.id].hasOwnProperty(v.impact) ? v.impact : 'serious';
      const count = (v.nodes || []).length;
      byRule[v.id][impact] += count;
      bySeverity[impact] += count;
    }
  }
  return { byRule, bySeverity };
}

/** One table: all rules run, with description, WCAG criteria, and violation counts; Status = pass/fail. */
function combinedRulesTable(rulesRun, byRule) {
  if (rulesRun.length === 0) return '';
  const lines = [
    '## Rules run and results',
    '',
    'All rules executed in this run (WCAG 2.2 Level A and AA, ACT). Status indicates whether the rule had any violations across the tested URLs.',
    '',
    '| Rule ID | Description | WCAG criteria | Errors | Status |',
    '| --- | --- | --- | --- | --- |',
  ];
  const sorted = [...rulesRun].sort((a, b) => a.id.localeCompare(b.id));
  for (const r of sorted) {
    const counts = byRule[r.id] || { critical: 0, serious: 0, moderate: 0, minor: 0 };
    const total = counts.critical + counts.serious + counts.moderate + counts.minor;
    const status = total > 0 ? ':x: fail' : ':white_check_mark: pass';
    const desc = (r.help || '').replace(/\|/g, '\\|').replace(/\n/g, ' ');
    const wcagCriteria = formatWcagCriteria(r.tags || []);
    const wcagCell = wcagCriteria.length > 0 ? wcagCriteria.map((c) => c.replace(/\|/g, '\\|')).join('; ') : '—';
    lines.push(`| ${r.id} | ${mdAngleBrackets(desc)} | ${wcagCell} | ${cell(total)} | ${status} |`);
  }
  return lines.join('\n');
}

const PREFIX_ANY = 'Fix any of the following:';
const PREFIX_ALL = 'Fix all of the following:';

/**
 * Normalize failure summary for markdown report only (JSON/TSV keep full text).
 * Strip "Fix any/all of the following:" prefix; collapse color-contrast and target-size variants to single summaries.
 */
function normalizeFailureSummaryForMarkdown(text) {
  let t = (text ?? '').trim();
  if (t.startsWith(PREFIX_ANY)) {
    t = t.slice(PREFIX_ANY.length).trim();
  } else if (t.startsWith(PREFIX_ALL)) {
    t = t.slice(PREFIX_ALL.length).trim();
  }
  if (t.startsWith('Element has insufficient color contrast of')) {
    return 'Element has insufficient color contrast.';
  }
  if (t.startsWith('Target has insufficient size') || t.startsWith('Target has insufficient space')) {
    return 'Target has insufficient size';
  }
  return t || '(no summary)';
}

/**
 * Build per-rule summary refs: byRule[ruleId] = unique summary texts in order; refMap["ruleId|summary"] = { label, anchorId };
 * refCount["ruleId|summary"] = number of failing nodes with that rule and summary.
 * ruleIdToTags[ruleId] = tags array from axe (for WCAG criteria in report).
 */
function buildSummaryRefs(allViolationsByUrl) {
  const byRule = {};
  const refCount = new Map();
  const ruleIdToTags = {};
  for (const { violations } of allViolationsByUrl) {
    for (const v of violations) {
      const ruleId = v.id;
      if (ruleId && v.tags && !ruleIdToTags[ruleId]) ruleIdToTags[ruleId] = v.tags;
      if (!byRule[ruleId]) byRule[ruleId] = [];
      for (const node of v.nodes || []) {
        const key = normalizeFailureSummaryForMarkdown(node.failureSummary);
        if (!byRule[ruleId].includes(key)) byRule[ruleId].push(key);
        const refKey = `${ruleId}|${key}`;
        refCount.set(refKey, (refCount.get(refKey) || 0) + 1);
      }
    }
  }
  const refMap = new Map();
  for (const ruleId of Object.keys(byRule)) {
    const summaries = byRule[ruleId];
    const useNumber = summaries.length > 1;
    summaries.forEach((key, i) => {
      const num = i + 1;
      const label = useNumber ? `Failure ${ruleId} ${num}` : `Failure ${ruleId}`;
      const anchorId = useNumber ? `${ruleId}-${num}` : ruleId;
      refMap.set(`${ruleId}|${key}`, { label, anchorId });
    });
  }
  return { byRule, refMap, refCount, ruleIdToTags };
}

/** Map axe level tags to short WCAG conformance labels. */
const WCAG_LEVEL_TAGS = {
  wcag2a: 'WCAG 2.0 Level A',
  wcag2aa: 'WCAG 2.0 Level AA',
  wcag2aaa: 'WCAG 2.0 Level AAA',
  wcag21a: 'WCAG 2.1 Level A',
  wcag21aa: 'WCAG 2.1 Level AA',
  wcag21aaa: 'WCAG 2.1 Level AAA',
  wcag22a: 'WCAG 2.2 Level A',
  wcag22aa: 'WCAG 2.2 Level AA',
  wcag22aaa: 'WCAG 2.2 Level AAA',
};

/**
 * Format axe rule tags as human-readable WCAG criteria only (conformance level + success criterion).
 * Includes only WCAG level tags (e.g. wcag2aa) and success criterion tags (e.g. wcag143);
 * excludes ACT, TT, EN-301-549, best-practice, section508, etc.
 */
function formatWcagCriteria(tags) {
  if (!Array.isArray(tags) || tags.length === 0) return [];
  const levels = [];
  const successCriteria = [];
  for (const tag of tags) {
    if (WCAG_LEVEL_TAGS[tag]) {
      levels.push(WCAG_LEVEL_TAGS[tag]);
    } else if (/^wcag(\d)(\d)(\d)$/.test(tag)) {
      const [, g, l, c] = tag.match(/^wcag(\d)(\d)(\d)$/);
      successCriteria.push(`Success Criterion ${g}.${l}.${c}`);
    }
  }
  const seen = new Set();
  return [...levels, ...successCriteria].filter((s) => s && !seen.has(s) && (seen.add(s), true));
}

/**
 * Strip "Fix any/all of the following:" from entire summary and format lines as an unordered list.
 */
function formatSummaryForDisplay(text) {
  let s = (text || '')
    .replace(/\s*Fix any of the following:\s*/gi, '\n')
    .replace(/\s*Fix all of the following:\s*/gi, '\n');
  const items = s
    .split(/\n/)
    .map((l) => l.trim())
    .filter(Boolean);
  if (items.length === 0) return '(no summary)';
  return items.map((l) => '- ' + mdAngleBrackets(l).replace(/\|/g, '\\|')).join('\n');
}

/** Render the failure summary reference section with ### rule-name (count) when disambiguation needed. */
function formatSummaryReference(byRule, refCount, ruleIdToTags) {
  const ruleIds = Object.keys(byRule).sort();
  if (ruleIds.length === 0) return '';
  const lines = ['## Failure summary reference', '', 'Each issue in the details below links to one of these summaries.', ''];
  for (const ruleId of ruleIds) {
    const summaries = byRule[ruleId];
    const useNumber = summaries.length > 1;
    const wcagCriteria = formatWcagCriteria(ruleIdToTags[ruleId] || []);
    for (let i = 0; i < summaries.length; i++) {
      const num = i + 1;
      const heading = useNumber ? `Failure ${ruleId} ${num}` : `Failure ${ruleId}`;
      const count = refCount.get(`${ruleId}|${summaries[i]}`) || 0;
      const headingWithCount = `${heading} (${count})`;
      const anchorId = useNumber ? `${ruleId}-${num}` : ruleId;
      const display = formatSummaryForDisplay(summaries[i]);
      lines.push(`<span id="${anchorId}"></span>`, `### ${headingWithCount}`, '');
      if (wcagCriteria.length > 0 && i === 0) {
        lines.push('**Related WCAG criteria:**', '', wcagCriteria.map((c) => `- ${c}`).join('\n'), '');
      }
      lines.push(display, '');
    }
  }
  return lines.join('\n');
}

/** Escape pipe and newline for markdown table cell content. */
function tableCell(s) {
  return String(s).replace(/\|/g, '\\|').replace(/\n/g, ' ').trim();
}

/** Build one table for all violations across all URLs; first column is Page (link to URL). */
function formatResultsTable(allViolationsByUrl, refMap, urlRoot) {
  const rows = [];
  for (const { url, violations } of allViolationsByUrl) {
    const pageHeading = shortUrlHeading(urlRoot, url);
    const pageLink = `[${pageHeading}](${url})`;
    for (const v of violations) {
      const ruleLink = `[${v.id}](${v.helpUrl})`;
      const impact = v.impact || '';
      for (const node of v.nodes || []) {
        const selector = Array.isArray(node.target) ? node.target.join(' ') : node.target;
        const key = normalizeFailureSummaryForMarkdown(node.failureSummary);
        const ref = refMap.get(`${v.id}|${key}`);
        const refLink = ref ? `[${ref.label}](#${ref.anchorId})` : '(see reference)';
        const htmlSnippet = node.html ? node.html.replace(/\s+/g, ' ').trim().slice(0, 200) + (node.html.length > 200 ? '…' : '') : '';
        rows.push([pageLink, ruleLink, impact, tableCell(selector), tableCell(htmlSnippet), refLink]);
      }
    }
  }
  if (rows.length === 0) return [];
  const tableHeader = '| Page | Rule | Impact | Selector | HTML | Issue ref |';
  const tableSep = '| --- | --- | --- | --- | --- | --- |';
  const tableRows = rows.map((r) => `| ${r[0]} | ${r[1]} | ${r[2]} | \`${r[3]}\` | \`${r[4]}\` | ${r[5]} |`);
  return [tableHeader, tableSep, ...tableRows, ''];
}

/**
 * Assemble and return the full markdown report string.
 * @param {Array<{url: string, violations: any[]}>} allResults
 * @param {Array<{url: string, violations: any[]}>} allViolationsByUrl
 * @param {any[]} rulesRun
 * @returns {string}
 */
function buildMarkdownReport(allResults, allViolationsByUrl, rulesRun) {
  const totalUrls = allResults.length;
  const urlsWithViolations = allViolationsByUrl.length;
  const urlsPassing = totalUrls - urlsWithViolations;
  const totalViolations = allViolationsByUrl.reduce((sum, { violations }) => sum + violations.length, 0);
  const totalNodes = allViolationsByUrl.reduce((sum, { violations }) => sum + violations.reduce((n, v) => n + (v.nodes || []).length, 0), 0);

  const { byRule } = buildByRule(allViolationsByUrl);

  const highLevelLines = [
    '# Accessibility report (WCAG 2.2)',
    '',
    `**URLs tested:** ${totalUrls}`,
    `**URLs passing (no violations):** ${urlsPassing}`,
    `**URLs with violations:** ${urlsWithViolations}`,
    `**Total rule violations:** ${totalViolations}`,
    `**Total failing elements (nodes):** ${totalNodes}`,
    '',
    summaryByUrlAndSeverity(allResults),
    '',
    combinedRulesTable(rulesRun, byRule),
    '',
  ];

  let summary = highLevelLines.join('\n');
  if (allViolationsByUrl.length > 0) {
    const { byRule: byRuleRefs, refMap, refCount, ruleIdToTags } = buildSummaryRefs(allViolationsByUrl);
    summary += '\n---\n\n## Details by URL\n\n';
    summary += formatSummaryReference(byRuleRefs, refCount, ruleIdToTags);
    summary += '\n---\n\n## Results\n\n';
    const allUrls = allResults.map((r) => r.url);
    const urlRoot = commonUrlRoot(allUrls);
    summary += formatResultsTable(allViolationsByUrl, refMap, urlRoot).join('\n');
  } else {
    summary += 'No accessibility violations found.\n';
  }

  return summary;
}

module.exports = { buildMarkdownReport };
