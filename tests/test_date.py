import unittest

from paper_cli.utils.date import extract_yyyymm, date_key


class TestDateHelpers(unittest.TestCase):
    def test_extract_yyyymm_strict(self) -> None:
        self.assertEqual(extract_yyyymm("2024.02"), "2024.02")
        self.assertEqual(date_key("2024.02"), (2024, 2))

    def test_extract_yyyymm_from_legacy_strings(self) -> None:
        # Legacy rows sometimes store extra text around the date.
        self.assertEqual(extract_yyyymm("arXiv(v2) 2023.10"), "2023.10")
        self.assertEqual(extract_yyyymm("2023.11(v2)"), "2023.11")

    def test_extract_yyyymm_invalid(self) -> None:
        self.assertIsNone(extract_yyyymm(""))
        self.assertIsNone(extract_yyyymm("not-a-date"))
        self.assertIsNone(extract_yyyymm("2023.13"))


if __name__ == "__main__":
    unittest.main()

