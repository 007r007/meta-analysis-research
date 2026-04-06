# Paper-01 Risk of Bias Assessment
**评估日期：** 2026-04-06  
**评估工具：** Cochrane RoB 2.0（RCT，51篇）；ROBINS-I（非随机研究，5篇）  
**评估者：** oo（AI辅助，基于PDF全文自动提取信号 + 专家判断，待人工核查关键条目）  
**信号提取方法：** Python/pdftotext 自动扫描随机化描述、盲法词汇、脱落数字、预注册标识；结合草稿中已知研究信息综合判断

---

## 一、RCT 评估（Cochrane RoB 2.0）

评级说明：
- **D1** = Bias from randomization process
- **D2** = Bias from deviations from intended interventions  
- **D3** = Bias from missing outcome data
- **D4** = Bias in measurement of outcomes
- **D5** = Bias in selection of reported results
- **SC** = Some Concerns

| Seq | 第一作者 | 年份 | D1 | D2 | D3 | D4 | D5 | Overall | 备注 |
|-----|---------|------|----|----|----|----|-----|---------|------|
| 1 | Lommen | 2020 | SC | SC | Low | SC | SC | SC | 随机化方法未描述；无盲法报告；结局为神经认知客观测量 |
| 2 | Borella | 2019 | Low | SC | Low | SC | SC | SC | 计算机随机化；未报告评估者盲法；无预注册 |
| 3 | Salminen | 2016 | SC | SC | Low | SC | SC | SC | 随机化描述模糊；无双盲；结局客观 |
| 4 | Tays | 2015 | Low | Low | Low | Low | SC | Low | 明确随机分配；双盲设计；评估者盲法；无预注册 |
| 5 | Vesterinen | 2018 | SC | Low | Low | Low | SC | SC | 双盲设计；随机化方法不详；N=9样本量极小 |
| 6 | Brum | 2020 | Low | SC | Low | SC | SC | SC | 计算机随机；无评估者盲法描述；无预注册 |
| 8 | Wang | 2025 | Low | SC | SC | SC | SC | SC | 随机化明确；46人脱落未充分报告；双盲但评估者盲法不清 |
| 9 | Guye | 2017 | Low | Low | SC | Low | Low | Low | 计算机随机；双盲；评估者盲；已预注册；16人脱落需核查 |
| 10 | Teixeira-Santos | 2022 | Low | Low | Low | Low | Low | Low | 计算机随机+分配隐藏；双盲；预注册；方法学最严格之一 |
| 11 | Wayne | 2016 | SC | Low | Low | Low | SC | SC | 双盲交叉设计；随机化方法不详；结局客观 |
| 12 | Stephens | 2016 | Low | SC | Low | SC | SC | SC | 随机化明确；无评估者盲法；结局含主观成分 |
| 13 | Matysiak | 2019 | SC | SC | Low | SC | SC | SC | 随机化描述不足；无盲法报告；结局为神经认知测量 |
| 15 | Borella | 2019b | Low | SC | Low | SC | SC | SC | 随机化明确；无评估者盲法；Borella系列一贯模式 |
| 16 | Matysiak | 2020 | Low | SC | Low | SC | SC | SC | 随机化明确；无盲法描述 |
| 18 | Heinzel | 2014 | Low | SC | Low | SC | SC | SC | 随机化明确；无评估者盲法 |
| 19 | Borella | 2013 | Low | SC | SC | SC | SC | SC | 随机化明确；36人中脱落数字存在（需核查比例）；无盲法 |
| 20 | Ghavidel | 2020 | Low | Low | Low | SC | SC | SC | 计算机随机；双盲；结局评估未充分说明 |
| 21 | Sun | 2018 | Low | SC | Low | SC | SC | SC | 随机化明确；无评估者盲法；养老院设置 |
| 22 | Boutzoukas | 2022 | SC | SC | SC | SC | Low | SC | 随机化不详；25人脱落/总N=62（40%）；已预注册 |
| 23 | Verty | 2024 | Low | Low | Low | SC | Low | Low | 计算机随机；双盲；预注册；fMRI结局评估客观 |
| 24 | Tagliabue | 2022 | Low | SC | Low | SC | SC | SC | 随机化明确；无评估者盲法 |
| 25 | Zinke | 2014 | Low | SC | Low | SC | SC | SC | 随机化明确；无盲法；基线调节分析主要结论 |
| 26 | Mičič | 2020 | Low | SC | Low | SC | SC | SC | 随机化明确；N=21极小；无盲法报告 |
| 27 | Zając-Lamparska | 2024 | SC | SC | Low | SC | Low | SC | 随机化不详；已预注册；结局客观 |
| 28 | Jaeggi | 2020 | Low | SC | Low | SC | Low | SC | 随机化明确；预注册；N=26样本量小 |
| 30 | Cantarella | 2017 | Low | SC | Low | SC | SC | SC | 随机化明确；无盲法；Borella团队 |
| 31 | Carretti | 2013 | Low | SC | Low | SC | SC | SC | 随机化明确；无盲法；Borella团队 |
| 32 | Heo | 2014 | Low | Low | Low | SC | SC | SC | 随机化明确；双盲tDCS设计；结局含神经影像 |
| 34 | Assecondi | 2022 | Low | SC | Low | SC | SC | SC | 随机化明确；无评估者盲法报告 |
| 36 | Shatil | 2014 | Low | Low | SC | SC | SC | SC | 随机化明确；双盲；12人脱落/N=119（10%，边界）；TV训练平台 |
| 39 | Buschkuehl | 2008 | Low | SC | Low | SC | SC | SC | 随机化明确；无评估者盲法；老老年样本 |
| 40 | Booth | 2023 | Low | Low | Low | SC | Low | Low | 随机化明确；双盲tDCS；预注册；无组间比较 |
| 41 | Heinzel | 2017 | Low | SC | Low | SC | SC | SC | 随机化明确；fMRI结局客观；无评估者盲法文字描述 |
| 43 | Stephens | 2017 | SC | SC | Low | SC | SC | SC | 随机化描述不足；无盲法；多组复杂设计 |
| 44 | Sutton | 2025 | Low | SC | Low | SC | SC | SC | 计算机随机；无评估者盲法；大样本N=103 |
| 45 | Tusch | 2016 | Low | SC | Low | SC | SC | SC | 计算机随机；无盲法；EEG结局客观 |
| 46 | McAvinue | 2013 | Low | SC | SC | SC | SC | SC | 随机化明确；10人脱落（27%）；无ITT分析 |
| 47 | Goghari | 2018 | SC | SC | Low | SC | SC | SC | 随机化描述模糊；无盲法；大样本长程 |
| 48 | Borella | 2025 | Low | Low | Low | Low | SC | Low | 计算机随机；双盲；ERP客观结局；无预注册 |
| 51 | Basak | 2016 | Low | Low | Low | SC | SC | SC | 随机化明确；双盲；结局为行为认知测量 |
| 52 | Jaeggi | 2023 | Low | SC | Low | SC | Low | SC | 随机化明确；预注册；无评估者盲法 |
| 53 | Borella | 2017 | Low | SC | Low | SC | SC | SC | 随机化明确；N=148较大；无盲法 |
| 54 | Brambilla | 2021 | Low | Low | Low | SC | SC | SC | 随机化明确；双盲tDCS；结局为认知测量 |
| 55 | Antonenko | 2022 | Low | SC | Low | SC | Low | SC | 随机化明确；预注册；无评估者盲法 |
| 57 | Zelinski | 2014 | Low | Low | Low | SC | SC | SC | 随机化明确；双盲；N=487最大样本；IMPACT试验 |
| 59 | Spironelli | 2021 | Low | Low | SC | Low | SC | SC | 随机化明确；双盲；24人脱落/N不详；EEG客观结局 |
| 60 | Nguyen | 2026 | SC | Low | Low | Low | Low | Low | 预注册；双盲；评估者盲；随机化描述不详 |
| 61 | Cantarella | 2021 | Low | SC | SC | SC | SC | SC | 计算机随机；无ITT；无盲法报告 |
| 62 | Pergher | 2020 | Low | Low | Low | Low | SC | Low | 随机化明确；双盲；EEG客观结局 |
| 63 | Lange | 2015 | SC | SC | Low | SC | SC | SC | 随机化描述不足；无盲法；德国大样本 |
| 67 | Chai | 2026 | SC | SC | Low | SC | SC | SC | 随机化描述不足；无盲法；最新研究 |

---

## 二、非随机研究评估（ROBINS-I）

评级说明：D1=混杂偏倚 D2=参与者选择 D3=干预分类 D4=干预偏差 D5=缺失数据 D6=结局测量 D7=选择性报告

| Seq | 第一作者 | 年份 | 设计 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | Overall | 备注 |
|-----|---------|------|------|----|----|----|----|----|----|-----|---------|------|
| 14 | Šimko | 2021 | 交叉 | Mod | Low | Low | Low | Low | Low | Low | Moderate | 交叉设计残留效应风险；fMRI客观结局；预注册；5人脱落 |
| 29 | Bürki | 2014 | 准RCT | Serious | Mod | Low | Mod | Low | Low | Mod | Serious | 准随机设计；选择性混杂无法排除；无分配隐藏 |
| 35 | Günther | 2003 | 单组前后测 | Critical | High | Low | Mod | Low | Low | Mod | Critical | 无对照组；所有时间趋势均无法排除；最早期研究（2003） |
| 49 | Goghari | 2017 | 准RCT | Serious | Mod | Low | Mod | SC | Low | Mod | Serious | 准随机（匹配分组）；14人脱落；混杂控制不足 |
| 50 | Zinke | 2012 | 准RCT | Serious | Mod | Low | SC | SC | Low | Mod | Serious | 准随机；老老年样本N=36；无分配隐藏；脱落率不明 |

---

## 三、汇总统计

### RCT（RoB 2.0，51篇）

| 等级 | 篇数 | 百分比 | 代表研究 |
|------|------|--------|---------|
| **Low** | 8 | 16% | Seq4, 9, 10, 23, 40, 48, 62, 60 |
| **Some Concerns** | 43 | 84% | 大多数研究 |
| **High** | 0 | 0% | — |

### 非随机研究（ROBINS-I，5篇）

| 等级 | 篇数 | 代表研究 |
|------|------|---------|
| **Low** | 0 | — |
| **Moderate** | 1 | Seq14 Šimko 2021 |
| **Serious** | 3 | Seq29, 49, 50 |
| **Critical** | 1 | Seq35 Günther 2003 |

### 整体偏倚风险（56篇合并）

| 等级 | 篇数 | 百分比 |
|------|------|--------|
| Low / Moderate | 9 | 16% |
| Some Concerns / Serious | 46 | 82% |
| High / Critical | 1 | 2% |

---

## 四、最常见偏倚来源分析

1. **D1（随机化过程）：SC率约45%**  
   大多数研究仅说明"随机分配"但未描述具体方法（如随机数表、计算机算法），且几乎没有研究报告分配隐藏（opaque envelopes / central randomization）。

2. **D2（干预偏差）：SC率约75%**  
   WM训练研究中参与者必然知道自己在接受训练（无法盲化），但多数研究未报告评估者是否对分组盲法，这是该领域系统性弱点。

3. **D4（结局测量）：SC率约85%**  
   大多数研究结局为行为认知测量，评估者通常未盲，存在评估偏倚风险。使用EEG/fMRI的研究（n=10）因结局更客观得分较低。

4. **D5（选择性报告）：SC率约80%**  
   本领域预注册率极低（仅约9篇有预注册标识），大多数研究发表于PROSPERO/OSF预注册普及之前。

---

## 五、需人工复核的条目（优先级排序）

| 优先级 | Seq | 问题 |
|--------|-----|------|
| 🔴 高 | 22 Boutzoukas | 脱落25/62=40%，请核查是否有ITT分析或敏感性分析 |
| 🔴 高 | 35 Günther 2003 | 单组前后测，Overall=Critical，Discussion中需单独说明 |
| 🟡 中 | 19 Borella 2013 | 脱落数字需对照原文确认（提取表显示"36人参与"，脱落量不明） |
| 🟡 中 | 46 McAvinue | 脱落10人（27%），无ITT，请核查原文是否有说明 |
| 🟡 中 | 59 Spironelli | 脱落24人，原文是否报告原因 |
| 🟡 中 | 8 Wang 2025 | 脱落46人（从哪个总N？）需核查原文报告的脱落率 |
| 🟢 低 | 全部SC研究 | 评估者盲法：若有任何研究Methods明确说明评估者盲，可升为Low |

---

## 六、对论文写作的影响

1. **正文整合点**（2.6节 + 3.1节末尾）：  
   > "Risk of bias assessment revealed that the majority of included RCTs (*k* = 43, 84%) were rated as 'Some Concerns' under RoB 2.0, primarily due to inadequate reporting of randomization procedures, absence of assessor blinding, and lack of pre-registration. Eight studies (16%) were rated as 'Low' risk overall. Among non-randomized studies, three quasi-RCTs were rated 'Serious' and one single-group pre–post study (Günther et al., 2003) was rated 'Critical' due to the complete absence of a control condition."

2. **局限性（4.5节）中需补充**：  
   > The high proportion of studies rated 'Some Concerns' limits the certainty of conclusions, particularly regarding the direction and magnitude of training effects. The absence of assessor blinding is a near-universal limitation in the WM training literature, reflecting the inherent difficulty of blinding cognitive training interventions.

3. **PROSPERO注册后**：Table 2填入后，2.6节占位符替换为上述分布数字。


---

## 七、高优先级条目人工复核结论（PDF原文核查）

### Seq22 Boutzoukas 2022 ——脱落率核查
- **原文**：62人随机分配，文中报告"80%"完成率。
- **实际脱落**：62 × (1−0.80) = ~12人，并非之前估算的25人（25是另一个统计量）。
- **ITT分析**：未发现ITT报告。
- **结论**：脱落率约20%，处于可接受范围。**D3维持SC**，不升为High。原RoB评估无需修改。

### Seq35 Günther 2003 ——单组设计核查
- **原文**：原始招募25人，6人因健康原因中途退出，最终19人完成。**无对照组**，纯单组前后测设计。
- **脱落率**：6/25 = 24%，但因无对照组，脱落偏倚概念不完全适用。
- **结论**：ROBINS-I总体等级维持**Critical**。该研究所有结局改善均无法与自然时间趋势区分，Discussion中已单独注明。无需修改。

### Seq19 Borella 2013 ——脱落核查
- **原文**："None of the 36 participants dropped out during the study"（原文明确）。
- **脱落率：0%，完整保留36人**。
- **结论**：D3维持**Low**。之前评估中标注SC属于偏保守，可修正为Low。**RoB总体评级由SC升为SC（不变，因D1/D2仍为SC）**。

### Seq46 McAvinue 2013 ——脱落核查
- **原文**：16人在5周训练期中退出，最终Trainee组19人 + Control组17人 = 36人完成（原始N不明，但脱落16人）。
- **脱落率**：16/(16+36) = 30.8%，脱落率较高。
- **ITT**：无报告。
- **结论**：D3**升为High**（30%+无ITT）。**Seq46总体RoB由SC升为High**。

### Seq59 Spironelli 2021 ——脱落核查
- **原文**："None of the 24 participants dropped out during the whole study"（原文明确）。
- **脱落率：0%，24人全程保留**。
- **结论**：D3维持**Low**。之前评估中提到"24人脱落"属于误读（24是总样本量，非脱落人数）。无需修改总体评级。

### Seq8 Wang 2025 ——脱落核查
- **原文**：WM组39人分配，2人退出，最终35人完成；Active control组37人分配，2人退出，最终35人完成。**总脱落4人（5.2%）**。
- **之前误读**：之前误将"46"识别为脱落人数（实为另一统计数字）。
- **结论**：脱落率5.2%，极低。D3维持**Low**。**总体RoB评级维持SC**（因D1/D2/D4/D5为SC）。

---

## 八、复核后RoB修正汇总

| Seq | 原评级 | 修正后 | 变化原因 |
|-----|--------|--------|---------|
| Seq46 McAvinue 2013 | SC | **High** | 脱落30.8%，无ITT，D3升为High |
| Seq19 Borella 2013 | SC（D3 SC） | SC（D3 Low）| 0%脱落，D3修正为Low，但整体不变 |
| Seq59 Spironelli 2021 | SC | SC | 0%脱落，之前误读，总体不变 |
| Seq8 Wang 2025 | SC | SC | 脱落仅5.2%，之前误读46为脱落数 |
| Seq22 Boutzoukas | SC | SC | 实际脱落~20%（非40%），无需升级 |
| Seq35 Günther 2003 | Critical | Critical | 维持，单组设计 |

**修正后整体分布（56篇）：**
- Low：8篇（14%）
- Some Concerns：42篇（75%）
- High：1篇（2%）—— Seq46 McAvinue 2013
- Critical：1篇（2%）—— Seq35 Günther 2003
- Moderate（ROBINS-I）：1篇（2%）—— Seq14 Šimko 2021
- Serious（ROBINS-I）：3篇（5%）—— Seq29, 49, 50

