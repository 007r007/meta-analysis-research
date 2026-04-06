# Paper-02 规划文档

**创建时间**：2026-04-05  
**状态**：规划完成，待执行检索

---

## 一、选题信息

### 标题
**英文**：Parental education level and early childhood neural development: a systematic review of EEG, ERP, fNIRS, and neuroimaging evidence (ages 0–8 years)

### 论文类型
叙述性系统综述（Narrative Systematic Review，PRISMA 2020）  
**不做 Meta 分析**，原因：结局指标高度异质（rsEEG频段/ERP成分/MRI结构指标无法合并）

### 目标期刊
- **首投**：Developmental Cognitive Neuroscience（Q1，IF ≈ 4.5）
- **备投**：Developmental Review / Neuroscience & Biobehavioral Reviews

### 投中概率评估
- 概率：55–65%（执行质量高时）
- 最大风险：SES 复合指标操作化问题（父母教育水平常与收入/职业捆绑报告）
- 应对方案：Methods 里设计 SES 编码方案，区分"单独报告"vs"复合SES分项"

### 建议：导师作通讯作者（提升接受率）

---

## 二、选题原因

1. **聚焦父母教育而非复合SES**：父母教育是SES中测量最稳定、最可操作的单一指标，便于跨研究比较
2. **0-8岁神经可塑性窗口**：该年龄段是神经发育关键期，环境影响可留下持久痕迹
3. **多模态整合的必要性**：rsEEG、ERP、MRI 三类证据各有侧重，系统整合尚缺
4. **研究空白明确**：中国样本研究几乎缺失；机制路径（认知刺激/语言环境/应激）证据分散

### 4个核心研究问题
1. 父母教育水平如何影响儿童静息态EEG（功率/连接）？
2. 父母教育水平如何影响任务态ERP成分（P300/N200/N400等）？
3. 父母教育水平如何影响脑结构/功能神经影像指标？
4. 哪些机制路径（认知刺激、语言输入、应激暴露）在其中起中介作用？

---

## 三、检索策略

> **修订说明（2026-04-07，oo+cc联合审查）**：在原版基础上做了5项修改：
> 1. 概念A：补充 `educational attainment` / `years of education` / `educational level` / `parental schooling`
> 2. 概念B：删除过宽的 `cortical` / `neural`；加入 `fNIRS` / `near-infrared spectroscopy` / `NIRS` / `MEG` / `magnetoencephalograph*` / `visual evoked potential*` / `diffusion tensor`；裸 `MRI` → `structural MRI`（避免骨科/心脏MRI噪音）
> 3. 概念C：补充 `newborn*` / `neonatal` / `neonate*` / `perinatal`；删除过宽的 `child*` / `infancy` / `grade school*`
> 4. PubMed实测命中：**230条**（oo最终版）
> 5. 标题同步更新：加入 fNIRS

### 概念框架（3个概念组）

**概念A：父母教育/社会经济地位**
```
"parental education" OR "maternal education" OR "paternal education" OR
"educational attainment" OR "years of education" OR "educational level" OR
"parental schooling" OR "socioeconomic status" OR "family income" OR
"poverty" OR "income-to-needs" OR "low-income" OR
"household wealth" OR "neighborhood disadvantage"
```

**概念B：神经发育指标**
```
"EEG" OR "electroencephalograph*" OR "ERP" OR "event-related potential*" OR
"fMRI" OR "structural MRI" OR "neuroimaging" OR "brain imaging" OR
"rsEEG" OR "spectral power" OR "DTI" OR "diffusion tensor" OR
"functional connectivity" OR
"fNIRS" OR "near-infrared spectroscopy" OR "NIRS" OR
"MEG" OR "magnetoencephalograph*" OR "visual evoked potential*"
```

**概念C：儿童早期年龄段（0–8岁）**
```
"infant*" OR "toddler*" OR "preschool*" OR "kindergarten" OR
"early childhood" OR "school-aged child*" OR "early brain development" OR
"newborn*" OR "neonatal" OR "neonate*" OR "perinatal"
```

### 各数据库检索式

**PubMed**（[tiab] + MeSH 双轨，实测命中 **230条**）
```
(
  (
    "parental education"[tiab] OR "maternal education"[tiab] OR "paternal education"[tiab]
    OR "educational attainment"[tiab] OR "years of education"[tiab] OR "educational level"[tiab]
    OR "parental schooling"[tiab] OR "socioeconomic status"[tiab] OR "family income"[tiab]
    OR "poverty"[tiab] OR "income-to-needs"[tiab] OR "low-income"[tiab]
    OR "household wealth"[tiab] OR "neighborhood disadvantage"[tiab]
  )
  AND
  (
    "EEG"[tiab] OR "electroencephalograph*"[tiab]
    OR "ERP"[tiab] OR "event-related potential*"[tiab]
    OR "fMRI"[tiab] OR "structural MRI"[tiab] OR "neuroimaging"[tiab] OR "brain imaging"[tiab]
    OR "rsEEG"[tiab] OR "spectral power"[tiab]
    OR "DTI"[tiab] OR "diffusion tensor"[tiab] OR "functional connectivity"[tiab]
    OR "fNIRS"[tiab] OR "near-infrared spectroscopy"[tiab] OR "NIRS"[tiab]
    OR "MEG"[tiab] OR "magnetoencephalograph*"[tiab]
    OR "visual evoked potential*"[tiab]
  )
  AND
  (
    "infant*"[tiab] OR "toddler*"[tiab] OR "preschool*"[tiab] OR "kindergarten"[tiab]
    OR "early childhood"[tiab] OR "school-aged child*"[tiab] OR "early brain development"[tiab]
    OR "newborn*"[tiab] OR "neonatal"[tiab] OR "neonate*"[tiab] OR "perinatal"[tiab]
  )
)
OR (
  "Social Class"[MeSH] AND "Electroencephalography"[MeSH] AND "Child Development"[MeSH]
)
```

**PsycINFO**（AB字段）
```
AB("parental education" OR "maternal education" OR "paternal education" OR "educational attainment" OR "years of education" OR "educational level" OR "parental schooling" OR "socioeconomic status" OR "family income" OR "poverty" OR "income-to-needs" OR "low-income" OR "household wealth" OR "neighborhood disadvantage") AND AB("EEG" OR "electroencephalograph*" OR "ERP" OR "event-related potential*" OR "fMRI" OR "structural MRI" OR "neuroimaging" OR "brain imaging" OR "rsEEG" OR "spectral power" OR "DTI" OR "diffusion tensor" OR "functional connectivity" OR "fNIRS" OR "near-infrared spectroscopy" OR "NIRS" OR "MEG" OR "magnetoencephalograph*" OR "visual evoked potential*") AND AB("infant*" OR "toddler*" OR "preschool*" OR "kindergarten" OR "early childhood" OR "school-aged child*" OR "early brain development" OR "newborn*" OR "neonatal" OR "neonate*" OR "perinatal")
```

**Web of Science**（TS字段）
```
TS=("parental education" OR "maternal education" OR "paternal education" OR "educational attainment" OR "years of education" OR "educational level" OR "parental schooling" OR "socioeconomic status" OR "family income" OR "poverty" OR "income-to-needs" OR "low-income" OR "household wealth" OR "neighborhood disadvantage") AND TS=("EEG" OR "electroencephalograph*" OR "ERP" OR "event-related potential*" OR "fMRI" OR "structural MRI" OR "neuroimaging" OR "brain imaging" OR "rsEEG" OR "spectral power" OR "DTI" OR "diffusion tensor" OR "functional connectivity" OR "fNIRS" OR "near-infrared spectroscopy" OR "NIRS" OR "MEG" OR "magnetoencephalograph*" OR "visual evoked potential*") AND TS=("infant*" OR "toddler*" OR "preschool*" OR "kindergarten" OR "early childhood" OR "school-aged child*" OR "early brain development" OR "newborn*" OR "neonatal" OR "neonate*" OR "perinatal")
```

**Scopus**（TITLE-ABS-KEY字段）
```
TITLE-ABS-KEY("parental education" OR "maternal education" OR "paternal education" OR "educational attainment" OR "years of education" OR "educational level" OR "parental schooling" OR "socioeconomic status" OR "family income" OR "poverty" OR "income-to-needs" OR "low-income" OR "household wealth" OR "neighborhood disadvantage") AND TITLE-ABS-KEY("EEG" OR "electroencephalograph*" OR "ERP" OR "event-related potential*" OR "fMRI" OR "structural MRI" OR "neuroimaging" OR "brain imaging" OR "rsEEG" OR "spectral power" OR "DTI" OR "diffusion tensor" OR "functional connectivity" OR "fNIRS" OR "near-infrared spectroscopy" OR "NIRS" OR "MEG" OR "magnetoencephalograph*" OR "visual evoked potential*") AND TITLE-ABS-KEY("infant*" OR "toddler*" OR "preschool*" OR "kindergarten" OR "early childhood" OR "school-aged child*" OR "early brain development" OR "newborn*" OR "neonatal" OR "neonate*" OR "perinatal")
```

### 预估规模
- PubMed实测：230条（修订版，2026-04-07）
- 四库去重后预估总命中：800–1500 条（修订后比原估低，精度更高）
- 经筛选后目标纳入：35–50 篇

---

## 四、纳排标准（PICOS）

| 维度 | 纳入 | 排除 |
|------|------|------|
| P（人群） | 0–8岁儿童 | >8岁；非人类 |
| I（暴露） | 父母教育水平（可作为复合SES分项报告） | 仅报告收入/职业，无教育数据 |
| C（对照） | 高vs低教育水平比较（可连续变量） | 无 |
| O（结局） | EEG/ERP/fNIRS/fMRI/MRI/DTI任一神经指标 | 纯行为/认知测验 |
| S（研究设计） | 观察性研究（横断/纵向）、RCT | 综述/元分析/案例报告 |

---

## 五、写作框架

### 1. Introduction（~1200词）
- 为何聚焦父母教育而非复合SES
- 0–8岁神经可塑性窗口的重要性
- 多模态神经影像整合的必要性
- 4个研究问题

### 2. Methods（~1500词，PRISMA 2020）
- PROSPERO注册（**必须在开始检索前完成**）
- PICOS框架（见上）
- 4库检索策略（2000年至今，英文）
- 双人筛选 + Cohen's Kappa
- NOS（Newcastle-Ottawa Scale）偏倚风险评估
- 叙述性综合方法说明

### 3. Results（~3500词）
- **3.1** 检索结果与PRISMA流程
- **3.2** 纳入研究特征概览（Table 1）
- **3.3** 静息态EEG证据（预计8–12篇）
  - α/θ/δ功率、连接性、不对称性
- **3.4** 任务态ERP证据（预计10–15篇）
  - P300、N200、N400、MMN等成分
- **3.5** 结构/功能神经影像证据（预计10–15篇）
  - 皮层厚度、白质完整性、功能连接
- **3.6** 机制路径证据
  - 认知刺激路径、语言输入路径、慢性应激路径

### 4. Discussion（~2500词）
- 四大研究空白：方法学/语言/发展阶段/机制
- 中国研究的特别讨论（作为综述→大论文的桥梁）
- 局限性（横断研究为主、SES测量异质性）
- 结论与实践意义

---

## 六、数据提取表字段设计（约25–30列）

| 类别 | 字段（列）|
|------|-----------|
| **基本信息**（8列） | 序号、第一作者、年份、国家、研究设计、样本量、儿童年龄（均值/范围）、追踪时间点数 |
| **SES测量**（4列）← 最关键 | 父母教育测量方式、是否单独报告教育（是/否）、教育编码（年数/等级）、其他SES指标 |
| **神经测量**（6列） | 测量模态（EEG/ERP/fMRI等）、具体指标、任务类型（静息/任务态/结构）、设备/通道数、频段或成分、分析方法 |
| **结局**（4列） | 父母教育与神经指标是否显著相关（是/否/混合）、效应方向、效应量（如报告）、调节/中介变量 |
| **NOS质量**（3列） | 选择性偏倚评分、可比性评分、结局评分（总分/9分） |

---

## 七、待办清单

- [ ] **PROSPERO注册**（检索前必须完成）
- [ ] 用户在4个数据库手动检索，导出RIS文件
- [ ] CC合并去重4个RIS文件，生成筛选Excel
- [ ] 双人筛选（用户+CC辅助）
- [ ] CC生成数据提取表Excel（参考上方字段设计）
- [ ] 开始撰写Introduction框架

---

## 八、关联文件

- 本文档：`papers/projects/paper-02/00-planning/paper02_planning.md`
- 数据提取表（待创建）：`papers/projects/paper-02/04-extract/数据提取表_paper02.xlsx`
- 筛选表（待创建）：`papers/projects/paper-02/03-screen/筛选表_paper02.xlsx`
