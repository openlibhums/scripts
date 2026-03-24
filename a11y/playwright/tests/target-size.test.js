// @ts-check
const { test, expect } = require('@playwright/test');
const fs = require('fs');
const path = require('path');

const MIN_TARGET_AA = 24; // WCAG 2.2 Level AA
const MIN_TARGET_AAA = 44; // WCAG 2.2 Level AAA

/** Single URL when A11Y_URL is set; otherwise use front_of_house list from JSON */
const DEFAULT_URL_LIST_PATH = path.join(__dirname, '..', '..', 'test_inputs', 'front_of_house.json');

function loadTestUrls() {
  const urlListPath = process.env.URL_LIST || DEFAULT_URL_LIST_PATH;
  const resolved = path.resolve(urlListPath);
  if (!fs.existsSync(resolved)) {
    throw new Error(`URL list not found: ${resolved}. Set URL_LIST or A11Y_URL, or add tests/test_inputs/front_of_house.json.`);
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

const TEST_URLS = getUrls();

test('record focusable elements target size to markdown table', async ({ page }, testInfo) => {
  const allRows = [];
  let totalFocusable = 0;

  for (const url of TEST_URLS) {
    await page.goto(url, { waitUntil: 'load' });

    const focusableData = await page.evaluate(({ minAA, minAAA }) => {
    const focusableSelector = [
      'a[href]',
      'button:not([disabled])',
      'input:not([disabled])',
      'select:not([disabled])',
      'textarea:not([disabled])',
      'summary',
      '[contenteditable="true"]',
      '[tabindex]:not([tabindex="-1"])',
    ].join(', ');

    const nodes = document.querySelectorAll(focusableSelector);

    return Array.from(nodes)
      .filter((el) => {
        const style = window.getComputedStyle(el);
        const hidden =
          style.display === 'none' ||
          style.visibility === 'hidden' ||
          style.opacity === '0' ||
          el.getBoundingClientRect().width === 0 ||
          el.getBoundingClientRect().height === 0;
        return !hidden;
      })
      .map((el, index) => {
        const rect = el.getBoundingClientRect();
        const width = Math.round(rect.width);
        const height = Math.round(rect.height);
        const tag = el.tagName.toLowerCase();
        const name =
          el.getAttribute('aria-label') ||
          el.getAttribute('title') ||
          el.getAttribute('placeholder') ||
          (el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 40) ||
          el.getAttribute('type') ||
          '(no name)';
        const meetsAA = width >= minAA && height >= minAA;
        // Text link = <a> with no img/svg; height is determined by font size (WCAG height exception)
        const isTextLink =
          tag === 'a' && !el.querySelector('img, svg') && el.textContent?.trim().length > 0;
        return {
          index: index + 1,
          tag,
          name: name.slice(0, 50),
          width,
          height,
          meetsAA,
          isTextLink,
        };
      });
  }, { minAA: MIN_TARGET_AA });

    for (const row of focusableData) {
      allRows.push({ url, ...row });
    }
    totalFocusable += focusableData.length;
  }

  const headers = [
    'URL',
    '#',
    'Tag',
    'Name / Label',
    'Width (px)',
    'Height (px)',
    'Text link',
    `≥${MIN_TARGET_AA}×${MIN_TARGET_AA} (AA)`,
  ];
  const separator = headers.map(() => '---');
  const headerRow = '| ' + headers.join(' | ') + ' |';
  const sepRow = '| ' + separator.join(' | ') + ' |';

  const bodyRows = allRows.map((row) => {
    return [
      row.url.replace(/\|/g, '\\|'),
      row.index,
      row.tag,
      row.name.replace(/\|/g, '\\|').replace(/\n/g, ' '),
      row.width,
      row.height,
      row.isTextLink ? ':white_check_mark:' : ':x:',
      row.meetsAA ? ':white_check_mark:' : ':x:'
    ].join(' | ');
  });

  const table = [
    '# Focusable elements target size',
    '',
    `Generated: ${new Date().toISOString()}`,
    `URLs tested: ${TEST_URLS.length}`,
    `Total focusable elements: ${totalFocusable}`,
    '',
    '**Text link** (✓) = inline text `<a href>` with no img/svg; height is determined by font size (WCAG 2.2 height exception applies).',
    '',
    headerRow,
    sepRow,
    ...bodyRows.map((r) => '| ' + r + ' |'),
  ].join('\n');

  const reportPath = testInfo.outputPath('target-size-report.md');
  const csvPath = testInfo.outputPath('target-size-report.csv');
  fs.mkdirSync(path.dirname(reportPath), { recursive: true });
  fs.writeFileSync(reportPath, table, 'utf8');

  // CSV output: escape fields that contain comma, quote, or newline
  const escapeCsv = (val) => {
    const s = String(val ?? '');
    if (/[",\r\n]/.test(s)) return `"${s.replace(/"/g, '""')}"`;
    return s;
  };

  testInfo.attachments.push({
    name: 'target-size-report',
    path: reportPath,
    contentType: 'text/markdown',
  });

  // Optional: log path so it's visible in runner output
  console.log('Target size report written to:', reportPath);

  expect(totalFocusable).toBeGreaterThanOrEqual(0);
});
