# Paper Fields Guide

本文档说明 papers.csv 中各字段的用途，特别是可选字段的使用场景，以及 README.md 表格的呈现格式。

## CSV 字段列表（11列）

| 字段名 | 必填 | 说明 | 示例 | README显示 |
|--------|------|------|------|------------|
| **Source** | 是 | 论文来源/会议 | `CHI 2024`, `arXiv(v1) 2024` | ✓ |
| **Title** | 是 | 论文标题 | `MetaGPT: Meta Programming...` | ✓ (带链接) |
| **Authors** | 否 | 作者列表（最多3位，超过用et al.） | `Sirui Hong, et al.` | ✓ (仅首作者) |
| **DOI** | 否 | 数字对象标识符 | `10.1145/3544548.3581468` | ✗ |
| **Journal_Ref** | 否 | 期刊/会议引用 | `NeurIPS 2023`, `ICLR 2024` | ✓ (合并到Source) |
| **Link** | 是 | 论文链接 | `https://arxiv.org/abs/2308.00352` | ✓ (在Title中) |
| **Tag** | 是 | 自定义标签（逗号分隔） | `llm, agent, framework` | ✓ |
| **Subjects** | 否 | arXiv 分类 | `cs.AI, cs.CL` | ✓ |
| **Additional_Info** | 否 | 附加信息/备注 | `Accepted to CHI 2024` | ✓ |
| **Date** | 否 | 发布日期 | `2024.03` | ✓ |
| **Topic** | 是 | 主题分类 | `HCI`, `LLM`, `RAG`, `Agent` | ✗ (用于分组) |

**注意**:
- CSV 存储 11 个字段（包括 DOI 和 Journal_Ref）
- README 表格显示 7 列（不显示 DOI 和 Topic）
- DOI 虽不在表格显示，但保存在 CSV 中供查询和引用

## README 表格呈现格式

### Source 列智能格式化

**新特性**: Source 列会智能识别 arXiv 链接并优先显示版本信息

#### 格式规则

1. **arXiv 论文 + 会议**: `arXiv(v1) 2024 (ICLR 2024)`
   - 优先显示 arXiv 版本和年份
   - 会议/期刊名称放在括号中

2. **纯 arXiv 论文**: `arXiv(v2) 2023`
   - 只显示版本和年份

3. **非 arXiv 论文**: `Ubicomp 2023`
   - 保持原会议名

#### 智能检测示例

**情况1**: CSV 中 Source 是会议名，但 Link 是 arXiv
```csv
Source: "ICLR 2024"
Link: "https://arxiv.org/abs/2308.00352v1"
```
**README 显示**: `arXiv(v1) 2024 (ICLR 2024)` ✓

**情况2**: CSV 中 Source 已经是 arXiv 格式，有 Journal_Ref
```csv
Source: "arXiv(v1) 2023"
Journal_Ref: "NeurIPS 2023"
```
**README 显示**: `arXiv(v1) 2023 (NeurIPS 2023)` ✓

**情况3**: 非 arXiv 论文
```csv
Source: "Ubicomp 2023"
Link: "https://dl.acm.org/doi/10.1145/xxx"
```
**README 显示**: `Ubicomp 2023` ✓

## 可选字段使用场景

### 1. DOI 字段

**用途**: 存储论文的DOI，便于引用和查找

**场景**:
- arXiv论文后来发表在会议/期刊上，会分配DOI
- 从ACM DL、IEEE等数据库添加的论文自带DOI

**示例**:
```csv
"CHI 2023","HOOV: Hand Out-Of-View...",".."10.1145/3544548.3581468","","...","HCI"
```

### 2. Journal_Ref 字段

**用途**: 记录论文的期刊或会议引用信息

**使用建议**:
- arXiv论文被会议接收后，在此字段标注会议名称
- 已发表的期刊论文，记录期刊名和年份

**示例**:
```csv
"arXiv(v2) 2023","MetaGPT...","..",,"ICLR 2024","...","Agent"
"NIPS 2023","Large Language Model...","..",,"NeurIPS 2023","...","LLM"
```

**注意**:
- Source 字段可以继续保留 `arXiv(v1) 2024` 表示原始发布
- Journal_Ref 记录最终发表的会议/期刊

### 3. Additional_Info 字段

**用途**: 记录论文的额外信息和备注

**来源**:
1. **arXiv API 的 comment 字段** - 作者提供的备注
2. **手动添加的信息** - 通过 `paper add` 的 `--note` 参数

**常见用途**:
- 会议接收状态: `Accepted to CHI 2024`
- 代码链接: `Code: https://github.com/xxx`
- 项目主页: `Project page: https://xxx`
- 其他说明: `v2: added experiments`, `Best paper award`

**示例**:
```csv
"arXiv(v1) 2024","IMUSIC...","..",,..,..,"code coming soon ([link](https://sites.google.com/view/projectpage-imusic))","2024.02","HCI"
```

## 工作流程示例

### 场景1: 追踪论文从 arXiv 到会议发表

**步骤1: 初始添加** (论文刚上传arXiv):
```bash
paper add 2308.00352 Agent -t "multi-agent, framework"
```

CSV 结果:
```csv
"arXiv(v1) 2023","MetaGPT: ...","Sirui Hong, et al.","","","...","multi-agent, framework","cs.AI","","2023.08","Agent"
```

README 显示: `arXiv(v1) 2023`

**步骤2: 论文被 ICLR 接收** (几个月后):

手动编辑 CSV，在 Journal_Ref 列填入:
```csv
Source: "arXiv(v1) 2023"
Journal_Ref: "ICLR 2024"  ← 添加这里
```

或者直接修改 Source:
```csv
Source: "ICLR 2024"  ← 修改为会议名
Link: "https://arxiv.org/abs/2308.00352"  ← 保持 arXiv 链接
```

**README 自动显示**: `arXiv(v1) 2024 (ICLR 2024)` ✓

> **关键**: 即使 Source 被改成会议名，只要 Link 还是 arXiv，README 就会自动恢复版本信息！

### 场景2: 添加已发表论文

从 ACM DL 添加已有DOI的论文:
```bash
paper add https://dl.acm.org/doi/10.1145/3544548.3581468 HCI -t "IMU, VR"
```

自动获取DOI:
```csv
"CHI 2023","HOOV: ...","Paul Streli, et al.","10.1145/3544548.3581468","","...","IMU, VR","cs.HC","","","HCI"
```

### 场景3: 添加备注信息

```bash
paper add 2403.06201 HCI -t "IMU, llm" -n "Interesting zero-shot approach"
```

结果:
```csv
"arXiv(v1) 2024","Are You Being Tracked?...","Huanqi Yang, et al.","","","...","IMU, llm","cs.CL","Interesting zero-shot approach","2024.03","HCI"
```

## 查看字段信息

### CLI 预览（包含所有字段）

使用 `paper add --dry-run` 预览所有 11 个字段:
```bash
paper add 2308.00352 Agent --dry-run
```

会显示:
```
╭─────────────────── Paper Details ───────────────────╮
│ Title: MetaGPT: Meta Programming...                │
│ Authors: Sirui Hong, et al.                        │
│ Source: arXiv(v1) 2023                             │
│ Topic: Agent                                       │
│ Tags: arxiv                                        │
│ Subjects: cs.AI, cs.MA                             │
│ Link: https://arxiv.org/abs/2308.00352             │
│ Date: 2023.08                                      │
│ DOI: N/A                    ← CSV 存储但不在表格显示  │
│ Journal Ref: N/A            ← CSV 存储，合并到Source │
│ Comment/Notes: N/A          ← CSV 存储在Additional_Info │
╰─────────────────────────────────────────────────────╯
```

### README 表格（7列）

同步后在 README.md 中显示:
```markdown
| arXiv(v1) 2023 | [MetaGPT: ...](link) | Sirui Hong, et al. | tags | cs.AI, cs.MA | | 2023.08 |
```

## 手动编辑 CSV

虽然CLI提供了添加功能，但某些情况下需要直接编辑 CSV:

1. **批量更新会议信息** - 多篇论文被同一会议接收
2. **修正错误** - 纠正自动获取的元数据
3. **补充DOI** - 论文后来分配了DOI

**编辑后记得同步**:
```bash
paper sync
```

## 最佳实践

1. **保持字段一致性**
   - 空字段用空字符串 `""` 而不是 `N/A`
   - 会议名称统一格式: `CHI 2024`, `NeurIPS 2023`

2. **利用可选字段跟踪论文生命周期**
   - Journal_Ref: 记录最终发表位置
   - Additional_Info: 记录投稿/接收状态变化

3. **定期更新**
   - 检查 arXiv 论文是否有更新版本
   - 补充已发表论文的DOI和会议信息

4. **搜索时利用这些字段**
   ```bash
   # 搜索某个会议的论文（通过Source或Journal_Ref）
   paper search CHI 2024

   # 查看完整字段信息
   paper list --all
   ```

## 未来功能建议

- `paper update <id>` - 命令行更新论文信息
- `paper check-updates` - 自动检查arXiv论文更新
- `paper add-doi <id> <doi>` - 批量添加DOI
- `paper set-venue <id> <venue>` - 快速设置会议信息
