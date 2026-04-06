# 叙述性系统综述论文撰写指导方案
> 基于 Paper-01（老年WM训练迁移效应系统综述）实战经验
> 整理人：CC（Claude Code）| 日期：2026-04-06
> 适用范围：叙述性系统综述（Narrative Systematic Review），尤其是认知训练/干预类选题
> 本文档供 oo 修改完善后作为后续写作标准操作流程（SOP）

---

## 一、总体原则：三件事必须在写作开始前确定

在 Paper-01 中，oo 和 cc 在协作过程中最深的体会是：**写作阶段的大部分困难，根源都在写作之前没有想清楚**。写作本身是相对机械的，真正困难的是以下三件事必须在落笔之前完成：

1. **核心论点（Thesis）**：你的综述想证明什么？是"训练有效"、"训练无效"、还是"效果依赖于条件X"？这个定位决定了整篇文章的叙事逻辑。
2. **证据体系**：你手里有多少篇文献，它们的数据能不能支撑你的论点？结论是否需要分层（例如有主动对照 vs 无主动对照单独报告）？
3. **节号框架**：每一节写什么，用什么数据，得出什么结论——这个框架必须在开始写第一行正文之前确定，且不能在写作过程中频繁调整。

Paper-01 的实际做法：oo 先设计框架，cc 按批次执行，每批次有明确的节编号和内容定义，写作过程无节号漂移。

---

## 二、写作前：框架设计流程

### 2.1 从研究问题到节号框架

**步骤：**

```
研究问题（1-2句话）
    ↓
识别数据维度：你要回答几个"子问题"？
    ↓
每个子问题 → 一个 Results 小节
    ↓
每个 Results 小节 → 它的 Discussion 对应节
    ↓
整体框架定稿，节号锁定
```

**Paper-01 的实际框架：**

```
研究问题：WM训练在健康老年人中的迁移效应如何，哪些因素调节效果？

Results:
  3.1  研究概况（纳入量、年份分布、方法特征）
  3.2  近迁移效应（整体 + 主动/被动对照对比）
  3.3  远迁移效应（按领域分节：流体智力/EF/情景记忆/日常功能/总体模式）
  3.4  调节因素（5个子节）
       3.4.1 基线WM水平
       3.4.2 年龄亚组
       3.4.3 认知过程重叠度（创新点）
       3.4.4 训练剂量与密度
       3.4.5 其他潜在调节变量（教育/监督方式）
  3.5  维持效应
  3.6  神经影像证据

Discussion:
  4.1  补偿 vs 放大效应：整合框架
  4.2  认知过程重叠度的角色
  4.3  训练剂量、设计质量与主动对照问题
  4.4  方法学建议（8条）
  4.5  局限性
```

**关键原则：**
- Discussion 节数 = Results 中的核心发现数，一一对应
- Discussion 不是 Results 的重复，而是"这意味着什么"
- Results 报数据，Discussion 讲机制和含义

### 2.2 框架审核清单（写作前必做）

在开始写第一个字之前，对照以下清单：

- [ ] 每个 Results 小节，我有多少篇文献的数据可以用？（<3篇 → 降级为 Limitations）
- [ ] 每个 Discussion 对应的 Results 节，核心结论是什么（一句话）？
- [ ] 全文最核心的"贡献句"是什么？（通常出现在 Introduction 末段 + Conclusion 开头）
- [ ] 如果有负面结果（比如"训练无效"），有没有想好怎么正面叙述它的意义？

---

## 三、各节写法详解

### 3.1 Abstract（摘要）

**结构：** Background → Objective → Methods → Results → Conclusions（共5段，APA格式）

**最重要的写法原则：Results 段必须有实际数字，不能只写方向性结论。**

Paper-01 Abstract Results 段的写法示例（oo 提供，cc 原文插入）：

> "Across 56 included studies, near transfer was assessed in 46 studies (82%) and far transfer in 43 studies (77%). Overall, transfer effects were limited and highly variable: only 9 studies (16%) reported consistent positive transfer across all outcomes, 8 studies (14%) showed mixed findings, and 35 studies (63%) found no significant between-group differences on any transfer measure. Among studies assessing near transfer, 30 of 46 (65%) yielded null overall conclusions, indicating that even proximal generalization is not reliably achieved under controlled conditions."

**模板要素：**
```
Results段必须包含：
- 纳入研究总数（k=XX）
- 最重要结局的百分比（XX%正向/XX%无效/XX%混合）
- 至少一个"反直觉"或"关键发现"（使读者想看全文）
```

**常见错误：**
- Results 段只写"findings were heterogeneous"——太模糊，期刊编辑直接拒稿
- Conclusions 段重复 Results 而不给行动建议

### 3.2 Introduction（引言）

**标准4段结构：**

```
段1：现象/背景（为什么这个话题重要）
段2：已有理论和研究（文献综述，指出分歧）
段3：已有综述/Meta分析的结论和不足（你的切入点）
段4：本研究目的（3个aim，逐条列出）
```

**Paper-01 Introduction 的实际逻辑链：**

```
WM随年龄下降 → 认知训练有望改善 → 但迁移效应不一致
→ 理论分歧：CRUNCH vs 放大效应 vs 认知储备
→ 已有综述：Lampit积极 vs Melby-Lervåg等消极
→ 缺口：（1）专门聚焦健康老年人≥60岁，（2）调节因素系统梳理，（3）认知过程重叠度作为新框架
→ 本研究目的：(1)综合迁移效应 (2)描述训练参数 (3)识别调节因素
```

**写作技巧：**
- 每一段之间要有"因此"或"然而"的逻辑转折，不能是平行罗列
- 第4段（目的段）的3个aim，必须和 Results 的3个大节一一对应

### 3.3 Methods（方法）

**叙述性综述 Methods 必须包含的7个子节：**

```
2.1 注册与方案（PROSPERO号）
2.2 纳入标准（PICOS框架逐条列出）
2.3 检索策略（4库 + 检索式 + 检索日期）
2.4 研究筛选（三轮流程，每轮人数）
2.5 数据提取（提取字段清单）
2.6 质量评估（RoB工具名称 + 维度）
2.7 数据综合（为什么用叙述而非Meta + SWiM指南 + 一致性分级标准）
```

**关键写法——2.7 数据综合：**

必须明确说明你的"证据强度"分级标准，否则审稿人会质疑。

Paper-01 使用的标准：
- *Consistent*：>75%研究结论一致
- *Moderate*：50–75%
- *Mixed*：<50%
- *Insufficient*：<3篇研究

这个标准必须在 Methods 里明确，在 Results 每节末尾用到，在 Table 3 中汇总。**三处使用必须完全一致。**

**关于研究设计异质性的处理（叙述综述常见陷阱）：**

如果你的纳入文献同时包含 RCT、准实验和单组前后测，需要在 Results 里**分层描述**，不能混同：

```
写法模板：
"共X篇研究考察了[结局]，其中Y篇RCT，Z篇准实验，W篇单组设计。
在Y篇RCT中，...
综合来看，证据一致性评级为[Consistent/Moderate/Mixed/Insufficient]。"
```

### 3.4 Results（结果）

**Results 的整体写作哲学：** 数据先行，解释从简，评判留给 Discussion。

**每个 Results 小节的标准段落结构：**

```
段1：该变量的整体分布（k=多少，占比多少）
段2：主要发现（正向/无效/混合的比例 + 代表性研究举例）
段3：亚组对比（有主动对照 vs 无主动对照，或其他重要分层）
段4：证据强度评级（Consistent/Moderate/Mixed/Insufficient）
     + 一句话解释为什么是这个等级
```

**Paper-01 Results 关键写作决策记录（供参考）：**

**决策1：近迁移结论如何报告**

问题：我们没有单独编码"近迁移专属结论"，只有综合结论字段。

解决：在 3.2 节开头加一句透明说明：
> *"The 'overall conclusion' classification reflects the aggregate pattern across all reported transfer outcomes (near and far combined). A near-transfer-specific conclusion field was not coded; readers should interpret near transfer findings in this section accordingly."*

原则：**信息不完整时，不是回避，而是明确说明局限，并让读者知道你知道这个局限。**

**决策2：效应量只有10篇有数据**

解决：报告这10篇的中位数 d=0.95，但立即加上3条限定语：
1. 仅代表56篇中的17.9%
2. 无主动对照的研究可能通货膨胀
3. 这是假设生成，不是结论

**决策3：低重叠度研究看似支持"远迁移更好"的悖论**

低重叠6篇：正向=3，无效=3，正向率50%，高于高重叠的21%。
这个数字表面上是反常的，但cc分析后发现：3篇正向研究全有设计缺陷（单组前后测/运动复合/脑刺激复合）。

解决：不是忽略这个数据，而是显式分析，最终写成比原框架更强的论据：

> "Removing these confounded cases, the adjusted positive rate for low-overlap studies drops to 0 of 3 (0%)...This corrected pattern actually strengthens the inference that WM training does not produce reliable transfer to cognitively distant domains."

原则：**反常数据不是问题，是机会。正面拆解反常数据，比忽略它更能体现论文的学术深度。**

### 3.5 Discussion（讨论）

**Discussion 的结构设计原则：**

Discussion 不应该是 Results 的翻译，每节必须完成以下3件事：
1. **陈述发现**（1-2句，非重复，要有新的角度或整合）
2. **与已有理论/文献对话**（为什么我们的结果和X一致/不一致）
3. **给出机制解释或研究意义**（这意味着什么，未来怎么做）

**Paper-01 Discussion 4节结构的设计逻辑：**

```
4.1 基线WM调节效应（对应Results 3.4.1）
    → 讨论补偿 vs 放大效应的理论分歧
    → 提出新整合框架：调节方向本身受训练设计调节（自适应 vs 固定难度）

4.2 认知过程重叠度（对应Results 3.4.3，也是全文创新点）
    → 拆解低重叠悖论，确立迁移距离假说
    → 末尾加实践意义句

4.3 训练剂量 + 设计质量 + 主动对照问题（对应Results 3.2/3.4.4）
    → 拆解中等剂量"假异常"（实为自适应+联合干预混淆）
    → 主动对照问题与非特异性因素

4.4 方法学建议（8条）
    → 从全文所有发现中提炼，不是泛泛而谈
    → 每条建议必须有数据支撑（例如"建议报告剂量"→因为33%研究缺失频率数据）

4.5 局限性
    → 按影响大小排序，不是走过场
```

**Discussion 最重要的写作技巧——"整合框架"段：**

在 Discussion 某节中提出一个新的整合框架，是从"描述性综述"升级为"理论贡献"的关键。

Paper-01 在 4.1 末尾的做法：
> "We propose that the direction of baseline moderation may itself be moderated by training design—specifically, task difficulty calibration. Adaptive training protocols...create conditions under which lower-ability individuals can sustain effortful engagement...Fixed-difficulty protocols, by contrast, may present a ceiling for lower-ability individuals..."

这段话不是描述已有证据，而是基于证据**提出新假设**，这是论文对理论的实际贡献。每篇论文至少应有一个这样的整合段落。

### 3.6 Conclusion（结论）

**Conclusion 的3段结构：**

```
段1：核心发现总结（最重要的一两个数字 + 总体判断）
段2：创新贡献（本研究在方法或理论上的特殊贡献）
段3：前景展望（下一步研究方向，要具体，不能是"更多研究需要X"这种空话）
```

**Paper-01 Conclusion 的实际写法（示例）：**

- 段1：WM训练在受训任务上有效，但63%研究无迁移效应，主动对照下更明显
- 段2：认知过程重叠度框架 + 低重叠悖论的数据驱动校正，是方法论贡献
- 段3：未来需要个体化训练设计，匹配基线能力，使用神经影像生物标记

---

## 四、批次写作工作流（cc 执行规范）

Paper-01 采用5批次写作，每批次有明确的输入、输出和验证点。

### 4.1 批次划分原则

```
批次1：骨架（Table 1 + Methods + Results 3.1 + 配套图脚本）
批次2：近迁移 + 远迁移（Results 3.2 + 3.3）
批次3：调节因素 + 维持 + 神经影像（Results 3.4–3.6）
批次4：Discussion 全文 + Conclusion
批次5：References + 表格校正 + 补充句
```

**优先级逻辑：**
- 先写 Methods（最客观，最好写）
- 再写 Results（数据驱动，有什么写什么）
- 最后写 Discussion（需要 Results 完整后才能整合）
- Abstract 最后写，或由 oo 在看完全文后起草 Results 段

### 4.2 每批次的交付标准

每批次完成后，cc 需要提供：
1. 修改后的完整文件（paper01_draft_v1.md）
2. commit 号
3. 该批次写作字数 + 总字数
4. 节号清单确认（防止节号漂移）

### 4.3 oo-cc 协作接口

**oo 提供：**
- 精确写法（特殊段落直接给文字）
- 数据解释方向（例如"低重叠悖论要正面拆解"）
- 框架调整决策（例如"教育和监督合并为3.4.5"）

**cc 提供：**
- 所有 Excel 数据查询和交叉表
- 数字精确性验证（所有 k 值、百分比从原始数据核查）
- 文字一致性检查（确保数字在 Abstract / Results / Table / Figure 中不矛盾）
- 发现 oo 框架中的潜在问题（例如低重叠悖论是 cc 分析后发现并提出的）

**协作原则：cc 不只是执行者，也是数据分析师。发现数据和框架不一致时，主动提出并给出分析。**

---

## 五、数字一致性管理（最容易被审稿人发现的问题）

### 5.1 易出错的数字位置

同一个数字往往出现在4-5个地方：
- Abstract Results 段
- Results 正文各节
- Table 3（证据汇总表）
- Figure 3（调节因素可视化）
- Discussion 引用时

**这4-5处必须完全一致。** Paper-01 发生过的错误示例：Abstract 最初写"far transfer in 47 studies (84%)"，实际 Excel 数据是43篇（77%）。

### 5.2 数字核查流程

```
写完每一批次后：
1. 从草稿中提取所有百分比和k值
2. 用 Python 脚本从 Excel 原始数据重新计算
3. 逐一比对
4. 修改所有不一致处（不只改一处，要改所有出现的位置）
```

### 5.3 cc 核查重点字段

- Overall 正向/无效/混合的 k 值和百分比
- 各亚组的 k 值（Active ctrl、N-back、Adaptive 等）
- 训练剂量的 NR 率（未报告率）
- 有无主动对照的正向率差值

---

## 六、图表写作规范

### 6.1 Figure 系列

Paper-01 的3个图的功能分工：

| 图号 | 内容 | 工具 | 关键参数 |
|------|------|------|---------|
| Figure 1 | PRISMA 流程图 | ggplot2（R） | 必须四库漏斗，每步n |
| Figure 2 | 发表年份分布 | ggplot2（R） | 年份范围，峰值年标注 |
| Figure 3 | 调节因素结局分布 | ggplot2（R） | 水平堆积条，facet_wrap分组 |

**R 图脚本标准：**
- 所有 k 值硬编码在脚本里（必须和文中一致）
- ggsave 路径使用绝对路径
- 文件名含 figure 编号（figure1_prisma.png）
- 在数据区上方加注释标明数据来源（"Based on Excel col40 cross-tab"）

### 6.2 Table 系列

Paper-01 的3个表的功能分工：

| 表号 | 内容 | 关键要求 |
|------|------|---------|
| Table 1 | 56篇研究特征汇总 | 按 Seq 排序，所有字段来自 Excel 原始数据 |
| Table 2 | 偏倚风险评估 | RoB2/ROBINS-I维度，投稿前必须完成 |
| Table 3 | 调节因素证据汇总 | 证据强度分级必须和 Methods 2.7 一致 |

**Table 3 证据强度填写原则（Paper-01经验）：**
- 不能填模糊的描述，必须套用 Methods 里定义的4个等级
- 认知过程重叠度这类"分布性发现"不能强行套等级，要写 "Insufficient – distributional pattern only"
- k 值使用精确数字，不要用 ~（约）

---

## 七、参考文献管理

### 7.1 文件结构

```
paper01_references.md    ← 独立文件，完整APA 7th列表
paper01_draft_v1.md      ← References节直接包含全文（方便审阅）
```

### 7.2 APA 7th 常见格式问题

| 问题 | 错误写法 | 正确写法 |
|------|---------|---------|
| 作者超过20人 | 全部列出 | 19位 + … + 最后一位 |
| 期刊名斜体 | 不斜体 | *Psychological Bulletin* |
| 卷号斜体 | 不斜体 | *Developmental Psychology, 49*(2) |
| 期号加括号 | 不用括号 | 错误：49, (2) → 正确：*49*(2) |
| DOI格式 | doi:10.xxxx | https://doi.org/10.xxxx |

### 7.3 引用一致性

每次 Discussion 引用数据时，如果引用了具体研究（"Zinke et al., 2014 found..."），该文献必须出现在 References 中。投稿前必须做一次全文 References 核查。

---

## 八、写作质量自检清单（投稿前）

### 8.1 结构检查

- [ ] Abstract 的5段结构完整，Results 段有实际数字
- [ ] Introduction 末段明确列出3个 aim，与 Results 节对应
- [ ] Methods 2.7 明确了证据强度分级标准
- [ ] Results 每节末尾都给出了证据强度评级
- [ ] Discussion 每节都有"与已有文献对话"，不只是重述 Results
- [ ] Discussion 至少有一个整合性框架或新假设
- [ ] Conclusion 第2段明确了本研究贡献（不是泛泛而谈）
- [ ] PROSPERO 注册号已填入 Methods 2.1

### 8.2 数字一致性检查

- [ ] Abstract 中的 k 值和百分比 = Results 正文数字
- [ ] Table 3 的 k 值 = Results 正文数字
- [ ] Figure 3 的 k 值 = Results 正文数字
- [ ] Figure 3 R脚本中的硬编码数字 = Table 3 数字
- [ ] 所有引用格式一致（APA 7th）
- [ ] References 中每篇文献都在正文中被引用

### 8.3 PRISMA 2020 合规检查

- [ ] PRISMA 流程图（Figure 1）已生成，数字正确
- [ ] Table 2 RoB 评估已完成
- [ ] Methods 2.6 说明了 RoB 工具（RoB2 for RCT + ROBINS-I for NRS）
- [ ] 检索策略全文作为 Supplementary Materials 附上
- [ ] PROSPERO 注册已完成

---

## 九、Paper-01 留下的未解问题（供后续参考）

以下是 Paper-01 在写作过程中碰到的、没有完美解决的问题，记录在此供后续 paper 参考：

### 问题1：认知过程重叠度的分类主观性

Paper-01 的 overlap 分类是 AI 辅助初分 + 人工确认，但"中等重叠"和"高重叠"之间的边界仍然模糊。

**建议做法（下次）：**
- 在 Methods 里列出完整的分类规则（每个 overlap 等级的操作性定义 + 例题类型）
- 建立双人独立分类流程，计算 Cohen's κ
- 将 overlap 分类列在 Supplementary Table 里，每篇文献一行

### 问题2：总体结论字段的编码信度

"总体结论"是最容易出错的字段，Paper-01 做了大量人工核查，但仍有不确定案例。

**建议做法（下次）：**
- 在提取表里为"边界案例"设一个 flag 列
- 边界案例全部请第二人独立判断
- 在 Methods 里写明 kappa 值

### 问题3：没有近迁移专属结论字段

Paper-01 的综合结论字段混合了近迁移和远迁移，导致近迁移专属分析受限。

**建议做法（下次）：**
- 在提取表里设独立的近迁移结论字段（Positive/Null/Mixed，单独基于近迁移测量）
- 如果文献只报告近迁移，这个字段和综合结论相同
- 如果文献同时有近远迁移，需要分别判断

---

## 十、从 Paper-01 到通用 SOP：可迁移的核心经验

### 经验1：数据驱动的反常分析比简单叙述更有价值

Paper-01 最强的论证不是"WM训练效果有限"（这是老结论），而是通过拆解低重叠度研究的设计缺陷，**用数据校正了一个表面悖论**。这种"发现反常 → 深挖原因 → 给出更强结论"的逻辑，比平铺直叙要有力得多。

**通用原则：** 遇到数据不符合预期时，不要绕过去，要正面分析。

### 经验2：cc 的价值不只是执行，更是数据核查和问题发现

Paper-01 中，cc 发现了：
- 低重叠悖论（3篇正向研究全有设计缺陷）
- Excel 数据中的原有字段占位符行（会导致计算错误）
- 中等剂量"假异常"（88%自适应+76%联合干预混淆）

这些都是 oo 的框架没有预见到的，但对文章质量有重大影响。

**通用原则：** cc 在执行每批次写作前，要先独立做一次数据核查，不能只是被动接受框架。

### 经验3：节号一旦确定就不要改

Paper-01 中曾经发生节号漂移（训练剂量被误放为独立的3.4节，而非3.4.5子节），导致返工。

**通用原则：** 写作开始前，把完整节号框架写在一个地方（可以是草稿文件第一行的注释），每批次写作前确认。

### 经验4：Abstract 的 Results 段由 oo 起草，cc 原文插入

这是最重要的质量控制节点。Abstract 是编辑和审稿人最先读的，也是最难写好的。Paper-01 的做法是 oo 看完全文草稿后起草精确措辞，cc 原文插入不做修改。

**通用原则：** 不确定措辞的段落，给 oo 看后再写进去，不要 cc 自行发挥。

---

## 附录：Paper-01 写作关键参数速查

| 参数 | 数值 |
|------|------|
| 最终纳入 | 56篇（2003-2026） |
| 检索数据库 | PubMed/PsycINFO/WoS/CNKI |
| 筛选漏斗 | 4168 → 445 → 56 |
| 整体正向率 | 16%（k=9） |
| 整体无效率 | 63%（k=35） |
| 近迁移正向率 | 20%（9/46） |
| 主动对照正向率 | 20%（vs 无主动对照 40%） |
| 草稿字数 | 10,105词（含References） |
| 写作批次 | 5批次 |
| 最终commit | d992275 |
| 目标期刊 | Ageing Research Reviews（Q1） |

---

*本文档供 oo 审阅修改后作为通用写作 SOP。*
*下次开始新 paper 写作前必须先读本文档。*
*更新日期：2026-04-06*
