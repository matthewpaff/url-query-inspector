from pathlib import Path
import unittest

from url_query_lab.core import inspect_url
from url_query_lab.fixture_check import check


class UrlTests(unittest.TestCase):
    def test_repeated_parameters_blanks_and_utf8(self):
        result = inspect_url("http://EXAMPLE.com:8080/?q=caf%C3%A9&tag=a&tag=b&empty=")
        self.assertEqual(result["host"], "example.com")
        self.assertEqual(result["port"], 8080)
        self.assertEqual(result["query"], {"q": ["café"], "tag": ["a", "b"], "empty": [""]})

    def test_rejects_bad_schemes_credentials_and_percent_escapes(self):
        for url in ("javascript:alert(1)", "https://u:p@example.com", "https://example.com?q=%GG", "https://example.com?q=%FF", "https://example.com:0"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                inspect_url(url)

    def test_default_path_and_ports(self):
        self.assertEqual(inspect_url("http://example.com")["path"], "/")
        self.assertEqual(inspect_url("http://example.com")["port"], 80)

    def test_all_generated_fixtures(self):
        self.assertGreaterEqual(check(Path(__file__).resolve().parents[1] / "fixtures" / "cases.jsonl", inspect_url), 350)


if __name__ == "__main__":
    unittest.main()
