# Paper CLI Usage Guide

CLI tool for managing academic papers: add paper → update README → git push in one command.

## Installation

```bash
cd /path/to/Awesome-HCI-LLM
pip install -e .
```

## Quick Start

```bash
# Add paper from arXiv (auto-fetch metadata)
paper add https://arxiv.org/abs/2312.00752 LLM -t "llm, mamba"

# Add paper from ACM DL
paper add https://dl.acm.org/doi/10.1145/3544548.3581468 HCI

# Add paper by DOI
paper add 10.1145/3569473 HCI -t "smartwatch"

# Search papers
paper search transformer

# Show stats
paper stats
```

## What's New in Current Version

✓ **Smart Source Column**: Automatically displays arXiv version info in format `arXiv(v1) 2024 (ICLR 2024)`
✓ **All Fields Visible**: DOI, Journal Ref, and Comment fields now shown in CLI preview
✓ **arXiv Priority**: Even if Source is set to conference name, arXiv info is recovered from Link
✓ **Version Tracking**: Paper versions (v1, v2, v3) automatically extracted and displayed

---

## Supported Sources

| Source | URL Format | Example |
|--------|------------|---------|
| **arXiv** | `https://arxiv.org/abs/xxx` or `2312.00752` | `paper add 2312.00752 LLM` |
| **ACM DL** | `https://dl.acm.org/doi/10.1145/xxx` | `paper add https://dl.acm.org/doi/10.1145/3544548.3581468 HCI` |
| **IEEE** | `https://ieeexplore.ieee.org/document/xxx` | `paper add https://ieeexplore.ieee.org/document/9878378 HCI` |
| **DOI** | `10.xxxx/xxx` or `https://doi.org/10.xxxx/xxx` | `paper add 10.1145/3569473 HCI` |

The CLI auto-detects the source from the URL and fetches metadata automatically.

If auto-fetch fails, you'll be prompted to enter details manually.

---

## Command Reference

### `paper add` - Add Paper

Add a paper to the library with auto metadata fetching.

```bash
paper add <link> <topic> [OPTIONS]
```

**Arguments**:
| Argument | Description |
|----------|-------------|
| `link` | Paper URL or ID (arXiv, ACM, IEEE, DOI) |
| `topic` | Category (free-form, e.g., HCI / LLM / RAG / Agent / Memory / Personalization / MLLM) |

**Options**:
| Option | Short | Description |
|--------|-------|-------------|
| `--tag` | `-t` | Custom tags (comma-separated) |
| `--note` | `-n` | Additional notes |
| `--source` | `-s` | Custom source (e.g., "CHI 2024") |
| `--no-sync` | | Don't update README |
| `--no-git` | | Don't commit/push |
| `--dry-run` | | Preview only, don't save |
| `--commit-msg` | `-m` | Custom commit message |

**Examples**:
```bash
# arXiv paper
paper add https://arxiv.org/abs/2312.00752 LLM

# arXiv by ID only
paper add 2312.00752 LLM -t "mamba, ssm"

# ACM paper
paper add https://dl.acm.org/doi/10.1145/3544548.3581468 HCI -t "IMU, VR"

# DOI directly
paper add 10.1145/3569473 HCI

# Preview without saving
paper add 2312.00752 LLM --dry-run

# Add without sync (batch mode)
paper add 2312.00752 LLM --no-sync
```

---

### `paper search` - Search Papers

Search papers by keyword, tag, author, or date. Alias: `paper s`

```bash
paper search [query] [OPTIONS]
```

**Options**:
| Option | Short | Description |
|--------|-------|-------------|
| `--tag` | `-t` | Filter by tag |
| `--author` | `-a` | Filter by author |
| `--topic` | | Filter by topic |
| `--from` | | Start date (YYYY.MM) |
| `--to` | | End date (YYYY.MM) |
| `--limit` | `-l` | Max results (default 20, 0 for all) |
| `--all` | | Show all fields |

**Examples**:
```bash
# Keyword search (title, tags, authors)
paper search transformer

# Filter by tag
paper search -t IMU

# Filter by author
paper search -a "Yang"

# Combined search
paper search pose -t IMU --topic HCI

# Date range
paper search --from 2024.01 --to 2024.06

# Show all fields
paper search transformer --all
```

---

### `paper list` - List Papers

List papers in the library. Alias: `paper ls`

```bash
paper list [OPTIONS]
```

**Options**:
| Option | Short | Description |
|--------|-------|-------------|
| `--topic` | `-t` | Filter by topic |
| `--limit` | `-l` | Max count (default 10, 0 for all) |
| `--recent` | | Sort by date (newest first) |
| `--all` | | Show all fields |

**Examples**:
```bash
# List recent 10
paper list --recent

# List all in a topic
paper list -t HCI -l 0

# Show all fields
paper list --all
```

---

### `paper preview` - Preview Markdown

Preview the Markdown table that will be generated.

```bash
paper preview [OPTIONS]
```

**Options**:
| Option | Short | Description |
|--------|-------|-------------|
| `--topic` | `-t` | Preview specific topic only |
| `--diff` | | Show diff with current README |

**Examples**:
```bash
# Preview all
paper preview

# Preview specific topic
paper preview -t LLM

# Show diff
paper preview --diff
```

---

### `paper sync` - Sync

Manually sync README and push to git.

```bash
paper sync [OPTIONS]
```

**Options**:
| Option | Short | Description |
|--------|-------|-------------|
| `--readme-only` | | Only update README, skip git |
| `--no-push` | | Commit but don't push |
| `--commit-msg` | `-m` | Custom commit message |

**Examples**:
```bash
# Full sync (README + commit + push)
paper sync

# Only update README
paper sync --readme-only

# Custom commit message
paper sync -m "Add new papers"
```

---

### `paper topics` - List Topics

List all topics and paper counts.

```bash
paper topics
```

---

### `paper stats` - Statistics

Show library statistics.

```bash
paper stats
```

---

## Common Workflows

### 1. Add a paper

```bash
# One command does everything
paper add https://arxiv.org/abs/2312.00752 LLM -t "llm, mamba"
```

### 2. Batch add then sync

```bash
# Add without sync
paper add 2312.00752 LLM --no-sync
paper add 2312.00753 LLM --no-sync
paper add 10.1145/xxx HCI --no-sync

# Sync all at once
paper sync -m "Add 3 papers"
```

### 3. Find a paper

```bash
# By keyword
paper search attention

# By tag
paper search -t transformer

# By date
paper search --from 2024.01
```

### 4. Preview changes

```bash
paper preview --diff
```

---

## README Table Format

The generated README.md uses a 7-column Markdown table format:

```markdown
| Source | Title (Link) | Authors | Tag | Subjects | Additional info | Date |
```

### Source Column Examples

The Source column intelligently displays arXiv information with conference details:

- **arXiv + Conference**: `arXiv(v1) 2024 (ICLR 2024)`
- **arXiv Only**: `arXiv(v2) 2023`
- **Non-arXiv**: `Ubicomp 2023`

**Smart Detection**: If Source is set to "ICLR 2024" but Link contains arxiv.org, the tool automatically extracts version info and displays as `arXiv(v1) 2024 (ICLR 2024)`.

### Column Details

- **Source**: Shows arXiv version (priority) or conference name
- **Title (Link)**: Clickable title, preferably linking to arXiv
- **Authors**: First author + "et al." (simplified for readability)
- **Tag**: User-defined tags (comma-separated)
- **Subjects**: arXiv categories (e.g., cs.AI, cs.CL)
- **Additional info**: Comments from arXiv API or manual notes
- **Date**: Publication date (YYYY.MM format)

---

## Tips

- All commands support `--help`
- `paper search` → `paper s`
- `paper list` → `paper ls`
- Default looks for `papers.csv` in current directory, use `--repo` to specify path
- See `FIELDS_GUIDE.md` for detailed field usage and best practices

---

## Files

```
papers.csv          # Paper data (11 columns including DOI, Journal_Ref)
README.md           # Auto-updated display page (7 columns)
FIELDS_GUIDE.md     # Field usage guide and workflows
USAGE.md            # This file - command reference
TODO.md             # Development roadmap
paper_cli/          # CLI source code
pyproject.toml      # Project config
```
