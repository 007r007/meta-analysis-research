# -*- coding: utf-8 -*-
"""
Paper-01 比较层新表生成脚本（v1，待 cx 审计）
=====================================================
按 07-review/数据字典_比较层新表_schema.md（冻结版 v1）生成「比较层新表」：
粒度 trial → arm → comparison → outcome → timepoint 五层。

硬性规则：
  - comp_type / 联合干预 / est_target 以 v3 终表（cx 仲裁）为人工核准结果，本脚本一律不自动判断。
  - 旧表 数据_6_数据提取表_v3_research.xlsx 保留为历史档，本脚本不读取也不改写它。
  - 臂明细(n/components)来自 07-review/数据_臂比较原文提取.txt 与 cl/v1 编码，不重跑 PDF。
  - 生成新文件：数据_7_比较层新表.xlsx（不影响旧表）。

本脚本只做「组装 + 写表」，不做任何语义判断；所有判断值均硬编码自 v3 终表。
"""
import openpyxl
from openpyxl.styles import Font, Alignment

BASE = r"E:\Meta-analysis writing project\projects\paper-01"
OUT  = BASE + r"\04-extract\数据_7_比较层新表.xlsx"

# ──────────────────────────────────────────────────────────────────────────────
# 一、56→51 去重/嵌套映射（v3 导入规则 1 + cx 仲裁 2026-11-15）
#    key = 被移除 Seq；value = (主报告 Seq 列表, exclusion_status, exclusion_reason)
#    cx 裁定：Seq43 双挂 Seq4+Seq12；Seq53 双挂 Seq19+Seq31（一对二合并）。
# ──────────────────────────────────────────────────────────────────────────────
SECONDARY = {
    16: ([13], "duplicate", "协议论文=Seq13(Matysiak 2019)重复"),
    43: ([4, 12], "duplicate", "Stephens 2017=Seq4(Jones)+Seq12(Stephens)合并重析，无新数据"),
    47: ([49], "duplicate", "Goghari 2018=Seq49(Goghari 2017)同样本再报告"),
    53: ([19, 31], "duplicate", "Borella 2017 IPD=Seq19+Seq31+2不在册研究合并；2不在册已拆为T52/T53"),
    28: ([52], "nested",    "Jaeggi 2020 ⊂ Seq52(Jaeggi 2023)嵌套，保留Seq52为主"),
}

# ──────────────────────────────────────────────────────────────────────────────
# 二、51 个独立试验（主报告）
#     字段：seq, author_year, country, design, note, co_int(v3联合干预),
#           arms[(label, intervention_components, control_components, n), ...],
#           comps[(arm_a_idx, arm_b_idx, comp_type, est_target, note), ...],
#           audit(cc_code, cl_code, cx_final)
#     comp_type 取值：①/②/③/④/⑤(S)/N(单组无比较)/excluded
# ──────────────────────────────────────────────────────────────────────────────
# comp_type 最终值（v3）→ est_target 映射（v3 定义，非本脚本判断）：
#   ①→WM效应  ②→WM增量  ③→刺激增益  ④→组合效果  ⑤→变体
TRIALS = [
    # ---- T01 Seq1 ----
    dict(seq=1, author_year="Maes 2020", country="Netherlands", design="single-group",
         note="作者Lommen→Maes；设计RCT→单组；高/低功能追踪，无对照组",
         co_int="无",
         arms=[("单臂WM训练(高/低功能追踪)", "WM训练(按初始EF水平分高/低功能)", "", None)],
         comps=[],
         audit=("N", "N", "N")),
    # ---- T02 Seq2 ----
    dict(seq=2, author_year="Borella 2019a", country="Italy", design="RCT",
         note="联合干预(Exercise→音乐)：训练前聆听音乐属④组合；4组",
         co_int="音乐(仅训练臂)",
         arms=[("Mozart+WM训练", "WM训练+莫扎特K448聆听", "", 19),
               ("Albinoni+WM训练", "WM训练+阿尔比诺尼聆听", "", 19),
               ("白噪音+WM训练", "WM训练+白噪音", "", 16),
               ("主动对照(其他活动,无音乐)", "", "其他活动(非WM)，无音乐", 18)],
         comps=[(0, 3, "④", "组合效果", "训练侧=arm1-3(音乐/白噪+WM)合并 vs arm4主动对照")],
         audit=("①", "④", "④")),
    # ---- T03 Seq3 ----
    dict(seq=3, author_year="Salminen 2016", country="Germany", design="RCT",
         note="老年亚组N待核(21/21?)；N=46；年轻样本人群不符合纳入标准，未计入",
         co_int="无",
         arms=[("训练组(老年)", "dual n-back训练", "", None),
               ("对照组(老年)", "", "被动/无训练对照", None)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T04 Seq4 ----
    dict(seq=4, author_year="Jones 2015", country="USA", design="RCT",
         note="作者Tays→Jones；类型③(刺激增益非WM效应)；4个tDCS montage组，N待核",
         co_int="tDCS",
         arms=[("sham-tDCS+WM训练", "WM训练+假tDCS", "", None),
               ("active-tDCS(PFC)+WM训练", "WM训练+额叶tDCS", "", None),
               ("active-tDCS(PPC)+WM训练", "WM训练+顶叶tDCS", "", None),
               ("active-tDCS(交替)+WM训练", "WM训练+交替tDCS", "", None)],
         comps=[(1, 0, "③", "刺激增益", "active montage vs sham(均WM)")],
         audit=("③", "③", "③")),
    # ---- T05 Seq5 ----
    dict(seq=5, author_year="Pergher 2018", country="Belgium", design="RCT",
         note="联合干预(Medication→无)；N(9→老年14/14)已修；年轻样本人群不符合纳入标准，未计入",
         co_int="无",
         arms=[("认知训练组(老年CTG)", "n-back训练", "", 14),
               ("被动对照组(老年PCG)", "", "被动对照", 14)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T06 Seq6-Study1 ----
    dict(seq="6-S1", author_year="Brum 2020 Study1", country="Brazil", design="RCT",
         note="Seq6(Brum 2020)子研究1，独立招募/分组；训练18/对照28，N=46；verbal span",
         co_int="无",
         arms=[("训练组(Study1)", "verbal WM span训练", "", 18),
               ("主动对照(Study1)", "", "问卷/主动对照", 28)],
         comps=[(0, 1, "①", "WM效应", "Study1")],
         audit=("①", "①", "①")),
    # ---- T07 Seq6-Study2 ----
    dict(seq="6-S2", author_year="Brum 2020 Study2", country="Brazil", design="RCT",
         note="Seq6(Brum 2020)子研究2，独立招募/分组；训练23/对照27，N=50；verbal span",
         co_int="无",
         arms=[("训练组(Study2)", "verbal WM span训练", "", 23),
               ("主动对照(Study2)", "", "问卷/主动对照", 27)],
         comps=[(0, 1, "①", "WM效应", "Study2")],
         audit=("①", "①", "①")),
    # ---- T07 Seq8 ----
    dict(seq=8, author_year="Wang 2025", country="China", design="RCT",
         note="N=76",
         co_int="无",
         arms=[("WM干预组", "游戏化WM训练", "", 39),
               ("主动对照组", "", "主动对照", 37)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T08 Seq9 ----
    dict(seq=9, author_year="Guye 2017", country="Switzerland", design="RCT",
         note="N(66→142待核)；主动视觉搜索对照",
         co_int="无",
         arms=[("实验组", "自适应WM训练(25次)", "", None),
               ("主动对照(视觉搜索)", "", "自适应视觉搜索", None)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T09 Seq10 ----
    dict(seq=10, author_year="Teixeira-Santos 2022", country="USA", design="RCT",
         note="联合干预(Medication→tDCS)；三臂拆两条比较(②主+③次)；N=54",
         co_int="tDCS",
         arms=[("atDCS+WMT", "anodal-tDCS+WM训练", "", None),
               ("stDCS+WMT", "sham-tDCS+WM训练", "", None),
               ("double-sham(假刺激+安慰剂任务)", "sham-tDCS+安慰剂任务", "", None)],
         comps=[(1, 2, "②", "WM增量", "stDCS+WMT vs double-sham(共同sham-tDCS)"),
                (0, 1, "③", "刺激增益", "atDCS+WMT vs stDCS+WMT(均WM)")],
         audit=("②+③", "②+③", "②+③")),
    # ---- T10 Seq11 ----
    dict(seq=11, author_year="Wayne 2016", country="USA", design="RCT",
         note="臂内容待核(首个人老年WM训练+言语噪声转移RCT)",
         co_int="无",
         arms=[("WM训练组(Cogmed)", "Cogmed WM训练", "", None),
               ("主动对照组", "", "主动对照", None)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T11 Seq12 ----
    dict(seq=12, author_year="Stephens 2016", country="USA", design="RCT",
         note="类型③；3组各30(Sham/1mA/2mA)",
         co_int="tDCS",
         arms=[("Sham+WM训练", "WM训练+假tDCS", "", 30),
               ("1mA tDCS+WM训练", "WM训练+1mA tDCS", "", 30),
               ("2mA tDCS+WM训练", "WM训练+2mA tDCS", "", 30)],
         comps=[(2, 0, "③", "刺激增益", "2mA(主) vs sham")],
         audit=("③", "③", "③")),
    # ---- T12 Seq13 ----
    dict(seq=13, author_year="Matysiak 2019", country="Poland", design="RCT",
         note="国家USA→Poland；联合干预(Exercise/Medication→无)；N=83/85",
         co_int="无",
         arms=[("实验组(dual n-back)", "自适应dual n-back训练", "", None),
               ("主动对照(记忆问答)", "", "语义记忆Quiz", None)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T13 Seq14 ----
    dict(seq=14, author_year="Šimko 2021", country="Czech Republic", design="crossover",
         note="设计交叉(非RCT)；类型③；被试内active/sham",
         co_int="tDCS",
         arms=[("active-tDCS(被试内)", "VWM任务+active tDCS", "", None),
               ("sham-tDCS(被试内)", "VWM任务+sham tDCS", "", None)],
         comps=[(0, 1, "③", "刺激增益", "被试内active vs sham")],
         audit=("③", "③", "③")),
    # ---- T14 Seq15 ----
    dict(seq=15, author_year="Cantarella 2019", country="Italy", design="RCT",
         note="作者Borella→Cantarella；联合干预(Medication→无)；N=32",
         co_int="无",
         arms=[("训练组", "WM训练", "", 16),
               ("主动对照(问卷)", "", "问卷/其他活动", 16)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T15 Seq18 ----
    dict(seq=18, author_year="Heinzel 2014", country="Germany", design="RCT",
         note="联合干预(Exercise/Medication→无)；老年N=30(N=60为全年龄)；年轻样本人群不符合纳入标准，未计入",
         co_int="无",
         arms=[("训练组(老年)", "WM训练(ISI自适应)", "", None),
               ("对照组(老年)", "", "对照", None)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T16 Seq19 ----
    dict(seq=19, author_year="Borella 2013", country="Italy", design="RCT",
         note="被Seq53(IPD)合并，但Seq53去重后本条独立；18训练/18主动；Seq53另含2不在册样本(Borella 2010 N=40/Borella 2017∧ N=36)记备注",
         co_int="无",
         arms=[("训练组", "verbal WM训练", "", 18),
               ("主动对照组", "", "主动对照", 18)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T17 Seq20 ----
    dict(seq=20, author_year="Fadardi 2020", country="Iran", design="RCT",
         note="作者Ghavidel→Fadardi；国家Germany→Iran；联合干预(Exercise→无)；整群随机",
         co_int="无",
         arms=[("实验中心", "n-back训练", "", None),
               ("对照中心(主动)", "", "主动对照", None)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T18 Seq21 ----
    dict(seq=21, author_year="Sun 2018", country="China", design="RCT",
         note="国家USA→China；N→86；联合干预(Exercise/Medication→无)；5组",
         co_int="无",
         arms=[("记忆训练组", "记忆训练(含WM)", "", None),
               ("无训练对照组", "", "无训练", None)],
         comps=[(0, 1, "①", "WM效应", "另有推理×2组不入本比较")],
         audit=("①", "①", "①")),
    # ---- T19 Seq22 ----
    dict(seq=22, author_year="Boutzoukas 2022", country="USA", design="RCT",
         note="子研究(NCT02851511)；多域训练非纯WM；N→87；两臂均配tDCS",
         co_int="tDCS",
         arms=[("多域CT+sham/active tDCS", "多域认知训练(含WM)+tDCS", "", 34),
               ("教育训练+sham/active tDCS", "教育训练+tDCS", "", 32)],
         comps=[(0, 1, "②", "WM增量", "共同X=tDCS(2×2平衡)")],
         audit=("②", "②", "②")),
    # ---- T20 Seq23 ----
    dict(seq=23, author_year="Verty 2024", country="Canada", design="RCT",
         note="联合干预(Exercise/Medication→无)；3组，N=30为合计",
         co_int="无",
         arms=[("WM更新训练组", "WM更新训练", "", None),
               ("主动对照组", "", "主动对照", None)],
         comps=[(0, 1, "①", "WM效应", "抑制训练组不入本比较")],
         audit=("①", "①", "①")),
    # ---- T21 Seq24 ----
    dict(seq=24, author_year="Tagliabue 2022", country="Italy", design="RCT",
         note="⑦排除：干预目标为注意(attentive individuation)非WM",
         co_int="无",
         arms=[("注意训练组", "枚举训练(注意个体化)", "", None),
               ("练习组(vWM重复)", "", "vWM任务重复", None),
               ("被动组", "", "test-retest被动", None)],
         comps=[],
         audit=("排除", "排除", "excluded")),
    # ---- T22 Seq25 ----
    dict(seq=25, author_year="Zinke 2014", country="Germany", design="RCT",
         note="无主动对照(Active ctrl Y→N)；N→80(40/40)",
         co_int="无",
         arms=[("训练组", "WM训练", "", 40),
               ("无接触对照组", "", "无接触对照", 40)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T23 Seq26 ----
    dict(seq=26, author_year="Mičič 2020", country="Slovenia", design="RCT",
         note="联合干预(Medication→无)；Active ctrl Y→N；N=21(10/11)",
         co_int="无",
         arms=[("实验组", "n-back训练", "", 10),
               ("被动对照组", "", "被动对照", 11)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T24 Seq27 ----
    dict(seq=27, author_year="Zając-Lamparska 2024", country="Poland", design="RCT",
         note="联合干预(TMS/Exercise→无)；事后注册；主=实验vs被动",
         co_int="无",
         arms=[("实验组(n-back)", "n-back训练", "", 25),
               ("被动对照组", "", "被动对照", 22),
               ("主动对照(多域)", "", "多域主动对照", 7)],
         comps=[(0, 1, "①", "WM效应", "主比较vs被动；vs主动为次")],
         audit=("①", "①", "①")),
    # ---- T25 Seq29 ----
    dict(seq=29, author_year="Bürki 2014", country="Switzerland", design="quasi-RCT",
         note="脚本曾误称无对照(实有对照)；准RCT；年轻样本人群不符合纳入标准，未计入",
         co_int="无",
         arms=[("WM训练组", "WM训练", "", 22),
               ("内隐学习对照(主动)", "", "内隐序列学习", 20),
               ("无接触对照", "", "无接触", 21)],
         comps=[(0, 1, "①", "WM效应", "主vs内隐；vs无接触为次")],
         audit=("①", "①", "①")),
    # ---- T26 Seq30 ----
    dict(seq=30, author_year="Cantarella 2017", country="Italy", design="RCT",
         note="N=36(18/18)",
         co_int="无",
         arms=[("训练组", "WM训练", "", 18),
               ("主动对照组", "", "问卷/主动对照", 18)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T27 Seq31 ----
    dict(seq=31, author_year="Carretti 2013", country="Italy", design="RCT",
         note="被Seq53(IPD)合并，但Seq53去重后本条独立；20/20；Seq53另含2不在册样本(Borella 2010 N=40/Borella 2017∧ N=36)记备注",
         co_int="无",
         arms=[("训练组", "WM训练", "", 20),
               ("对照组", "", "主动对照", 20)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T28 Seq32 ----
    dict(seq=32, author_year="Heo 2014", country="Korea", design="RCT",
         note="联合干预(TMS→tDCS)；类型③；anodal/sham各20",
         co_int="tDCS",
         arms=[("anodal-tDCS+CACT", "计算机认知训练+anodal tDCS", "", 20),
               ("sham-tDCS+CACT", "计算机认知训练+sham tDCS", "", 20)],
         comps=[(0, 1, "③", "刺激增益", "")],
         audit=("③", "③", "③")),
    # ---- T29 Seq34 ----
    dict(seq=34, author_year="Assecondi 2022", country="USA", design="RCT",
         note="类型③；ACTIVE/SHAM各~30(两年龄组)；N=28待核",
         co_int="tDCS",
         arms=[("ACTIVE tDCS+n-back", "5天n-back+active tDCS", "", None),
               ("SHAM tDCS+n-back", "5天n-back+sham tDCS", "", None)],
         comps=[(0, 1, "③", "刺激增益", "")],
         audit=("③", "③", "③")),
    # ---- T30 Seq35 ----
    dict(seq=35, author_year="Günther 2003", country="Austria", design="single-group",
         note="联合干预(Exercise/Medication→无)；单组19人前后测",
         co_int="无",
         arms=[("单臂训练组", "计算机认知训练", "", 19)],
         comps=[],
         audit=("N", "N", "N")),
    # ---- T31 Seq36 ----
    dict(seq=36, author_year="Shatil 2014", country="Israel", design="RCT",
         note="iTV训练；随机140/分析119",
         co_int="无",
         arms=[("认知训练组(iTV)", "iTV认知训练", "", None),
               ("主动对照(iTV)", "", "iTV主动对照", None)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T32 Seq39 ----
    dict(seq=39, author_year="Buschkuehl 2008", country="Switzerland", design="RCT",
         note="运动是对照组活动非联合干预；分析13/19",
         co_int="运动(仅对照臂)",
         arms=[("实验组", "WM训练", "", 13),
               ("主动对照(体力训练)", "", "体力训练(运动)", 19)],
         comps=[(0, 1, "①", "WM效应", "对照臂为运动(非联合干预)")],
         audit=("①", "①或②", "①")),
    # ---- T33 Seq40 ----
    dict(seq=40, author_year="Booth 2023", country="UK", design="RCT",
         note="联合干预(tDCS→无)；4组(分散/密集×WMT/对照)合并",
         co_int="无",
         arms=[("WMT组(分散+密集合并)", "WM训练", "", None),
               ("主动对照(分散+密集合并)", "", "主动对照", None)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T34 Seq41 ----
    dict(seq=41, author_year="Heinzel 2017", country="USA", design="RCT",
         note="无主动对照(Active ctrl Y→N)；训练组含已发表样本",
         co_int="无",
         arms=[("训练组(n-back)", "n-back训练", "", 18),
               ("无接触对照组", "", "无接触对照", 16)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T35 Seq44 ----
    dict(seq=44, author_year="Sutton 2025", country="UK", design="RCT",
         note="联合干预(Exercise/Medication→无)；多域App非纯WM；N=103",
         co_int="无",
         arms=[("脑训练App组", "自适应认知训练App", "", None),
               ("主动对照组", "", "主动对照", None)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T36 Seq45 ----
    dict(seq=45, author_year="Tusch 2016", country="USA", design="RCT",
         note="Cogmed自适应 vs 非自适应CCT；N=35",
         co_int="无",
         arms=[("自适应CCT组(Cogmed)", "Cogmed自适应WM训练", "", 18),
               ("非自适应CCT组", "", "非自适应CCT(主动对照)", 17)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T37 Seq46 ----
    dict(seq=46, author_year="McAvinue 2013", country="USA", design="RCT",
         note="联合干预(Exercise→无)；19/17",
         co_int="无",
         arms=[("训练组(自适应)", "自适应WM训练", "", 19),
               ("对照组(非自适应)", "", "非自适应WM(主动对照)", 17)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T38 Seq48 ----
    dict(seq=48, author_year="Borella 2025", country="Italy", design="RCT",
         note="15/15；N=30",
         co_int="无",
         arms=[("训练组(TG)", "WM训练", "", 15),
               ("主动对照(ACG)", "", "主动对照", 15)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T39 Seq49 ----
    dict(seq=49, author_year="Goghari 2017", country="Canada", design="quasi-RCT",
         note="国家USA→Canada；Age(90→错)已修；N→97；准随机",
         co_int="无",
         arms=[("WM训练组", "WM训练", "", None),
               ("逻辑规划训练组", "", "逻辑规划(主动对照)", None),
               ("无训练组(被动)", "", "被动对照", None)],
         comps=[(0, 2, "①", "WM效应", "主vs被动；vs逻辑规划为次")],
         audit=("①", "①", "①")),
    # ---- T40 Seq50 ----
    dict(seq=50, author_year="Zinke 2012", country="Germany", design="quasi-RCT",
         note="old-old；N=36",
         co_int="无",
         arms=[("训练组", "WM训练(span)", "", None),
               ("匹配对照组", "", "匹配对照", None)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T41 Seq51 ----
    dict(seq=51, author_year="Basak 2016", country="USA", design="RCT",
         note="⑤S：PT vs UT=W变体互比(无对照组)；联合干预(Exercise/Medication→无)；N=46",
         co_int="无",
         arms=[("可预测更新组(PT)", "可预测记忆更新训练", "", None),
               ("不可预测更新组(UT)", "不可预测记忆更新训练", "", None)],
         comps=[(0, 1, "⑤", "变体", "PT vs UT(W变体互比)")],
         audit=("S", "S", "⑤")),
    # ---- T42 Seq52 ----
    dict(seq=52, author_year="Jaeggi 2023", country="USA", design="RCT",
         note="嵌套主(⊃Seq28)；N=119；EngAge+WM vs WM为次比较(元认知附加)",
         co_int="元认知(仅一臂)",
         arms=[("WM训练组", "WM训练", "", None),
               ("主动对照(KB)", "", "知识训练(KB主动对照)", None)],
         comps=[(0, 1, "①", "WM效应", "主比较；EngAge+WM vs WM为次")],
         audit=("①", "①+W+X vs W", "①")),
    # ---- T43 Seq54 ----
    dict(seq=54, author_year="Brambilla 2021", country="UK", design="RCT",
         note="联合干预(tDCS/Exercise/Medication→tRNS)；三臂0.705/1/sham；N=42",
         co_int="tRNS",
         arms=[("0.705mA tRNS+CT", "认知训练(EF)+0.705mA tRNS", "", 14),
               ("1mA tRNS+CT", "认知训练(EF)+1mA tRNS", "", 14),
               ("sham tRNS+CT", "认知训练(EF)+sham tRNS", "", 19)],
         comps=[(0, 2, "③", "刺激增益", "active tRNS vs sham")],
         audit=("③", "③", "③")),
    # ---- T44 Seq55 ----
    dict(seq=55, author_year="Antonenko 2022", country="Germany", design="RCT",
         note="联合干预(Medication→tDCS)；各28；N=56",
         co_int="tDCS",
         arms=[("atDCS+CT", "认知训练+anodal tDCS", "", 28),
               ("sham+CT", "认知训练+sham tDCS", "", 28)],
         comps=[(0, 1, "③", "刺激增益", "")],
         audit=("③", "③", "③")),
    # ---- T45 Seq57 ----
    dict(seq=57, author_year="Zelinski 2014", country="USA", design="RCT",
         note="联合干预(Medication→无)；IMPACT训练242/教育DVD245；N=487",
         co_int="无",
         arms=[("IMPACT训练组", "多模态认知训练", "", 242),
               ("主动对照(教育DVD)", "", "教育DVD主动对照", 245)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T46 Seq59 ----
    dict(seq=59, author_year="Spironelli 2021", country="USA", design="RCT",
         note="联合干预(Exercise→无)；TG12/ACG12",
         co_int="无",
         arms=[("训练组(TG)", "WM训练", "", 12),
               ("主动对照(ACG)", "", "问卷主动对照", 12)],
         comps=[(0, 1, "①", "WM效应", "")],
         audit=("①", "①", "①")),
    # ---- T47 Seq60 ----
    dict(seq=60, author_year="Nguyen 2026", country="Australia", design="RCT",
         note="联合干预(Exercise/Medication→无)；单域WM/多域EF/对照各22；N=66",
         co_int="无",
         arms=[("单域WM训练组", "单域WM训练", "", 22),
               ("主动对照组", "", "主动对照", 22)],
         comps=[(0, 1, "①", "WM效应", "多域EF组不入本比较")],
         audit=("①", "①", "①")),
    # ---- T48 Seq61-Exp1 ----
    dict(seq="61-E1", author_year="Cantarella 2017 Exp1", country="Italy", design="RCT",
         note="Seq61(Cantarella 2017校样)实验1，独立样本；训练18/对照17，N=35",
         co_int="无",
         arms=[("训练组(Exp1)", "WM训练", "", 18),
               ("对照组(Exp1)", "", "主动对照", 17)],
         comps=[(0, 1, "①", "WM效应", "Experiment 1")],
         audit=("①", "①", "①")),
    # ---- T49 Seq61-Exp2 ----
    dict(seq="61-E2", author_year="Cantarella 2017 Exp2", country="Italy", design="RCT",
         note="Seq61(Cantarella 2017校样)实验2，独立样本；训练16/对照19，N=35",
         co_int="无",
         arms=[("训练组(Exp2)", "WM训练", "", 16),
               ("对照组(Exp2)", "", "主动对照", 19)],
         comps=[(0, 1, "①", "WM效应", "Experiment 2")],
         audit=("①", "①", "①")),
    # ---- T49 Seq62 ----
    dict(seq=62, author_year="Pergher 2020", country="USA", design="RCT",
         note="⑤S：CTG(n-back+策略) vs ACG(自发策略)；联合干预(Medication→无)；N=26(EEG子样本)",
         co_int="无",
         arms=[("策略组(CTG)", "n-back训练+复述策略", "", None),
               ("自发策略组(ACG)", "n-back训练(自发策略)", "", None),
               ("被动对照(PCG)", "", "被动对照", None)],
         comps=[(0, 1, "⑤", "变体", "策略使用互比；ACG亦做n-back")],
         audit=("S", "S/①", "⑤")),
    # ---- T50 Seq63 ----
    dict(seq=63, author_year="Lange 2015", country="Germany", design="RCT",
         note="联合干预(Exercise→无)；EG31/aCG31/pCG29；N=91",
         co_int="无",
         arms=[("实验组(EG)", "WM训练", "", 31),
               ("主动对照(aCG)", "", "测验+桌游", 31),
               ("被动对照(pCG)", "", "被动对照", 29)],
         comps=[(0, 1, "①", "WM效应", "主vs主动；vs被动为次")],
         audit=("①", "①", "①")),
    # ---- T51 Seq67 ----
    dict(seq=67, author_year="Chai 2026", country="Switzerland", design="RCT",
         note="联合干预(tDCS→无)；训练22/主动22/无接触25；N=69(分析68)",
         co_int="无",
         arms=[("训练组(自适应)", "自适应WM训练", "", 22),
               ("主动对照(固定难度)", "", "固定难度主动对照", 22),
               ("无接触对照组", "", "无接触对照", 25)],
         comps=[(0, 1, "①", "WM效应", "主vs主动；vs无接触为次")],
         audit=("①", "①", "①")),
]

# cx 裁定（真 Codex 2026-11-16/17）：Seq53 的 2 个不在册样本拆为独立 trial 记录。
# Borella 2010：2026-11-17 cx 复核原 E1 排除理由错配（"27岁 n-back"），实为 65-75 岁 CWMS，
#   恢复纳入 → 正式 ①、进核心候选池（核心池 40→41）。
# Borella 2017∧：仍 ①-pending（未独立收录，提取状态待核）。
# WOME 2018：cx 复核原 E1"儿童"排除错误（实为健康老人 60-77 岁），撤销排除、恢复资格，
#   待 cc/cl 比较编码（暂 ①-pending，不进核心池）。
EXTERNAL_TRIALS = [
    dict(seq="ext-Borella2010", author_year="Borella 2010", country="Italy", design="RCT",
         note="cx裁定恢复纳入(2026-11-17)：原E1排除理由错配；65-75岁CWMS言语WM训练(3次)，训练20/对照20，N=40，8个月随访；源自Seq53 IPD",
         co_int="无",
         arms=[("训练组(CWMS)", "CWMS言语WM训练(3次)", "", 20),
               ("主动对照(问卷)", "", "自传记忆/生活满意度问卷", 20)],
         comps=[(0, 1, "①", "WM效应", "cx裁定恢复纳入")],
         audit=("①", "①", "①")),
    dict(seq="ext-Borella2017a", author_year="Borella 2017∧", country="Italy", design="RCT",
         note="不在册样本，源自Seq53(Borella 2017 IPD)；未独立收录，尚未完成独立报告提取；提取状态待核；N=36",
         co_int="无", arms=[], comps=[], audit=("①", "①", "①-pending")),
    dict(seq="ext-WOME2018", author_year="Weicker 2018", country="Germany", design="RCT",
         note="cx裁定撤销E1排除(2026-11-17)：原排除误标儿童，实为健康老人60-77岁均龄67.7；高WM/低WM/无接触三组N=60；待cc/cl比较编码",
         co_int="无",
         arms=[("训练组(高/低WM)", "WOME理论WM训练", "", None),
               ("无接触对照", "", "无接触对照", None)],
         comps=[],
         audit=("", "", "①-pending")),
    dict(seq="ext-Zajac2016", author_year="Zając-Lamparska 2016", country="Poland", design="RCT",
         note="cx裁定恢复纳入(2026-11-17)：原E1'37.87岁'系Raven基线分误读；late adulthood组60-85岁各臂30人；WM(n-back)/AC(Donders)/waiting三臂；两①共用WM臂",
         co_int="无",
         arms=[("老年WM组", "n-back WM训练", "", 30),
               ("老年AC组", "Donders反应/注意控制训练", "", 30),
               ("老年waiting组", "", "等待无训练", 30)],
         comps=[(0, 2, "①", "WM效应", "WM vs waiting(被动对照)；与comp2共用WM臂"),
                (0, 1, "①", "WM效应", "WM vs AC(主动对照)；与comp1共用WM臂")],
         audit=("①", "①+①", "①")),
]

# comp_type → est_target（v3 定义；仅用于校验，不据此生成）
COMP_TYPE_EST = {"①": "WM效应", "②": "WM增量", "③": "刺激增益", "④": "组合效果", "⑤": "变体"}

# ──────────────────────────────────────────────────────────────────────────────
# 三、组装
# ──────────────────────────────────────────────────────────────────────────────
# 主报告按 seq 升序排序，赋 trial_id T01..T53（Seq6/Seq61 各拆两子研究）
MAIN_SEQ_ORDER = [t["seq"] for t in TRIALS]
assert len(MAIN_SEQ_ORDER) == 53, f"期望53主报告(Seq6/61各拆两子研究)，实际{len(MAIN_SEQ_ORDER)}"
assert len(set(MAIN_SEQ_ORDER)) == 53, "主报告seq重复"

seq_to_tid = {seq: f"T{i+1:02d}" for i, seq in enumerate(MAIN_SEQ_ORDER)}

# 生成 trial 行（51 主报告 + 2 不在册样本）
def build_trial_row(t, tid):
    # 次要报告：哪些被移除的 seq 映射到本主报告（cx 裁定：可双挂）
    seq = t["seq"]
    if isinstance(seq, int):
        secondaries = sorted([s for s, (ms, _, _) in SECONDARY.items() if seq in ms])
    elif str(seq).startswith("ext-"):
        secondaries = [53]  # 不在册样本：来源链接 Seq53
    else:
        secondaries = []  # 子研究(如 6-S1/6-S2)，无次要报告
    # trial 级 comp_type 摘要（v3 人工核准）：
    #   有比较 → 各比较类型去重拼接；无比较 → N/excluded/①-pending
    ctypes = [c[2] for c in t["comps"]]
    if not ctypes:
        t_comp = {"N": "N", "excluded": "excluded", "①-pending": "①-pending"}.get(t["audit"][2], "无")
    else:
        t_comp = "+".join(dict.fromkeys(ctypes))
    return dict(
        trial_id=tid,
        main_report_seq=t["seq"],
        secondary_report_seq=",".join(str(s) for s in secondaries) if secondaries else "",
        author_year=t["author_year"],
        design=t["design"],
        country=t["country"],
        comp_type=t_comp,
        note=t["note"],
        co_intervention_v3=t["co_int"],  # 辅助列(v3人工核准，非脚本判断)
    )

trial_rows = []
for t in TRIALS:
    trial_rows.append(build_trial_row(t, seq_to_tid[t["seq"]]))
for i, t in enumerate(EXTERNAL_TRIALS):
    trial_rows.append(build_trial_row(t, f"T{53+i+1:02d}"))  # T54, T55

# 5 条去重/嵌套记录（dedup 表）
dedup_rows = []
for s in sorted(SECONDARY.keys()):
    mains, st, reason = SECONDARY[s]
    dedup_rows.append(dict(seq=s, maps_to_main_seq=",".join(str(m) for m in mains),
                           exclusion_status=st, exclusion_reason=reason))

# 报告↔trial 关系表（cx 阶段1要求：报告—试验映射、拆分/合并、多对多显式化）
report_trial_rows = []
# 主报告边（含一篇多试验拆分：Seq6→2、Seq61→2）
for t in TRIALS:
    tid = seq_to_tid[t["seq"]]
    role_note = ""
    if t["seq"] in ("6-S1", "6-S2"):
        role_note = "Seq6(Brum 2020)拆两子研究"
    elif t["seq"] in ("61-E1", "61-E2"):
        role_note = "Seq61(Cantarella 2017)拆两实验"
    report_trial_rows.append(dict(report_key=str(t["seq"]), report_role="main",
                                  trial_id=tid, note=role_note))
# 次要报告边（重复/嵌套/合并报告 → 其主 trial）
for s, (ms, st, reason) in SECONDARY.items():
    for m in ms:
        report_trial_rows.append(dict(report_key=str(s), report_role="secondary",
                                      trial_id=seq_to_tid[m], note=f"{st}: {reason[:60]}"))
# 恢复/不在册报告边（含 Seq53 对 T54/T55 的合并关系）
for i, t in enumerate(EXTERNAL_TRIALS):
    tid = f"T{53+i+1:02d}"
    if t["seq"] == "ext-Borella2010" or t["seq"] == "ext-Borella2017a":
        report_trial_rows.append(dict(report_key="53", report_role="secondary",
                                      trial_id=tid, note="Seq53 IPD 合并样本构成试验"))
    report_trial_rows.append(dict(report_key=str(t["seq"]), report_role="restored",
                                  trial_id=tid, note=t["note"][:60]))

# 生成 arm 行 + comparison 行（主报告 + 外部/恢复 trial）
arm_rows = []
comp_rows = []
all_trials = [(t, seq_to_tid[t["seq"]]) for t in TRIALS] + \
             [(t, f"T{53+i+1:02d}") for i, t in enumerate(EXTERNAL_TRIALS)]
for t, tid in all_trials:
    arm_ids = []
    for i, (label, interv, ctrl, n) in enumerate(t["arms"], 1):
        aid = f"A{tid}_{i}"
        arm_ids.append(aid)
        arm_rows.append(dict(
            arm_id=aid, trial_id=tid, arm_label=label,
            intervention_components=interv, control_components=ctrl, n=n))
    for j, (a_idx, b_idx, ctype, est, note) in enumerate(t["comps"], 1):
        cid = f"C{tid}_{j}"
        arm_a = arm_ids[a_idx] if 0 <= a_idx < len(arm_ids) else ""
        arm_b = arm_ids[b_idx] if 0 <= b_idx < len(arm_ids) else ""
        in_core = (ctype in ("①", "②"))
        comp_rows.append(dict(
            comparison_id=cid, trial_id=tid, arm_a=arm_a, arm_b=arm_b,
            comp_type=ctype, est_target=est, in_core_ma=in_core, note=note,
            cc_code=t["audit"][0], cl_code=t["audit"][1], cx_final=t["audit"][2],
            exclusion_status="included", exclusion_reason=""))

# 为 5 条去重/嵌套 + Seq24/Seq1/Seq35 补 exclusion_status（附在 trial 层）
# trial 层增加 audit 列
for tr in trial_rows:
    tr["exclusion_status"] = "included"
    tr["exclusion_reason"] = ""
for s, (main, st, reason) in SECONDARY.items():
    # 在主报告的 secondary_report_seq 已挂；这里不再单独建 trial 行
    pass

# 对 N(单组) / excluded / 不在册样本 的 trial，标记 exclusion_status（用于断言）
for tr in trial_rows:
    tid = tr["trial_id"]
    if tr["main_report_seq"] in (1, 35):
        tr["exclusion_status"] = "included"  # N 保留在证据流，但无比较
        tr["exclusion_reason"] = "单组无组间比较(comp_type=N)"
    if tr["main_report_seq"] == 24:
        tr["exclusion_status"] = "excluded"
        tr["exclusion_reason"] = "干预目标非WM(注意训练)"
    if isinstance(tr["main_report_seq"], str) and tr["main_report_seq"].startswith("ext-"):
        tr["exclusion_status"] = "included"  # 保留在证据流，但无可单独提取效应量
        tr["exclusion_reason"] = "不在册样本，当前无可单独提取效应量，不生成核心比较"

# ──────────────────────────────────────────────────────────────────────────────
# 四、写 Excel
# ──────────────────────────────────────────────────────────────────────────────
wb = openpyxl.Workbook()

def write_sheet(name, headers, rows):
    ws = wb.create_sheet(name)
    ws.append(headers)
    for r in rows:
        ws.append([r.get(h, "") for h in headers])
    # 简单格式化
    for c in range(1, len(headers) + 1):
        ws.cell(1, c).font = Font(bold=True)
    ws.freeze_panes = "A2"
    return ws

# 1. 说明
ws0 = wb.active
ws0.title = "README"
readme = [
    ["Paper-01 比较层新表（v1，待 cx 审计）"],
    ["粒度", "trial → arm → comparison → outcome → timepoint"],
    ["生成", "脚本_13_比较层新表生成.py；数据源=v3终表(cx仲裁)+臂比较原文提取.txt"],
    ["硬性规则", "comp_type/联合干预/est_target 均为 v3 人工核准，脚本不自动判断"],
    ["旧表", "数据_6_数据提取表_v3_research.xlsx 保留为历史档，未改写"],
    ["ID约定", "trial_id=T01..T51；arm_id=A{trial_id}_{序号}；comparison_id=C{trial_id}_{序号}；outcome_id=O{comparison_id}_{序号}"],
    ["", ""],
    ["表清单", "trial / dedup / arm / comparison / outcome / timepoint"],
    ["注意", "outcome 与 timepoint 为冻结 schema 脚手架，v3 无结局级数据，暂空"],
]
for row in readme:
    ws0.append(row)
ws0.column_dimensions['A'].width = 20
ws0.column_dimensions['B'].width = 100

# 2. trial
write_sheet("trial",
    ["trial_id", "main_report_seq", "secondary_report_seq", "author_year",
     "design", "country", "comp_type", "note", "co_intervention_v3",
     "exclusion_status", "exclusion_reason"],
    trial_rows)

# 2b. dedup（5 条去重/嵌套映射）
write_sheet("dedup",
    ["seq", "maps_to_main_seq", "exclusion_status", "exclusion_reason"],
    dedup_rows)

# 2c. report_trial（报告↔trial 多对多关系，cx 阶段1）
write_sheet("report_trial",
    ["report_key", "report_role", "trial_id", "note"],
    report_trial_rows)

# 3. arm
write_sheet("arm",
    ["arm_id", "trial_id", "arm_label", "intervention_components",
     "control_components", "n"],
    arm_rows)

# 4. comparison
write_sheet("comparison",
    ["comparison_id", "trial_id", "arm_a", "arm_b", "comp_type", "est_target",
     "in_core_ma", "note", "cc_code", "cl_code", "cx_final",
     "exclusion_status", "exclusion_reason"],
    comp_rows)

# 5. outcome（脚手架，空；cx 裁定：domain 去 followup，加 result_ids 指针，effect_size_available 只读自动生成）
write_sheet("outcome",
    ["outcome_id", "comparison_id", "domain", "measure", "timepoint", "result_ids",
     "effect_size_available"],
    [])

# 6. timepoint（脚手架，空）
write_sheet("timepoint",
    ["timepoint_id", "label", "timing"],
    [])

wb.save(OUT)

# ──────────────────────────────────────────────────────────────────────────────
# 五、控制台摘要
# ──────────────────────────────────────────────────────────────────────────────
n_core = sum(1 for c in comp_rows if c["in_core_ma"])
print("=" * 60)
print("比较层新表已生成：", OUT)
print(f"trial 行数      : {len(trial_rows)}  (期望57=53主报告[Seq6/61拆2]+4不在册/恢复)")
print(f"dedup 行数      : {len(dedup_rows)}  (期望5)")
print(f"arm 行数        : {len(arm_rows)}")
print(f"comparison 行数 : {len(comp_rows)}")
print(f"  in_core_ma=True: {n_core}")
from collections import Counter
print("comp_type 分布  :", dict(Counter(c['comp_type'] for c in comp_rows)))
print("=" * 60)
