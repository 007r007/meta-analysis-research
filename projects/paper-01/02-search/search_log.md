# 文献检索记录

## 检索策略

### 概念1（工作记忆训练）
"working memory training" OR "working memory intervention" OR "n-back training" OR "dual n-back" OR "complex span training" OR "Cogmed" OR "cognitive training"

### 概念2（老年人群）
"older adults" OR "elderly" OR "aging" OR "aged"

### 完整逻辑
概念1 AND 概念2

### 过滤条件
- 时间：2000–2026
- 语言：英文
- 文献类型：同行评审期刊文章（Peer-reviewed journal articles）

---

## 各数据库检索记录

| 数据库 | 检索日期 | 检索式字段 | 命中数 | 导出文件 | 备注 |
|--------|---------|-----------|--------|---------|------|
| PubMed | 2026-04-02 | [tiab] + Aged[MeSH] | 2404 | pubmed-workingmem-set.txt | MEDLINE格式 |
| PsycINFO | 2026-04-02 | AB + TI | 1111 | psycinfo_raw—1.ris + psycinfo_raw—2.ris | 分两批导出，RIS格式 |
| Web of Science | 2026-04-02 | TS= | 2295 | wos_raw_1.bib + wos_raw_2.bib + wos_raw_3.bib | 分三批导出，BibTeX格式 |
| Scopus | 2026-04-02 | TITLE-ABS-KEY | 3232 | scopus_raw.ris | RIS格式 |

---

## 去重统计

| 项目 | 数量 |
|------|------|
| 合并前总计 | 9042 |
| 重复记录 | 4874 |
| **去重后总计** | **4168** |

去重输出文件：`merged_deduplicated.ris`

去重方法：优先 DOI 精确匹配，DOI 缺失时用标题+年份模糊匹配（前120字符）

---

## 备注
- "cognitive training" 保留以确保覆盖范围，迁移效应在筛选阶段判断
- Cochrane Library 跳过：WM训练为心理学研究，CENTRAL与PubMed重叠率>90%，四库已充分覆盖
- 去重脚本：`count_and_deduplicate.py`
- 统计数据：`search_stats.json`
