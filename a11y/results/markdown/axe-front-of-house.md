# Axe general accessibility report

**Test date:** a11y-audit-1.9

| Rule | Description | Tags | Results |
| --- | --- | --- | --- |
| aria-allowed-attr | Elements must only use supported ARIA attributes | `EN-301-549`, `EN-9.4.1.2`, `RGAA-7.1.1`, `RGAAv4`, `cat.aria`, `wcag2a`, `wcag412` | :white_check_mark: |
| aria-allowed-role | ARIA role should be appropriate for the element | `best-practice`, `cat.aria` | :white_check_mark: |
| aria-command-name | ARIA commands must have an accessible name | `ACT`, `EN-301-549`, `EN-9.4.1.2`, `RGAA-11.9.1`, `RGAAv4`, `TT6.a`, `TTv5`, `cat.aria`, `wcag2a`, `wcag412` | :white_check_mark: |
| aria-conditional-attr | ARIA attributes must be used as specified for the element's role | `EN-301-549`, `EN-9.4.1.2`, `RGAA-7.1.1`, `RGAAv4`, `cat.aria`, `wcag2a`, `wcag412` | :white_check_mark: |
| aria-deprecated-role | Deprecated ARIA roles must not be used | `EN-301-549`, `EN-9.4.1.2`, `RGAA-7.1.1`, `RGAAv4`, `cat.aria`, `wcag2a`, `wcag412` | :white_check_mark: |
| aria-hidden-body | aria-hidden="true" must not be present on the document body | `EN-301-549`, `EN-9.1.3.1`, `EN-9.4.1.2`, `RGAA-10.8.1`, `RGAAv4`, `cat.aria`, `wcag131`, `wcag2a`, `wcag412` | :white_check_mark: |
| aria-hidden-focus | ARIA hidden element must not be focusable or contain focusable elements | `EN-301-549`, `EN-9.4.1.2`, `RGAA-10.8.1`, `RGAAv4`, `TT6.a`, `TTv5`, `cat.name-role-value`, `wcag2a`, `wcag412` | :white_check_mark: |
| aria-prohibited-attr | Elements must only use permitted ARIA attributes | `EN-301-549`, `EN-9.4.1.2`, `RGAA-7.1.1`, `RGAAv4`, `cat.aria`, `wcag2a`, `wcag412` | :white_check_mark: |
| aria-required-attr | Required ARIA attributes must be provided | `EN-301-549`, `EN-9.4.1.2`, `RGAA-7.1.1`, `RGAAv4`, `cat.aria`, `wcag2a`, `wcag412` | :white_check_mark: |
| aria-required-children | Certain ARIA roles must contain particular children | `EN-301-549`, `EN-9.1.3.1`, `RGAA-9.3.1`, `RGAAv4`, `cat.aria`, `wcag131`, `wcag2a` | [4](#aria-required-children) |
| aria-required-parent | Certain ARIA roles must be contained by particular parents | `EN-301-549`, `EN-9.1.3.1`, `RGAA-9.3.1`, `RGAAv4`, `cat.aria`, `wcag131`, `wcag2a` | [4](#aria-required-parent) |
| aria-roles | ARIA roles used must conform to valid values | `EN-301-549`, `EN-9.4.1.2`, `RGAA-7.1.1`, `RGAAv4`, `cat.aria`, `wcag2a`, `wcag412` | :white_check_mark: |
| aria-valid-attr | ARIA attributes must conform to valid names | `EN-301-549`, `EN-9.4.1.2`, `RGAA-7.1.1`, `RGAAv4`, `cat.aria`, `wcag2a`, `wcag412` | :white_check_mark: |
| aria-valid-attr-value | ARIA attributes must conform to valid values | `EN-301-549`, `EN-9.4.1.2`, `RGAA-7.1.1`, `RGAAv4`, `cat.aria`, `wcag2a`, `wcag412` | :white_check_mark: |
| autocomplete-valid | autocomplete attribute must be used correctly | `ACT`, `EN-301-549`, `EN-9.1.3.5`, `RGAA-11.13.1`, `RGAAv4`, `cat.forms`, `wcag135`, `wcag21aa` | :white_check_mark: |
| avoid-inline-spacing | Inline text spacing must be adjustable with custom stylesheets | `ACT`, `EN-301-549`, `EN-9.1.4.12`, `cat.structure`, `wcag1412`, `wcag21aa` | :white_check_mark: |
| button-name | Buttons must have discernible text | `ACT`, `EN-301-549`, `EN-9.4.1.2`, `RGAA-11.9.1`, `RGAAv4`, `TT6.a`, `TTv5`, `cat.name-role-value`, `section508`, `section508.22.a`, `wcag2a`, `wcag412` | :white_check_mark: |
| bypass | Page must have means to bypass repeated blocks | `EN-301-549`, `EN-9.2.4.1`, `RGAA-12.7.1`, `RGAAv4`, `TT9.a`, `TTv5`, `cat.keyboard`, `section508`, `section508.22.o`, `wcag241`, `wcag2a` | :white_check_mark: |
| color-contrast | Elements must meet minimum color contrast ratio thresholds | `ACT`, `EN-301-549`, `EN-9.1.4.3`, `RGAA-3.2.1`, `RGAAv4`, `TT13.c`, `TTv5`, `cat.color`, `wcag143`, `wcag2aa` | [10562](#color-contrast) |
| definition-list | `<dl>` elements must only directly contain properly-ordered `<dt>` and `<dd>` groups, `<script>`, `<template>` or `<div>` elements | `EN-301-549`, `EN-9.1.3.1`, `RGAA-9.3.3`, `RGAAv4`, `cat.structure`, `wcag131`, `wcag2a` | :white_check_mark: |
| dlitem | `<dt>` and `<dd>` elements must be contained by a `<dl>` | `EN-301-549`, `EN-9.1.3.1`, `RGAA-9.3.3`, `RGAAv4`, `cat.structure`, `wcag131`, `wcag2a` | :white_check_mark: |
| document-title | Documents must have `<title>` element to aid in navigation | `ACT`, `EN-301-549`, `EN-9.2.4.2`, `RGAA-8.5.1`, `RGAAv4`, `TT12.a`, `TTv5`, `cat.text-alternatives`, `wcag242`, `wcag2a` | [7](#document-title) |
| duplicate-id-aria | IDs used in ARIA and labels must be unique | `EN-301-549`, `EN-9.4.1.2`, `RGAA-8.2.1`, `RGAAv4`, `cat.parsing`, `wcag2a`, `wcag412` | :white_check_mark: |
| empty-heading | Headings should not be empty | `best-practice`, `cat.name-role-value` | [14](#empty-heading) |
| empty-table-header | Table header text should not be empty | `best-practice`, `cat.name-role-value` | :white_check_mark: |
| form-field-multiple-labels | Form field must not have multiple label elements | `EN-301-549`, `EN-9.3.3.2`, `RGAA-11.2.1`, `RGAAv4`, `TT5.c`, `TTv5`, `cat.forms`, `wcag2a`, `wcag332` | :white_check_mark: |
| heading-order | Heading levels should only increase by one | `best-practice`, `cat.semantics` | [35](#heading-order) |
| html-has-lang | `<html>` element must have a lang attribute | `ACT`, `EN-301-549`, `EN-9.3.1.1`, `RGAA-8.3.1`, `RGAAv4`, `TT11.a`, `TTv5`, `cat.language`, `wcag2a`, `wcag311` | [28](#html-has-lang) |
| html-lang-valid | `<html>` element must have a valid value for the lang attribute | `ACT`, `EN-301-549`, `EN-9.3.1.1`, `RGAA-8.4.1`, `RGAAv4`, `TT11.a`, `TTv5`, `cat.language`, `wcag2a`, `wcag311` | :white_check_mark: |
| image-alt | Images must have alternative text | `ACT`, `EN-301-549`, `EN-9.1.1.1`, `RGAA-1.1.1`, `RGAAv4`, `TT7.a`, `TT7.b`, `TTv5`, `cat.text-alternatives`, `section508`, `section508.22.a`, `wcag111`, `wcag2a` | [175](#image-alt) |
| image-redundant-alt | Alternative text of images should not be repeated as text | `best-practice`, `cat.text-alternatives` | :white_check_mark: |
| input-button-name | Input buttons must have discernible text | `ACT`, `EN-301-549`, `EN-9.4.1.2`, `RGAA-11.9.1`, `RGAAv4`, `TT5.c`, `TTv5`, `cat.name-role-value`, `section508`, `section508.22.a`, `wcag2a`, `wcag412` | :white_check_mark: |
| label | Form elements must have labels | `ACT`, `EN-301-549`, `EN-9.4.1.2`, `RGAA-11.1.1`, `RGAAv4`, `TT5.c`, `TTv5`, `cat.forms`, `section508`, `section508.22.n`, `wcag2a`, `wcag412` | [56](#label) |
| label-title-only | Form elements should have a visible label | `best-practice`, `cat.forms` | :white_check_mark: |
| landmark-banner-is-top-level | Banner landmark should not be contained in another landmark | `best-practice`, `cat.semantics` | :white_check_mark: |
| landmark-complementary-is-top-level | Aside should not be contained in another landmark | `best-practice`, `cat.semantics` | [45](#landmark-complementary-is-top-level) |
| landmark-contentinfo-is-top-level | Contentinfo landmark should not be contained in another landmark | `best-practice`, `cat.semantics` | :white_check_mark: |
| landmark-main-is-top-level | Main landmark should not be contained in another landmark | `best-practice`, `cat.semantics` | :white_check_mark: |
| landmark-no-duplicate-banner | Document should not have more than one banner landmark | `best-practice`, `cat.semantics` | :white_check_mark: |
| landmark-no-duplicate-contentinfo | Document should not have more than one contentinfo landmark | `best-practice`, `cat.semantics` | :white_check_mark: |
| landmark-no-duplicate-main | Document should not have more than one main landmark | `best-practice`, `cat.semantics` | :white_check_mark: |
| landmark-one-main | Document should have one main landmark | `best-practice`, `cat.semantics` | :white_check_mark: |
| landmark-unique | Landmarks should have a unique role or role/label/title (i.e. accessible name) combination | `best-practice`, `cat.semantics` | [21](#landmark-unique) |
| link-in-text-block | Links must be distinguishable without relying on color | `EN-301-549`, `EN-9.1.4.1`, `RGAA-10.6.1`, `RGAAv4`, `TT13.a`, `TTv5`, `cat.color`, `wcag141`, `wcag2a` | :white_check_mark: |
| link-name | Links must have discernible text | `ACT`, `EN-301-549`, `EN-9.2.4.4`, `EN-9.4.1.2`, `RGAA-6.2.1`, `RGAAv4`, `TT6.a`, `TTv5`, `cat.name-role-value`, `section508`, `section508.22.a`, `wcag244`, `wcag2a`, `wcag412` | [133](#link-name) |
| list | `<ul>` and `<ol>` must only directly contain `<li>`, `<script>` or `<template>` elements | `EN-301-549`, `EN-9.1.3.1`, `RGAA-9.3.1`, `RGAAv4`, `cat.structure`, `wcag131`, `wcag2a` | [206](#list) |
| listitem | `<li>` elements must be contained in a `<ul>` or `<ol>` | `EN-301-549`, `EN-9.1.3.1`, `RGAA-9.3.1`, `RGAAv4`, `cat.structure`, `wcag131`, `wcag2a` | [4](#listitem) |
| meta-viewport | Zooming and scaling must not be disabled | `ACT`, `EN-301-549`, `EN-9.1.4.4`, `RGAA-10.4.2`, `RGAAv4`, `cat.sensory-and-visual-cues`, `wcag144`, `wcag2aa` | :white_check_mark: |
| meta-viewport-large | Users should be able to zoom and scale the text up to 500% | `best-practice`, `cat.sensory-and-visual-cues` | :white_check_mark: |
| nested-interactive | Interactive controls must not be nested | `EN-301-549`, `EN-9.4.1.2`, `RGAA-7.1.1`, `RGAAv4`, `TT6.a`, `TTv5`, `cat.keyboard`, `wcag2a`, `wcag412` | :white_check_mark: |
| page-has-heading-one | Page should contain a level-one heading | `best-practice`, `cat.semantics` | [14](#page-has-heading-one) |
| presentation-role-conflict | Elements marked as presentational should be consistently ignored | `ACT`, `best-practice`, `cat.aria` | :white_check_mark: |
| region | All page content should be contained by landmarks | `RGAA-9.2.1`, `RGAAv4`, `best-practice`, `cat.keyboard` | :white_check_mark: |
| scope-attr-valid | scope attribute should be used correctly | `best-practice`, `cat.tables` | :white_check_mark: |
| scrollable-region-focusable | Scrollable region must have keyboard access | `EN-301-549`, `EN-9.2.1.1`, `EN-9.2.1.3`, `RGAA-7.3.2`, `RGAAv4`, `TT4.a`, `TTv5`, `cat.keyboard`, `wcag211`, `wcag213`, `wcag2a` | [8](#scrollable-region-focusable) |
| select-name | Select element must have an accessible name | `ACT`, `EN-301-549`, `EN-9.4.1.2`, `RGAA-11.1.1`, `RGAAv4`, `TT5.c`, `TTv5`, `cat.forms`, `section508`, `section508.22.n`, `wcag2a`, `wcag412` | [189](#select-name) |
| skip-link | The skip-link target should exist and be focusable | `RGAA-12.7.1`, `RGAAv4`, `best-practice`, `cat.keyboard` | :white_check_mark: |
| tabindex | Elements should not have tabindex greater than zero | `best-practice`, `cat.keyboard` | :white_check_mark: |
| table-duplicate-name | Tables should not have the same summary and caption | `RGAA-5.2.1`, `RGAAv4`, `best-practice`, `cat.tables` | :white_check_mark: |
| td-headers-attr | Table cell headers attributes must refer to other `<th>` elements in the same table | `EN-301-549`, `EN-9.1.3.1`, `RGAA-5.7.4`, `RGAAv4`, `TT14.b`, `TTv5`, `cat.tables`, `section508`, `section508.22.g`, `wcag131`, `wcag2a` | :white_check_mark: |
| th-has-data-cells | Table headers in a data table must refer to data cells | `EN-301-549`, `EN-9.1.3.1`, `RGAA-5.7.1`, `RGAAv4`, `TT14.b`, `TTv5`, `cat.tables`, `section508`, `section508.22.g`, `wcag131`, `wcag2a` | :white_check_mark: |
| valid-lang | lang attribute must have a valid value | `ACT`, `EN-301-549`, `EN-9.3.1.2`, `RGAA-8.8.1`, `RGAAv4`, `TT11.b`, `TTv5`, `cat.language`, `wcag2aa`, `wcag312` | :white_check_mark: |

| URL | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [404/?theme=clean](#url-404-theme-clean) | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| [404/?theme=olh](#url-404-theme-olh) | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| [?theme=clean](#url-theme-clean) | 27 | 27 | 27 | 27 | 27 | 27 | 27 |
| [?theme=olh](#url-theme-olh) | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| [contact/?theme=clean](#url-contact-theme-clean) | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| [contact/?theme=olh](#url-contact-theme-olh) | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| [journals/?theme=clean](#url-journals-theme-clean) | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| [journals/?theme=olh](#url-journals-theme-olh) | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| [olh/?theme=clean](#url-olh-theme-clean) | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| [olh/?theme=material](#url-olh-theme-material) | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| [olh/?theme=olh](#url-olh-theme-olh) | 13 | 13 | 11 | 11 | 13 | 13 | 13 |
| [olh/accessibility/?theme=clean](#url-olh-accessibility-theme-clean) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [olh/accessibility/?theme=material](#url-olh-accessibility-theme-material) | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| [olh/accessibility/?theme=olh](#url-olh-accessibility-theme-olh) | 2 | 2 | :white_check_mark: | :white_check_mark: | 2 | 2 | 2 |
| [olh/article/id/4403/?theme=clean](#url-olh-article-id-4403-theme-clean) | 1 | 1 | 2 | 2 | 2 | 1 | 1 |
| [olh/article/id/4403/?theme=material](#url-olh-article-id-4403-theme-material) | 149 | 149 | 156 | 156 | 147 | 148 | 149 |
| [olh/article/id/4403/?theme=olh](#url-olh-article-id-4403-theme-olh) | 158 | 157 | 152 | 152 | 158 | 160 | 160 |
| [olh/article/id/4405/?theme=clean](#url-olh-article-id-4405-theme-clean) | 11 | 11 | 13 | 13 | 12 | 12 | 11 |
| [olh/article/id/4405/?theme=material](#url-olh-article-id-4405-theme-material) | 281 | 281 | 286 | 287 | 280 | 281 | 281 |
| [olh/article/id/4405/?theme=olh](#url-olh-article-id-4405-theme-olh) | 293 | 293 | 274 | 274 | 293 | 293 | 293 |
| [olh/articles/?theme=clean](#url-olh-articles-theme-clean) | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| [olh/articles/?theme=material](#url-olh-articles-theme-material) | 74 | 74 | 74 | 74 | 74 | 74 | 74 |
| [olh/articles/?theme=olh](#url-olh-articles-theme-olh) | 7 | 7 | 7 | 7 | 9 | 9 | 7 |
| [olh/collections/846/?theme=clean](#url-olh-collections-846-theme-clean) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [olh/collections/846/?theme=material](#url-olh-collections-846-theme-material) | 56 | 56 | 56 | 56 | 55 | 56 | 56 |
| [olh/collections/846/?theme=olh](#url-olh-collections-846-theme-olh) | 54 | 54 | 52 | 52 | 54 | 54 | 54 |
| [olh/collections/?theme=clean](#url-olh-collections-theme-clean) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [olh/collections/?theme=material](#url-olh-collections-theme-material) | 50 | 50 | 52 | 50 | 42 | 53 | 50 |
| [olh/collections/?theme=olh](#url-olh-collections-theme-olh) | 2 | 2 | :white_check_mark: | :white_check_mark: | 2 | 2 | 2 |
| [olh/contact/?theme=clean ](#url-olh-contact-theme-clean) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [olh/contact/?theme=material ](#url-olh-contact-theme-material) | 14 | 14 | 14 | 14 | 14 | 14 | 14 |
| [olh/contact/?theme=olh ](#url-olh-contact-theme-olh) | 3 | 3 | 1 | 1 | 3 | 3 | 3 |
| [olh/editorialteam/?theme=clean](#url-olh-editorialteam-theme-clean) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [olh/editorialteam/?theme=material](#url-olh-editorialteam-theme-material) | 20 | 20 | 20 | 20 | 20 | 20 | 20 |
| [olh/editorialteam/?theme=olh](#url-olh-editorialteam-theme-olh) | 17 | 17 | 15 | 15 | 15 | 17 | 17 |
| [olh/issue/402/info/?theme=clean](#url-olh-issue-402-info-theme-clean) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [olh/issue/402/info/?theme=material](#url-olh-issue-402-info-theme-material) | 25 | 25 | 25 | 25 | 25 | 25 | 25 |
| [olh/issue/402/info/?theme=olh](#url-olh-issue-402-info-theme-olh) | 3 | 3 | 20 | 20 | 22 | 22 | 3 |
| [olh/issue/409/info/?theme=clean](#url-olh-issue-409-info-theme-clean) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [olh/issue/409/info/?theme=material](#url-olh-issue-409-info-theme-material) | 25 | 25 | 25 | 25 | 25 | 25 | 25 |
| [olh/issue/409/info/?theme=olh](#url-olh-issue-409-info-theme-olh) | 3 | 3 | 20 | 20 | 22 | 22 | 3 |
| [olh/issues/?theme=clean](#url-olh-issues-theme-clean) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [olh/issues/?theme=material](#url-olh-issues-theme-material) | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| [olh/issues/?theme=olh](#url-olh-issues-theme-olh) | 3 | 3 | 1 | 1 | 3 | 3 | 3 |
| [olh/news/429/?theme=clean](#url-olh-news-429-theme-clean) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [olh/news/429/?theme=material](#url-olh-news-429-theme-material) | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| [olh/news/429/?theme=olh](#url-olh-news-429-theme-olh) | 3 | 3 | 1 | 1 | 3 | 3 | 3 |
| [olh/news/?theme=clean](#url-olh-news-theme-clean) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [olh/news/?theme=material](#url-olh-news-theme-material) | 18 | 18 | 18 | 18 | 18 | 18 | 18 |
| [olh/news/?theme=olh](#url-olh-news-theme-olh) | 14 | 14 | 12 | 12 | 14 | 14 | 14 |
| [olh/search/?theme=clean](#url-olh-search-theme-clean) | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| [olh/search/?theme=material](#url-olh-search-theme-material) | 16 | 16 | 16 | 16 | 16 | 16 | 16 |
| [olh/search/?theme=olh](#url-olh-search-theme-olh) | 5 | 5 | 3 | 3 | 5 | 5 | 5 |
| [olh/site/about/?theme=clean](#url-olh-site-about-theme-clean) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [olh/site/about/?theme=material](#url-olh-site-about-theme-material) | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| [olh/site/about/?theme=olh](#url-olh-site-about-theme-olh) | 17 | 17 | 10 | 10 | 17 | 17 | 17 |
| [olh/site/author-guidelines/?theme=clean](#url-olh-site-author-guidelines-theme-clean) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [olh/site/author-guidelines/?theme=material](#url-olh-site-author-guidelines-theme-material) | 18 | 18 | 18 | 18 | 18 | 18 | 18 |
| [olh/site/author-guidelines/?theme=olh](#url-olh-site-author-guidelines-theme-olh) | 15 | 15 | 13 | 13 | 15 | 15 | 15 |
| [olh/site/journal-policies/?theme=clean](#url-olh-site-journal-policies-theme-clean) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [olh/site/journal-policies/?theme=material](#url-olh-site-journal-policies-theme-material) | 30 | 30 | 30 | 30 | 30 | 30 | 30 |
| [olh/site/journal-policies/?theme=olh](#url-olh-site-journal-policies-theme-olh) | 54 | 54 | 25 | 25 | 55 | 55 | 54 |
| [olh/submissions/?theme=clean](#url-olh-submissions-theme-clean) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [olh/submissions/?theme=material](#url-olh-submissions-theme-material) | 19 | 19 | 20 | 20 | 20 | 20 | 19 |
| [olh/submissions/?theme=olh](#url-olh-submissions-theme-olh) | 16 | 16 | 14 | 14 | 16 | 16 | 16 |

## aria-required-children

Certain ARIA roles must contain particular children

Tags: `EN-301-549`, `EN-9.1.3.1`, `RGAA-9.3.1`, `RGAAv4`, `cat.aria`, `wcag131`, `wcag2a`

| URL | chromium | firefox | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- |
| olh/articles/?theme=olh | :white_check_mark: | :white_check_mark: | 1 | 1 | :white_check_mark: | 2 |

## aria-required-parent

Certain ARIA roles must be contained by particular parents

Tags: `EN-301-549`, `EN-9.1.3.1`, `RGAA-9.3.1`, `RGAAv4`, `cat.aria`, `wcag131`, `wcag2a`

| URL | chromium | firefox | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- |
| olh/articles/?theme=olh | :white_check_mark: | :white_check_mark: | 1 | 1 | :white_check_mark: | 2 |

## color-contrast

Elements must meet minimum color contrast ratio thresholds

Tags: `ACT`, `EN-301-549`, `EN-9.1.4.3`, `RGAA-3.2.1`, `RGAAv4`, `TT13.c`, `TTv5`, `cat.color`, `wcag143`, `wcag2aa`

| URL | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ?theme=clean | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 21 |
| ?theme=olh | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |
| 404/?theme=clean | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 21 |
| 404/?theme=olh | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |
| contact/?theme=clean | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 21 |
| contact/?theme=olh | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |
| journals/?theme=clean | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 21 |
| journals/?theme=olh | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |
| olh/?theme=material | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 84 |
| olh/?theme=olh | 10 | 10 | 8 | 8 | 10 | 10 | 10 | 66 |
| olh/accessibility/?theme=material | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 21 |
| olh/accessibility/?theme=olh | 2 | 2 | :white_check_mark: | :white_check_mark: | 2 | 2 | 2 | 10 |
| olh/article/id/4403/?theme=material | 147 | 147 | 153 | 153 | 145 | 146 | 147 | 1038 |
| olh/article/id/4403/?theme=olh | 158 | 157 | 152 | 152 | 158 | 160 | 160 | 1097 |
| olh/article/id/4405/?theme=clean | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 63 |
| olh/article/id/4405/?theme=material | 278 | 278 | 282 | 282 | 277 | 278 | 278 | 1953 |
| olh/article/id/4405/?theme=olh | 292 | 292 | 273 | 273 | 292 | 292 | 292 | 2006 |
| olh/articles/?theme=material | 68 | 68 | 68 | 68 | 68 | 68 | 68 | 476 |
| olh/articles/?theme=olh | 4 | 4 | 1 | 1 | 3 | 3 | 4 | 20 |
| olh/collections/?theme=material | 48 | 48 | 50 | 48 | 40 | 51 | 48 | 333 |
| olh/collections/?theme=olh | 2 | 2 | :white_check_mark: | :white_check_mark: | 2 | 2 | 2 | 10 |
| olh/collections/846/?theme=material | 53 | 53 | 53 | 53 | 52 | 53 | 53 | 370 |
| olh/collections/846/?theme=olh | 52 | 52 | 50 | 50 | 52 | 52 | 52 | 360 |
| olh/contact/?theme=material  | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 63 |
| olh/contact/?theme=olh  | 2 | 2 | :white_check_mark: | :white_check_mark: | 2 | 2 | 2 | 10 |
| olh/editorialteam/?theme=material | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 126 |
| olh/editorialteam/?theme=olh | 17 | 17 | 15 | 15 | 15 | 17 | 17 | 113 |
| olh/issue/402/info/?theme=material | 22 | 22 | 22 | 22 | 22 | 22 | 22 | 154 |
| olh/issue/402/info/?theme=olh | 2 | 2 | 19 | 19 | 21 | 21 | 2 | 86 |
| olh/issue/409/info/?theme=material | 22 | 22 | 22 | 22 | 22 | 22 | 22 | 154 |
| olh/issue/409/info/?theme=olh | 2 | 2 | 19 | 19 | 21 | 21 | 2 | 86 |
| olh/issues/?theme=material | 22 | 22 | 22 | 22 | 22 | 22 | 22 | 154 |
| olh/issues/?theme=olh | 2 | 2 | :white_check_mark: | :white_check_mark: | 2 | 2 | 2 | 10 |
| olh/news/?theme=material | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 105 |
| olh/news/?theme=olh | 14 | 14 | 12 | 12 | 14 | 14 | 14 | 94 |
| olh/news/429/?theme=material | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 49 |
| olh/news/429/?theme=olh | 3 | 3 | 1 | 1 | 3 | 3 | 3 | 17 |
| olh/search/?theme=clean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 42 |
| olh/search/?theme=material | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 84 |
| olh/search/?theme=olh | 4 | 4 | 2 | 2 | 4 | 4 | 4 | 24 |
| olh/site/about/?theme=material | 13 | 13 | 13 | 13 | 13 | 13 | 13 | 91 |
| olh/site/about/?theme=olh | 16 | 16 | 10 | 10 | 16 | 16 | 16 | 100 |
| olh/site/author-guidelines/?theme=material | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 112 |
| olh/site/author-guidelines/?theme=olh | 15 | 15 | 13 | 13 | 15 | 15 | 15 | 101 |
| olh/site/journal-policies/?theme=material | 28 | 28 | 28 | 28 | 28 | 28 | 28 | 196 |
| olh/site/journal-policies/?theme=olh | 53 | 53 | 25 | 25 | 54 | 54 | 53 | 317 |
| olh/submissions/?theme=material | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 119 |
| olh/submissions/?theme=olh | 16 | 16 | 14 | 14 | 16 | 16 | 16 | 108 |

## document-title

Documents must have `<title>` element to aid in navigation

Tags: `ACT`, `EN-301-549`, `EN-9.2.4.2`, `RGAA-8.5.1`, `RGAAv4`, `TT12.a`, `TTv5`, `cat.text-alternatives`, `wcag242`, `wcag2a`

| URL | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 404/?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

## empty-heading

Headings should not be empty

Tags: `best-practice`, `cat.name-role-value`

| URL | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| ?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

## heading-order

Heading levels should only increase by one

Tags: `best-practice`, `cat.semantics`

| URL | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| olh/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/collections/846/?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/issues/?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

## html-has-lang

`<html>` element must have a lang attribute

Tags: `ACT`, `EN-301-549`, `EN-9.3.1.1`, `RGAA-8.3.1`, `RGAAv4`, `TT11.a`, `TTv5`, `cat.language`, `wcag2a`, `wcag311`

| URL | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| 404/?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| contact/?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| journals/?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

## image-alt

Images must have alternative text

Tags: `ACT`, `EN-301-549`, `EN-9.1.1.1`, `RGAA-1.1.1`, `RGAAv4`, `TT7.a`, `TT7.b`, `TTv5`, `cat.text-alternatives`, `section508`, `section508.22.a`, `wcag111`, `wcag2a`

| URL | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ?theme=clean | 22 | 22 | 22 | 22 | 22 | 22 | 22 | 154 |
| 404/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| contact/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| journals/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

## label

Form elements must have labels

Tags: `ACT`, `EN-301-549`, `EN-9.4.1.2`, `RGAA-11.1.1`, `RGAAv4`, `TT5.c`, `TTv5`, `cat.forms`, `section508`, `section508.22.n`, `wcag2a`, `wcag412`

| URL | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| contact/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| contact/?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/articles/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/contact/?theme=material  | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |
| olh/contact/?theme=olh  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/search/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

## landmark-complementary-is-top-level

Aside should not be contained in another landmark

Tags: `best-practice`, `cat.semantics`

| URL | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| olh/articles/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/articles/?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/collections/846/?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/issue/402/info/?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/issue/409/info/?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/site/about/?theme=olh | 1 | 1 | :white_check_mark: | :white_check_mark: | 1 | 1 | 1 | 5 |
| olh/site/journal-policies/?theme=olh | 1 | 1 | :white_check_mark: | :white_check_mark: | 1 | 1 | 1 | 5 |

## landmark-unique

Landmarks should have a unique role or role/label/title (i.e. accessible name) combination

Tags: `best-practice`, `cat.semantics`

| URL | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

## link-name

Links must have discernible text

Tags: `ACT`, `EN-301-549`, `EN-9.2.4.4`, `EN-9.4.1.2`, `RGAA-6.2.1`, `RGAAv4`, `TT6.a`, `TTv5`, `cat.name-role-value`, `section508`, `section508.22.a`, `wcag244`, `wcag2a`, `wcag412`

| URL | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| olh/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/accessibility/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/article/id/4403/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/article/id/4405/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/articles/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/collections/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/collections/846/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/contact/?theme=material  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/editorialteam/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/issue/402/info/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/issue/409/info/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/issues/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/news/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/news/429/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/search/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/site/about/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/site/author-guidelines/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/site/journal-policies/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/submissions/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

## list

`<ul>` and `<ol>` must only directly contain `<li>`, `<script>` or `<template>` elements

Tags: `EN-301-549`, `EN-9.1.3.1`, `RGAA-9.3.1`, `RGAAv4`, `cat.structure`, `wcag131`, `wcag2a`

| URL | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| olh/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/accessibility/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/article/id/4403/?theme=clean | 1 | 1 | 2 | 2 | 2 | 1 | 1 | 10 |
| olh/article/id/4403/?theme=material | :white_check_mark: | :white_check_mark: | 1 | 1 | :white_check_mark: | :white_check_mark: | :white_check_mark: | 2 |
| olh/article/id/4405/?theme=clean | 2 | 2 | 3 | 3 | 3 | 2 | 2 | 17 |
| olh/article/id/4405/?theme=material | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 9 |
| olh/article/id/4405/?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/articles/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/collections/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/collections/846/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/collections/846/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/contact/?theme=clean  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/editorialteam/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/issue/402/info/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/issue/402/info/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/issue/409/info/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/issue/409/info/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/issues/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/news/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/news/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/news/429/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/search/?theme=clean | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |
| olh/search/?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/site/about/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/site/author-guidelines/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/site/journal-policies/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/submissions/?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

## listitem

`<li>` elements must be contained in a `<ul>` or `<ol>`

Tags: `EN-301-549`, `EN-9.1.3.1`, `RGAA-9.3.1`, `RGAAv4`, `cat.structure`, `wcag131`, `wcag2a`

| URL | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| olh/articles/?theme=olh | :white_check_mark: | :white_check_mark: | 1 | 1 | 1 | 1 | :white_check_mark: | 4 |

## page-has-heading-one

Page should contain a level-one heading

Tags: `best-practice`, `cat.semantics`

| URL | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ?theme=clean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| ?theme=olh | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

## scrollable-region-focusable

Scrollable region must have keyboard access

Tags: `EN-301-549`, `EN-9.2.1.1`, `EN-9.2.1.3`, `RGAA-7.3.2`, `RGAAv4`, `TT4.a`, `TTv5`, `cat.keyboard`, `wcag211`, `wcag213`, `wcag2a`

| URL | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | Total |
| --- | --- | --- | --- | --- | --- |
| olh/article/id/4405/?theme=clean | 1 | 1 | :white_check_mark: | 1 | 3 |
| olh/article/id/4405/?theme=material | :white_check_mark: | 1 | :white_check_mark: | :white_check_mark: | 1 |
| olh/submissions/?theme=material | 1 | 1 | 1 | 1 | 4 |

## select-name

Select element must have an accessible name

Tags: `ACT`, `EN-301-549`, `EN-9.4.1.2`, `RGAA-11.1.1`, `RGAAv4`, `TT5.c`, `TTv5`, `cat.forms`, `section508`, `section508.22.n`, `wcag2a`, `wcag412`

| URL | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| olh/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/accessibility/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/article/id/4403/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/article/id/4405/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/articles/?theme=clean | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |
| olh/articles/?theme=material | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 21 |
| olh/articles/?theme=olh | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |
| olh/collections/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/collections/846/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/contact/?theme=material  | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |
| olh/editorialteam/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/issue/402/info/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/issue/409/info/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/issues/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/news/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/news/429/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/search/?theme=material | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |
| olh/site/about/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/site/author-guidelines/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/site/journal-policies/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| olh/submissions/?theme=material | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-404-theme-clean"></span>
## 404/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 21 |
| image-alt | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-404-theme-olh"></span>
## 404/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |
| document-title | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| html-has-lang | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-theme-clean"></span>
## ?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 21 |
| empty-heading | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| image-alt | 22 | 22 | 22 | 22 | 22 | 22 | 22 | 154 |
| page-has-heading-one | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-theme-olh"></span>
## ?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |
| empty-heading | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| html-has-lang | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| landmark-unique | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| page-has-heading-one | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-contact-theme-clean"></span>
## contact/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 21 |
| image-alt | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| label | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-contact-theme-olh"></span>
## contact/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |
| html-has-lang | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| label | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-journals-theme-clean"></span>
## journals/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 21 |
| image-alt | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-journals-theme-olh"></span>
## journals/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |
| html-has-lang | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-theme-clean"></span>
## olh/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| heading-order | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| landmark-unique | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-theme-material"></span>
## olh/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 84 |
| heading-order | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| select-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-theme-olh"></span>
## olh/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 10 | 10 | 8 | 8 | 10 | 10 | 10 | 66 |
| heading-order | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| label | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| landmark-unique | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-accessibility-theme-clean"></span>
## olh/accessibility/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-accessibility-theme-material"></span>
## olh/accessibility/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 21 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| select-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-accessibility-theme-olh"></span>
## olh/accessibility/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 2 | 2 | :white_check_mark: | :white_check_mark: | 2 | 2 | 2 | 10 |

<span id="url-olh-article-id-4403-theme-clean"></span>
## olh/article/id/4403/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| list | 1 | 1 | 2 | 2 | 2 | 1 | 1 | 10 |

<span id="url-olh-article-id-4403-theme-material"></span>
## olh/article/id/4403/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 147 | 147 | 153 | 153 | 145 | 146 | 147 | 1038 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| list | :white_check_mark: | :white_check_mark: | 1 | 1 | :white_check_mark: | :white_check_mark: | :white_check_mark: | 2 |
| select-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-article-id-4403-theme-olh"></span>
## olh/article/id/4403/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 158 | 157 | 152 | 152 | 158 | 160 | 160 | 1097 |

<span id="url-olh-article-id-4405-theme-clean"></span>
## olh/article/id/4405/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 63 |
| list | 2 | 2 | 3 | 3 | 3 | 2 | 2 | 17 |
| scrollable-region-focusable | :white_check_mark: | :white_check_mark: | 1 | 1 | :white_check_mark: | 1 | :white_check_mark: | 3 |

<span id="url-olh-article-id-4405-theme-material"></span>
## olh/article/id/4405/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 278 | 278 | 282 | 282 | 277 | 278 | 278 | 1953 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| list | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 9 |
| scrollable-region-focusable | :white_check_mark: | :white_check_mark: | :white_check_mark: | 1 | :white_check_mark: | :white_check_mark: | :white_check_mark: | 1 |
| select-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-article-id-4405-theme-olh"></span>
## olh/article/id/4405/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 292 | 292 | 273 | 273 | 292 | 292 | 292 | 2006 |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-articles-theme-clean"></span>
## olh/articles/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| select-name | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |

<span id="url-olh-articles-theme-material"></span>
## olh/articles/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 68 | 68 | 68 | 68 | 68 | 68 | 68 | 476 |
| label | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| landmark-complementary-is-top-level | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| select-name | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 21 |

<span id="url-olh-articles-theme-olh"></span>
## olh/articles/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aria-required-children | :white_check_mark: | :white_check_mark: | 1 | 1 | 1 | 1 | :white_check_mark: | 4 |
| aria-required-parent | :white_check_mark: | :white_check_mark: | 1 | 1 | 1 | 1 | :white_check_mark: | 4 |
| color-contrast | 4 | 4 | 1 | 1 | 3 | 3 | 4 | 20 |
| landmark-complementary-is-top-level | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| listitem | :white_check_mark: | :white_check_mark: | 1 | 1 | 1 | 1 | :white_check_mark: | 4 |
| select-name | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |

<span id="url-olh-collections-846-theme-clean"></span>
## olh/collections/846/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-collections-846-theme-material"></span>
## olh/collections/846/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 53 | 53 | 53 | 53 | 52 | 53 | 53 | 370 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| select-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-collections-846-theme-olh"></span>
## olh/collections/846/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 52 | 52 | 50 | 50 | 52 | 52 | 52 | 360 |
| heading-order | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| landmark-complementary-is-top-level | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-collections-theme-clean"></span>
## olh/collections/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-collections-theme-material"></span>
## olh/collections/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 48 | 48 | 50 | 48 | 40 | 51 | 48 | 333 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| select-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-collections-theme-olh"></span>
## olh/collections/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 2 | 2 | :white_check_mark: | :white_check_mark: | 2 | 2 | 2 | 10 |

<span id="url-olh-contact-theme-clean"></span>
## olh/contact/?theme=clean 

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-contact-theme-material"></span>
## olh/contact/?theme=material 

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 63 |
| label | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| select-name | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |

<span id="url-olh-contact-theme-olh"></span>
## olh/contact/?theme=olh 

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 2 | 2 | :white_check_mark: | :white_check_mark: | 2 | 2 | 2 | 10 |
| label | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-editorialteam-theme-clean"></span>
## olh/editorialteam/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-editorialteam-theme-material"></span>
## olh/editorialteam/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 126 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| select-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-editorialteam-theme-olh"></span>
## olh/editorialteam/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 17 | 17 | 15 | 15 | 15 | 17 | 17 | 113 |

<span id="url-olh-issue-402-info-theme-clean"></span>
## olh/issue/402/info/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-issue-402-info-theme-material"></span>
## olh/issue/402/info/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 22 | 22 | 22 | 22 | 22 | 22 | 22 | 154 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| select-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-issue-402-info-theme-olh"></span>
## olh/issue/402/info/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 2 | 2 | 19 | 19 | 21 | 21 | 2 | 86 |
| landmark-complementary-is-top-level | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-issue-409-info-theme-clean"></span>
## olh/issue/409/info/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-issue-409-info-theme-material"></span>
## olh/issue/409/info/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 22 | 22 | 22 | 22 | 22 | 22 | 22 | 154 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| select-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-issue-409-info-theme-olh"></span>
## olh/issue/409/info/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 2 | 2 | 19 | 19 | 21 | 21 | 2 | 86 |
| landmark-complementary-is-top-level | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-issues-theme-clean"></span>
## olh/issues/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-issues-theme-material"></span>
## olh/issues/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 22 | 22 | 22 | 22 | 22 | 22 | 22 | 154 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| select-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-issues-theme-olh"></span>
## olh/issues/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 2 | 2 | :white_check_mark: | :white_check_mark: | 2 | 2 | 2 | 10 |
| heading-order | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-news-429-theme-clean"></span>
## olh/news/429/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-news-429-theme-material"></span>
## olh/news/429/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 49 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| select-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-news-429-theme-olh"></span>
## olh/news/429/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 3 | 3 | 1 | 1 | 3 | 3 | 3 | 17 |

<span id="url-olh-news-theme-clean"></span>
## olh/news/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-news-theme-material"></span>
## olh/news/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 105 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| select-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-news-theme-olh"></span>
## olh/news/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 14 | 14 | 12 | 12 | 14 | 14 | 14 | 94 |

<span id="url-olh-search-theme-clean"></span>
## olh/search/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 42 |
| list | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |

<span id="url-olh-search-theme-material"></span>
## olh/search/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 84 |
| label | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| select-name | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |

<span id="url-olh-search-theme-olh"></span>
## olh/search/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 4 | 4 | 2 | 2 | 4 | 4 | 4 | 24 |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-site-about-theme-clean"></span>
## olh/site/about/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-site-about-theme-material"></span>
## olh/site/about/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 13 | 13 | 13 | 13 | 13 | 13 | 13 | 91 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| select-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-site-about-theme-olh"></span>
## olh/site/about/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 16 | 16 | 10 | 10 | 16 | 16 | 16 | 100 |
| landmark-complementary-is-top-level | 1 | 1 | :white_check_mark: | :white_check_mark: | 1 | 1 | 1 | 5 |

<span id="url-olh-site-author-guidelines-theme-clean"></span>
## olh/site/author-guidelines/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-site-author-guidelines-theme-material"></span>
## olh/site/author-guidelines/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 112 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| select-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-site-author-guidelines-theme-olh"></span>
## olh/site/author-guidelines/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 15 | 15 | 13 | 13 | 15 | 15 | 15 | 101 |

<span id="url-olh-site-journal-policies-theme-clean"></span>
## olh/site/journal-policies/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-site-journal-policies-theme-material"></span>
## olh/site/journal-policies/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 28 | 28 | 28 | 28 | 28 | 28 | 28 | 196 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| select-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-site-journal-policies-theme-olh"></span>
## olh/site/journal-policies/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 53 | 53 | 25 | 25 | 54 | 54 | 53 | 317 |
| landmark-complementary-is-top-level | 1 | 1 | :white_check_mark: | :white_check_mark: | 1 | 1 | 1 | 5 |

<span id="url-olh-submissions-theme-clean"></span>
## olh/submissions/?theme=clean

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| list | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-submissions-theme-material"></span>
## olh/submissions/?theme=material

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 119 |
| link-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| scrollable-region-focusable | :white_check_mark: | :white_check_mark: | 1 | 1 | 1 | 1 | :white_check_mark: | 4 |
| select-name | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |

<span id="url-olh-submissions-theme-olh"></span>
## olh/submissions/?theme=olh

| Rule | chromium | firefox | mobile-chrome | mobile-safari | tablet-chrome | tablet-safari | webkit | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| color-contrast | 16 | 16 | 14 | 14 | 16 | 16 | 16 | 108 |
