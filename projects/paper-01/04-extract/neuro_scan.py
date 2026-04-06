import fitz, sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

PDF_DIR = r'E:\Meta-analysis writing project\projects\paper-01\03-screen\全文PDF'

PDF_MAP = {
    1: '2020_The effect of cognitive training in older adults_ be aware of CRUNCH..pdf',
    2: '2019_Is working memory training in older adults sensitive to music_.pdf',
    3: '2016_Age-specific differences of dual n-back training..pdf',
    4: '2015_Longitudinal neurostimulation in older adults improves working memory..pdf',
    5: '2018_N-back training and transfer effects revealed by behavioral responses and EEG..pdf',
    6: '2020_Verbal working memory training in older adults_ an investigation of dose respons.pdf',
    8: '2025_Gamified working memory intervention enhances prefrontal neurocognitive plastici.pdf',
    9: '2017_Working memory training in older adults_ Bayesian evidence supporting the absenc.pdf',
    10: '2022_Working Memory Training Coupled With Transcranial Direct Current Stimulation in.pdf',
    11: '2016_Working Memory Training and Speech in Noise Comprehension in Older Adults..pdf',
    12: '2016_Older Adults Improve on Everyday Tasks after Working Memory Training and Neurost.pdf',
    13: '2019_Working Memory Capacity as a Predictor of Cognitive Training Efficacy in the Eld.pdf',
    14: '2021_Cognitive Aftereffects of Acute tDCS Coupled with Cognitive Training_ An fMRI St.pdf',
    15: '2019_Improving Everyday Functioning in the Old-Old with Working Memory Training..pdf',
    16: '2020_Working Memory Training for Older Participants_ A Control Group Training Regimen.pdf',
    18: '2014_Working memory training improvements and gains in non-trained cognitive tasks in.pdf',
    19: '2013_Working memory training in old age_ an examination of transfer and maintenance e.pdf',
    20: '2020_Feasibility of using a computer-assisted working memory training program for hea.pdf',
    21: '2018_The Effects of Cognitive Training on Cognitive Abilities and Everyday Function_.pdf',
    22: '2022_Higher white matter hyperintensity load adversely affects pre-post proximal cogn.pdf',
    23: '2024_Youth-like brain activation linked with greater cognitive training gains in olde.pdf',
    24: '2022_Training attentive individuation leads to visuo-spatial working memory improveme.pdf',
    25: '2014_Working memory training and transfer in older adults_ effects of age, baseline p.pdf',
    26: '2020_The Impact of Working Memory Training on Cognitive Abilities in Older Adults_ Th.pdf',
    27: '2024_Limited training and transfer effects in older and young adults who participated.pdf',
    28: '2020_Investigating the Effects of Spacing on Working Memory Training Outcome_ A Rando.pdf',
    29: '2014_Individual differences in cognitive plasticity_ an investigation of training cur.pdf',
    30: '2017_Benefits in tasks related to everyday life competences after a working memory tr.pdf',
    31: '2013_Gains in language comprehension relating to working memory training in healthy o.pdf',
    32: '2014_Long-term effects of transcranial direct current stimulation combined with compu.pdf',
    34: '2022_Older adults with lower working memory capacity benefit from transcranial direct.pdf',
    35: '2003_Long-term improvements in cognitive performance through computer-assisted cognit.pdf',
    36: '2014_Novel television-based cognitive training improves working memory and executive.pdf',
    39: '2008_Impact of working memory training on memory performance in old-old adults..pdf',
    40: '2023_Experimental investigation of training schedule on home-based working memory tra.pdf',
    41: '2017_Transfer Effects to a Multimodal Dual-Task after Working Memory Training and Ass.pdf',
    43: '2017_Task demands, tDCS intensity, and the COMT val(158)met polymorphism impact tDCS-.pdf',
    44: '2025_Practice makes perfect, but to what end_ Computerised brain training has limited.pdf',
    45: '2016_Changes in Neural Activity Underlying Working Memory after Computerized Cognitiv.pdf',
    46: '2013_An evaluation of a working memory training scheme in older adults..pdf',
    47: '2018_Self-Perceived Benefits of Cognitive Training in Healthy Older Adults..pdf',
    48: '2025_Short- and long-term cognitive and electrophysiological effects of a brief worki.pdf',
    49: '2017_Comparison of Cognitive Change after Working Memory Training and Logic and Plann.pdf',
    50: '2012_Potentials and limits of plasticity induced by working memory training in old-ol.pdf',
    51: '2016_To Switch or Not to Switch_ Role of Cognitive Control in Working Memory Training.pdf',
    52: '2023_EngAge - A metacognitive intervention to supplement working memory training_ A f.pdf',
    53: '2017_Working Memory Training for Healthy Older Adults_ The Role of Individual Charact.pdf',
    54: '2021_The Effect of Transcranial Random Noise Stimulation on Cognitive Training Outcom.pdf',
    55: '2022_Randomized trial of cognitive training and brain stimulation in non-demented old.pdf',
    57: '2014_Evaluating the relationship between change in performance on training tasks and.pdf',
    59: '2021_Working Memory Training and Cortical Arousal in Healthy Older Adults_ A Resting-.pdf',
    60: '2026_A comparison of single-domain and multidomain executive functions cognitive trai.pdf',
    61: '2021_The influence of training task stimuli on transfer effects of working memory tra.pdf',
    62: '2020_Impact of strategy use during N-Back training in older adults.pdf',
    63: '2015_Experimental evaluation of near\u200b and far-transfer effects of an adaptive multico.pdf',
    67: '2026_The Impact of Working Memory Training on Cognitive Reappraisal Ability Among Old.pdf',
}

NEURO_PATTERNS = [
    r'EEG\s+(?:data\s+)?(?:was|were)\s+(?:recorded|collected|acquired)',
    r'resting.state\s+EEG',
    r'\d+-channel\s+EEG',
    r'electrodes?\s+(?:were\s+)?placed\s+(?:on|at|over)',
    r'ERP\s+(?:components?|data|analysis)',
    r'event.related\s+potential',
    r'fMRI\s+(?:data\s+)?(?:was|were)\s+(?:collected|acquired)',
    r'fMRI\s+scan(?:ning|ner)?',
    r'underwent\s+(?:an?\s+)?(?:fMRI|MRI|EEG)\s+scan',
    r'MRI\s+(?:data\s+)?(?:was|were)\s+(?:acquired|collected)',
    r'BOLD\s+(?:signal|response|activation)',
    r'neuroimaging\s+(?:data|session|protocol)',
    r'MRI\s+scanner',
    r'structural\s+MRI',
    r'resting.state\s+fMRI',
    r'functional\s+MRI',
    r'functional\s+connectivity',
    r'cortical\s+thickness',
    r'brain\s+(?:activity|activation)\s+(?:was|were)\s+(?:measured|assessed|recorded)',
    r'electrophysiological\s+(?:data|measure|recording)',
]

print('Scanning all 56 PDFs for neuroimaging indicators...')
print()
neuro_seqs = []
for seq in sorted(PDF_MAP.keys()):
    fname = PDF_MAP[seq]
    path = os.path.join(PDF_DIR, fname)
    if not os.path.exists(path):
        print(f'seq{seq:2d}: PDF NOT FOUND')
        continue
    doc = fitz.open(path)
    text = ''
    for page in doc:
        text += page.get_text()
    doc.close()

    found_pat = None
    found_ctx = ''
    for pat in NEURO_PATTERNS:
        m = re.search(pat, text, re.I)
        if m:
            found_pat = pat
            found_ctx = text[max(0, m.start()-30):m.start()+100]
            break

    if found_pat:
        neuro_seqs.append(seq)
        print(f'seq{seq:2d}: NEURO=YES  [{found_pat[:50]}]')
        print(f'       context: {repr(found_ctx[:80])}')
    else:
        print(f'seq{seq:2d}: NEURO=no')

print()
print('Neuroimaging seqs:', neuro_seqs)
