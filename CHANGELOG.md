# CHANGELOG

## [Unreleased] - 2024-12-13

### Added
- **Smart Source Column Format**: README tables now intelligently display arXiv version information in format `arXiv(v1) 2024 (ICLR 2024)`
  - Automatically extracts version from Link even when Source is set to conference name
  - Prioritizes arXiv information for better paper tracking
  - Conference/journal names preserved in parentheses

- **All Fields Visible in CLI**: DOI, Journal_Ref, and Comment fields now shown in CLI preview
  - Empty fields display as "N/A" for clarity
  - All 11 CSV fields preserved, 7 columns shown in README

- **Enhanced Documentation**:
  - `FORMAT_EXAMPLES.md` - Real examples with before/after comparisons
  - Updated `USAGE.md` with new format examples and README format section
  - Enhanced `FIELDS_GUIDE.md` with smart format rules and detection logic
  - Updated `TODO.md` with recently completed features

- **src/ Directory Refactoring**:
  - `src/README.md` - Comprehensive guide for legacy scripts
  - `src/REFACTORING_SUMMARY.md` - Detailed refactoring documentation
  - All scripts now have type hints and docstrings
  - Deprecation warnings for legacy scripts

### Changed
- Source column in README now automatically formats based on Link content
- Authors display simplified to "First Author, et al." in README (full list in CSV)
- Journal_Ref field now merged into Source column in README display

### Improved
- **test_arxiv_api.py**: Fully refactored with type hints, better error handling, emoji output
- **csv2md_table.py**: Added deprecation warnings, points to `paper sync`
- **add_arxiv_paper.py**: Added deprecation warnings, points to `paper add`
- All scripts now have proper exit codes and user-friendly messages

### Technical Details
- Added `_format_source_column()` method in `MarkdownGenerator` class
- Added `_extract_arxiv_version()` method for version detection
- Updated `display_paper_detail()` to show all optional fields

### Migration Notes
- No CSV format changes - existing data fully compatible
- README tables automatically regenerated with new format on next sync
- Legacy scripts still work with deprecation warnings
- No action required from users

---

## [0.1.0] - 2024-12

### Added
- Initial release of Paper CLI tool
- CSV-based paper storage (11 fields)
- Markdown table generation for README (7 columns)
- arXiv API integration for automatic metadata fetching
- Crossref API support for DOI resolution
- Search and filter functionality
- Git auto-commit and push
- Command-line interface with typer

### Features
- `paper add` - Add papers from arXiv, ACM DL, IEEE, or DOI
- `paper search` - Search papers by keyword, tag, author, topic, date
- `paper list` - List papers with filtering options
- `paper preview` - Preview Markdown table before sync
- `paper sync` - Update README and push to git
- `paper topics` - Show topic statistics
- `paper stats` - Show library statistics

### Supported Sources
- arXiv (https://arxiv.org/abs/xxx or paper ID)
- ACM Digital Library (https://dl.acm.org/doi/xxx)
- IEEE Xplore (https://ieeexplore.ieee.org/document/xxx)
- Any DOI (https://doi.org/xxx or 10.xxxx/xxx)

---

## Format Comparison

### Before (Old Format)
```markdown
| ICLR 2024 | [MetaGPT: ...](link) | ... |
| NIPS 2023 (NeurIPS 2023) | [Paper...](link) | ... |
```

### After (New Format)
```markdown
| arXiv(v1) 2024 (ICLR 2024) | [MetaGPT: ...](link) | ... |
| arXiv(v1) 2023 (NIPS 2023) | [Paper...](link) | ... |
```

**Benefits:**
- ✓ arXiv version always visible
- ✓ Consistent format across all papers
- ✓ Easy to identify paper versions
- ✓ Conference info preserved
