# 指导语：cx 综合裁决「效应量可提取性核查」方法（定稿）

> 角色：你是 **cx（Codex，最终裁决者）**。cc 与 cl 已各自独立评估完毕，且**已在两个分歧点上收敛**（cc 采纳 cl 立场）。请你最终定稿方法 + 拍板 schema 升级清单。

## 必读
1. `E:\...\07-review\评估_效应量提取方法_cc.md`（cc 评估）
2. cl 评估（见本指导语末附的 cl 立场摘要；cl 原文由用户转达）
3. `D:\Research_Agent_Lab\references\schemas\statistical_result.schema.json`（canonical 统计结果 schema）
4. `E:\...\07-review\数据字典_比较层新表_schema.md`

## 背景
paper-01 比较层已定稿（55 trial / 40 核心候选比较）。下一步「效应量可提取性核查」——逐条判断能否提取效应量，决定能否上全量元分析。正则提取被证不可靠（fitz 断行/拆表 + 字符层工具做语义层判定）。

## 已收敛的结论（cc + cl 一致，请你确认）
- 弃正则；Read 按页渲染读为判定层，file:page 溯源。
- 首遍只做「可提取性」（布尔 + 统计量类型 + 溯源），不直接抽数值；抽数待类型定后。
- FTS5 建库作「定位层」（即开即用），不上向量 RAG。
- 效应量记录落独立 `statistical_result` JSON 库，outcome 层只存引用键。

## 待你拍板的 2 件事

### 1. schema 升级清单（cl 独立发现的缺口，cc 认可）
`statistical_result.schema.json`（当前 v1）缺页级溯源与比较绑定字段：
- `sourcePage`（页级溯源，现有 sourceScript/sourceOutput 只是脚本级）
- `comparison_id`（绑定到 paper-01 比较层）
- `seq`（原始 Seq）
- 方差/SE 字段（反算 Hedges' g 需要）

**请裁定**：确认按宪法第 10 条走 v1→v2 升级吗？最终字段清单（除上述，是否还要 `statistic_type`/`outcome_domain`/`timepoint`）？请给最终字段列表。

### 2. 落点细则
若确认独立 JSON 库：
- 路径/命名（建议 `04-extract\结果_1_效应量提取库.json`，顶层 `{schemaVersion:2, results:[...]}`）
- `resultId` 命名（建议 `R{outcome_id}`，沿用 T/A/C/O 前缀）
- `数据_7` outcome 层指针字段名（建议 `result_id`）
- 双编码规模：先 10 条定标（覆盖 M/SD/change/t/F/group×time/SEM 各至少 1 条）再全量双人，还是直接全量双人？

## 输出格式
直接给最终定案：
1. schema v1→v2 升级：确认 + 最终字段清单
2. JSON 库路径/resultId/指针字段名
3. 双编码规模
4. 一句话确认已收敛结论

---

## 附：cl 立场摘要（原文由用户转达）
- 根因：字符层工具做语义层判定，漏报（Seq19 断行/拆表、Seq57 SEM、Seq6 小写标题）+ 误报（引用他人 p 值）双向失败。
- 方法四步：建 FTS5 索引 → 候选页定位 → 页级 Read 判定（可提取性）→ 数值提取+三层一致性审计。
- 三立场：①首遍可提取性不抽数；②FTS5 定位层+Read 判定层，不上向量库；③独立 statistical_result JSON 库，但必须先补 sourcePage/comparison_id 字段缺口（v1→v2）。
