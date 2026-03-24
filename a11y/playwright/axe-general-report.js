// @ts-check
/**
 * Generate a markdown report from an existing axe-general JSON results file.
 *
 * Usage:
 *   node axe-general-report.js <path/to/results.json>
 *   node axe-general-report.js          (uses the most recent results-*.json in test-results/)
 *
 * Writes the markdown to the same directory and base name as the input, with a .md extension.
 */
const fs = require('fs');
const path = require('path');
const { buildGeneralMarkdown } = require('./axe-general-markdown');

const testResultsDir = path.join(__dirname, 'test-results');

function findLatestResults() {
  if (!fs.existsSync(testResultsDir)) {
    console.error(`No test-results directory found at ${testResultsDir}`);
    process.exit(1);
  }
  const files = fs.readdirSync(testResultsDir)
    .filter((f) => f.startsWith('results-') && f.endsWith('.json'))
    .map((f) => path.join(testResultsDir, f))
    .sort((a, b) => fs.statSync(b).mtimeMs - fs.statSync(a).mtimeMs);
  if (files.length === 0) {
    console.error('No results-*.json files found in test-results/');
    process.exit(1);
  }
  return files[0];
}

const inputPath = path.resolve(process.argv[2] || findLatestResults());

if (!fs.existsSync(inputPath)) {
  console.error(`File not found: ${inputPath}`);
  process.exit(1);
}

const output = JSON.parse(fs.readFileSync(inputPath, 'utf8'));
const markdown = buildGeneralMarkdown(output);

const outPath = inputPath.replace(/\.json$/, '.md');
fs.writeFileSync(outPath, markdown, 'utf8');
console.log(`Written: ${outPath}`);
