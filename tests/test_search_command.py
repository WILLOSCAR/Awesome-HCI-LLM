import csv
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import typer

from paper_cli.commands.search import search_papers
from paper_cli.core.models import Paper
from paper_cli.core.storage import PaperStorage


class TestSearchCommand(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name)
        self.csv_path = self.repo / "papers.csv"

        with self.csv_path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=PaperStorage.FIELDNAMES, quoting=csv.QUOTE_ALL)
            w.writeheader()
            w.writerow(Paper(title="old", date="2023.01", topic="HCI").to_csv_row())
            w.writerow(Paper(title="new", date="2024.12", topic="HCI").to_csv_row())
            w.writerow(Paper(title="no date", date="", topic="HCI").to_csv_row())

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_search_recent_sorting(self) -> None:
        captured = {}

        def _capture(papers, title, show_all):  # noqa: ANN001
            captured["titles"] = [p.title for p in papers]
            captured["title"] = title

        with patch("paper_cli.commands.search.display_papers_table", side_effect=_capture):
            search_papers(recent=True, limit=0, repo_path=self.repo)

        self.assertEqual(captured["titles"], ["new", "old", "no date"])
        self.assertIn("sort=recent", captured["title"])

    def test_search_rejects_invalid_from_date(self) -> None:
        with patch("paper_cli.commands.search.print_error") as print_error:
            with self.assertRaises(typer.Exit) as cm:
                search_papers(date_from="2024-01", repo_path=self.repo)

        self.assertEqual(cm.exception.exit_code, 2)
        print_error.assert_called_once()

    def test_search_rejects_inverted_date_range(self) -> None:
        with patch("paper_cli.commands.search.print_error") as print_error:
            with self.assertRaises(typer.Exit) as cm:
                search_papers(date_from="2024.12", date_to="2024.01", repo_path=self.repo)

        self.assertEqual(cm.exception.exit_code, 2)
        print_error.assert_called_once()


if __name__ == "__main__":
    unittest.main()
