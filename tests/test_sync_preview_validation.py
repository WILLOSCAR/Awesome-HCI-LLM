import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import typer

from paper_cli.commands.preview import preview_markdown
from paper_cli.commands.sync import sync_readme


class TestSyncPreviewValidation(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_sync_requires_papers_csv(self) -> None:
        with patch("paper_cli.commands.sync.print_error") as print_error:
            with self.assertRaises(typer.Exit) as cm:
                sync_readme(readme_only=True, repo_path=self.repo)

        self.assertEqual(cm.exception.exit_code, 1)
        print_error.assert_called_once()

    def test_preview_requires_papers_csv(self) -> None:
        with patch("paper_cli.commands.preview.print_error") as print_error:
            with self.assertRaises(typer.Exit) as cm:
                preview_markdown(repo_path=self.repo)

        self.assertEqual(cm.exception.exit_code, 1)
        print_error.assert_called_once()


if __name__ == "__main__":
    unittest.main()
