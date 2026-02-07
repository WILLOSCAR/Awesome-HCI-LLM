# Legacy Scripts

`src/` now keeps only lightweight compatibility wrappers and historical scripts.
For day-to-day usage, use the `paper` CLI directly.

## Preferred commands

- Add paper: `paper add <link_or_doi_or_arxiv_id> <topic>`
- Rebuild README tables: `paper sync --readme-only`

## Files in this folder

- `_legacy_cli_bridge.py`: shared helper for deprecation warning + import bootstrap
- `add_arxiv_paper.py`: legacy wrapper (delegates to `paper add`, CSV-only behavior)
- `csv2md_table.py`: legacy wrapper (delegates to `paper sync --readme-only`)
- `test_arxiv_api.py`: ad-hoc arXiv API inspection tool
- `migrate_and_enrich.py`: historical one-time migration script
