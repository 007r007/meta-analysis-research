# 指导语：cx 综合裁决「科研工作平台升级」方案

> 角色：你是 **cx（Codex，最终裁决者）**。cc 已起草问题清单+升级地图，cl 独立审后补 8 漏项、纠 1 映射、重排优先级。请你综合裁决，给出平台升级的最终方案与执行顺序。裁决后 cc/cl 按定稿动手。

## 必读
1. `D:\Research_Agent_Lab\reports\平台升级_问题清单与方案_cc初版.md`（cc 六问题 + 三层解析策略）
2. `D:\Research_Agent_Lab\reports\平台升级_cl独立审.md`（cl 补 8 漏项 + 纠错 + 优先级）
3. `D:\Research_Agent_Lab\PLATFORM_CONSTITUTION.md`（平台宪法）
4. `D:\Research_Agent_Lab\references\rag_conventions.md`（RAG 约定）

## 已收敛（cc+cl 一致，请你确认即可）

- 问题域 = cc 的 6 项 + cl 补的 8 项 = **14 项**（语料治理、权威键绑定、双人编码工具化、解析↔索引联动、supplement 分节、图-only 规则、批处理台账、项目结构对齐、文档解析、三脑身份、效应量 skill、schema 收尾、检索模板、trial 边界）。
- P1 文档解析三层：A `fitz.find_tables()` 先上（零依赖）→ B MinerU 按需触发 → C 多模态 VLM 过合规闸门。
- P3 落点纠错：cc"并入 meta-analysis"是错的（meta-analysis 是本地拷贝）→ **新建 public skill**（cl 纠，cc 接受）。
- P1 补两条（cl 加，cc 接受）：①解析输出绑定 sha256:page 回灌 FTS5 chunks；②解析质量断言。

## 待你裁决的分歧

### 分歧 1：优先级排序
- **cc**：P1 → P2 → P4 → P3 → P6 → P5
- **cl**：P2 → P1-A → P4 → P6 → P3 → P5
- 核心两问：(a) P2（三脑身份规则补丁）提到第 1 还是 P1 第 1？(b) P6（trial 边界）提到 P3（效应量 skill）之前还是之后？
- cl 理由：P2 半小时级、事故已发生、不阻塞其他；P6 是 P3 的依赖（判定手册挂在 trial 结构上）。

### 分歧 2：P1 的 B/C 触发条件
- cc：B 评估/安装 MinerU、C 打通多模态。
- cl：B 只对 `find_tables` 校验失败的篇目按需调用；C 需用户授权 + 数据出机声明（宪法第 6 条 + no-cloud 纪律）。
- 请裁定：B/C 是"立即做"还是"按需/过闸门"。

### 事实澄清（供你知悉，非分歧）
- cl 标"codex 命令已装 = UNVERIFIED"；cc 实测已装（codex-cli 0.153.4，`codex doctor` 通过）。以 cc 实测为准。

## 输出格式

1. 最终执行顺序（列 14 项的先后 + 每项一句话）
2. P1-B/C 的触发条件定案
3. 一句话确认已收敛项（三层解析、P3 新建 skill、P1 两条补动作、14 项问题域）
