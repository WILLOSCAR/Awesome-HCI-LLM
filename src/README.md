# Legacy Scripts

This directory contains early standalone scripts that have been **superseded by the `paper_cli` package**. They are kept for reference and backward compatibility.

## Current Status

| Script | Status | Replacement | Purpose |
|--------|--------|-------------|---------|
| `test_arxiv_api.py` | ✅ **Active** | - | Testing tool for arXiv API responses |
| `csv2md_table.py` | 🔶 **Legacy** | `paper_cli/core/markdown.py` | Generate Markdown tables from CSV |
| `add_arxiv_paper.py` | 🔶 **Legacy** | `paper add` command | Add arXiv papers to collection |
| `migrate_and_enrich.py` | 🔶 **Legacy** | One-time migration script | Initial data migration |

## Recommended Usage

### Instead of legacy scripts, use the paper_cli:

```bash
# Old way (legacy scripts)
python src/add_arxiv_paper.py 2308.00352 Agent
python src/csv2md_table.py

# New way (paper_cli)
paper add 2308.00352 Agent
paper sync
```

## Active Scripts

### test_arxiv_api.py

**Purpose**: Inspect complete arXiv API response for a paper

**Usage**:
```bash
python src/test_arxiv_api.py 2308.00352
```

**Output**: All available fields from arXiv API including title, authors, categories, DOI, journal_ref, comment, etc.

---

## Migration Guide

If you're still using legacy scripts, here's how to migrate:

### 1. csv2md_table.py → paper sync

**Before**:
```python
python src/csv2md_table.py
```

**After**:
```bash
paper sync --readme-only
```

**Benefits**:
- Smart Source column formatting
- arXiv version detection
- Automatic Journal_Ref merging

### 2. add_arxiv_paper.py → paper add

**Before**:
```bash
python src/add_arxiv_paper.py https://arxiv.org/abs/2308.00352 Agent
```

**After**:
```bash
paper add 2308.00352 Agent -t "multi-agent, framework"
```

**Benefits**:
- Auto-sync README
- Git commit and push
- Preview with --dry-run
- Support for multiple sources (arXiv, ACM DL, IEEE, DOI)

---

## For Developers

These legacy scripts are useful for understanding the evolution of the codebase:

- **csv2md_table.py**: See the original table generation logic
- **add_arxiv_paper.py**: See how arXiv API integration started
- **migrate_and_enrich.py**: Understand the initial data structure

For new features, always extend the `paper_cli` package, not these scripts.
