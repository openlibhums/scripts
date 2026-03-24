// @ts-check
/**
 * Teardown for axe-general.test.js.
 * Collates per-URL raw results into a single JSON report with violation counts per browser per URL.
 * Node-level detail is omitted; use axe-detail-teardown for that.
 */
const fs = require('fs');
const path = require('path');
const { buildGeneralMarkdown } = require('./axe-general-markdown');

const testResultsDir = path.join(__dirname, 'test-results');
const rawDir = path.join(testResultsDir, 'raw');

module.exports = async function axeGeneralTeardown() {
  if (!fs.existsSync(rawDir)) return;

  const files = fs.readdirSync(rawDir).filter((f) => f.endsWith('.json'));
  if (files.length === 0) return;

  files.sort((a, b) => {
    const na = parseInt(a.replace(/\D/g, ''), 10);
    const nb = parseInt(b.replace(/\D/g, ''), 10);
    if (!isNaN(na) && !isNaN(nb)) return na - nb;
    return a.localeCompare(b);
  });

  const results = files.map((f) => JSON.parse(fs.readFileSync(path.join(rawDir, f), 'utf8')));

  const startFile = path.join(testResultsDir, 'run-start.txt');
  const collated = fs.existsSync(startFile)
    ? fs.readFileSync(startFile, 'utf8').trim()
    : new Date().toISOString().slice(0, 16);

  const ruleMeta = new Map(); // Map<ruleId, { id, help, tags }>
  const ruleUrlBrowsers = new Map(); // Map<ruleId, Map<url, Map<browser, test_date>>>
  const ruleUrlViolations = new Map(); // Map<ruleId, Map<url, Map<browser, count>>>

  for (const { url, violations, rulesRun, browser } of results) {
    for (const { id, help, tags } of (rulesRun || [])) {
      if (!ruleMeta.has(id)) {
        ruleMeta.set(id, { id, help, tags: [...tags].sort() });
      }
      if (!ruleUrlBrowsers.has(id)) ruleUrlBrowsers.set(id, new Map());
      const urlMap = ruleUrlBrowsers.get(id);
      if (!urlMap.has(url)) urlMap.set(url, new Map());
      urlMap.get(url).set(browser, collated);
    }
    for (const { id, nodes } of violations) {
      if (!ruleUrlViolations.has(id)) ruleUrlViolations.set(id, new Map());
      const urlMap = ruleUrlViolations.get(id);
      if (!urlMap.has(url)) urlMap.set(url, new Map());
      const browserMap = urlMap.get(url);
      browserMap.set(browser, (browserMap.get(browser) || 0) + nodes.length);
    }
  }

  const output = [...ruleMeta.values()]
    .sort((a, b) => a.id.localeCompare(b.id))
    .map(({ id, help, tags }) => {
      const urlBrowsers = ruleUrlBrowsers.get(id) || new Map();
      const urlViolations = ruleUrlViolations.get(id) || new Map();

      const urls = [...urlBrowsers.entries()]
        .sort(([a], [b]) => a.localeCompare(b))
        .map(([u, browserMap]) => ({
          url: u,
          browsers: Object.fromEntries(
            [...browserMap.entries()].sort().map(([b, test_date]) => [
              b,
              { test_date, violations: (urlViolations.get(u) || new Map()).get(b) || 0 },
            ])
          ),
        }));

      return { id, help, tags, urls };
    });

  const timestamp = collated.replace(/[:.]/g, '-').slice(0, 19);
  fs.mkdirSync(testResultsDir, { recursive: true });
  const outPath = path.join(testResultsDir, `results-${timestamp}.json`);
  fs.writeFileSync(outPath, JSON.stringify(output, null, 2), 'utf8');
  const mdPath = path.join(testResultsDir, `results-${timestamp}.md`);
  fs.writeFileSync(mdPath, buildGeneralMarkdown(output), 'utf8');
};
