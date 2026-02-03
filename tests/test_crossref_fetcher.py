import unittest

from paper_cli.core.fetchers.crossref import CrossRefFetcher


class DummyCrossRefFetcher(CrossRefFetcher):
    def _fetch_ieee_doi(self, url: str):  # type: ignore[override]
        return "10.1109/TVCG.2023.1234567"


class TestCrossRefFetcher(unittest.TestCase):
    def test_extract_doi_from_acm_url(self) -> None:
        f = CrossRefFetcher()
        self.assertEqual(
            f._extract_doi("https://dl.acm.org/doi/pdf/10.1145/3631424"),
            "10.1145/3631424",
        )

    def test_extract_doi_from_bare(self) -> None:
        f = CrossRefFetcher()
        self.assertEqual(f._extract_doi("10.1145/3631424"), "10.1145/3631424")

    def test_extract_ieee_doi_from_html_meta(self) -> None:
        f = CrossRefFetcher()
        html = '<meta name="citation_doi" content="10.1109/TVCG.2023.1234567" />'
        self.assertEqual(f._extract_ieee_doi_from_html(html), "10.1109/TVCG.2023.1234567")

    def test_extract_ieee_doi_from_html_multiple_tokens(self) -> None:
        # Some IEEE pages embed the DOI in multiple places, e.g. in URLs with query params.
        f = CrossRefFetcher()
        html = '... 10.1109/CVPR.2016.90 ... 10.1109/CVPR.2016.90&orderBeanReset=true ...'
        self.assertEqual(f._extract_ieee_doi_from_html(html), "10.1109/CVPR.2016.90")

    def test_extract_doi_from_ieee_document_url_via_fetch(self) -> None:
        f = DummyCrossRefFetcher()
        self.assertEqual(
            f._extract_doi("https://ieeexplore.ieee.org/document/9878378"),
            "10.1109/TVCG.2023.1234567",
        )


if __name__ == "__main__":
    unittest.main()
