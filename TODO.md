# Development Roadmap

## Phase 1: Core Enhancement

- [ ] **Multi-source Fetcher**
  - [ ] Semantic Scholar API support
  - [ ] Google Scholar scraper (with anti-bot handling)
  - [ ] OpenAlex API integration
  - [ ] PubMed support for medical/bio papers

- [ ] **Search Improvements**
  - [ ] Fuzzy search (typo tolerance)
  - [ ] Full-text search in abstracts
  - [ ] Advanced query syntax (`tag:IMU AND author:Wang`)
  - [ ] Search history and saved queries

- [ ] **Export Features**
  - [ ] BibTeX export (`paper export bibtex`)
  - [ ] EndNote/RIS format
  - [ ] JSON export for programmatic use
  - [ ] Markdown bibliography

## Phase 2: Data Management

- [ ] **Deduplication**
  - [ ] Auto-detect duplicate papers (by DOI/title similarity)
  - [ ] Merge duplicates command
  - [ ] Duplicate report generation

- [ ] **Tags Management**
  - [ ] `paper tags list` - show all tags with counts
  - [ ] `paper tags rename old new` - batch rename
  - [ ] `paper tags merge tag1 tag2` - merge similar tags
  - [ ] Tag suggestions based on title/abstract

- [ ] **Batch Operations**
  - [ ] Import from CSV/JSON file
  - [ ] Import from BibTeX
  - [ ] Bulk update tags/topics
  - [ ] Import from Zotero/Mendeley export

## Phase 3: Enhanced Features

- [ ] **Paper Notes**
  - [ ] Add personal notes to papers
  - [ ] Reading status (unread/reading/done)
  - [ ] Rating system (1-5 stars)
  - [ ] Key takeaways field

- [ ] **Reading Lists**
  - [ ] Create named reading lists
  - [ ] `paper list create "CVPR 2024 picks"`
  - [ ] Add/remove papers to lists
  - [ ] Share lists as Markdown

- [ ] **Statistics & Visualization**
  - [ ] Publication timeline chart
  - [ ] Tag co-occurrence network
  - [ ] Author collaboration graph
  - [ ] Topic distribution pie chart
  - [ ] Export stats as HTML report

## Phase 4: Integration & Automation

- [ ] **External Services**
  - [ ] Zotero sync (two-way)
  - [ ] Notion database sync
  - [ ] Obsidian vault integration
  - [ ] Slack/Discord notifications for new papers

- [ ] **Automation**
  - [ ] Watch arXiv categories for new papers
  - [ ] Auto-tag using ML classifier
  - [ ] Citation count auto-update
  - [ ] Related papers recommendation

- [ ] **Web Interface**
  - [ ] Local web UI (Flask/FastAPI)
  - [ ] Table view with sorting/filtering
  - [ ] Quick add form
  - [ ] Mobile-friendly design

## Phase 5: Quality & DevOps

- [ ] **Testing**
  - [ ] Unit tests for core modules
  - [ ] Integration tests for CLI commands
  - [ ] Mock API responses for offline testing
  - [ ] CI/CD with GitHub Actions

- [ ] **Documentation**
  - [ ] API documentation (if exposing as library)
  - [ ] Developer guide for contributors
  - [ ] Video tutorial

- [ ] **Performance**
  - [ ] SQLite backend option (for large collections)
  - [ ] Async API calls for batch operations
  - [ ] Caching layer for frequent queries

---

## Quick Wins (Easy to implement)

- [x] Basic CLI with add/search/list/sync
- [x] arXiv metadata fetching
- [x] Markdown table generation
- [ ] `paper open <id>` - open paper URL in browser
- [ ] `paper cite <id>` - copy citation to clipboard
- [ ] `paper random` - show random paper for reading
- [ ] `paper edit <id>` - interactive edit mode
- [ ] Config file support (`~/.paper-cli/config.toml`)

---

## Ideas / Maybe Later

- [ ] PDF download and local storage
- [ ] Abstract summarization using LLM
- [ ] Paper similarity search (embeddings)
- [ ] Conference deadline tracker
- [ ] Collaborative features (multi-user)
