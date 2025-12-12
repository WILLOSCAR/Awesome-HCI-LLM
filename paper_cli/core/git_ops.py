"""Git operations for paper CLI."""

import subprocess
from pathlib import Path
from typing import List, Optional


class GitOperations:
    """Git 操作封装，负责 add/commit/push。"""

    def __init__(self, repo_path: Path):
        self.repo_path = Path(repo_path)

    def is_git_repo(self) -> bool:
        """检查是否是 Git 仓库。"""
        result = subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            cwd=self.repo_path,
            capture_output=True,
            text=True
        )
        return result.returncode == 0

    def has_changes(self) -> bool:
        """检查是否有未提交的更改。"""
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=self.repo_path,
            capture_output=True,
            text=True
        )
        return bool(result.stdout.strip())

    def add_files(self, files: List[str]) -> bool:
        """添加文件到暂存区。"""
        try:
            for file in files:
                subprocess.run(
                    ["git", "add", file],
                    cwd=self.repo_path,
                    check=True,
                    capture_output=True
                )
            return True
        except subprocess.CalledProcessError:
            return False

    def commit(self, message: str) -> bool:
        """提交更改。"""
        try:
            subprocess.run(
                ["git", "commit", "-m", message],
                cwd=self.repo_path,
                check=True,
                capture_output=True
            )
            return True
        except subprocess.CalledProcessError:
            return False

    def push(self) -> bool:
        """推送到远程。"""
        try:
            subprocess.run(
                ["git", "push"],
                cwd=self.repo_path,
                check=True,
                capture_output=True
            )
            return True
        except subprocess.CalledProcessError:
            return False

    def add_commit_push(
        self,
        files: List[str],
        message: str,
        push: bool = True
    ) -> tuple[bool, str]:
        """
        添加文件、提交并推送。

        Args:
            files: 要添加的文件列表
            message: 提交消息
            push: 是否推送到远程

        Returns:
            (success, error_message)
        """
        if not self.is_git_repo():
            return False, "Not a git repository"

        # git add
        if not self.add_files(files):
            return False, "Failed to add files"

        # git commit
        if not self.commit(message):
            return False, "Failed to commit (no changes?)"

        # git push
        if push:
            if not self.push():
                return False, "Failed to push"

        return True, ""
