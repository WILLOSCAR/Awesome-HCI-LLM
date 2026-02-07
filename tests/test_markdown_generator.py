import csv
import tempfile
import unittest
from pathlib import Path

from paper_cli.core.markdown import MarkdownGenerator
from paper_cli.core.models import Paper
from paper_cli.core.storage import PaperStorage


class TestMarkdownGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name)
        self.csv_path = self.repo / "papers.csv"
        self.readme_path = self.repo / "README.md"

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def _write_rows(self, papers: list[Paper]) -> None:
        with self.csv_path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=PaperStorage.FIELDNAMES, quoting=csv.QUOTE_ALL)
            w.writeheader()
            for p in papers:
                w.writerow(p.to_csv_row())

    def test_get_diff_reports_removed_topics(self) -> None:
        self._write_rows([Paper(title="new", topic="A")])
        self.readme_path.write_text(
            "# Collection\n\n# B\n<!-- TABLE_START: B -->\nold\n<!-- TABLE_END: B -->\n",
            encoding="utf-8",
        )

        md = MarkdownGenerator(self.csv_path, self.readme_path)
        diff = md.get_diff()

        self.assertIn("A: NEW", diff)
        self.assertIn("B: REMOVED", diff)

    def test_update_readme_removes_stale_topic_sections(self) -> None:
        self._write_rows([Paper(title="new", topic="A")])
        self.readme_path.write_text(
            "# Collection\n\n# B\n<!-- TABLE_START: B -->\nold\n<!-- TABLE_END: B -->\n",
            encoding="utf-8",
        )

        md = MarkdownGenerator(self.csv_path, self.readme_path)
        md.update_readme()
        content = self.readme_path.read_text(encoding="utf-8")

        self.assertNotIn("TABLE_START: B", content)
        self.assertNotIn("# B", content)
        self.assertIn("TABLE_START: A", content)

    def test_generate_tables_ignores_blank_topics(self) -> None:
        self._write_rows(
            [
                Paper(title="blank", topic="   "),
                Paper(title="valid", topic="Memory"),
            ]
        )

        md = MarkdownGenerator(self.csv_path, self.readme_path)
        tables = md.generate_tables_by_topic()

        self.assertEqual(set(tables.keys()), {"Memory"})

    def test_generate_tables_escapes_table_breaking_characters(self) -> None:
        self._write_rows(
            [
                Paper(
                    source="CHI 2024",
                    title="A | B",
                    authors="Alice | Bob, Charlie",
                    link="https://example.com/paper",
                    tag="x|y",
                    subjects="HCI|LLM",
                    additional_info="line1\nline2",
                    date="2024.01",
                    topic="Memory",
                )
            ]
        )

        md = MarkdownGenerator(self.csv_path, self.readme_path)
        table = md.generate_tables_by_topic()["Memory"]

        self.assertIn("A \\| B", table)
        self.assertIn("x\\|y", table)
        self.assertIn("line1<br>line2", table)

    def test_format_source_does_not_duplicate_journal_ref(self) -> None:
        md = MarkdownGenerator(self.csv_path, self.readme_path)
        source = md._format_source_column(
            source="arXiv(v1) 2024 (ICLR 2024)",
            link="https://arxiv.org/abs/2401.00001v1",
            journal_ref="ICLR 2024",
        )
        self.assertEqual(source, "arXiv(v1) 2024 (ICLR 2024)")


if __name__ == "__main__":
    unittest.main()
