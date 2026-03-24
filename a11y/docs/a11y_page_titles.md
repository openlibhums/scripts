# a11y_page_titles

Django management command that generates a markdown report comparing page titles across the OLH, Material, and Clean themes for a list of URLs.

## Purpose
To assit with finding areas of non-compliance with [WCAG 2.4.2 Page Titled](https://www.w3.org/WAI/WCAG22/Understanding/page-titled)
> Web pages have titles that describe topic or purpose.

"Describe" is subjective.  This command cannot determine whether the title is descriptive. It is a helper command, to generate list of titles for a developer to review."  A check is included as to whether all three themes have the same title, but this has no direct bearing on whether the title passes the requirement.  Where the same title is expected across all three themes this provides a quick way to review the results.

## What it does

The command:

1. Loads a list of URLs (from a JSON file)
2. Fetches each URL once per theme (olh, material, clean) via the Django test client
3. Extracts the `<title>` from each response
4. Writes a markdown table to a file, with one row per URL and columns for each theme’s title and whether all three match

## How to use

### Defaults
- Input [`page_title_urls.json`](../playwright/tests/test_inputs/page_title_urls.json)
- Output [`results/markdown/page_titles.md`](../results/markdown/page_titles.md)

> **Note:** This command uses `page_title_urls.json` as its default, not `front_of_house.json` (which is the default for the Playwright tests). The page title check deliberately spans multiple journals (OLH, ANE, Glossa) so that titles which should include the journal name can be verified across different journals — a single-journal list would not catch errors where the journal name is missing or incorrect.

### Options

| Option | Default | Description |
|--------|---------|-------------|
| `--output PATH` | `a11y/results/page_titles.md` | Path to the output markdown file. The directory is created if it doesn’t exist. |
| `--urls-json PATH` | `a11y/test_inputs/localhost_urls.json` | Path to a JSON file containing an array of URL strings to check. |

### Examples

**Default behaviour** — use default URL list and write to default output:

```bash
python manage.py a11y_page_titles
```

**Both options** — custom URLs and custom output:

```bash
python manage.py a11y_page_titles --urls-json path/to/urls.json --output path/to/report.md
```

### URL list format

The `--urls-json` file must be valid JSON and contain a **single array of URL strings**. Order is preserved and determines the order of rows in the report. Duplicates are removed while keeping the first occurrence.

Example:

```json
[
  "http://localhost:8000/",
  "http://localhost:8000/contact",
  "http://localhost:8000/olh/"
]
```

## Results

The results can be found at [`scripts/results/markdown/page_titles.md`](../../results/markdown/page_titles.md). There is only a markdown file, no json.   The generated results table includes a final blank column for human review.

| URL | OLH Title | Material Title | Clean Title | All Identical | Human Review |
|-----|-----------|----------------|-------------|---------------|--------------|
| [http://localhost:8000/](http://localhost:8000/) | Open Library of Humanities | Open Library of Humanities | Open Library of Humanities | :white_check_mark: | |
| ...| ... | ... | ... | ... | |

This should be filled out by a **human** after the table has been generated, to show which titles satisfy the requirement of a descriptive title, and which do not.

Line 4 must also be added afterwards, to note which commit the test was run against, e.g. 

> Test run on tag a11y-audit-1.9, 17 March 2026.
