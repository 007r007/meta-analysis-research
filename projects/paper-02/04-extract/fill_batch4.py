import openpyxl, subprocess, re, glob

PDF_DIR = "/root/.openclaw/workspace/research/papers/projects/paper-02/03-screen/全文PDF"

wb = openpyxl.load_workbook('数据_7_数据提取表_v1.xlsx')
ws = wb.active

col_map = {
    'A1':1,'A2':2,'A3':3,'A4':4,'A5':5,'A6':6,'A7':7,'A8':8,'A9':9,
    'B1':10,'B2':11,'B3':12,'B4':13,'B5':14,
    'C1':15,'C2':16,'C3':17,'C4':18,'C5':19,'C6':20,'C7':21,
    'D1':22,'D2':23,'D3':24,'D3b':25,'D4':26,'D5':27,'D6':28,
    'E1':29,'E2':30,'E3':31,
    'F1':32,'F2':33,'F3':34,
    'G1':36,'G2':37
}

data = [
    # ---------- #43 Ozernov-Palchik 2019 ----------
    dict(row=13, A1=43, A2='Ozernov-Palchik', A3=2019, A4='USA', A5='横断',
         A6=125, A7='5–8 years (kindergarten & 2nd grade)', A8=1, A9='early-school(6-8y)',
         B1='母亲/父亲受教育年数（连续变量）', B2='单独报告', B3='连续变量', B4='r',
         B5='家庭收入',
         C1='DTI', C2='白质微结构（FA, MD）', C3='结构',
         C4='Pearson相关+回归', C5='全脑白质束（包括弓状束、胼胝体）',
         C6='否', C7='未命名队列（Boston, USA）',
         D1='显著正相关',
         D2='母亲教育与多条白质束FA显著正相关，同时与阅读技能正相关（r值0.19–0.33，p<.05）',
         D3='maternal education × phonological awareness r=0.33, p<.001; maternal education × FA various tracts p<.05',
         D3b='positive', D4='Pearson相关（控制性别）', D5='儿童性别、年龄',
         D6='白质FA部分中介教育与阅读成绩关联',
         E1='认知刺激', E2='中介分析', E3='部分中介',
         F1=3, F2=2, F3=2,
         G1='主要是education与阅读技能的关联，DTI是中间变量；FA中介路径更完整；paternal education无显著效应，仅maternal education显著',
         G2='oo'),

    # ---------- #64 Troller-Renfree 2022 ----------
    dict(row=14, A1=64, A2='Troller-Renfree', A3=2022, A4='USA', A5='纵向',
         A6=38, A7='出生→2岁（birth→8.6 months扫描）', A8=2, A9='infant(1-12m)',
         B1='母亲受教育年数（连续变量）', B2='单独报告', B3='连续变量', B4='r',
         B5='无其他SES指标单独报告',
         C1='DTI', C2='白质FA（fractional anisotropy）', C3='结构',
         C4='Spearman相关+偏相关', C5='全脑白质束',
         C6='否', C7='未命名队列（Baby Connectome Project子集）',
         D1='显著正相关',
         D2='母亲教育年数与婴儿期白质FA显著正相关（r=0.48, p<.05），且家庭读写环境（StimQ-Reading）中介该关联',
         D3='r=0.48, p<.05',
         D3b='positive', D4='Spearman相关（偏相关控制月龄）', D5='婴儿月龄',
         D6='StimQ-Reading中介教育→白质FA关联',
         E1='语言输入', E2='中介分析', E3='部分中介',
         F1=3, F2=2, F3=2,
         G1='N=38，样本量较小；家庭读写环境（StimQ-Reading）作为中介变量；双语/多文化样本',
         G2='oo'),

    # ---------- #72 Tomalski 2019 ----------
    dict(row=15, A1=72, A2='Tomalski', A3=2019, A4='USA', A5='横断',
         A6=91, A7='6–24 months', A8=1, A9='infant(1-12m)',
         B1='母亲受教育年数（连续变量）', B2='单独报告', B3='连续变量', B4='r',
         B5='家庭词汇环境、CHAOS量表',
         C1='rsEEG', C2='静息态EEG功率（theta频段）', C3='静息态',
         C4='多元线性回归', C5='全脑（Fz, Cz, Pz等）',
         C6='否', C7='未命名队列（New York, USA）',
         D1='显著正相关',
         D2='母亲教育显著预测婴儿theta EEG功率（F(9,79)=4.22, p<.001），且与词汇量显著相关（r=0.48, p<.001）',
         D3='F(9,79)=4.22, p<.001; r(maternal education × vocabulary)=0.48, p<.001',
         D3b='positive', D4='多元线性回归', D5='儿童年龄、家庭环境（CHAOS）、家庭收入',
         D6='未检验正式中介',
         E1='语言输入', E2='未检验', E3='未检验',
         F1=3, F2=2, F3=2,
         G1='rsEEG与词汇量双重分析；母亲教育、词汇量、家庭环境共同进入回归；theta功率反映成熟度',
         G2='oo'),

    # ---------- #75 Shephard 2019 ----------
    dict(row=16, A1=75, A2='Shephard', A3=2019, A4='UK', A5='横断',
         A6=50, A7='6–12 months', A8=1, A9='infant(1-12m)',
         B1='母亲受教育水平（连续变量）', B2='单独报告', B3='连续变量', B4='beta',
         B5='无其他SES单独报告',
         C1='fMRI', C2='静息态脑网络连接强度（rs-fMRI ICA网络）', C3='静息态',
         C4='ICA+回归分析', C5='默认模式网络、感觉运动网络等',
         C6='否', C7='未命名队列（UK）',
         D1='显著负相关',
         D2='低母亲教育与更弱的默认模式网络连接显著相关（p=0.01），该关联在控制母亲/婴儿年龄和SES后仍显著（p<.02）',
         D3='p=0.01（网络连接×母亲教育）；控制SES后p<.02',
         D3b='negative', D4='ICA回归分析', D5='母亲年龄、婴儿年龄、总体SES',
         D6='未检验中介',
         E1='慢性应激', E2='未检验', E3='未检验',
         F1=3, F2=2, F3=2,
         G1='以低教育关联更弱连接报告（负向关联）；SES控制后效应保持；母亲焦虑和教育水平共同分析',
         G2='oo'),

    # ---------- #78 Conejero 2018 ----------
    dict(row=17, A1=78, A2='Conejero', A3=2018, A4='Spain', A5='横断',
         A6=56, A7='12–30 months（toddler）', A8=1, A9='toddler(1-3y)',
         B1='父母教育水平（连续变量）', B2='单独报告', B3='连续变量', B4='beta',
         B5='家庭收入',
         C1='ERP', C2='ERN振幅+错误后theta功率', C3='任务态-go-nogo',
         C4='简单线性回归', C5='前额区（Fz, FCz）',
         C6='否', C7='未命名队列（Granada, Spain）',
         D1='显著正相关',
         D2='父母教育水平显著预测幼儿ERN振幅和错误后theta功率增强（p<.05），教育越高误差监控神经指标越强',
         D3='parental education significantly predicted ERN amplitude and error-related theta, p<.05',
         D3b='positive', D4='简单线性回归', D5='儿童年龄、性别',
         D6='未检验中介',
         E1='认知刺激', E2='未检验', E3='未检验',
         F1=3, F2=2, F3=2,
         G1='错误监控（ERN）研究；幼儿样本；父母教育作为单一预测变量进入回归；家庭SES（含收入）同时分析',
         G2='oo'),

    # ---------- #79 Ding 2021 ----------
    dict(row=18, A1=79, A2='Ding', A3=2021, A4='China', A5='横断',
         A6=86, A7='12–24 months（toddler）', A8=1, A9='toddler(1-3y)',
         B1='父母教育水平（连续变量）', B2='单独报告', B3='连续变量', B4='beta',
         B5='家庭收入、家庭教养环境（HRE）',
         C1='fNIRS', C2='前额叶激活（oxyHb）', C3='任务态-social',
         C4='GLM回归', C5='前额叶（PFC）',
         C6='否', C7='未命名队列（中国）',
         D1='显著正相关',
         D2='高父母教育水平与幼儿联合注意任务中更强的前额叶fNIRS激活相关（p<.05）',
         D3='Higher parental education level associated with prefrontal activation, p<.05',
         D3b='positive', D4='GLM回归', D5='儿童年龄、性别、家庭收入、家庭教养环境',
         D6='未检验中介',
         E1='认知刺激', E2='未检验', E3='未检验',
         F1=3, F2=2, F3=2,
         G1='fNIRS联合注意任务；中国样本；父母教育与HRE共同进入回归模型',
         G2='oo'),

    # ---------- #104 Ursache 2016 ----------
    dict(row=19, A1=104, A2='Ursache', A3=2016, A4='USA', A5='横断',
         A6=107, A7='3–21 years（重点6–9岁）', A8=1, A9='early-school(6-8y)',
         B1='父母受教育年数（连续变量）', B2='单独报告', B3='连续变量', B4='r',
         B5='家庭收入（income-to-needs）',
         C1='DTI', C2='白质FA（fractional anisotropy）', C3='结构',
         C4='多元线性回归', C5='全脑白质束（corpus callosum等）',
         C6='否', C7='未命名队列（New York, USA）',
         D1='显著正相关',
         D2='父母教育水平与更高的白质FA显著正相关，且与更好的执行功能相关（p=.001）',
         D3='parental education × WM FA: p=.001; parental education × EF scores: p<.05; r(income, education)=.546',
         D3b='positive', D4='多元线性回归', D5='儿童年龄、性别、家庭收入',
         D6='白质FA中介教育对执行功能的影响（未正式检验）',
         E1='认知刺激', E2='未检验', E3='未检验',
         F1=3, F2=2, F3=3,
         G1='收入与教育高度相关r=.546；两变量同时进入回归；教育效应在控制收入后仍显著',
         G2='oo'),

    # ---------- #109 Lange 2010 ----------
    dict(row=20, A1=109, A2='Lange', A3=2010, A4='UK', A5='横断',
         A6=309, A7='4–18 years', A8=1, A9='early-school(6-8y)',
         B1='父母最高学历（有序多分类：高中至研究生）', B2='单独报告', B3='多分类', B4='group-comparison',
         B5='家庭调整收入（AFI）',
         C1='sMRI', C2='IQ（VIQ/PIQ/FSIQ）及脑体积（TBV/lobar GM/WM）', C3='结构',
         C4='多元线性回归（AIC模型选择）', C5='全脑及额颞顶枕叶',
         C6='否', C7='MRI normative sample（UK）',
         D1='显著正相关',
         D2='父母教育水平与VIQ显著正相关，父母大学毕业比高中毕业VIQ高14–15分（p<.00001）；PIQ增加8–10分（p=.004）',
         D3='VIQ: +14–15 pts if parents college grad, p<.00001; PIQ: +8–10 pts, p=.004; FSIQ p<.05',
         D3b='positive', D4='多元线性回归（AIC选择）+分组比较', D5='儿童年龄、性别、家庭调整收入',
         D6='父母教育对IQ的影响不经由脑体积中介',
         E1='认知刺激', E2='中介分析', E3='不显著（教育→IQ不通过脑体积）',
         F1=3, F2=2, F3=2,
         G1='结局变量是IQ而非直接脑结构；脑体积是协变量；年龄跨度大（4-18岁）；收入与教育分开报告均有独立效应',
         G2='oo'),
]

for entry in data:
    r = entry['row']
    for field, col in col_map.items():
        if field in entry:
            ws.cell(r, col).value = entry[field]

wb.save('数据_7_数据提取表_v1.xlsx')
print(f"最后8篇数据已写入提取表 rows 13-20")
