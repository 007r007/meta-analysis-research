# 指导语：cl 独立审「科研工作平台升级方案」（第二评估者）

> 角色：你是 **cl（第二评估者）**。用户已裁定主线转为「升级科研工作平台」。cc 已起草问题清单+升级地图，你**独立**审这份方案，不看 cc 的结论锚定，从平台实际代码与 paper-01 实战卡点出发独立判断。之后 cc/cl 对照、cx 综合裁决。

## 背景

paper-01 证据重建实战暴露了一批卡点（PDF 拆表、多模态看不了图、cc 假代理冒充 cl/cx、统计 schema 缺字段、检索口径漂移、一篇多试验拆分）。用户认为平台价值 > 单篇论文，要把这些卡点都解决、沉淀成平台能力。

## 必读

1. cc 初版方案：`D:\Research_Agent_Lab\reports\平台升级_问题清单与方案_cc初版.md`
2. 平台宪法：`D:\Research_Agent_Lab\PLATFORM_CONSTITUTION.md`
3. 平台操作细则：`D:\Research_Agent_Lab\AGENTS.md`
4. RAG 约定：`D:\Research_Agent_Lab\references\rag_conventions.md`
5. schema 目录：`D:\Research_Agent_Lab\references\schemas\`（含刚升 v2 的 statistical_result）
6. Paperflow 映射：`D:\Research_Agent_Lab\references\paperflow_mapping.md`

## 你要独立回答的 4 件事

1. **问题清单是否漏项**：paper-01 实战里还有哪些卡点没被 cc 列出来？（从你独立读 PDF、做定标的经验补充）
2. **每个升级动作选对了吗**：尤其 P1 文档解析——用 `fitz.find_tables()` 还是直接上 MinerU 还是切多模态？各代价/收益？
3. **"结合当前现实与之前代码"是否合理**：cc 把问题映射到平台已有代码/工具的映射对不对？有没有"已有能力没用上"或"方案重复造轮子"的地方？
4. **优先级排序**：cc 排的 1-6 顺序你认不认同？

## 输出格式

四节：①漏项清单 ②每个升级动作的独立判断（尤其 P1）③映射纠错/补漏 ④你的优先级排序。

只报告你独立判断的结论，不要猜 cc 的结论。
