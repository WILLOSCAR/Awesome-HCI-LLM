# Format Examples

This document shows real examples of how papers are displayed in CSV vs README, with before/after comparisons of the new smart format.

## Table Format Overview

### CSV Storage (11 columns)
```
Source, Title, Authors, DOI, Journal_Ref, Link, Tag, Subjects, Additional_Info, Date, Topic
```

### README Display (7 columns)
```
| Source | Title (Link) | Authors | Tag | Subjects | Additional info | Date |
```

---

## Format Examples by Paper Type

### 1. arXiv Paper with Conference Acceptance

**CSV Data:**
```csv
"ICLR 2024","MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework","Sirui Hong, Mingchen Zhuge, Xiawu Zheng, et al.","","","https://arxiv.org/abs/2308.00352","autonomous system, SOP, multi-agent, framework","cs.AI, cs.MA","","","Agent"
```

**README Output (Smart Format):**
```markdown
| arXiv(v1) 2024 (ICLR 2024) | [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) | Sirui Hong, et al. | autonomous system, SOP, multi-agent, framework | cs.AI, cs.MA |  |  |
```

**Key Points:**
- ✓ Source shows arXiv version even though CSV has "ICLR 2024"
- ✓ Version extracted from Link: v1 (default when not specified)
- ✓ Conference name preserved in parentheses
- ✓ Authors simplified to "First Author, et al."

---

### 2. arXiv Paper with Journal_Ref

**CSV Data:**
```csv
"arXiv(v1) 2023","CAMEL: Communicative Agents for Mind Exploration of Large Language Model Society","Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, et al.","","NIPS 2023","https://arxiv.org/abs/2303.17760","role play, autonomous, user&assistant","cs.AI, cs.CL, cs.CY, cs.LG, cs.MA","","2023.11(v2)","Agent"
```

**README Output:**
```markdown
| arXiv(v1) 2023 (NIPS 2023) | [CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society](https://arxiv.org/abs/2303.17760) | Guohao Li, et al. | role play, autonomous, user&assistant | cs.AI, cs.CL, cs.CY, cs.LG, cs.MA |  | 2023.11(v2) |
```

**Key Points:**
- ✓ Source already in arXiv format
- ✓ Journal_Ref merged into Source column
- ✓ Format: `arXiv(v1) 2023 (NIPS 2023)`

---

### 3. Pure arXiv Paper (Not Published Yet)

**CSV Data:**
```csv
"arXiv(v1) 2024","IMUSIC: IMU-based Facial Expression Capture","Youjia Wang, Zijun Zhao, Zhengyang Shen, et al.","","","https://arxiv.org/abs/2402.03944","IMU, generation, simulate, transformer diffusion","cs.CV","code coming soon ([link](https://sites.google.com/view/projectpage-imusic))","2024.02","HCI"
```

**README Output:**
```markdown
| arXiv(v1) 2024 | [IMUSIC: IMU-based Facial Expression Capture](https://arxiv.org/abs/2402.03944) | Youjia Wang, et al. | IMU, generation, simulate, transformer diffusion | cs.CV | code coming soon ([link](https://sites.google.com/view/projectpage-imusic)) | 2024.02 |
```

**Key Points:**
- ✓ No conference info, shows only arXiv version
- ✓ Additional_Info with project link displayed
- ✓ Clean format: `arXiv(v1) 2024`

---

### 4. Non-arXiv Conference Paper

**CSV Data:**
```csv
"Ubicomp 2023","From 2D to 3D: Facilitating Single-Finger Mid-Air Typing on QWERTY Keyboards with Probabilistic Touch Modeling","","","","https://dl.acm.org/doi/10.1145/3580829","mid air, text entry, VR","","","","HCI"
```

**README Output:**
```markdown
| Ubicomp 2023 | [From 2D to 3D: Facilitating Single-Finger Mid-Air Typing on QWERTY Keyboards with Probabilistic Touch Modeling](https://dl.acm.org/doi/10.1145/3580829) |  | mid air, text entry, VR |  |  |  |
```

**Key Points:**
- ✓ Non-arXiv link, keeps original Source format
- ✓ No author info in CSV (empty field)
- ✓ Links to ACM DL instead of arXiv

---

### 5. Conference Paper with arXiv Version

**CSV Data:**
```csv
"CHI 2023","HOOV: Hand Out-Of-View Tracking for Proprioceptive Interaction using Inertial Sensing","Paul Streli, Rayan Armani, Yi Fei Cheng, et al.","10.1145/3544548.3581468","","https://arxiv.org/abs/2303.07016","IMU, VR, transformer","cs.HC, cs.CV, I.2; I.5; H.5","","","HCI"
```

**README Output:**
```markdown
| arXiv(v1) 2023 (CHI 2023) | [HOOV: Hand Out-Of-View Tracking for Proprioceptive Interaction using Inertial Sensing](https://arxiv.org/abs/2303.07016) | Paul Streli, et al. | IMU, VR, transformer | cs.HC, cs.CV, I.2; I.5; H.5 |  |  |
```

**Key Points:**
- ✓ Source was "CHI 2023" but Link is arXiv
- ✓ Smart detection extracts arXiv info from Link
- ✓ Year extracted from conference name (2023)
- ✓ DOI stored in CSV but not shown in README

---

## Before vs After Comparison

### Before (Old Format)

```markdown
| ICLR 2024 | [MetaGPT: ...](https://arxiv.org/abs/2308.00352) | Sirui Hong, et al. | ... |
| CHI 2023 | [HOOV: ...](https://arxiv.org/abs/2303.07016) | Paul Streli, et al. | ... |
| NIPS 2023 (NeurIPS 2023) | [Large Language Model...](https://arxiv.org/abs/2306.15895) | ... |
```

**Issues:**
- ✗ arXiv version information lost
- ✗ Inconsistent format (some have double parentheses)
- ✗ Can't easily identify paper versions

### After (New Format)

```markdown
| arXiv(v1) 2024 (ICLR 2024) | [MetaGPT: ...](https://arxiv.org/abs/2308.00352) | ... |
| arXiv(v1) 2023 (CHI 2023) | [HOOV: ...](https://arxiv.org/abs/2303.07016) | ... |
| arXiv(v1) 2023 (NIPS 2023) | [Large Language Model...](https://arxiv.org/abs/2306.15895) | ... |
```

**Improvements:**
- ✓ arXiv version always visible
- ✓ Consistent format: `arXiv(vX) YEAR (CONFERENCE)`
- ✓ Easy to identify and compare versions
- ✓ Conference info preserved in parentheses

---

## CLI Preview Example

When you run `paper add --dry-run`, you see all 11 fields:

```
╭─────────────────────────────── Paper Details ────────────────────────────────╮
│ Title: MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework   │
│ Authors: Sirui Hong, Mingchen Zhuge, et al.                                  │
│ Source: arXiv(v1) 2023                                                       │
│ Topic: Agent                                                                 │
│ Tags: multi-agent, framework, SOP                                            │
│ Subjects: cs.AI, cs.MA                                                       │
│ Link: https://arxiv.org/abs/2308.00352                                       │
│ Date: 2023.08                                                                │
│ DOI: N/A                      ← Saved in CSV, not in README                  │
│ Journal Ref: ICLR 2024        ← Merged into Source in README                 │
│ Comment/Notes: N/A            ← Becomes Additional_Info in CSV               │
╰──────────────────────────────────────────────────────────────────────────────╯
```

Then in README, it becomes:

```markdown
| arXiv(v1) 2023 (ICLR 2024) | [MetaGPT: ...](link) | ... |
```

---

## Field Mapping: CSV → README

| CSV Field | README Column | Processing |
|-----------|---------------|------------|
| Source | Source | Smart format: extracts arXiv info from Link |
| Title | Title (Link) | Combined with Link |
| Authors | Authors | First author only + "et al." |
| DOI | *Not shown* | Stored in CSV for reference |
| Journal_Ref | Source | Merged into Source column in parentheses |
| Link | Title (Link) | Embedded in Title |
| Tag | Tag | Direct display |
| Subjects | Subjects | Direct display |
| Additional_Info | Additional info | Direct display |
| Date | Date | Direct display |
| Topic | *Not shown* | Used for grouping sections |

---

## Version Detection Examples

The system automatically extracts version numbers from arXiv links:

| Link | Extracted Version |
|------|-------------------|
| `https://arxiv.org/abs/2308.00352v1` | v1 |
| `https://arxiv.org/abs/2308.00352v2` | v2 |
| `https://arxiv.org/pdf/2308.00352v3.pdf` | v3 |
| `https://arxiv.org/abs/2308.00352` | v1 (default) |

---

## Summary

**What's Stored (CSV):** 11 fields including DOI and Journal_Ref
**What's Displayed (README):** 7 columns with smart formatting
**Key Feature:** arXiv version information is always visible, even when Source is modified to conference name

For more details, see:
- `USAGE.md` - Command reference and usage
- `FIELDS_GUIDE.md` - Detailed field usage and workflows
- `README.md` - Live examples in the paper tables
