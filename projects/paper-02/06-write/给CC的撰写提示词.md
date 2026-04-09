# 给 CC 的撰写提示词
> 撰写人：oo | 日期：2026-04-09
> 目的：请 CC 基于已完成的数据提取表，撰写 Paper-02 完整初稿

---

## 一、背景说明

CC 你好，数据提取阶段已全部完成。

**Paper-02 主题：** 父母教育水平与儿童早期神经发育：EEG、ERP、fNIRS及神经影像证据的系统综述（0–8岁）
**英文标题（暂定）：** Parental education level and early childhood neural development: a systematic review of EEG, ERP, fNIRS, and neuroimaging evidence (ages 0–8 years)
**纳入文献：** 17篇（最终，经方案A严格筛选）
**综述方法：** 叙述性系统综述（Narrative Synthesis）
**目标期刊：** Developmental Cognitive Neuroscience（Q1，IF≈4.5）

---

## 二、关键文件路径

```
projects/paper-02/
├── 03-screen/
│   └── 数据_5_第三轮全文筛选.xlsx        ← 筛选流程（109→17篇）
├── 04-extract/
│   ├── 数据_7_数据提取表_v1.xlsx         ← 核心数据（17篇，rows 4–20）
│   └── 文档_数据提取表字段设计_v2.md     ← 字段说明
└── 06-write/
    └── 文档_1_Methods检索筛选段落草稿.md ← Methods v1.3（已更新至17篇）
```

---

## 三、提取表字段速查（撰写时直接引用）

| 字段 | 含义 |
|------|------|
| A1–A9 | 基本信息（作者/年/国家/设计/N/年龄/A9年龄分组） |
| B1–B5 | 父母教育测量方式、效应类型 |
| C1–C7 | 神经测量模态、指标、方法、脑区 |
| D1–D6, D3b | 结局方向、D2一句话摘要、D3精确统计值、D3b方向标签 |
| E1–E3 | 机制路径（认知刺激/慢性应激/中介分析） |
| F1–F4 | NOS偏倚风险评分 |
| G1–G2 | 备注、提取者 |

---

## 四、论文结构框架

```
Abstract（5段：Background/Objective/Methods/Results/Conclusions）
1. Introduction
   1.1 父母教育水平与儿童发展：概述
   1.2 神经发育的关键窗口期（0–8岁）
   1.3 已有综述的不足与本研究目的
2. Methods（直接使用 文档_1_Methods v1.3，已完成）
   2.1 注册与方案
   2.2 纳入/排除标准（PICOS）
   2.3 检索策略
   2.4 研究筛选（三轮流程，109→17篇）
   2.5 数据提取
   2.6 质量评估（NOS）
   2.7 数据综合
3. Results
   3.1 研究概况（PRISMA流程 + 17篇特征表）
   3.2 研究质量（NOS评分分布）
   3.3 rsEEG/ERP证据（#5 #13 #72 #78）
   3.4 fNIRS证据（#7 #79）
   3.5 神经影像证据（sMRI/fMRI/DTI：#9 #15 #19 #20 #23 #28 #43 #64 #75 #104 #109）
   3.6 机制路径分析（认知刺激 vs 慢性应激；中介变量）
4. Discussion
   4.1 跨模态证据整合：父母教育→神经发育的一致性
   4.2 年龄窗口效应（新生儿期/婴儿期/幼儿期/学龄期）
   4.3 机制路径：认知刺激与慢性应激的双路径模型
   4.4 方法学局限与未来方向
   4.5 局限性
5. Conclusion
References（APA 7th）
```

---

## 五、17篇纳入文献速查表

| Row | # | 作者年份 | 模态 | N | 年龄组 | 国家 | 方向 | D3关键统计 |
|-----|---|---------|------|---|--------|------|------|-----------|
| 4 | #5 | Wienke 2024 | ERP | 255 | infant | Germany | negative | F(3,250)=2.7, p=0.049 |
| 5 | #7 | Wijeakumar 2019 | fNIRS | 35 | early-school | India | positive | F(1,33)=5.594, p<0.05 |
| 6 | #9 | Stiver 2015 | sMRI | 26 | toddler | Canada | positive | p=0.006 (2yr) |
| 7 | #13 | Brito 2020 | rsEEG | 179 | infant | USA | positive | β=0.05, p=0.025 |
| 8 | #15 | McKinnon 2023 | sMRI | 261 | neonatal | UK | positive | β=0.09–0.15 (FDR) |
| 9 | #19 | Zhu 2023 | sMRI | 373 | early-school | USA/UK/Norway | positive | p=0.033 (energy distance) |
| 10 | #20 | Konrad 2024 | sMRI | 105 | neonatal | Canada/Germany | positive | p=0.005 (interaction) |
| 11 | #23 | Demir-Lira 2021 | fMRI | 42 | school-age | USA | positive | p<0.05 (SVC) |
| 12 | #28 | Ramphal 2020 | fMRI | 112 | neonatal | USA | positive | CI [-0.81, -0.06] |
| 13 | #43 | Ozernov-Palchik 2019 | DTI | 125 | early-school | USA | positive | r=0.33, p<.001 |
| 14 | #64 | Turesky 2022 | DTI | 38 | infant | USA | positive | r=0.48, p<.05 |
| 15 | #72 | Maguire 2019 | rsEEG | 90 | school-age | USA | positive | β=0.31, p=.02 |
| 16 | #75 | Shephard 2019 | fMRI | 50 | infant | UK | positive | p=0.01 |
| 17 | #78 | Conejero 2018 | ERP | 56 | toddler | Spain | positive | β=.355, F(1,51)=7.10, p<.05 |
| 18 | #79 | Ding 2021 | fNIRS | 86 | toddler | China | positive | SES group F=9.81, p=.02 |
| 19 | #104 | Ursache 2016 | DTI | 107 | early-school | USA | positive | p=.001 |
| 20 | #109 | Lange 2010 | sMRI | 309 | mixed | UK | positive | VIQ +14–15pts, p<.00001 |

---

## 六、Results各节撰写要点

### 3.3 rsEEG/ERP证据（4篇）
- **#13 Brito 2020**：婴儿期rsEEG，高父母教育→更高alpha/beta功率（β=0.05, p=0.025）；注意FDR边界问题（G1已注）
- **#72 Maguire 2019**：学龄儿童rsEEG，母亲教育独立预测词汇量（β=0.31, p=.02），低收入组alpha↓theta↑
- **#5 Wienke 2024**：婴儿ERP，低教育移民家庭→更弱的神经分化（negative方向，注意是唯一负向ERP）
- **#78 Conejero 2018**：幼儿ERP（ERN），父母教育→更强误差监控（β=.355, p<.05）

### 3.4 fNIRS证据（2篇）
- **#7 Wijeakumar 2019**：印度农村低SES vs 美国中高SES，母亲教育独立预测IFG激活（F=5.594, p<.05）
- **#79 Ding 2021**：中国学前儿童，SES分组→右IFG激活差异（F=9.81, p=.02）；HRE中介

### 3.5 神经影像证据（11篇）
按模态分三组：
- **sMRI（5篇）**：#9 #15 #19 #20 #109 — 脑体积/皮质厚度/小脑
- **fMRI（3篇）**：#23 #28 #75 — 任务激活/静息连接
- **DTI（3篇）**：#43 #64 #104 — 白质FA

### 3.6 机制路径
- 认知刺激路径：#7 #43 #64 #72 #79（语言输入/HRE中介）
- 慢性应激路径：#75（母亲焦虑+教育联合效应）
- 直接效应（无中介检验）：其余篇

---

## 七、关键数字（撰写时直接使用）

| 统计项 | 数值 |
|--------|------|
| 总纳入 | 17篇 |
| 检索总量 | 109篇（去重后） |
| 排除（E2，教育无独立效应） | 92篇 |
| 正向关联 | 16篇（94%） |
| 负向/混合 | 1篇（#5，负向） |
| 样本量范围 | N=26–373 |
| 年龄范围 | 出生→15岁（重点0–8岁） |
| 国家数 | 10+（USA/UK/Germany/Canada/Spain/China/India/Norway等） |
| 模态分布 | sMRI×5, fMRI×3, DTI×3, ERP×2, rsEEG×2, fNIRS×2 |

---

## 八、Methods草稿使用说明

`文档_1_Methods检索筛选段落草稿.md`（v1.3）已包含：
- 检索策略（3个数据库检索式）
- 三轮筛选流程（109→17篇，含各轮排除数）
- PICOS标准（方案A：父母教育独立效应p<.05）
- NOS质量评估说明

CC直接复制使用，无需重写。

---

## 九、写作注意事项

1. **#79 Ding 2021**：主暴露是SES分组，教育是SES成分之一，D3b=positive但无独立β值——Results中描述时需说明"SES（以父母教育为主要指标）"
2. **#5 Wienke 2024**：唯一负向结果，需在3.3节单独讨论（移民背景+低教育的交互效应）
3. **#13 Brito 2020**：FDR边界问题，Results中加注"未通过FDR校正，原始p=0.025"
4. **#20 Konrad 2024**：效应是调节效应（interaction），不是主效应——"母亲教育调节海马→认知关联"
5. **年龄分组**：A9字段有neonatal/infant/toddler/early-school/school-age/mixed，Results按年龄窗口组织叙述

---

## 十、请CC完成后告知oo的问题

1. **Table 1特征表**：17篇完整特征，CC生成后请oo核查NOS评分列
2. **PRISMA流程图数字**：109→（第一轮排除X篇）→（第二轮排除X篇）→（第三轮排除92篇）→17篇，请CC从筛选表提取各轮数字
3. **#79 Ding 2021最终裁定**：oo建议排除E2（SES分组研究，教育无独立β），CC确认后更新筛选表和提取表（17→16篇）
4. **草稿整体质量判断**：完成后请CC告知是否需要oo补充任何段落

---

*CC完成初稿后，请push并告知oo，oo负责审阅和补充Discussion关键论点。*
