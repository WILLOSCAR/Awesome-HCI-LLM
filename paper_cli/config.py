"""Configuration management for paper CLI."""

from pathlib import Path
from pydantic import BaseModel
from typing import Optional

try:
    # Python 3.11+
    import tomllib  # type: ignore[import-not-found]
except ModuleNotFoundError:  # pragma: no cover
    # Python <3.11
    import tomli as tomllib


class Config(BaseModel):
    """CLI 配置。"""

    repo_path: Path = Path(".")
    csv_path: Path = Path("papers.csv")
    readme_path: Path = Path("README.md")
    default_topic: str = "HCI"
    auto_sync: bool = True
    auto_git: bool = True

    @classmethod
    def load(cls, config_path: Optional[Path] = None) -> "Config":
        """加载配置文件。"""
        if config_path and config_path.exists():
            with open(config_path, 'rb') as f:
                data = tomllib.load(f)
            return cls(**data)

        # 查找默认配置位置
        default_paths = [
            Path(".paper-cli.toml"),
            Path.home() / ".config" / "paper-cli" / "config.toml",
        ]

        for path in default_paths:
            if path.exists():
                with open(path, 'rb') as f:
                    data = tomllib.load(f)
                return cls(**data)

        return cls()

    def get_csv_path(self) -> Path:
        """获取 CSV 文件的绝对路径。"""
        if self.csv_path.is_absolute():
            return self.csv_path
        return self.repo_path / self.csv_path

    def get_readme_path(self) -> Path:
        """获取 README 文件的绝对路径。"""
        if self.readme_path.is_absolute():
            return self.readme_path
        return self.repo_path / self.readme_path
