// @ts-check
const { test } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;
const fs = require('fs');
const path = require('path');

const url = process.env.A11Y_URL;
const ruleId = process.env.A11Y_RULE;

if (!url || !ruleId) {
  throw new Error('A11Y_URL and A11Y_RULE must both be set to run axe-detail tests.\nExample: A11Y_URL=http://localhost:8000/ A11Y_RULE=color-contrast npx playwright test axe-detail');
}

const rawDir = path.join(__dirname, '..', 'test-results', 'raw');

test(`axe detail: ${ruleId} on ${url}`, async ({ page }, testInfo) => {
  test.setTimeout(90000);

  await page.goto(url, { waitUntil: 'load' });

  const results = await new AxeBuilder({ page })
    .withRules([ruleId])
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

  const browser = testInfo.project.name;
  const resultFile = path.join(rawDir, `axe-${browser}-0.json`);
  fs.mkdirSync(rawDir, { recursive: true });
  fs.writeFileSync(resultFile, JSON.stringify({ url, violations, rulesRun, browser }), 'utf8');
});
