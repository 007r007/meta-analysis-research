# 评估：效应量可提取性核查的正确方法（cc 第一评估）

> 触发：用户质疑正则提取准确性，要求结合 D 盘科研工作平台评估当前工作，cc/cl 独立评估、cx 综合裁决。
> 生成：cc 2026-11-16。

---

## 一、问题诊断：正则提取不可靠（有实锤）

刚才对 38 篇核心论文 Results 段做正则统计量探测，得到 6 篇"全 False"（Seq6/19/36/40/57/60）。逐篇抽查即证伪：

| Seq | 正则结论 | 实际 |
|---|---|---|
| 6 Brum 2020 | 全 False | 两子研究（Study1/Study2），Results 标题为"results"小写且夹在引文后，段标题没抓对 |
| 19 Borella 2013 | 全 False | 明确报告 group×session 统计量（"results"→抓成了摘要的"results of this study"） |
| 40 Booth 2023 | 全 False（n_chars=414） | Results 段只抓到 414 字符，段边界全错 |
| 57 Zelinski 2014 | 全 False | N=487 大样本，用 SEM/结构方程，统计量不是 F/t 形态 |
| 60 Nguyen 2026 | 全 False | 应报告统计量，但 fitz 文本断行导致正则漏配 |

**根因**：fitz `get_text()` 产出的是断行/失序的纯文本，表格在 PDF 里被拆成碎片；正则既抓不准段边界，也抓不准表格里的 M/SD。**正则只能做粗筛，不能做"能否提取效应量"的判定。**

## 二、平台能提供什么（三个杠杆）

### 杠杆 1：canonical 统计结果 schema（最重要）
`D:\Research_Agent_Lab\references\schemas\statistical_result.schema.json`
- 字段封闭：`resultId / construct / effectSize / effectSizeType(r/d/g/eta2/F/t…) / ciLow / ciHigh / pValue / n / df / sampleFlow / evidenceStrength(frozen>confirmatory>exploratory>expert>unverified) / sourceScript / interpretation / notes`
- 把"能否提取效应量"从一个布尔 flag，升级为**可审计的记录**（每个效应一条，带证据强度 + 来源）。

### 杠杆 2：页级证据检索（定位统计段落）
- `paper-evidence-rag`（FTS5，sqlite3+fitz，**即开即用**）→ 页级 snippet + file:page。
- `rag_vector_index/search`（ChromaDB+BGE 语义，**需先装 env**，`chromadb`/`fastembed` 系统 Python 未装）→ 语义补 FTS5 用词不同搜不到的缺口。

### 杠杆 3：高质量 PDF 解析（Paperflow 的 MinerU）
- 师兄的 `literature` 工作流用 MinerU 做 PDF→结构化（**表格不丢**），远优于 fitz 纯文本。
- 位置：`state/paperflow_sandbox/literature`（沙箱）。

## 三、推荐的正确方法（cc 提案）

**核心：放弃正则，改用「LLM 读 Results 段 + 按 statistical_result schema 记录 + 页级溯源」。**

具体流程（38 条核心比较）：
1. **定位**：用 FTS5 RAG（`index_pdfs.py` 建库 → `search_papers.py` 查"near transfer / working memory / group × time"）定位每篇 Results 的页码；或直接 Read 工具按页读 PDF。
2. **读取**：LLM（cc/cl）逐页读 Results 段（Read 工具渲染 PDF 页，保留表格/版面，比 fitz 文本可靠）。
3. **记录**：对每条核心比较，判断近迁移主结局能否提取效应量，按 `statistical_result` 兼容结构记录：
   - `effect_size_available`（bool）
   - `stats_type`（M/SD 或 F/t/p 或 SE 或 SEM 系数）
   - `evidence_source`（file:page，如 `2013_Borella.pdf:7`）
   - `evidenceStrength` = `unverified`（首遍）
4. **双盲**：cc/cl 各自独立读、独立记录；cx 比对分歧、裁决。

## 四、待 cx 裁决的开放问题

1. **粒度**：首遍只做"可提取性"（布尔 + 统计量类型 + page 溯源），还是直接到"提取效应量数值"（statistical_result 全字段）？—— cc 建议**先只做可提取性**（快、能先给"能否上元分析"的判定），数值提取作为下一步。
2. **溯源层**：是否必须走 FTS5 RAG 建库（要装依赖/建索引），还是"Read 工具按页读 + 手动记 file:page"已足够可查可验证？—— cc 建议**先不装 RAG 依赖**，Read 直接读 + 记 file:page 已满足"可查可验证"，RAG 留作 38 篇之外的规模化时再上。
3. **schema 落点**：效应量记录写进现有 `数据_7_比较层新表.xlsx` 的 outcome 层，还是单独建 `statistical_result` JSON 库（对齐平台 canonical）？—— cc 建议**outcome 层加 3 列**（effect_size_source / stats_type / evidence_strength），暂不建独立 JSON 库，避免双源。

## 五、工作流（对齐你要的"cx 监控 + cc/cl 独立 + 全程可查"）

```
cc 评估(本文件) ──┐
                  ├─→ cx 综合独立分析 → 定方法 → cc/cl 各自独立执行 → cx 裁决分歧
cl 独立评估      ──┘
```
每一步产物走 schema + file:page 溯源，对齐平台宪法第 2（单一权威源）、8（证据强度分级）、9（交接协议）。
