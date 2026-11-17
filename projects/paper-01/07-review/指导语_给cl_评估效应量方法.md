# 指导语：cl 独立评估「效应量可提取性核查」方法（第二评估者）

> 角色：你是 **cl（Cline，第二评估者）**。cc 已做第一评估，你**独立**评估同一问题，**不要看 cc 的评估文件**（`评估_效应量提取方法_cc.md`），只从下面的源文件独立推导。之后与 cc 对照，由 cx 综合裁决。

## 背景

paper-01 比较层已重建：51 独立试验、38 条核心比较（①36 + ②2）。下一步「效应量可提取性核查」——对 38 条核心比较逐条判断能否提取效应量（M/SD/change/t），以决定能否上全量元分析。

cc 用「fitz 纯文本 + 正则」对 38 篇 Results 段探测统计量，得到 6 篇"全 False"（Seq6/19/36/40/57/60），抽查发现是**误报漏报**：Seq19(Borella 2013) 明确报告 group×session 统计量、Seq57(Zelinski 2014, N=487) 用 SEM、Seq6 两子研究 Results 小写标题。根因：fitz 断行/拆表/段边界抓不准。**正则不可靠。**

## 必读文件（绝对路径）

平台（D 盘科研工作平台）：
1. `D:\Research_Agent_Lab\AGENTS.md`
2. `D:\Research_Agent_Lab\PLATFORM_CONSTITUTION.md`
3. `D:\Research_Agent_Lab\references\schemas\statistical_result.schema.json`
4. `D:\Research_Agent_Lab\references\rag_conventions.md`
5. `D:\Research_Agent_Lab\skills\public\paper-evidence-rag\SKILL.md`
6. `D:\Research_Agent_Lab\references\paperflow_mapping.md`

项目（paper-01）：
7. `E:\Meta-analysis writing project\projects\paper-01\07-review\数据字典_比较层新表_schema.md`（含 outcome 层字段）
8. `E:\Meta-analysis writing project\projects\paper-01\07-review\比较层重编码表_v3_终表.md`

## 要回答的 4 个问题

1. 正则为什么不可靠？（一句话 + 关键根因）
2. 平台里有哪些能力能帮上忙？（列你找到的，注明「即开即用」还是「需装依赖」）
3. 你推荐的正确方法（流程分几步、每步产出什么）
4. 三个开放问题各给立场 + 一句理由：
   - 首遍做「可提取性」（布尔+类型+溯源）还是直接「提取效应量数值」？
   - 溯源层要不要上 RAG 建库，还是「Read 按页读 + 手动记 file:page」已够？
   - 效应量记录落点：写进 `数据_7` 的 outcome 层，还是单独建 statistical_result JSON 库？

## 输出格式

四节：①问题诊断 ②平台能力盘点 ③你的推荐方法 ④三个开放问题的立场。只报告你独立推导的结论，不要猜 cc 的结论。
