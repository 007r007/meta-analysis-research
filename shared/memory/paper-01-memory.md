# Paper 1 记忆

## 基本信息
- 标题：老年人工作记忆训练迁移效应的调节因素：系统综述
- 英文标题：Individual and Training-Related Moderators of Transfer Effects in Working Memory Training for Older Adults: A Systematic Review
- 论文类型：叙述性系统综述（Narrative Systematic Review，PRISMA 标准）
- 创建时间：2026-04-01
- 选题确认时间：2026-04-02
- 目标期刊：Ageing Research Reviews (IF ~10-12，首选) / Neuroscience & Biobehavioral Reviews (IF ~8，备选)

## 选题变更记录
- 原始选题（2026-04-01）：老年人视觉知觉学习的神经可塑性机制（VPL）
- 放弃原因：Perplexity 精确检索后确认实际文献量仅 9 篇（核心 6 篇），严重不足
- 新选题（2026-04-02）：WM 训练迁移效应调节因素系统综述
- 新选题确认依据：三轮 Perplexity 深度检索

## 当前状态
- 阶段：1 - 主题定义
- 进度：100% ✅
- 状态：已完成，准备进入阶段 2（文献检索）

## 已完成
- ✅ 环境配置完成（2026-04-01）
  - 本地 Git 配置
  - GitHub 私有仓库创建
  - Skills 安装（Humanizer, Zotero MCP）
  - CLAUDE.md 配置

- ✅ 阶段 1：主题定义（2026-04-02 完成，经历选题调整）
  - 第一次选题（VPL）：Perplexity 检索后发现文献量仅 9 篇，放弃
  - 转向 WM 训练调节因素方向
  - 三轮 Perplexity 检索确认选题可行性：
    - 第一轮：梳理现有综述格局，发现 Heinzel 2020 为最近似竞争文献
    - 第二轮：确认 Karbach 2014、Hindin 2012、Melby-Lervåg 2016 等文献范围
    - 第三轮：确认 2020-2024 年新增 6-8 篇实证研究，总可用文献约 24 篇
  - 选题可行性评估：✅ 文献量充足，研究空白明确

## 核心竞争文献
- **Heinzel et al. (2020)** — *Frontiers in Aging Neuroscience*
  - 最接近的已有综述，16 篇研究，叙述性，截止 2020 年
  - 局限：仅 16 篇、无 PRISMA、年龄 ≥55、无法量化调节因素
- **Teixeira-Santos et al. (2019)** — *Neuroscience & Biobehavioral Reviews*
  - 元分析，27 篇，老年人专属，含研究层面调节变量
  - 局限：调节因素为研究均值，非个体层面
- Karbach & Verhaeghen (2014) — 元分析，设计调节因素，无个体差异调节
- Lima-Silva et al. (2022) — 叙述综述，47 篇，无正式调节分析

## 研究空白（论文核心贡献）
1. 无综述同时涵盖个体差异调节因素 + 训练设计调节因素（2020年后仍如此）
2. 2020-2024 年新增 6-8 篇实证研究未被任何综述纳入
3. Heinzel 2020 无法量化调节因素，且文献量不足（16 篇）
4. 迁移结局分类不清：现有研究混淆训练获益 / 近迁移 / 远迁移

## 论文框架（三类调节因素）
- **个体特征调节因素**：年龄、基线认知能力、教育水平、认知储备
- **训练设计调节因素**：任务类型、训练剂量、自适应性、训练频率、监督方式
- **迁移测量调节因素**：近迁移 vs 远迁移、测量时间点、结局域

## 可用文献清单（已知）
**2020 年前（来自 Heinzel 2020 文献库，约 16 篇）**
- Borella et al. (2010)、Dahlin et al. (2008)、Brehmer et al. (2012) 等

**2020-2024 年新增（6-8 篇）**
1. Boujut & Belleville et al., 2020 — ACTOP 三臂 RCT，60-85 岁
2. Brum et al., 2020 — 个人 vs 团体训练格式
3. Jaeggi et al., 2020 — 训练间隔 RCT，多中心
4. Teixeira-Santos et al., 2022 — tDCS + 双 n-back，唯一正式检验个体差异调节
5. Zamarreño et al., 2024 — 复杂广度训练 + 情节记忆迁移，>60 岁
6. Zając-Lamparska, 2024 — 12 次 n-back 训练，60-75 岁
7. Pergher et al., 2021 — 模型驱动 WM 训练，50-81 岁
8. Booth et al., 2023 — 家庭训练间隔操控，55-85 岁

## 阶段 2 检索结果（2026-04-02 完成）

| 数据库 | 条数 | 导出格式 |
|--------|------|---------|
| PubMed | 2404 | MEDLINE (.txt) |
| PsycINFO | 1111 | RIS（2批） |
| Web of Science | 2295 | BibTeX（3批） |
| Scopus | 3232 | RIS |
| 合并前总计 | 9042 | — |
| 重复 | 4874 | — |
| **去重后** | **4168** | merged_deduplicated.ris |

- 去重脚本：`02-search/count_and_deduplicate.py`
- Cochrane 跳过（与PubMed重叠>90%，WM训练非临床医学）

## 待办
- [ ] 阶段 3：文献筛选（PRISMA 流程图，基于 merged_deduplicated.ris，4168条）
- [ ] 阶段 4：数据提取（建文献信息表）
- [ ] 阶段 5：论文撰写（叙述性整合）
- [ ] 阶段 6：审校投稿

## 时间线
- 阶段 1 完成：2026-04-02
- 预计总耗时：45-60 天
- 预计完成：2026-05-15 至 2026-06-01
