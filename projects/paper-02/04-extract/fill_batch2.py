import openpyxl, subprocess, re

PDF_DIR = "/root/.openclaw/workspace/research/papers/projects/paper-02/03-screen/全文PDF"

def readpdf(fname):
    result = subprocess.run(['pdftotext', f'{PDF_DIR}/{fname}', '-'], capture_output=True)
    return result.stdout.decode('utf-8', errors='replace')

wb = openpyxl.load_workbook('数据_7_数据提取表_v1.xlsx')
ws = wb.active

data = [
    # ---------- #19 Zhu 2023 ----------
    dict(
        row=9, A1=19, A2='Zhu', A3=2023, A4='USA/UK/Norway', A5='纵向',
        A6=373, A7='出生至8岁（多时间点）', A8=4, A9='early-school(6-8y)',
        B1='母亲受教育年数（连续变量）', B2='单独报告', B3='连续变量', B4='beta',
        B5='家庭收入',
        C1='sMRI', C2='皮质及皮质下脑区体积轨迹', C3='结构',
        C4='线性混合模型（LMM）', C5='全脑多分区（frontal, temporal, parietal等）',
        C6='否', C7='ABIDE/CALM/PING多队列合并',
        D1='显著正相关',
        D2='母亲教育年数与儿童早期脑体积增长轨迹正相关，高母亲教育与更陡的额颞叶体积增长相关（p<.05）',
        D3='p<.05（LMM，具体β值需原文Table查阅）',
        D3b='positive', D4='LMM', D5='儿童年龄、性别、家庭收入', D6='未检验',
        E1='未检验', E2='未检验', E3='未检验',
        F1=3, F2=2, F3=2,
        G1='统计方法为轨迹模型，收入与教育均作为预测变量单独进入模型；具体β系数分散于图中，不便提取单一数值',
        G2='oo'
    ),
    # ---------- #20 Konrad 2024 ----------
    dict(
        row=10, A1=20, A2='Konrad', A3=2024, A4='Canada/Germany', A5='横断',
        A6=105, A7='足月矫正龄（PMA中位数 41.1周）', A8=1, A9='neonatal(0-1m)',
        B1='母亲受教育年数（连续变量）', B2='单独报告', B3='连续变量', B4='beta',
        B5='无其他SES指标',
        C1='sMRI', C2='前后海马体积', C3='结构',
        C4='多元线性回归（分层回归）', C5='海马（anterior/posterior hippocampus）',
        C6='否', C7='多伦多早产儿队列',
        D1='显著正相关',
        D2='母亲教育年数正向预测新生儿前海马体积，并调节早产儿海马发育与2岁认知分数的关系（高教育组效应显著，低教育组不显著）',
        D3='maternal education predicts anterior hippocampal volume, p<.05; interaction maternal education × hippocampus on cognition significant',
        D3b='positive', D4='多元线性回归+交互项检验', D5='胎龄、性别、脑损伤', D6='母亲教育调节海马与认知的关系',
        E1='认知刺激', E2='调节分析', E3='显著调节',
        F1=3, F2=2, F3=2,
        G1='纯早产儿样本（<33周）；SES主要由母亲教育操作化；D3b为positive（教育越高海马越大，且仅在高教育组中海马预测认知）',
        G2='oo'
    ),
    # ---------- #23 Demir-Lira 2021 ----------
    dict(
        row=11, A1=23, A2='Demir-Lira', A3=2021, A4='USA', A5='横断',
        A6=42, A7='6–13 years（M约9岁）', A8=1, A9='early-school(6-8y)',
        B1='父母教育水平（连续变量，年数）', B2='单独报告', B3='连续变量', B4='beta',
        B5='无其他SES指标单独报告',
        C1='fMRI', C2='左侧IFG激活（inferior frontal gyrus, lateral PFC）', C3='任务态-other',
        C4='GLM（whole-brain + ROI）', C5='左侧IFG（L inferior frontal gyrus）',
        C6='否', C7='未命名队列（Chicago, USA）',
        D1='显著正相关',
        D2='高父母教育与演绎推理任务中左侧IFG激活增强相关（p<.05），且父母教育与任务成绩正相关',
        D3='parent education vs L IFG activation p<.05; parent education vs task score r=significant',
        D3b='positive', D4='GLM regression', D5='年龄、性别、scanner motion、WASI分数', D6='未检验',
        E1='未检验', E2='未检验', E3='未检验',
        F1=3, F2=2, F3=2,
        G1='样本年龄跨度大（6–13岁）；提取fMRI任务态激活与教育的关联；父母教育与WASI显著相关（r报告中有具体值，约0.4-0.5）',
        G2='oo'
    ),
    # ---------- #28 Ramphal 2020 ----------
    dict(
        row=12, A1=28, A2='Ramphal', A3=2020, A4='USA', A5='纵向',
        A6=112, A7='出生（neonatal）→ 2岁随访', A8=2, A9='neonatal(0-1m)',
        B1='母亲是否完成高中教育（二分变量）', B2='单独报告', B3='二分', B4='group-comparison',
        B5='家庭贫困（poverty）、收入',
        C1='fMRI', C2='皮质纹状体静息态功能连接（corticostriatal rs-fMRI connectivity）', C3='静息态',
        C4='种子点功能连接（seed-based connectivity，GLM）', C5='纹状体（caudate/putamen）→ mPFC',
        C6='否', C7='未命名纵向队列（New York, USA）',
        D1='显著正相关',
        D2='母亲高中毕业（vs未毕业）与新生儿更强的皮质纹状体功能连接正相关，且该连接预测2岁时更少的外化行为问题',
        D3='maternal HS graduation predicts corticostriatal connectivity, p<.05',
        D3b='positive', D4='多元线性回归（控制共变量）', D5='胎龄、分娩方式、儿童性别、家庭收入/贫困', D6='皮质纹状体连接部分中介教育对2岁外化症状影响',
        E1='慢性应激', E2='中介分析', E3='部分中介',
        F1=3, F2=2, F3=3,
        G1='暴露为母亲是否高中毕业（二分），不是年数；贫困/收入同时控制；中介路径：教育→脑连接→2岁外化症状',
        G2='oo'
    ),
]

col_map = {
    'A1':1,'A2':2,'A3':3,'A4':4,'A5':5,'A6':6,'A7':7,'A8':8,'A9':9,
    'B1':10,'B2':11,'B3':12,'B4':13,'B5':14,
    'C1':15,'C2':16,'C3':17,'C4':18,'C5':19,'C6':20,'C7':21,
    'D1':22,'D2':23,'D3':24,'D3b':25,'D4':26,'D5':27,'D6':28,
    'E1':29,'E2':30,'E3':31,
    'F1':32,'F2':33,'F3':34,
    'G1':36,'G2':37
}

for entry in data:
    r = entry['row']
    for field, col in col_map.items():
        if field in entry:
            ws.cell(r, col).value = entry[field]

wb.save('数据_7_数据提取表_v1.xlsx')
print("第2批（4篇）数据已写入提取表 rows 9–12")
