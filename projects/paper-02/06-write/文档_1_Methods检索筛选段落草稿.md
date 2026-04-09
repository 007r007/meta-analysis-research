# Methods §2.3–2.4 检索与筛选段落草稿

**版本**：v1.0（2026-04-09）
**说明**：基于实际执行数据撰写，供正式写作阶段参考。数字待oo核查76篇后最终确认。

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

**Stage 3 (Full-text eligibility):** Full-text PDFs were obtained for 109 of the 133 records (82%); 24 records were excluded prior to full-text review on the basis of abstract information (22 records), confirmed retraction (1 record), or inability to locate the full text after reasonable effort (1 record). Two reviewers independently assessed all 109 full texts against the eligibility criteria. Disagreements were resolved by consensus discussion. This process yielded **76 studies** meeting all inclusion criteria; 33 were excluded at full-text stage. Primary reasons for full-text exclusion were: parental education not independently estimable (E2, *k* = 23); duplicate records of an included study or preprint superseded by a published version (E7, *k* = 5); non-empirical publication type (E4, *k* = 2); sample age not within 0–8 years (E1, *k* = 1); no neural outcome reported (E3, *k* = 1); and full text inaccessible (E6, *k* = 1). A PRISMA 2020 flow diagram is presented in Figure 1.

---

## 数字核查备忘

| 节点 | 数字 | 来源文件 |
|------|------|---------|
| 四库原始命中 | 3,097（521+296+1011+1269） | 结果_1_检索统计数据.json |
| 去重后 | 1,827 | 脚本_1合并去重输出 |
| Stage 1保留 | 513 | 数据_2_第一轮自动筛选结果.xlsx |
| Stage 2保留 | 133 | 数据_3_全文筛选待下载列表.xlsx |
| 全文筛选输入 | 109 | 数据_5_第三轮全文筛选.xlsx |
| 最终纳入 | 76（待oo核查确认） | 数据_5_第三轮全文筛选.xlsx |
| Stage 3排除明细 | E2×23/E7×5/E4×2/E1×1/E3×1/E6×1 | 数据_5_第三轮全文筛选.xlsx |
