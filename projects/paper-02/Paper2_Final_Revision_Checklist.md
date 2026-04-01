# Paper 2 终版修改建议（给 CC）

## 📋 修改清单

### 必须修改（Critical）

#### 1. 补充发表偏倚讨论
**位置**：Discussion 4.4 Limitations 部分

**在现有局限性后增加一段**：
```
Publication Bias. All nine included studies reported statistically 
significant ERP changes following training; no null-result studies 
were identified. This apparent unanimity is likely a consequence of 
small samples (which inflate Type I error risk), outcome-selective 
reporting, and the well-documented tendency against publishing 
non-significant findings in specialized pediatric neuroimaging 
literatures. Formal publication bias diagnostics (e.g., funnel plots, 
Egger's test) were not feasible given the small number of studies 
and the inability to pool effect sizes across heterogeneous ERP 
paradigms. Readers should therefore interpret the apparent consistency 
of findings with appropriate caution; independent replication with 
larger, pre-registered samples is essential before drawing firm 
conclusions about the reliability and generalizability of 
training-induced ERP effects.
```

---

#### 2. 增强批判性讨论
**位置**：Discussion 4.5 Directions for Future Research 之前

**增加一个新小节 4.5 Critical Appraisal**：
```
4.5 Critical Appraisal

The small sample sizes (median n = 15 per DD group) and absence of 
pre-registration in 8/9 studies raise concerns about replicability. 
The field would benefit from:

(1) Multi-site consortia to achieve adequate statistical power 
(minimum n = 30 per group for detecting medium effects);

(2) Open data sharing to enable independent verification and 
secondary analyses;

(3) Standardized ERP paradigms and analysis pipelines to reduce 
methodological heterogeneity;

(4) Pre-registration of analysis plans to minimize researcher 
degrees of freedom.

Without these improvements, the current evidence base—while 
suggestive—remains preliminary.
```

**然后将原来的 4.5 改为 4.6**

---

#### 3. 统一效应量报告
**位置**：Table 3 最后一列

**修改列标题**：
- 当前：`ES (reported)`
- 改为：`ES (type)`

**在 Table 3 的 Note 中增加**：
```
Effect size types: d = Cohen's d (pooled SD); ηp² = partial eta-squared; 
d₂ = within-subject d (Morris & DeShon, 2002). N/A = insufficient data 
for calculation. Effect sizes across studies should be interpreted with 
awareness of the formula used.
```

---

### 建议修改（Recommended）

#### 4. 增加 Figure 2：效应方向汇总图
**位置**：Results 3.4 之后

**创建一个简单的 Forest plot 风格图表**（即使不能做 Meta）：

```
Figure 2. Direction of ERP Changes Following Phonological Training

[创建一个表格式图表，显示：]

Study          | Component | Direction | Magnitude
---------------|-----------|-----------|----------
Mayhew 2013    | N170      | ↓         | Medium (d=0.54)
Spironelli 2010| N150      | ← (left)  | Large
Jucla 2010     | N170      | ↓ latency | Medium
Basma 2026     | N400      | ↑         | Large (ηp²=0.71)
Hasko 2014     | N400      | ↑         | Medium (d=0.54)
Lovio 2012     | MMN       | ↑         | Large (d=1.18)
Ferraz 2018    | P300      | ↓ latency | Large (d=1.43)
Zygouris 2018  | P300      | ↓ latency | Very Large
Santos 2007    | P300      | ↑         | Medium

Note. ↑ = amplitude increase; ↓ = amplitude/latency decrease; 
← = leftward lateralization shift.
```

---

#### 5. 增加 Figure 3：ERP 成分示意图
**位置**：Introduction 1.3 之后

**创建一个简单的时间线图**：
```
Figure 3. Timeline of ERP Components in Reading-Related Processing

[创建一个时间轴图，显示：]

0ms -------- 150ms -------- 300ms -------- 400ms -------- 600ms
     |              |              |              |              |
   MMN          N170/N150      N300/N400         P300
(Pre-attentive) (Orthographic) (Phonological-  (Cognitive
                               Semantic)        Updating)

Note. Approximate peak latencies for each component. MMN = mismatch 
negativity; N170/N150 = visual word form processing; N300/N400 = 
phonological-semantic integration; P300 = cognitive updating.
```

---

### 可选修改（Optional）

#### 6. 补充材料准备
**创建 Supplementary Material 文档**，包含：

**S1. 完整检索式**（6 个数据库）
- PubMed 完整检索式
- Web of Science 完整检索式
- PsycINFO 完整检索式
- ERIC 完整检索式
- Scopus 完整检索式
- ProQuest 完整检索式

**S2. PRISMA 2020 检查表**（27 项）

**S3. 排除研究列表**
- 全文筛选阶段排除的研究
- 排除原因（FE1-FE5）

**S4. 数据提取表模板**（65 字段）

---

#### 7. 预注册声明
**位置**：Methods 2.1 最后

**增加一句**：
```
This review was not pre-registered. However, the search strategy 
and eligibility criteria were defined a priori before database 
searches were conducted.
```

---

## 📊 修改优先级

| 优先级 | 修改项 | 预计时间 |
|--------|--------|----------|
| **P0** | 1. 发表偏倚讨论 | 10 分钟 |
| **P0** | 2. 批判性讨论 | 15 分钟 |
| **P0** | 3. 效应量统一 | 5 分钟 |
| **P1** | 4. Figure 2 | 20 分钟 |
| **P1** | 5. Figure 3 | 15 分钟 |
| **P2** | 6. 补充材料 | 30 分钟 |
| **P2** | 7. 预注册声明 | 2 分钟 |

---

## ✅ 修改后检查清单

完成修改后，请确认：
- [ ] Discussion 包含发表偏倚段落
- [ ] Discussion 包含批判性评价小节
- [ ] Table 3 效应量列标题和 Note 已更新
- [ ] Figure 2 已创建（可选）
- [ ] Figure 3 已创建（可选）
- [ ] 补充材料已准备（可选）
- [ ] 预注册声明已添加（可选）

---

## 🎯 修改完成后

**立即可投稿**，无需等待其他修改。

**目标期刊**：Annals of Dyslexia (IF ~2.5, Q2)

**预期审稿周期**：2-3 个月

---

**修改人**：Claude Code
**审查人**：OpenClaw Research
**日期**：2026-04-02
