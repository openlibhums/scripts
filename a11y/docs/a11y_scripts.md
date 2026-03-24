# Accessiblity Testing Helper Scripts

## Management Commands
These are in the same directory as the other managment commands. 
1. [a11y_page_titles](docs/a11y_page_titles.md)


## Playwright Scripts
These are in the `playwright/` directory. Run from there with `npx playwright test`.

Results appear in `playwright/test-results/` and this directory is overwritten each time tests are run, so results need to be copyied out of there.  For tracking, results are manually copied to `a11y/results/json`.

1. [axe](docs/axe.md) — `tests/axe-general.test.js` and `tests/axe-detail.test.js`
   Runs axe-core against a list of URLs and checks for WCAG 2.2 Level A/AA violations.
2. [Target size](docs/target_size.md) — `tests/target_size.test.js`
   Records the pixel dimensions of every focusable element against WCAG 2.2 AA (24 px) and AAA (44 px) thresholds. Outputs a markdown table and CSV to `test-results/`.


## URL input files

All URL lists live in `playwright/tests/test_inputs/`. Pass a different file to any test with the `URL_LIST` environment variable, or run a single URL with `A11Y_URL`.

| File | Default for | Description |
|------|------------|-------------|
| `front_of_house.json` | Accessibility test, Target size test | Broad front-of-house URL list covering the three main themes (clean, OLH, material) across a representative set of page types. Used as the default for most automated tests. |
| `page_title_urls.json` | `a11y_page_titles` management command | Multi-journal URL list (OLH, ANE, Glossa) used to verify page titles include the correct journal name. Intentionally spans multiple journals — a single-journal list would not catch errors where the journal name is missing or wrong. |
| `clarity.json` | — | URLs for the Clarity theme. Use with `URL_LIST` when testing Clarity specifically. |
| `clean.json` | — | URLs for the Clean theme. |
| `hourglass.json` | — | URLs for the Hourglass theme. |
| `material.json` | — | URLs for the Material theme. |
| `olh.json` | — | URLs for the OLH theme. |

## Results
When playwright runs, it deletes the contents of `playwright/test-results` and then puts the new results inside there.  Any results we wish to keep and track should be copied to `a11y/results`.

The JSON is the source of truth, the markdown is a human readable summary. 
