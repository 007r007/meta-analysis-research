# 给 oo 的交接提示词
> 撰写人：cc（Claude Code）| 日期：2026-04-06
> 目的：请 oo 审阅 Paper-01 完整初稿，评估质量，确认后续计划

---

## 一、背景说明

oo 你好，我和 cc 在过去几天完成了 Paper-01 的完整初稿写作（共5批次）。
所有文件已推送至 git 仓库，最新 commit 为 `d992275`（2026-04-06）。

**Paper-01 主题：** 健康老年人工作记忆训练迁移效应的系统综述
**纳入文献：** 56篇（2003–2026），17个国家
**综述方法：** 叙述性系统综述（Narrative Synthesis，SWiM指南）
**目标期刊：** Ageing Research Reviews（Q1，IF~10）

---

## 二、06-write 目录下生成的所有文件

以下文件全部已提交 git，oo 可直接读取：

### 主文件

| 文件名 | 内容 | 字数/规模 |
|--------|------|----------|
| `paper01_draft_v1.md` | **完整论文草稿**（从Abstract到References） | ~10,105词 |
| `paper01_tables.md` | Table 1（56篇特征）+ Table 2（RoB占位）+ Table 3（调节因素证据） | 3张表 |
| `paper01_references.md` | 完整APA 7th参考文献列表 | 56篇纳入 + ~20篇方法论文献 |

### 图脚本（paper01_figures/ 目录下）

| 文件名 | 内容 | 状态 |
|--------|------|------|
| `figure1_prisma.R` | PRISMA 2020 流程图（ggplot2） | 脚本完整，可直接在R中运行生成PNG |
| `figure2_year_dist.R` | 发表年份分布柱状图 | 脚本完整，56篇年份硬编码 |
| `figure3_moderator_summary.R` | 调节因素结局分布堆积条形图 | 脚本完整，k值已按Excel实际数据校正 |

### git 提交历史（写作阶段）

| commit | 内容 |
|--------|------|
| `39a3768` | 批次1：Table1 + Methods + Results 3.1 + 3个R图脚本 |
| `4f07997` | 批次2：Abstract Results段 + Results 3.2近迁移 + 3.3远迁移 |
| `94c5cba` | 批次3：Results 3.4调节因素 + 3.5维持效应 + 3.6神经影像 |
| `1a9d70f` | 批次4：Discussion 4.1–4.5全文重构 + Conclusion |
| `d992275` | 批次5：完整References列表 + Table3数据修正 + 4.2实践意义句 |

---

## 三、草稿结构总览

```
Abstract（5段：Background/Objective/Methods/Results/Conclusions）
1. Introduction（4段逻辑链：WM下降→训练争议→已有综述不足→本研究目的）
2. Methods
   2.1 注册与方案（PROSPERO待填）
   2.2 纳入标准（PICOS）
   2.3 检索策略（4库）
   2.4 研究筛选（三轮流程）
   2.5 数据提取（57字段）
   2.6 质量评估（RoB2 + ROBINS-I）
   2.7 数据综合（SWiM + 证据强度4级）
3. Results
   3.1 研究概况
   3.2 近迁移效应
   3.3 远迁移效应（3.3.1流体智力/3.3.2EF/3.3.3情景记忆/3.3.4日常功能/3.3.5总体模式）
   3.4 调节因素（3.4.1基线WM/3.4.2年龄亚组/3.4.3认知过程重叠度/3.4.4训练剂量/3.4.5其他）
   3.5 维持效应
   3.6 神经影像证据
4. Discussion
   4.1 补偿 vs 放大效应：整合框架
   4.2 认知过程重叠度的角色
   4.3 训练剂量、设计质量与主动对照问题
   4.4 方法学建议（8条）
   4.5 局限性（4条）
5. Conclusion（3段）
References（完整APA 7th，按字母顺序）
```

---

## 四、关键数据（Excel 实际计数，已核验）

| 分析维度 | 数据 |
|---------|------|
| 整体结论 | Null=35(63%), Positive=13(23%), Mixed=8(14%) |
| 近迁移（n=46）| 正向9(20%), 混合7(15%), 无效30(65%) |
| 远迁移（n=43）| 正向9(21%), 混合5(12%), 无效29(67%) |
| 主动对照（n=46）| 正向率20% |
| 无主动对照（n=10）| 正向率40% |
| 高重叠（n=43）| 正向率21% |
| 低重叠（n=6，校正后）| 正向率0%（3篇正向均有设计缺陷） |
| 中等剂量11-25session（n=25）| 正向率36%（但88%自适应+76%联合干预，存在混淆） |

---

## 五、已确认写入草稿的 oo 原文段落

以下段落由 oo 直接提供文字，cc 原文插入，未做任何修改：

1. **Abstract Results 段**（commit 4f07997）
2. **3.2节开头注记**（"The 'overall conclusion' classification reflects..."）
3. **3.2节 d值说明段**（"The median effect size (d = 0.95) should be interpreted with caution..."）
4. **4.1节整合框架段**（"We propose that the direction of baseline moderation may itself be moderated..."）
5. **4.3节中等剂量异常段**（"An exploratory observation from the present review warrants cautious attention..."）
6. **4.2节末尾实践意义句**（"Practically, this implies that training programs designed to improve specific everyday competencies..."）

---

## 六、当前待完成项（投稿前必须）

| 项目 | 优先级 | 说明 |
|------|--------|------|
| **Table 2 RoB评估** | 🔴 最高 | 目前为占位符，需对56篇文献逐条用RoB2/ROBINS-I评估 |
| **PROSPERO注册** | 🔴 最高 | Methods 2.1有占位符，PRISMA 2020强制要求 |
| **R图脚本运行生成PNG** | 🟡 中 | 3个脚本已写好，需在R环境中运行生成实际图片 |
| **Supplementary：完整检索式** | 🟡 中 | Methods 2.3提到，需整理4个数据库完整检索式 |
| **双人核查记录** | 🟡 中 | PRISMA要求至少20%文献双人独立提取，需补记录 |
| **Borella系列交叉引用** | 🟢 低 | 4.1节可选补充点，不影响主体质量 |

---

## 七、请 oo 重点审阅的问题

**问题1：整体结论的百分比口径**

草稿里 Positive=13(23%)，但 Abstract Results 段 oo 原文写的是"only 9 studies (16%) reported consistent positive transfer"。
这两个数字口径不同：9是"所有结局均正向"，13是"总体结论=正向"。
**请 oo 确认：全文统一用哪个口径，并告知 cc 修正所有出现的位置。**

**问题2：Table 3 证据强度是否准确**

Table 3 目前的证据强度分级：
- Baseline WM → Mixed（两个子行都是Mixed）
- Age Group → Consistent（k=42 young-old，k=14 old-old）
- Cognitive Process Overlap → "Insufficient – distributional pattern only"
- Training Dose → Insufficient
- Active Control → Consistent（active）/ Moderate（no active）

**请 oo 核查这些分级是否与 Results 文本一致。**

**问题3：Results 3.4.2 年龄亚组的证据强度**

草稿 3.4.2 末尾写的是"Evidence for age as a moderator is therefore classified as *mixed*"，但 Table 3 里年龄亚组写的是"Consistent"。
**请 oo 确认应统一为 Mixed 还是 Consistent，并告知 cc 修正。**

**问题4：Discussion 4.1 的 Borella 系列补充**

oo 之前提到 Borella 系列（seq2/15/19/48，old-old near-transfer维持）可以作为"补充点A"加入 4.1。
**请 oo 决定是否需要补充，如需要请提供文字，cc 插入。**

---

## 八、请 oo 给 cc 的后续任务安排

请 oo 审阅草稿后，给出以下几项的明确指示：

1. **草稿整体质量判断**：可以进入润色阶段，还是需要大幅修改某节？
2. **口径问题修正**（问题1）：确认 Positive 的统一定义和数字
3. **Table 3 修正清单**（问题2+3）：哪些格里的数字或分级需要改
4. **RoB 启动计划**：是否由 Kimi 预评 + 人工核查，还是其他安排
5. **PROSPERO 注册**：是否现在就注册，还是等 RoB 完成后一起
6. **目标期刊确认**：Ageing Research Reviews 是否仍然是首选，还是考虑其他期刊

---

## 九、文件路径速查

```
E:\Meta-analysis writing project\projects\paper-01\
├── 06-write\
│   ├── paper01_draft_v1.md          ← 完整草稿（10,105词）
│   ├── paper01_tables.md            ← Table 1/2/3
│   ├── paper01_references.md        ← 完整参考文献
│   └── paper01_figures\
│       ├── figure1_prisma.R         ← PRISMA流程图脚本
│       ├── figure2_year_dist.R      ← 年份分布脚本
│       └── figure3_moderator_summary.R ← 调节因素脚本
├── 04-extract\
│   └── 数据_6_数据提取表_v3_research.xlsx  ← 原始数据（57列，56行）
└── 03-screen\
    └── 数据_5_第三轮全文筛选.xlsx    ← 56篇纳入名单
```

---

*请 oo 读完草稿后，在此文档下方或单独文档中给出审阅意见，cc 将按批次执行修改。*
