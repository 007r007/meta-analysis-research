# Methods §2.3–2.4 检索与筛选段落草稿

**版本**：v1.1（2026-04-09，oo系统排查后更新）
**说明**：基于实际执行数据撰写，供正式写作阶段参考。数字已经oo逐篇核查确认（76→67篇）。

---

### 2.3 Search Strategy

We conducted systematic searches in four electronic databases: PubMed/MEDLINE, PsycINFO (via EBSCOhost), Web of Science Core Collection, and Scopus. Searches were conducted in April 2026. No publication date restriction was applied. The Cochrane Library was not searched because this review focuses on observational studies, which are not systematically indexed in Cochrane.

The search strategy combined three concept blocks: (1) parental education or socioeconomic status, (2) young children aged 0–8 years, and (3) neural or neuroimaging measures. The PubMed search string integrated title/abstract [tiab] fields with MeSH terms, and was iteratively refined against a set of eight benchmark studies with known eligibility status prior to finalisation. The core PubMed search string was:

> ("parental education"[tiab] OR "maternal education"[tiab] OR "paternal education"[tiab] OR "educational attainment"[tiab] OR "socioeconomic status"[tiab] OR "socioeconomic background"[tiab] OR "family income"[tiab] OR "household income"[tiab] OR "child poverty"[tiab] OR "social disadvantage"[tiab]) AND ("infant*"[tiab] OR "newborn*"[tiab] OR "neonatal"[tiab] OR "toddler*"[tiab] OR "preschool*"[tiab] OR "pre-school*"[tiab] OR "young children"[tiab] OR "early childhood"[tiab] OR "kindergarten"[tiab] OR Child[MeSH] OR "Child, Preschool"[MeSH] OR Infant[MeSH]) AND ("EEG"[tiab] OR "electroencephalograph*"[tiab] OR "electrophysiolog*"[tiab] OR "event-related potential*"[tiab] OR "ERP"[tiab] OR "MMN"[tiab] OR "N400"[tiab] OR "P300"[tiab] OR "alpha power"[tiab] OR "theta power"[tiab] OR "resting-state"[tiab] OR "fNIRS"[tiab] OR "fMRI"[tiab] OR "functional MRI"[tiab] OR "functional magnetic resonance"[tiab] OR "DTI"[tiab] OR "diffusion tensor"[tiab] OR "structural MRI"[tiab] OR "cortical thickness"[tiab] OR "gray matter"[tiab] OR "white matter"[tiab] OR "VBM"[tiab] OR "brain function"[tiab] OR "brain activity"[tiab] OR "brain development"[tiab] OR "neural"[tiab] OR "neuroimaging"[tiab])

Search strings for PsycINFO, Web of Science, and Scopus were adapted to each database's controlled vocabulary and field codes. Full database-specific search strings are provided in Supplementary Materials.

---

### 2.4 Study Selection

Search results from all four databases were combined and deduplicated. Deduplication prioritised exact DOI matching; records without a DOI were matched on title and publication year (first 120 characters of title). This process yielded a deduplicated pool of 1,827 records from 3,097 initial hits (PubMed = 521, PsycINFO = 296, Web of Science = 1,011, Scopus = 1,269).

Title and abstract screening proceeded in two stages:

**Stage 1 (Automated pre-screening):** A keyword-based algorithm retained records containing terms from all three concept blocks—parental education/SES, child age (0–8 years), and a neural measurement indicator. Records were excluded if they lacked a term from any single block. Neural indicators were applied in two tiers: records containing modality-specific terms (e.g., EEG, fMRI, cortical thickness) were automatically retained; records matching only broad neuroscientific terms (e.g., *brain development*, *brain function*) without a modality-specific term were excluded at this stage, as these terms alone could not confirm the presence of a neural measurement. Stage 1 excluded 1,314 records, retaining 513 for Stage 2.

**Stage 2 (Title/abstract review):** Two reviewers independently screened all 513 records against the full PICOS eligibility criteria. Disagreements were resolved by discussion and consensus. Stage 2 excluded 380 records, retaining 133 for full-text retrieval.

**Stage 3 (Full-text eligibility):** Full-text PDFs were obtained for 109 of the 133 records (82%); 24 records were excluded prior to full-text review on the basis of abstract information (22 records), confirmed retraction (1 record), or inability to locate the full text after reasonable effort (1 record). Two reviewers independently assessed all 109 full texts against the eligibility criteria. Full-text review included systematic verification that parental education had an independently estimable effect (i.e., reported as a separate regression coefficient or as the primary exposure variable); studies in which education was subsumed within a composite SES factor or served only as a covariate without a reported beta coefficient were excluded (E2). Disagreements were resolved by consensus discussion. This process yielded **67 studies** meeting all inclusion criteria; 42 were excluded at full-text stage. Primary reasons for full-text exclusion were: parental education not independently estimable (E2, *k* = 31); duplicate records of an included study or preprint superseded by a published version (E7, *k* = 5); non-empirical publication type (E4, *k* = 2); sample age not within 0–8 years (E1, *k* = 1); no neural outcome reported (E3, *k* = 1); and full text inaccessible (E6, *k* = 1). A PRISMA 2020 flow diagram is presented in Figure 1.

---

## 数字核查备忘

| 节点 | 数字 | 来源文件 |
|------|------|---------|
| 四库原始命中 | 3,097（521+296+1011+1269） | 结果_1_检索统计数据.json |
| 去重后 | 1,827 | 脚本_1合并去重输出 |
| Stage 1保留 | 513 | 数据_2_第一轮自动筛选结果.xlsx |
| Stage 2保留 | 133 | 数据_3_全文筛选待下载列表.xlsx |
| 全文筛选输入 | 109 | 数据_5_第三轮全文筛选.xlsx |
| 最终纳入 | 67（oo逐篇核查确认） | 数据_5_第三轮全文筛选.xlsx |
| Stage 3排除明细 | E2×31/E7×5/E4×2/E1×1/E3×1/E6×1 | 数据_5_第三轮全文筛选.xlsx |

---

## 系统排查备注（2026-04-09，oo执行）

**背景**：数据提取阶段发现#2 Myers 2014误纳入（主暴露为白质发育非父母教育），触发对全部纳入文献的系统E2核查。

**8篇追加排除（全部E2）**：

| 原序号 | 文献 | 排除原因 |
|--------|------|---------|
| #2 | Myers 2014 | 主暴露白质发育预测阅读能力，教育非主暴露 |
| #16 | Troller-Renfree 2022 | 主暴露现金转移干预(RCT) |
| #33 | Di Lonardo Burr 2024 | 主暴露LI vs MI收入分组，教育仅做组间描述 |
| #37 | Pellowski 2023 | 主暴露产前抑郁，母亲教育仅作协变量控制 |
| #58 | Xie 2019 | 主暴露生长迟缓(HAZ) |
| #61 | Triplett 2022 | 主暴露产前逆境综合评分 |
| #73 | Gonzalez 2020 | 父母教育为"parental ecology"复合因子之一，无独立beta |
| #77 | Luby 2013 | 主暴露income-to-needs |
| #102 | Sandre 2024 | 标题明确"not parental education" |

**注**：上表共9篇，其中包含commit 0b37e98已处理的Myers 2014，最终净新增8篇。

**漏网原因**：第三轮全文筛选时，这些文章标题/摘要提到了SES或父母教育，但未深入读Methods/Results确认教育是否有独立效应量。叙述性综述的PICOS在此边界比Meta分析更严格。

**筛选漏斗更新**：109篇全文 → 排除42篇 → **最终纳入67篇**
