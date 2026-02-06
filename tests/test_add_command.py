import csv
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import typer

from paper_cli.commands.add import add_paper
from paper_cli.core.models import Paper
from paper_cli.core.storage import PaperStorage


class _FakeFetcher:
    def fetch(self, url: str, custom_tag=None) -> Paper:  # noqa: ANN001
        return Paper(
            source="IEEE VR 2024",
            title="Existing IEEE Paper",
            authors="A. Author",
            doi="10.1109/TVCG.2023.1234567",
            link="https://doi.org/10.1109/TVCG.2023.1234567",
            tag="IEEE",
            date="2024.01",
            topic="",
        )


class _FakeRegistry:
    def detect_source(self, url: str) -> str:  # noqa: ARG002
        return "IEEE"

    def get_fetcher(self, url: str) -> _FakeFetcher:  # noqa: ARG002
        return _FakeFetcher()


class TestAddCommand(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name)
        self.csv_path = self.repo / "papers.csv"

        with self.csv_path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=PaperStorage.FIELDNAMES, quoting=csv.QUOTE_ALL)
            w.writeheader()
            w.writerow(
                Paper(
                    source="IEEE VR 2024",
                    title="Existing IEEE Paper",
                    authors="A. Author",
                    doi="10.1109/TVCG.2023.1234567",
                    link="https://doi.org/10.1109/TVCG.2023.1234567",
                    tag="IEEE",
                    topic="VR",
                ).to_csv_row()
            )

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_add_detects_duplicate_after_metadata_fetch(self) -> None:
        with patch("paper_cli.commands.add.FetcherRegistry", return_value=_FakeRegistry()):
            with patch("paper_cli.commands.add.typer.confirm", return_value=False) as confirm:
                with self.assertRaises(typer.Exit) as cm:
                    add_paper(
                        link="https://ieeexplore.ieee.org/document/9878378",
                        topic="VR",
                        no_sync=True,
                        no_git=True,
                        repo_path=self.repo,
                    )

        self.assertEqual(cm.exception.exit_code, 0)
        self.assertEqual(confirm.call_count, 1)

        # Still one data row + header.
        with self.csv_path.open("r", encoding="utf-8", newline="") as f:
            rows = list(csv.reader(f))
        self.assertEqual(len(rows), 2)


if __name__ == "__main__":
    unittest.main()
