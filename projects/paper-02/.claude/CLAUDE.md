# Paper-02 项目记忆（CLAUDE.md）

**最后更新**：2026-04-08
**版本**：v2.0（oo-cc联合讨论确认版）

---

## 项目信息

- **标题**：Parental education level and early childhood neural development: a systematic review of EEG, ERP, fNIRS, and neuroimaging evidence (ages 0–8 years)
- **类型**：叙述性系统综述（PRISMA 2020，非Meta分析）
- **不做Meta原因**：结局指标高度异质（rsEEG/ERP/fMRI/DTI跨模态，无法合并效应量）
- **目标期刊**：Developmental Cognitive Neuroscience（Q1，IF≈4.5）
- **备用期刊**：Developmental Science / Infant and Child Development
- **预估纳入**：35–50篇

---

## PICOS核心标准

| 要素 | 标准 |
|------|------|
| P | 0–8岁儿童（含婴儿期） |
| I/E | 父母教育水平（SES单一维度） |
| O | EEG/ERP/fNIRS/fMRI/DTI/structural-MRI任一神经指标（MEG/MRS预计为零但若有则纳入） |
| S | 观察性研究（横断/纵向）或RCT；排除综述/元分析 |

### SES编码方案（Methods关键设计）

| 情况 | 判断 | 理由 |
|------|------|------|
| 单独报告父母教育效应 | ✅ 纳入 | 直接可提取 |
| 复合SES，但回归模型中教育有独立Beta/b系数及显著性 | ✅ 纳入 | 可提取教育独立效应 |
| 教育作为协变量，文献未报告教育的Beta系数 | ❌ 排除 | 无法提取教育效应 |
| PCA合成SES主成分，教育权重隐含 | ❌ 排除 | 无法分离教育效应 |
| 收入分组+教育连续变量分别报告 | ✅ 纳入 | 教育有独立统计结果 |

**ses_type字段三分类**：
- `edu-only`：单独报告父母教育
- `composite-separable`：复合SES但教育效应可单独提取
- `composite-inseparable`：复合SES，教育效应无法分离（→排除）

---

## 四方协作分工

| 角色 | 工具 | 职责 |
|------|------|------|
| **oo（OpenClaw）** | 云端服务器 | 战略决策、提示词设计、核查、记忆管理 |
| **cc（Claude Code）** | 用户本地Windows | 脚本执行、Excel处理、git管理、文件同步 |
| **xhs（Kimi）** | 云端服务器 | 全文PDF阅读、批量筛选、直接写入Excel |
| **用户** | 本地 | 专业判断、边界案例决策、数据库手动检索 |

**协作原则**：
- oo和cc在每个重要节点必须充分讨论后再提交用户决策，不单方面拍板
- 纯技术问题（脚本/Excel格式）：cc直接决定，事后告知
- 方法学问题：必须提交用户，不能单方面决定
- cc push → oo git pull确认 → 核查 → 通知用户
- xhs提示词由oo生成，用户转发给xhs
- oo不主动同步，等用户指令后再git pull

---

## 当前进度

- ✅ 00-planning：选题规划完成
- ✅ 01-topic：选题确认
- ✅ 02-search：四库检索完成，去重后1827条
- 🔄 03-screen：第一轮筛选进行中
- ⬜ 04-extract：数据提取
- ⬜ 05-analysis：综合分析
- ⬜ 06-write：论文写作
- ⬜ 07-review：同行评审
- ⬜ 08-submit：投稿

---

## 检索统计

| 数据库 | 原始条数 |
|--------|---------|
| PubMed | 521 |
| PsycINFO | 296 |
| Web of Science | 1011 |
| Scopus | 1269 |
| 合并前总计 | 3097 |
| **去重后** | **1827** |

不含Cochrane（观察性研究综述，Methods需说明原因）

---

## 关键文件

| 阶段 | 文件 | 说明 |
|------|------|------|
| 02-search | `数据_1_四库检索式_v4最终版.md` | 文件名为v4，内容实为v5（含alpha/theta power等补充词） |
| 02-search | `数据_2_四库合并去重后.ris` | 1827条 |
| 02-search | `结果_1_检索统计数据.json` | 各库原始数量 |
| 03-screen | `数据_1_第一轮筛选.xlsx` | 1827条待筛 |
| 00-planning | `文档_1_方法学决策记录.md` | oo-cc决策记录，纳入git追踪 |

---

## 文件路径

- 项目根（cc本地）：`E:\Meta-analysis writing project\projects\paper-02\`
- 项目根（oo云端）：`/root/.openclaw/workspace/research/papers/projects/paper-02/`
- 共享记忆：`shared/memory/paper-02-memory.md`

---

## PROSPERO注册

- **状态**：⚠️ 尚未注册，由用户和导师决定是否注册
- **说明**：叙述性综述无强制要求，但注册可提升DCN投稿可信度
- **截止**：若决定注册，必须在开始撰写前完成

---

## 论文结构框架（oo-cc共识版）

| 章节 | 预估字数 | 核心内容 |
|------|---------|---------|
| Introduction | ~1000词 | 为何聚焦父母教育而非复合SES、0-8岁神经可塑性窗口、多模态整合必要性、4个研究问题 |
| Methods | ~1500词 | PRISMA 2020、PICOS、双人筛选+Kappa、NOS偏倚风险、叙述性综合说明 |
| Results | ~4000–4500词 | 按模态组织，模态内按年龄段排序 |
| Discussion | ~2500词 | 四大研究空白、局限性（含跨文化推广性不足）、未来方向 |
| **总计** | **~9000–10500词** | 符合DCN综述字数范围 |

**Results组织方式**：
- 3.1 文献筛选结果（PRISMA流程）
- 3.2 纳入文献特征概述
- 3.3 静息态EEG（预计8-12篇，婴儿期→幼儿期→学龄前）
- 3.4 任务态ERP（预计10-15篇，按年龄段排序）
- 3.5 fMRI/fNIRS（预计8-12篇）
- 3.6 DTI/结构MRI（预计5-8篇）
- 3.7 偏倚风险评估

**Discussion局限性**（必含）：
- 检索限于英文文献库，非西方/低中收入国家（尤其中国）样本严重不足，限制结论的跨文化推广性
- 不含"中国研究特别讨论"节（文献支撑不足）

---

## 数据提取表字段设计（oo-cc共识版，约32-35列）

### 基本信息（8列）
| 字段 | 说明 |
|------|------|
| study_id | 序号 |
| author_year | 作者+年份 |
| country | 国家/地区 |
| sample_n | 样本量 |
| age_mean_sd | 儿童年龄均值±SD |
| design | 横断/纵向 |
| followup_months | 纵向研究随访月数（横断填NA） |
| db_source | 数据库来源 |

### SES测量（5列）
| 字段 | 受控词表 |
|------|---------|
| ses_type | edu-only / composite-separable / composite-inseparable |
| edu_measure | years / level-categorical / continuous-score |
| edu_reporter | father / mother / mean / highest |
| ses_range | full-range / low-SES-only / high-SES-only / mixed |
| ses_control | 是否控制其他SES变量（是/否+说明） |

### 神经测量（9列）
| 字段 | 受控词表/说明 |
|------|-------------|
| modality | rsEEG / ERP / fNIRS / fMRI / DTI / structural-MRI |
| paradigm | 见Paradigm受控词表 |
| eeg_band | alpha/theta/delta/beta/gamma/broadband（EEG适用） |
| erp_component | MMN/N400/P300/N170/Nc/P1/LPC/ERN/other（ERP适用） |
| electrode_region | frontal/central/parietal/occipital/temporal/whole-scalp |
| brain_roi | PFC/ACC/IFG/STG/MTG/hippocampus/amygdala/ILF/AF/SLF/DMN/other |
| measure_type | task-based/resting-state/structural/functional-connectivity |
| dti_metric | FA/MD/RD/AD/volume/myelin/other（DTI适用） |
| lateralization | left/right/bilateral/not-reported |

### 结局（4列）
| 字段 | 说明 |
|------|------|
| effect_direction | positive/negative/null/mixed |
| effect_size | Cohen's d或r（若报告则填，否则NA） |
| confounders_controlled | 已控制的混淆变量列表（含是否控制儿童认知能力） |
| age_at_measure | 神经测量时儿童年龄 |

### 质量评估（3列，NOS量表）
| 字段 | 范围 |
|------|------|
| NOS_selection | 0–4 |
| NOS_comparability | 0–2 |
| NOS_outcome | 0–3 |

**删除字段**：~~analysis_software~~、~~significance(p值)~~

---

## Paradigm受控词表

### EEG/ERP
| 词条 | 预计频率 |
|------|---------|
| resting-state | 高（≥10篇） |
| selective-attention | 中（3-5篇） |
| go-nogo | 中（4-6篇） |
| error-monitoring | 低中（2-3篇） |
| oddball-MMN | 低中（3-4篇） |
| habituation-dishabituation | 低中（婴儿期为主） |
| language-N400 | 低（多为>8岁） |
| naturalistic | 低（新兴） |
| other | — |

### fMRI/fNIRS
| 词条 | 预计频率 |
|------|---------|
| resting-state-fc | 中（3-4篇） |
| language-story | 中（3-5篇） |
| selective-attention | 低（1-2篇） |
| executive-function | 低中（2-3篇） |
| social-processing | 低中（2-3篇） |
| statistical-learning | 低（1-2篇） |
| other | — |

### DTI/Structural MRI
| 词条 | 说明 |
|------|------|
| tractography | DTI，无任务 |
| morphometry | VBM/皮层厚度/体积 |
| myelin-imaging | qMRI髓鞘成像 |

---

## 排除代码（筛选用）

| 代码 | 含义 |
|------|------|
| E1 | 年龄不符：样本非0–8岁 |
| E2 | 暴露不符：非父母教育/SES |
| E3 | 无神经指标 |
| E4 | 综述/元分析/protocol/评论 |
| E5 | 非英文 |
| E6 | 无法获取全文 |
| E7 | 样本重复报告 |
| E8 | 其他（备注列说明） |

---

## 投中概率评估

- 概率：55–65%（执行质量高时）
- 最大风险：SES复合指标操作化问题
- 应对：已设计SES编码方案（见上）
- 建议导师作通讯作者

---

## 启动时执行

1. 读取本文件，显示当前阶段和待办
2. 检查git最新commit：`git log --oneline -3`
3. 询问今天要做什么任务
