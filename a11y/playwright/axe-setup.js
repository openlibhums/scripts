// @ts-check
/**
 * Global setup: record test run start time for use in teardown.
 */
const fs = require('fs');
const path = require('path');

const testResultsDir = path.join(__dirname, 'test-results');

module.exports = async function globalSetup() {
  fs.mkdirSync(testResultsDir, { recursive: true });
  fs.writeFileSync(
    path.join(testResultsDir, 'run-start.txt'),
    new Date().toISOString().slice(0, 16),
    'utf8'
  );
};
