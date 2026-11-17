# 效应量 10 条定标：cc vs cl 对照（分歧记录）

> 2026-11-17。cc 初版 + cl 独立判定。两者总数一致（available 8 / pending 1 / unavailable 1），但归属有 2 处实质分歧。

## 一致（8 条）
Seq57 unavailable、Seq6/Seq41/Seq48/Seq25 available、Seq61 available、Seq3 available(有条件)、Seq11 available —— 双方一致。

## 分歧（3 处，cl 更严谨）

| 比较 | cc | cl | 判断 |
|---|---|---|---|
| **Seq9 Guye** | pending（只看到 Bayesian BF） | **available**（查到 Table 5 的 21 任务 M/SD 兜底） | **cl 对**——我漏看了 Table 5 |
| **Seq22 Boutzoukas** | available（复杂） | **pending**（无组别 M/SD 表，仅 Fig 均值图；η²p 无 F/df2） | **cl 对**——我"available"判得太松 |
| **Seq3 Salminen** | available | available（有条件：老年层部分结局 pending） | cl 更细，采纳 |

## 结论
- cl 这轮明显更严谨：**先查表再查正文**的纪律抓到了我两处漏判（Seq9 漏 Table、Seq22 判松）。
- 判定手册以 **cl 的 8 条 + 8 个开放点**为基础，分歧交 cx 冻结后铺开全量 40 条。

## cl 的 8 个开放点（待 cx 冻结手册时一并裁决）
1. Bayesian-only 判 pending 还是 unavailable
2. SEM 一律 unavailable；跨文献借数边界
3. η²p 无 F/df 时 df2 重建的公式规则
4. 补充材料是否算报告来源（算，标 sourceSection=supplement）
5. 交叉/反平衡设计口径
6. p+df 反算、t→d_change 的换算公式
7. 混合年龄 pooled F 能否用于老年层
8. proximal(训练任务)结局是否进迁移综合
