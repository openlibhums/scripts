import json
import os
from html import unescape
from urllib.parse import urlparse

from django.conf import settings
from django.test import Client
from django.test.utils import override_settings
from django.utils import translation
from bs4 import BeautifulSoup

from utils.management.base import ProfiledCommand


class Command(ProfiledCommand):
    """CLI interface for generating a markdown file comparing page titles across themes."""

    help = "Generates a markdown file with a table comparing page titles across OLH, Material, and Clean themes."

    DEFAULT_URLS_JSON = os.path.join(
        settings.BASE_DIR, "plugins", "scripts", "a11y", "test_inputs", "page_title_urls.json"
    )
    DEFAULT_OUTPUT = os.path.join(
        settings.BASE_DIR, "plugins", "scripts", "a11y", "results", "markdown", "page_titles.md"
    )

    def add_arguments(self, parser):
        """Adds arguments to Django's management command-line parser."""
        super().add_arguments(parser)
        parser.add_argument(
            "--output",
            default=None,
            metavar="PATH",
            help=f"Output markdown file path (default: {self.DEFAULT_OUTPUT})",
        )
        parser.add_argument(
            "--urls-json",
            default=None,
            metavar="PATH",
            help=f"Path to JSON file containing list of URLs to check (default: {self.DEFAULT_URLS_JSON})",
        )

    def extract_title_from_html(self, html_content):
        """Extract the title from HTML content."""
        try:
            soup = BeautifulSoup(html_content, "html.parser")
            title_tag = soup.find("title")
            if title_tag:
                return unescape(title_tag.get_text().strip())
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"Error parsing HTML: {e}"))
        return None

    def normalize_url_for_client(self, url):
        """Normalize URL to make it work with Django test client."""
        parsed = urlparse(url)
        # Extract path and query string
        path = parsed.path
        if parsed.query:
            path += f"?{parsed.query}"
        return path, parsed.netloc

    def get_title_for_theme(self, url, theme):
        """Get the page title for a given URL and theme."""
        try:
            with override_settings(DEBUG=True, IN_TEST_RUNNER=True):
                client = Client()
                path, server_name = self.normalize_url_for_client(url)

                # Add theme parameter
                path = f"{path}?theme={theme}"

                # Use SERVER_NAME if it's an absolute URL (domain mode)
                kwargs = {"follow": True}
                if server_name:
                    kwargs["SERVER_NAME"] = server_name

                response = client.get(path, **kwargs)

                if response.status_code == 200:
                    title = self.extract_title_from_html(response.content)
                    return title
                else:
                    return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {str(e)}"

    def load_urls_from_json(self, path):
        """Load list of URLs from a JSON file. Returns list of URL strings."""
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError(f"JSON file must contain a list of URLs, got {type(data)}")
        return [str(u) for u in data]

    def handle(self, *args, **options):
        """Main command handler."""
        with override_settings(DEBUG=True, IN_TEST_RUNNER=True):
            with translation.override(settings.LANGUAGE_CODE):
                output_file = options.get("output") or self.DEFAULT_OUTPUT
                urls_json = options.get("urls_json") or self.DEFAULT_URLS_JSON

                try:
                    all_urls = self.load_urls_from_json(urls_json)
                except FileNotFoundError:
                    self.stderr.write(
                        self.style.ERROR(f"URLs file not found: {urls_json}")
                    )
                    return
                except (json.JSONDecodeError, ValueError) as e:
                    self.stderr.write(
                        self.style.ERROR(f"Invalid URLs JSON: {e}")
                    )
                    return

                # Preserve order by filtering duplicates while maintaining order
                seen = set()
                deduped = []
                for url in all_urls:
                    if url not in seen:
                        seen.add(url)
                        deduped.append(url)
                all_urls = deduped

                self.stdout.write(f"Processing {len(all_urls)} URL(s)")

                # Get titles for each URL in each theme
                themes = ["olh", "material", "clean"]
                results = []

                self.stdout.write("Fetching titles for each URL and theme...")
                for i, url in enumerate(all_urls, 1):
                    self.stdout.write(f"Processing {i}/{len(all_urls)}: {url}")

                    titles = {}
                    for theme in themes:
                        title = self.get_title_for_theme(url, theme)
                        titles[theme] = title

                    # Check if all titles are identical
                    # Get all title values (including errors)
                    all_title_values = [titles[t] for t in themes if titles[t]]

                    # All identical if all titles are the same (including if they're all errors)
                    if len(all_title_values) == len(themes):
                        all_identical = len(set(all_title_values)) <= 1
                    else:
                        all_identical = False

                    results.append(
                        {
                            "url": url,
                            "titles": titles,
                            "all_identical": all_identical,
                        }
                    )

                def escape_markdown(text):
                    if not text or text.startswith("Error"):
                        return text or "N/A"
                    return text.replace("|", "\\|").replace("\n", " ")

                # Build all row data before writing so column widths can be computed
                headers = ["URL", "OLH Title", "Material Title", "Clean Title", "All Identical", "Human Review"]
                rows = []
                for result in results:
                    url = result["url"]
                    titles = result["titles"]
                    all_identical = ":white_check_mark:" if result["all_identical"] else ":x:"
                    page_link = f"[{url}]({url})"
                    olh_title = escape_markdown(titles.get("olh", "N/A"))
                    material_title = escape_markdown(titles.get("material", "N/A"))
                    clean_title = escape_markdown(titles.get("clean", "N/A"))
                    rows.append([page_link, olh_title, material_title, clean_title, all_identical, ""])

                # Calculate column widths for vertical alignment
                col_widths = [len(h) for h in headers]
                for row in rows:
                    for i, cell in enumerate(row):
                        col_widths[i] = max(col_widths[i], len(cell))

                # Generate markdown table
                self.stdout.write(f"Generating markdown file: {output_file}")
                output_dir = os.path.dirname(output_file)
                if output_dir:
                    os.makedirs(output_dir, exist_ok=True)
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write("# Page Title Comparison Across Themes\n\n")
                    f.write(f"Generated from {len(all_urls)} URL(s).\n\n")

                    header_row = "| " + " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers)) + " |"
                    separator_row = "| " + " | ".join("-" * col_widths[i] for i in range(len(headers))) + " |"
                    f.write(header_row + "\n")
                    f.write(separator_row + "\n")

                    for row in rows:
                        data_row = "| " + " | ".join(cell.ljust(col_widths[i]) for i, cell in enumerate(row)) + " |"
                        f.write(data_row + "\n")

                self.stdout.write(
                    self.style.SUCCESS(f"Successfully generated {output_file}")
                )
