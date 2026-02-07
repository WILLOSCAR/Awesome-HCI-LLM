# Paper CLI Usage

This document focuses on `paper` CLI usage only.

## Install

```bash
cd /path/to/Awesome-HCI-LLM
pip install -e .
```

## Quick Start

```bash
# 1) Add a paper (auto-fetch metadata)
paper add 2312.00752 LLM -t "llm, mamba"

# 2) Search
paper search transformer --topic LLM

# 3) Rebuild README tables
paper sync --readme-only

# 4) View stats
paper stats
```

## Supported Input Sources

- arXiv: `2312.00752` or `https://arxiv.org/abs/2312.00752`
- ACM DL: `https://dl.acm.org/doi/10.1145/...`
- IEEE Xplore: `https://ieeexplore.ieee.org/document/...`
- DOI: `10.xxxx/...` or `https://doi.org/10.xxxx/...`

## Command Cheatsheet

- `paper add <link_or_id> <topic>`: add one paper
- `paper search [query]`: search papers (alias: `paper s`)
- `paper list`: list papers (alias: `paper ls`)
- `paper preview`: preview generated markdown tables
- `paper sync`: sync README and optional git actions
- `paper topics`: list topics and counts
- `paper stats`: show library statistics

---

## `paper add`

```bash
paper add <link_or_id> <topic> [OPTIONS]
```

Common options:
- `-t, --tag TEXT`: custom tags, comma-separated
- `-n, --note TEXT`: additional notes
- `-s, --source TEXT`: override source label (e.g., `CHI 2024`)
- `--no-sync`: skip README update
- `--no-git`: skip git commit/push
- `--dry-run`: preview only, do not write
- `-m, --commit-msg TEXT`: custom commit message
- `--repo PATH`: repo root (default `.`)

Examples:

```bash
paper add 2312.00752 LLM
paper add https://dl.acm.org/doi/10.1145/3544548.3581468 HCI -t "imu,vr"
paper add 10.1145/3569473 HCI --dry-run
paper add 2502.12110 Memory --no-sync
```

## `paper search`

```bash
paper search [query] [OPTIONS]
```

Common options:
- `-t, --tag TEXT`
- `-a, --author TEXT`
- `--topic TEXT`
- `--from YYYY.MM`
- `--to YYYY.MM`
- `-l, --limit INTEGER` (`0` means all)
- `--all`: show all fields
- `--repo PATH`

Examples:

```bash
paper search transformer
paper search --tag IMU --topic HCI
paper search --author Wang --from 2024.01 --to 2024.12
paper s memory -l 50
```

## `paper list`

```bash
paper list [OPTIONS]
```

Common options:
- `-t, --topic TEXT`
- `-l, --limit INTEGER` (`0` means all)
- `--recent`
- `--all`
- `--repo PATH`

Examples:

```bash
paper list --recent
paper list -t Agent -l 0
paper ls --all
```

## `paper preview`

```bash
paper preview [OPTIONS]
```

Options:
- `-t, --topic TEXT`: preview one topic
- `--diff`: show diff against current README
- `--repo PATH`

Examples:

```bash
paper preview
paper preview -t HCI
paper preview --diff
```

## `paper sync`

```bash
paper sync [OPTIONS]
```

Options:
- `--readme-only`: only update README
- `--no-push`: commit but do not push
- `-m, --commit-msg TEXT`
- `--repo PATH`

Examples:

```bash
paper sync
paper sync --readme-only
paper sync -m "Update paper tables" --no-push
```

## `paper topics`

```bash
paper topics [--repo PATH]
```

## `paper stats`

```bash
paper stats [--repo PATH]
```

---

## Common Workflows

### Add first, sync later (batch mode)

```bash
paper add 2312.00752 LLM --no-sync --no-git
paper add 10.1145/3569473 HCI --no-sync --no-git
paper sync --readme-only
```

### Check what will change before syncing

```bash
paper preview --diff
paper sync --readme-only
```

### Use another repository path

```bash
paper list --repo /path/to/another/repo
paper add 2502.12110 Memory --repo /path/to/another/repo
```

## Help

```bash
paper --help
paper add --help
paper search --help
```
