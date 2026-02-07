import csv
import tempfile
import unittest
from pathlib import Path

from paper_cli.core.models import Paper
from paper_cli.core.storage import PaperStorage


class TestPaperStorageExists(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.csv_path = Path(self._tmp.name) / "papers.csv"
        self.storage = PaperStorage(self.csv_path)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def _write_rows(self, papers: list[Paper]) -> None:
        # PaperStorage.add_paper appends; for tests we want deterministic ordering.
        with self.csv_path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=PaperStorage.FIELDNAMES, quoting=csv.QUOTE_ALL)
            w.writeheader()
            for p in papers:
                w.writerow(p.to_csv_row())

    def test_exists_matches_doi_across_urls(self) -> None:
        self._write_rows(
            [
                Paper(
                    title="CAvatar",
                    doi="10.1145/3631424",
                    link="https://doi.org/10.1145/3631424",
                    topic="HCI",
                )
            ]
        )
        self.assertTrue(self.storage.exists("https://dl.acm.org/doi/pdf/10.1145/3631424"))
        self.assertTrue(self.storage.exists("10.1145/3631424"))

    def test_exists_matches_arxiv_id(self) -> None:
        self._write_rows(
            [
                Paper(
                    title="A-MEM",
                    link="http://arxiv.org/abs/2502.12110v1",
                    topic="Memory",
                )
            ]
        )
        self.assertTrue(self.storage.exists("2502.12110"))
        self.assertTrue(self.storage.exists("https://arxiv.org/abs/2502.12110v2"))

    def test_exists_does_not_misclassify_doi_as_arxiv(self) -> None:
        # Regression: avoid treating ACM DOIs like 10.1145/3706598.3713728 as arXiv IDs.
        self._write_rows([])
        self.assertFalse(self.storage.exists("10.1145/3706598.3713728"))

    def test_exists_matches_doi_wrapped_in_parentheses(self) -> None:
        self._write_rows(
            [
                Paper(
                    title="CAvatar",
                    doi="10.1145/3631424",
                    link="https://doi.org/10.1145/3631424",
                    topic="HCI",
                )
            ]
        )
        self.assertTrue(self.storage.exists("(10.1145/3631424)"))

    def test_exists_matches_normalized_non_doi_links(self) -> None:
        self._write_rows(
            [
                Paper(
                    title="Example",
                    link="https://Example.com/paper/abc/",
                    topic="HCI",
                )
            ]
        )
        self.assertTrue(self.storage.exists("https://example.com/paper/abc"))


if __name__ == "__main__":
    unittest.main()
