// @ts-check
const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;
const fs = require('fs');
const path = require('path');

/** Single URL when A11Y_URL is set; otherwise use front_of_house list from JSON */
const DEFAULT_URL_LIST_PATH = path.join(__dirname, '..', '..', 'test_inputs', 'front_of_house.json');

function loadTestUrls() {
  const urlListPath = process.env.URL_LIST || DEFAULT_URL_LIST_PATH;
  const resolved = path.resolve(urlListPath);
  if (!fs.existsSync(resolved)) {
    throw new Error(`URL list not found: ${resolved}. Set URL_LIST or A11Y_URL, or add test_inputs/front_of_house.json.`);
  }
  const raw = fs.readFileSync(resolved, 'utf8');
  const urls = JSON.parse(raw);
  if (!Array.isArray(urls) || urls.some((u) => typeof u !== 'string')) {
    throw new Error('URL list must be a JSON array of strings.');
  }
  return urls;
}

function getUrls() {
  if (process.env.A11Y_URL) {
    return [process.env.A11Y_URL];
  }
  return loadTestUrls();
}

const urls = getUrls();
const rawDir = path.join(__dirname, '..', 'test-results', 'raw');

for (let index = 0; index < urls.length; index++) {
  const url = urls[index];
  test(`axe scan (${index + 1}/${urls.length}): ${url}`, async ({ page }, testInfo) => {
    test.setTimeout(90000);

    await page.goto(url, { waitUntil: 'load' });

    const results = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa', 'best-practice', 'EN-301-549', 'ACT'])
      .options({ resultTypes: ['violations'] })
      .analyze();

    const violations = results.violations ?? [];
    const passes = results.passes ?? [];
    const rulesRun = [];
    const seen = new Set();
    for (const r of [...passes, ...violations]) {
      if (r.id && !seen.has(r.id)) {
        seen.add(r.id);
        rulesRun.push({ id: r.id, help: r.help || '', tags: r.tags || [] });
      }
    }
    rulesRun.sort((a, b) => a.id.localeCompare(b.id));
    const browser = testInfo.project.name;
    const resultFile = path.join(rawDir, `axe-${browser}-${index}.json`);
    fs.mkdirSync(rawDir, { recursive: true });
    fs.writeFileSync(resultFile, JSON.stringify({ url, violations, rulesRun, browser }), 'utf8');
  });
}
