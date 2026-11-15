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
| domain | str | near / far / followup / trained |
| measure | str | 结局测验名 |
| effect_size_available | bool | 能否提取 mean/SD/change/t |
| effect_size_value | float | 若已提取则填 |

### 5. 审计层（audit 列，附在 comparison 表）
| 字段 | 类型 | 说明 |
|---|---|---|
| cc_code | str | cc 第一编码类型 |
| cl_code | str | cl 第二编码类型 |
| cx_final | str | cx 仲裁后类型 |
| exclusion_status | str | included / excluded / duplicate / nested |
| exclusion_reason | str | 排除/去重理由 |

## 三、v3 → 新表 导入规则（固定）

1. **56→51**：Seq16/43/47/53 标 `duplicate`，Seq28 标 `nested`（保留 Seq52 为主）；主报告取 Seq4/12/19/31/49/13/52 等，次要报告挂到 `secondary_report_seq`。
2. **Seq10 拆两条**：C10A = stDCS+WMT vs double-sham（②，in_core_ma=True）；C10B = atDCS+WMT vs stDCS+WMT（③，in_core_ma=False）。
3. **Seq24 排除**：`exclusion_status=excluded`，reason="干预目标非WM（注意训练）"，不进任何比较层。
4. **Seq1/35**：`comp_type=N`，保留在证据流（trial+arm 有记录），但不生成 comparison、不进 WM 组间效应量。
5. **Seq51/62**：`comp_type=S`，生成 comparison 但 `in_core_ma=False`。

## 四、一致性检查断言（脚本自动跑）

- [ ] 独立 trial_id 数 = 51
- [ ] Seq10 恰好 2 条 comparison
- [ ] Seq24 无 comparison、exclusion_status=excluded
- [ ] Seq1/35 comp_type=N、无 comparison
- [ ] 5 重复（16/43/47/53/28）正确映射到主报告
- [ ] 核心元分析池（in_core_ma=True）计数 ≈35

## 五、分工

- **cx**：冻结本 schema + 审计脚本 diff + 抽查新表 + 裁决新增歧义。
- **cc**：改脚本（只抽臂结构）、生成新表、导入 v3、跑一致性检查、提交 git。
- **cl**：只处理新增臂结构/比较疑难，不重审 51 个已定条目。
