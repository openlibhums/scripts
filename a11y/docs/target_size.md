# Target size test

Playwright test that records the pixel dimensions of every focusable element on each tested page and checks them against the WCAG 2.2 target size thresholds.

## Purpose

To assist with finding areas of non-compliance with [WCAG 2.5.8 Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum) (Level AA) and [WCAG 2.5.5 Target Size (Enhanced)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced) (Level AAA):

| Level | Minimum size |
|-------|-------------|
| AA    | 24 × 24 px  |
| AAA   | 44 × 44 px  |

The test collects data for all focusable elements — it does not fail on small targets. Use the output report to identify elements that fall below the thresholds.

**Text links** (`<a href>` with no `img` or `svg` child) are flagged separately in the report. WCAG 2.2 provides a height exception for inline text links because their height is determined by the surrounding line height rather than the author.

## Prerequisites

Install dependencies and browsers once from the `playwright/` directory:

```bash
npm install
npx playwright install
```

## URL list

Defaults to `tests/test_inputs/front_of_house.json`. This is the same default as the accessibility test — see [playwright_accessibility_testing.md](playwright_accessibility_testing.md) for details on the URL list format and environment variable overrides.

| Environment variable | Effect |
|---------------------|--------|
| `URL_LIST=/path/to/urls.json` | Use a different JSON file (array of URL strings) |
| `A11Y_URL=http://localhost:8000/olh/` | Run against a single URL only |

## How to run

From the `playwright/` directory:

```bash
npx playwright test target_size --project=chromium
```

### Run against a single URL

```bash
A11Y_URL=http://localhost:8000/olh/ npx playwright test target_size --project=chromium
```

### Use a different URL list

```bash
URL_LIST=/path/to/my-urls.json npx playwright test target_size --project=chromium
```

### Run in headed mode

```bash
npx playwright test target_size --project=chromium --headed
```

## Output

After the run, two files are written to the test's output directory inside `test-results/`:

- **`target-size-report.md`** — a markdown table with one row per focusable element, showing URL, tag, accessible name, width, height, whether it is a text link, and whether it meets AA and AAA thresholds.
- **`target-size-report.csv`** — the same data in CSV format for spreadsheet analysis.

The report header also shows the total number of URLs tested and total focusable elements found.

## Reading the results

Each row in the report shows:

| Column | Description |
|--------|-------------|
| URL | Page the element was found on |
| # | Element index on that page |
| Tag | HTML tag (`a`, `button`, `input`, etc.) |
| Name / Label | Accessible name (aria-label, title, placeholder, or text content) |
| Width / Height (px) | Rendered size |
| Text link | ✓ if this is an inline text `<a href>` with no img/svg |
| ≥24×24 (AA) | ✓ meets WCAG 2.2 Level AA minimum |
| ≥44×44 (AAA) | ✓ meets WCAG 2.2 Level AAA enhanced |

Elements where **Text link** is ✓ and the AA column is ✗ may still pass WCAG 2.2 due to the height exception — review these manually.
