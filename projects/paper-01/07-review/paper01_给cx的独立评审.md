# 给 cx 的独立评审（红队任务）

> 你被请来不是因为要附和，而是要**找出我们三方都没想到的漏洞、更优解、和死结**。请先读下面的原始文件，独立核实，再回答末尾 5 题。所有判断请给 file:line 或可核查的依据；外部知识（期刊政策、先例等）标注 UNVERIFIED。

## 背景一句话

paper-01（工作记忆训练迁移效应系统综述）投 GeroScience 被明确拒稿（非 R&R），编辑给了 15 条方法学意见。cc / claude-19 / cl（Cline）三方已收敛出一套修订方案，请你红队它。

## 请先读这些文件（你本地可读）

1. 正文：`e:\Meta-analysis writing project\projects\paper-01\06-write\paper01_draft_v1.md`
2. 表格：`e:\Meta-analysis writing project\projects\paper-01\06-write\paper01_tables.md`
3. 筛选标准：`e:\Meta-analysis writing project\projects\paper-01\03-screen\纳入排除标准_PICOS.md`
4. 三方收敛记录：`e:\Meta-analysis writing project\projects\paper-01\07-review\paper01_GeroScience拒稿_修订指导语.md`（第八节后附 V2）

## 15 条审稿意见（5 组速览，全文见指导语）

- **A 核心方法**：显著性投票计数(vote counting)而非元分析；Positive/Mixed 分类不互斥；近/远迁移未分开编码（"65% null"实为研究层结论而非近迁移结论）；按显著性投票忽略效应量/CI/样本量；51 RCT 完全可做随机效应 SMD 元分析。
- **B 干预纯度**：73%(41/56) 含联合干预（运动26/药物21/脑刺激14），仅 15 篇纯 WM，正效应无法归因于 WM。
- **C 透明度**：自动分类器排除 89%(3723/4168) 未报告算法/无人工审计；未预注册；process overlap 事后选择性删 3 正例→报"0/3"。
- **D 统计**：调节分析是生态学 between-study 比较；RoB 2 用错层面(应 outcome-specific)；无 GRADE。
- **E 口径**：入选标准 mean age≥60 但摘要写"60岁以上"；样本量仅 44/56、平均年龄 48/56 有数据(疑 AI 提取不全)；随访仅 19 篇。

## 三方已收敛的结论（供你挑战）

1. **路线 = 升级元分析**（SMD 随机效应 + meta-regression），放弃叙述性大修。
2. **根因** = vote counting 是症状，病根是「干预纯度 + 结局在研究层而非结局层编码」。
3. **co-intervention** = categorical moderator + 纯 WM k=15 作预声明敏感度，不排除，主分析用全样本。
4. **顺序** = P0 数据对账 → 效应量提取 pilot(10篇算"可计算率") → 若 <70% 降级 outcome-level RVE 部分元分析 → 再 meta-regression/GRADE。
5. **工时** ~150-170h（约 6-8 周）。

## 已发现 P0：draft 正文与自家 Table 1 打架

- 联合干预：正文 `paper01_draft_v1.md:137` 写"14(25%)/15(27%)" ↔ Table 1 实际 41(73%)/15。
- 样本量：正文 `:131` 写"53 篇 reported sample size" ↔ Table 1 仅 44 篇有 N（12 行 NR）。
- 年龄口径：`纳入排除标准_PICOS.md:117` 写"55-60岁 older adults 纳入" ↔ 摘要 `:19` 写"≥60岁"。

## 请犀利回答（要独立，不要附和）

1. **"升级元分析"这个结论你同意吗？** 不同意的话，你的替代方案是什么？（给核心理由）
2. **有没有一个我们三方都没想到的更优解？**（可以是方法、目标期刊、甚至"这篇该不该救"的层面）
3. **最大的隐藏风险是什么？**（不要重复我们已列出的：提取不全、RVE 相关系数、k 不足、双人编码、预注册）
4. **73% 联合干预、仅 15 篇纯 WM——元分析还能不能对"WM 训练本身"做出有效结论？这是不是死结？** 如果是死结，出路在哪？
5. **若你是终审编辑，看到这个修订方案，给 R&R 还是再拒？** 给一条决定性理由。
