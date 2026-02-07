"""Git operations for paper CLI."""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import List


class GitOperations:
    """Git 操作封装，负责 add/commit/push。"""

    def __init__(self, repo_path: Path):
        self.repo_path = Path(repo_path)
        self.last_error = ""

    def _run(self, args: List[str], *, check: bool = False) -> subprocess.CompletedProcess[str]:
        """Run a git command and keep the most recent stderr/stdout on failure."""
        try:
            result = subprocess.run(
                args,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=check,
            )
        except subprocess.CalledProcessError as exc:
            self.last_error = (exc.stderr or exc.stdout or str(exc)).strip()
            raise
        except OSError as exc:
            self.last_error = str(exc)
            raise

        if result.returncode != 0:
            self.last_error = (result.stderr or result.stdout or "").strip()
        else:
            self.last_error = ""

        return result

    def is_git_repo(self) -> bool:
        """检查是否是 Git 仓库。"""
        try:
            result = self._run(["git", "rev-parse", "--git-dir"])
        except OSError:
            return False
        return result.returncode == 0

    def has_changes(self) -> bool:
        """检查是否有未提交的更改。"""
        try:
            result = self._run(["git", "status", "--porcelain"])
        except OSError:
            return False
        if result.returncode != 0:
            return False
        return bool(result.stdout.strip())

    def add_files(self, files: List[str]) -> bool:
        """添加文件到暂存区。"""
        try:
            for file in files:
                self._run(["git", "add", file], check=True)
            return True
        except (subprocess.CalledProcessError, OSError):
            return False

    def commit(self, message: str) -> bool:
        """提交更改。"""
        try:
            self._run(["git", "commit", "-m", message], check=True)
            return True
        except (subprocess.CalledProcessError, OSError):
            return False

    def push(self) -> bool:
        """推送到远程。"""
        try:
            self._run(["git", "push"], check=True)
            return True
        except (subprocess.CalledProcessError, OSError):
            return False

    def add_commit_push(
        self,
        files: List[str],
        message: str,
        push: bool = True,
    ) -> tuple[bool, str]:
        """添加文件、提交并推送。"""
        if not self.is_git_repo():
            return False, self.last_error or "Not a git repository"

        if not self.add_files(files):
            return False, self.last_error or "Failed to add files"

        if not self.commit(message):
            return False, self.last_error or "Failed to commit (no changes?)"

        if push and not self.push():
            return False, self.last_error or "Failed to push"

        return True, ""
