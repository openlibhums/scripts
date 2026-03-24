// @ts-check
/**
 * Global teardown dispatcher.
 * Routes to the appropriate teardown based on which test was run:
 *   - A11Y_RULE set → axe-detail-teardown (single rule, full node detail)
 *   - otherwise    → axe-general-teardown (all rules, counts per URL per browser)
 */
module.exports = async function globalTeardown() {
  if (process.env.A11Y_RULE) {
    return require('./axe-detail-teardown')();
  }
  return require('./axe-general-teardown')();
};
