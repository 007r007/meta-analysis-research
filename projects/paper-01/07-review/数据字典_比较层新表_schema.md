# Paper-01 比较层新表 Schema（冻结版 v1）

> 冻结：cx 2026-11-15 裁定；cc 执行落地。本表是比较层 SSOT，旧 `数据_6_数据提取表_v3_research.xlsx` 作历史档不再修补。

## 一、粒度

```
trial_id → arm_id → comparison_id → outcome_id → timepoint
```

一个试验多条臂，一对臂可生成一条或多条比较，一条比较对应多个结局、多个时间点。

## 二、字段字典

### 1. 试验层（trial 表）
| 字段 | 类型 | 说明 |
|---|---|---|
| trial_id | str | 去重后试验编号（T01…T51） |
| main_report_seq | int | 主报告 Seq |
| secondary_report_seq | str | 次要报告 Seq（逗号分隔，无则空） |
| author_year | str | 最终作者+年份（经 v3 修正） |
| design | str | RCT/quasi-RCT/crossover/single-group |
| country | str | 修正后国家 |
| note | str | 去重/合并关系说明 |

### 2. 臂层（arm 表）
| 字段 | 类型 | 说明 |
|---|---|---|
| arm_id | str | A{trial_id}_{序号} |
| trial_id | str | 所属试验 |
| arm_label | str | 臂名（如 "WM训练组"/"主动对照"/"sham-tDCS"） |
| intervention_components | str | 该臂实际接受的干预（从 Methods 提取，非关键词） |
| control_components | str | 该臂的对照要素（空白对照/问卷/教育视频/运动等） |
| n | int | 该臂样本量（NULL 表缺失） |

### 3. 比较层（comparison 表）
| 字段 | 类型 | 说明 |
|---|---|---|
| comparison_id | str | C{trial_id}_{序号} |
| trial_id | str | 所属试验 |
| arm_a / arm_b | str | 比较两臂 arm_id |
| comp_type | str | ①/②/③/④/S/N（最终裁决） |
| est_target | str | 该比较估计什么（WM效应/WM增量/刺激增益/组合/变体/无） |
| in_core_ma | bool | 是否进核心元分析（①+②为 True） |

### 4. 结局层（outcome 表）
| 字段 | 类型 | 说明 |
|---|---|---|
| outcome_id | str | O{comparison_id}_{序号} |
| comparison_id | str | 所属比较 |
| domain | str | near / far / trained（followup 迁入时间维度，随访可同时是 near 或 far） |
| measure | str | 结局测验名 |
| timepoint | str | 时间点（post / followup 等） |
| result_ids | str | 指向效应量库 `结果_1_效应量提取库.json` 的 resultId（JSON 数组文本）；JSON 库为核查状态与统计数值的唯一权威源 |
| effect_size_available | bool | **只读自动生成**：available→true、unavailable→false、pending→空；不再手工编辑 |

### 5. 审计层（audit 列，附在 comparison 表）
| 字段 | 类型 | 说明 |
|---|---|---|
| cc_code | str | cc 第一编码类型 |
| cl_code | str | cl 第二编码类型 |
| cx_final | str | cx 仲裁后类型 |
| exclusion_status | str | included / excluded / duplicate / nested |
| exclusion_reason | str | 排除/去重理由 |

## 三、v3 → 新表 导入规则（固定）

1. **56→51 主报告**：Seq16/43/47/53 标 `duplicate`，Seq28 标 `nested`（保留 Seq52 为主）；主报告取 Seq4/12/19/31/49/13/52 等，次要报告挂到 `secondary_report_seq`。
2. **Seq10 拆两条**：C10A = stDCS+WMT vs double-sham（②，in_core_ma=True）；C10B = atDCS+WMT vs stDCS+WMT（③，in_core_ma=False）。
3. **Seq24 排除**：`exclusion_status=excluded`，reason="干预目标非WM（注意训练）"，不进任何比较层。
4. **Seq1/35**：`comp_type=N`，保留在证据流（trial+arm 有记录），但不生成 comparison、不进 WM 组间效应量。
5. **Seq51/62**：`comp_type=S`，生成 comparison 但 `in_core_ma=False`。
6. **Seq53 双挂 + 拆不在册样本**（cx 裁定 2026-11-16）：Seq53 双挂 Seq19+Seq31；其 2 个不在册样本（Borella 2010 N=40、Borella 2017∧ N=36）拆为独立 trial 记录（T54/T55），`comp_type=①-pending`（未独立收录，尚未完成独立报告提取）、不生成核心比较、来源链接 Seq53。
7. **一篇多试验拆分**（cx 裁定 2026-11-16）：trial 边界统一为「按独立招募/分组/参与者样本识别，不按论文数量或训练方案」；Seq6(Brum 2020) 拆 Study1(N=46)/Study2(N=50)、Seq61(Cantarella 2017校样) 拆 Exp1(18/17)/Exp2(16/19)，各建一个 trial。**登记记录数 51→55**。
8. **年轻样本人群资格**（cx 裁定 2026-11-16）：识别试验结构与应用综述资格分两步——独立样本/独立实施可分别登记（决定是否拆）；但只有符合老年人 PICOS 的样本进入综述（决定是否计入）。Seq3/5/18/29 含年轻组，**不增加本综述 trial 或候选比较**，年轻部分在来源说明标记「人群不符合纳入标准」。

## 四、一致性检查断言（脚本自动跑）

- [ ] 登记 trial 记录数 = 57（53 主报告[Seq6/61拆2] + 4 不在册/恢复[Borella2010①/Borella2017∧①-pending/WOME①-pending/Zając2016①×2]）
- [ ] Seq10 恰好 2 条 comparison
- [ ] Seq24 无 comparison、exclusion_status=excluded
- [ ] Seq1/35 comp_type=N、无 comparison
- [ ] 5 重复（16/43/47/53/28）正确映射到主报告（43 双挂 4+12、53 双挂 19+31）
- [ ] Seq6 拆 2 子研究（Study1/Study2）、Seq61 拆 2 子研究（Exp1/Exp2），各 1 条 ①
- [ ] 2 不在册样本（Borella 2010/Borella 2017∧）已拆为独立 trial，comp_type=①-pending，链接 Seq53
- [ ] 核心候选比较池（in_core_ma=True）计数 = 43（①41[含Borella2010恢复+Zając2016双①] + ②2；候选数非最终可算效应量数，Borella 2017∧/WOME 编码后→45）

## 五、分工

- **cx**：冻结本 schema + 审计脚本 diff + 抽查新表 + 裁决新增歧义。
- **cc**：改脚本（只抽臂结构）、生成新表、导入 v3、跑一致性检查、提交 git。
- **cl**：只处理新增臂结构/比较疑难，不重审 51 个已定条目。
