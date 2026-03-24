# Axe

Two test files are provided, both producing the same JSON output format via the shared teardown:

| | `axe-general.test.js` | `axe-detail.test.js` |
|---|---|---|
| **Scope** | All URLs in the URL list | Single URL (`A11Y_URL`) |
| **Rules** | Full WCAG 2.2 A/AA rule set | Single rule (`A11Y_RULE`) |
| **Purpose** | Overview — breadth across all pages | Investigation — depth on one rule |
| **Node detail** | None — violation counts per URL per browser only | Full axe node data including `any`/`all`/`none` check arrays |
| **Env vars required** | None | `A11Y_URL` and `A11Y_RULE` (errors if either missing) |

## How to use
:warning: If running against a dev install, then disable the debug toolbar before running tests or you will get errors from the toolbar itself.

### Overview run (`axe-general.test.js`)
This is for a general list of errors that we store in this repo, track over time and use to generate reports.

From the playwright directory. Note: use `axe-general.test` 

```
npx playwright test axe-general.test --project=chromium
```

Run against multiple browsers in one pass by adding more `--project` flags, or omit `--project` entirely to run all configured browsers (chromium, firefox, webkit):

```
npx playwright test axe-general.test --project=chromium --project=firefox
npx playwright test axe-general.test
```

Additional browser configurations (e.g. mobile viewports) can be added to the `projects` array in `playwright.config.js`.

### Detail run (`axe-detail.test.js`)
This gathers more information about a specific rule and page, and is used when working on fixing errors.  This is for information only and we do not store the results in this repo.

Requires `A11Y_URL` and `A11Y_RULE` to be set:

```
A11Y_URL=http://localhost:8000/ A11Y_RULE=color-contrast npx playwright test axe-detail --project=chromium
```

Run across all browsers:

```
A11Y_URL=http://localhost:8000/ A11Y_RULE=color-contrast npx playwright test axe-detail
```

Note: all tests should report as 'passed' in the terminal. Pass/fail during testing is on whether the test runs. If the tests fail, check the server is running!

## JSON output

Results are written to `playwright/test-results/results-{timestamp}.json` after each run. The file is a JSON array — one entry per axe rule that was run, sorted alphabetically by rule `id`.

The `{timestamp}` is minute-precision (`YYYY-MM-DDTHH-MM`) and is taken at the moment the run begins, so it is consistent across all entries in the file and can be used to identify the run.

All rules use the same structure: a `urls` array where every tested URL appears, each with a `browsers` object recording how many violations that browser found. `violations: 0` means the rule passed on that URL for that browser.

```json
{
  "id": "aria-allowed-attr",
  "help": "Elements must only use supported ARIA attributes",
  "tags": ["cat.aria", "wcag2a", "wcag412", "..."],
  "urls": [
    {
      "url": "http://localhost:8000/",
      "browsers": {
        "chromium": { "test_date": "2026-03-23T12:56", "violations": 0 },
        "firefox":  { "test_date": "2026-03-23T12:56", "violations": 0 }
      }
    }
  ]
}
```

A rule with violations looks the same — URLs where the rule passed still appear with `violations: 0`, and URLs with failures show the count:

```json
{
  "id": "color-contrast",
  "help": "Elements must have sufficient color contrast",
  "tags": ["cat.color", "wcag2aa", "wcag143", "..."],
  "urls": [
    {
      "url": "http://localhost:8000/",
      "browsers": {
        "chromium": { "test_date": "2026-03-23T12:56", "violations": 0 },
        "firefox":  { "test_date": "2026-03-23T12:56", "violations": 0 }
      }
    },
    {
      "url": "http://localhost:8000/articles/",
      "browsers": {
        "chromium": { "test_date": "2026-03-23T12:56", "violations": 3 },
        "firefox":  { "test_date": "2026-03-23T12:56", "violations": 1 }
      }
    }
  ]
}
```

To investigate which specific elements are failing, use `axe-detail.test.js`.

**Detail run (`axe-detail.test.js`)** — nodes additionally include the full axe check arrays:

- **`any`** — checks where at least one must pass; maps to "Fix any of the following" in the failure summary
- **`all`** — checks that must all pass
- **`none`** — conditions that must all be false

Each check entry contains `id`, `impact`, `message`, and `data` (e.g. exact contrast ratios, specific ARIA attributes). Use the detail run when you need this level of diagnostic information for a specific rule.

### Field reference

| Field | Description |
|-------|-------------|
| `id` | Axe rule identifier |
| `help` | Short description of what the rule checks |
| `tags` | WCAG and category tags (e.g. `wcag2a`, `best-practice`) |
| `urls` | All pages the rule was tested on, sorted by URL |
| `urls[].url` | The page URL |
| `urls[].browsers` | Per-browser results for this rule on this page |
| `urls[].browsers[browser].test_date` | Minute-precision timestamp of the run, taken at test start — consistent across the entire run |
| `urls[].browsers[browser].violations` | Number of failing elements found by that browser on that page; `0` if the rule passed |

### Tracking history over time

The `test_date` inside each `occurrences` entry records when that failure was observed. When running `axe-general`, the output file should be copied onto the appropriate history file after each run (`a11y/results/json/file.json`) — git will show exactly which nodes were added or removed between runs.

## Quality Assurance

These tests should be repeatable when run locally a few minutes apart with no other changes. When running the tests, you should run them twice a few minutes apart and check, for example using:
```bash
git diff | grep '^[+-]' | grep -v 'test_date'
```
If there are differences between runs, investigate whether any dynamic page content is affecting violation counts. It is important that the data is repeatable before results are relied upon.