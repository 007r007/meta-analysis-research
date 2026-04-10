# 给 CC 的 Word 文档生成提示词
> 撰写人：oo | 日期：2026-04-10
> 目的：请 CC 生成 Paper-02 可直接投稿的 Word 文档（.docx）

---

## 一、任务概述

请生成一个 Python 脚本 `generate_docx.py`，运行后输出 `paper02_final.docx`，该文档须符合 *Developmental Cognitive Neuroscience*（DCN）投稿格式要求，可直接用于投稿。

**参考脚本：** `projects/paper-01/06-write/generate_docx.py`（paper-01 已有完整实现，直接参考其结构和工具函数，不要从零写）

**输入文件（均在 `projects/paper-02/06-write/` 下）：**
```
文档_2_paper02_draft_v1.md          ← 正文全文
文档_3_Supplementary_TableS1_NOS.md ← 补充表格
figures/figure1_prisma.png
figures/figure2_modality_age_bubble.png
figures/figure3_effect_direction.png
figures/figure4_age_timeline.png
```

**输出文件：**
```
projects/paper-02/06-write/paper02_final.docx
```

---

## 二、DCN 投稿格式要求（逐条执行）

### 2.1 页面设置
- 纸张：A4
- 页边距：上下左右各 2.54 cm（1 inch）
- 行距：**双倍行距**（全文，包括 References）
- 页码：右下角，从第 1 页开始

### 2.2 字体
- 正文：**Times New Roman 12pt**
- 标题（1级，如 "1. Introduction"）：Times New Roman 12pt，**加粗**，左对齐
- 标题（2级，如 "3.1 Study selection"）：Times New Roman 12pt，**加粗**，左对齐
- 标题（3级，如 "3.3.1 Resting-state EEG"）：Times New Roman 12pt，加粗斜体，左对齐
- Abstract 标签（"Background:"、"Objective:" 等）：加粗
- 图注（Figure caption）：Times New Roman 10pt，左对齐
- 表格内容：Times New Roman 10pt
- 表格标题（"Table X."）：Times New Roman 10pt，加粗
- 脚注/Note：Times New Roman 9pt，斜体

### 2.3 文档结构顺序（严格按此顺序排列页面）

```
1. 标题页（Title Page）
2. Abstract（单独一页）
3. Keywords（紧接 Abstract 后，同页）
4. 正文（Introduction → Methods → Results → Discussion）
5. References
6. 图注列表（Figure Captions，单独一页，所有图的标题和说明集中列出）
7. 图（每张图单独一页，按 Figure 1–4 顺序）
8. 表格（Table 1 单独一页，三线表格式）
9. 补充材料（Supplementary Table S1，单独一页）
```

> **注意：** DCN 要求图和表格放在正文之后，不嵌入正文中。但在正文对应位置需插入占位符，格式为：
> `[INSERT FIGURE 1 ABOUT HERE]`
> `[INSERT TABLE 1 ABOUT HERE]`
> 占位符单独成段，居中，Times New Roman 12pt，加方括号。

### 2.4 标题页内容
```
论文标题（居中，14pt，加粗）：
Parental education level and early childhood neural development: a systematic
review of EEG, ERP, fNIRS, and neuroimaging evidence (ages 0–8 years)

作者行（居中，12pt）：
[Author names — to be filled by oo]

机构行（居中，12pt，斜体）：
[Affiliations — to be filled by oo]

通讯作者（左对齐，12pt）：
Corresponding author: [to be filled by oo]

字数统计（左对齐，12pt）：
Word count (main text, excluding abstract, references, tables, figure captions): ~[X] words
```

### 2.5 Abstract 格式
- 结构式摘要，5个标签段：**Background / Objective / Methods / Results / Conclusions**
- 每个标签加粗，后接冒号，同行继续正文
- 总字数不超过 250 词
- 关键词（Keywords）紧接摘要后，同页，格式：
  `Keywords: parental education; socioeconomic status; neural development; EEG; ERP; fNIRS; fMRI; DTI; systematic review; early childhood`

### 2.6 正文段落格式
- 段落首行缩进：1.27 cm（0.5 inch）
- 段落间距：不加额外段前/段后间距（仅靠双倍行距区分）
- 节标题前加一个空行（段前 12pt 间距）
- 统计数值格式：斜体（*p*, *β*, *r*, *F*, *t*, *N*, *k*）
- 置信区间格式：95% CI [下限, 上限]

### 2.7 表格格式（三线表，booktable 风格）

**Table 1 是本文唯一的正文表格**，格式要求：

```
表格标题：左对齐，加粗，格式为 "Table 1"（加粗）+ 空格 + 标题文字（不加粗）
示例：Table 1  Characteristics of included studies (N = 16)

三线表规则：
- 顶线（toprule）：1.5pt 实线
- 表头下分隔线（midrule）：0.75pt 实线
- 底线（bottomrule）：1.5pt 实线
- 表格内部：无竖线，无横线
- 表头行：加粗，居中
- 数据行：左对齐（文字列）或居中（数字列）
- 行高：最小 0.6 cm

Note 格式（紧接表格底线下方）：
- 缩进与表格左边对齐
- 格式：Note. [说明文字]（"Note." 加粗斜体，后接正文）
- 脚注标记（如 †）：在表格内对应单元格上标，在 Note 中解释
```

**Table 1 的列定义（按草稿 Table 1 内容）：**

| 列名 | 宽度比例 |
|------|---------|
| Study | 15% |
| Country | 8% |
| *N* | 5% |
| Age at measure | 14% |
| Design | 8% |
| Modality | 8% |
| Education operationalization | 20% |
| Effect direction | 10% |
| NOS | 5% |

表格总宽度：页面文字区域宽度（16 cm）

**Table 1 的 Note 内容：**
```
Note. NOS = Newcastle–Ottawa Scale total score (range 0–9; ≥7 = high quality, 5–6 = moderate quality, ≤4 = low quality). Effect direction classified as positive when higher parental education was associated with a more mature, stronger, or larger neural index; negative when associated with reduced amplitude, lower connectivity, or a less differentiated neural response. Design: CS = cross-sectional; L = longitudinal. Modality: rsEEG = resting-state electroencephalography; ERP = event-related potential; fNIRS = functional near-infrared spectroscopy; fMRI = functional magnetic resonance imaging; DTI = diffusion tensor imaging; sMRI = structural MRI. † Original p = .025; association did not survive false-discovery rate (FDR) correction.
```

### 2.8 图注格式（Figure Captions 页）

图注列表页标题：`Figure Captions`（居中，加粗，12pt）

每张图的格式：
```
Figure X.（加粗）+ 空格 + 图注正文（不加粗）
图注正文后换行，如有 Note 则格式为：
Note.（加粗斜体）+ 说明文字
```

**四张图的图注内容：**

**Figure 1.**
PRISMA 2020 flow diagram depicting the study selection process. Records were identified from four electronic databases (PubMed/MEDLINE, PsycINFO, Web of Science, Scopus; total = 3,097). After deduplication (n = 1,827), automated keyword pre-screening (Stage 1) and title/abstract review (Stage 2) yielded 133 records for full-text retrieval. Full-text review of 109 records resulted in 16 studies meeting all inclusion criteria.
*Note.* E2 = parental education/SES not independently estimable (k = 87); E7 = duplicate or superseded record (k = 4); E4 = non-empirical publication type (k = 1); E6 = full text inaccessible (k = 1).

**Figure 2.**
Modality and age distribution of included studies. Each bubble represents one study; bubble size is proportional to sample size (*N*); color indicates neural measurement modality; position on the x-axis indicates age group at neural measurement; position on the y-axis indicates modality. Studies with positive associations between parental education and neural outcomes are shown in solid fill; the single study with a negative association (Wienke et al., 2024) is shown with a cross-hatched fill.
*Note.* Age groups: Neonatal = birth to 1 month; Infant = 1–12 months; Toddler = 1–3 years; Preschool = 3–5 years; School-age = 5 years and older. rsEEG = resting-state EEG; ERP = event-related potential; fNIRS = functional near-infrared spectroscopy.

**Figure 3.**
Effect direction by neural modality. Horizontal stacked bars show the number of studies reporting positive (blue) or negative (red) associations between parental education and neural outcomes within each modality. Numbers at the end of each bar indicate total studies per modality (*k*).

**Figure 4.**
Age range of neural measurement across included studies. Each horizontal bar represents one study, spanning the age range at which neural data were collected. Bar color indicates neural measurement modality (see legend). Vertical background shading indicates developmental age periods. The single study with a negative association (Wienke et al., 2024; ERP) is shown with cross-hatching and a dashed border.
*Note.* Bar width reflects the age range of neural measurement, not the full study duration. Ramphal et al. (2020): neonatal fMRI scan; bar extended to 24 months to indicate longitudinal behavioral follow-up. Stiver et al. (2015): preterm sample; bar starts at term-equivalent age. Shephard et al. (2019): point measurement at 6 months; bar shown at minimum width. rsEEG = resting-state EEG; DTI = diffusion tensor imaging; sMRI = structural MRI.

### 2.9 References 格式（APA 7th）

- 双倍行距
- 悬挂缩进（hanging indent）：1.27 cm
- 按第一作者姓氏字母顺序排列
- 期刊名和卷号斜体
- DOI 格式：`https://doi.org/10.xxxx`
- 作者超过 20 人：列前 19 位，省略号，最后一位

---

## 三、脚本实现要求

### 3.1 依赖库
```python
pip install python-docx pillow
```

### 3.2 脚本结构（参考 paper-01 的 generate_docx.py）

```python
# 路径配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DRAFT_FILE = os.path.join(BASE_DIR, "文档_2_paper02_draft_v1.md")
FIG_DIR    = os.path.join(BASE_DIR, "figures")
OUT_FILE   = os.path.join(BASE_DIR, "paper02_final.docx")

# 主要函数
def set_font(run, ...)          # 字体设置工具函数
def add_heading(doc, text, level)  # 标题段落
def add_paragraph(doc, text)    # 正文段落（含首行缩进）
def add_figure(doc, fig_num)    # 插入图片（单独页）
def add_table1(doc)             # 生成 Table 1 三线表
def add_three_line_borders(table)  # 三线表边框工具函数
def add_figure_captions_page(doc)  # 图注列表页
def add_references(doc)         # References 节（悬挂缩进）
def add_supplementary(doc)      # Supplementary Table S1

# 执行顺序
main():
    doc = Document()
    setup_page(doc)          # 页面/页边距设置
    add_title_page(doc)
    add_abstract(doc)
    add_body(doc)            # Introduction → Discussion，含占位符
    add_references(doc)
    add_figure_captions_page(doc)
    add_figures(doc)         # Figure 1–4，每张单独页
    add_table1(doc)          # Table 1，单独页
    add_supplementary(doc)   # Supplementary Table S1
    doc.save(OUT_FILE)
```

### 3.3 正文解析规则

从 `文档_2_paper02_draft_v1.md` 解析正文时：

| Markdown 标记 | Word 处理 |
|--------------|----------|
| `# Title` | 跳过（标题页单独处理）|
| `## 1. Introduction` | 1级标题（加粗，12pt）|
| `### 3.1 Study selection` | 2级标题（加粗，12pt）|
| `#### 3.3.1 Resting-state EEG` | 3级标题（加粗斜体，12pt）|
| `**text**` | 加粗 run |
| `*text*` | 斜体 run |
| `> blockquote` | 缩进段落（左缩进 1.27cm，斜体）|
| `\| table \|` | 跳过（Table 1 由 add_table1() 单独生成）|
| `[INSERT FIGURE X ABOUT HERE]` | 居中段落，方括号保留 |
| 空行 | 段落分隔，不额外加间距 |
| `*(Section X to follow.)*` | 跳过（草稿占位符）|

### 3.4 三线表实现（关键）

```python
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def set_cell_border(cell, **kwargs):
    """设置单元格边框，kwargs: top/bottom/left/right，值为 (sz, color, val)"""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for edge, (sz, color, val) in kwargs.items():
        border = OxmlElement(f'w:{edge}')
        border.set(qn('w:val'), val)
        border.set(qn('w:sz'), str(sz))
        border.set(qn('w:color'), color)
        tcBorders.append(border)
    tcPr.append(tcBorders)

def add_three_line_table(doc, headers, rows, col_widths_cm, note_text=None):
    """
    生成三线表：
    - toprule: 顶部 1.5pt 实线（所有列顶部）
    - midrule: 表头行底部 0.75pt 实线
    - bottomrule: 最后行底部 1.5pt 实线
    - 无竖线，无内部横线
    """
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.style = 'Table Grid'  # 先用 Grid，再手动覆盖边框

    # 设置列宽
    for i, w in enumerate(col_widths_cm):
        for cell in table.columns[i].cells:
            cell.width = Cm(w)

    # 表头行
    hdr_row = table.rows[0]
    for i, h in enumerate(headers):
        cell = hdr_row.cells[i]
        cell.text = h
        # 字体：加粗，10pt，居中
        for para in cell.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in para.runs:
                set_font(run, size_pt=10, bold=True)
        # 边框：顶部 toprule(1.5pt) + 底部 midrule(0.75pt)，无左右
        set_cell_border(cell,
            top=('12', '000000', 'single'),     # 1.5pt = 12 eighths
            bottom=('6', '000000', 'single'),   # 0.75pt = 6 eighths
            left=('0', 'FFFFFF', 'none'),
            right=('0', 'FFFFFF', 'none'),
        )

    # 数据行
    for r_idx, row_data in enumerate(rows):
        row = table.rows[r_idx + 1]
        is_last = (r_idx == len(rows) - 1)
        for c_idx, val in enumerate(row_data):
            cell = row.cells[c_idx]
            cell.text = str(val)
            for para in cell.paragraphs:
                para.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for run in para.runs:
                    set_font(run, size_pt=10)
            # 边框：无顶/左/右；最后行加 bottomrule(1.5pt)
            bottom_border = ('12', '000000', 'single') if is_last else ('0', 'FFFFFF', 'none')
            set_cell_border(cell,
                top=('0', 'FFFFFF', 'none'),
                bottom=bottom_border,
                left=('0', 'FFFFFF', 'none'),
                right=('0', 'FFFFFF', 'none'),
            )

    # Note（紧接表格后）
    if note_text:
        note_para = doc.add_paragraph()
        note_run_label = note_para.add_run("Note. ")
        set_font(note_run_label, size_pt=9, bold=True, italic=True)
        note_run_text = note_para.add_run(note_text)
        set_font(note_run_text, size_pt=9, italic=True)
        note_para.paragraph_format.left_indent = Cm(0)

    return table
```

### 3.5 图片插入（每张单独页）

```python
def add_figure_page(doc, fig_path, fig_num, max_width_cm=16.0):
    doc.add_page_break()
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = para.add_run()
    # 按比例缩放，最大宽度 16cm
    from PIL import Image
    img = Image.open(fig_path)
    w_px, h_px = img.size
    aspect = h_px / w_px
    width_cm = min(max_width_cm, 16.0)
    run.add_picture(fig_path, width=Cm(width_cm))
```

---

## 四、Table 1 数据（直接硬编码，不从 Markdown 解析）

从草稿 Table 1 提取，共 16 行，按以下顺序排列（与草稿一致）：

```python
TABLE1_HEADERS = [
    "Study", "Country", "N", "Age at measure", "Design",
    "Modality", "Education operationalization", "Effect direction", "NOS"
]

TABLE1_ROWS = [
    ["Wienke et al. (2024)", "Germany", "255", "6–14 months", "CS", "ERP", "Maternal education (years); composite-separable", "Negative", "6"],
    ["Wijeakumar et al. (2019)", "India", "35", "5–8 years", "CS", "fNIRS", "Maternal education (categorical); edu-only", "Positive", "6"],
    ["Stiver et al. (2015)", "Canada", "26", "Term-equivalent age → 2 years corrected age (longitudinal)", "L", "sMRI", "Parental education (categorical); edu-only", "Positive", "8"],
    ["Brito & Noble (2020)", "USA", "179", "6–12 months", "CS", "rsEEG", "Parental education (years); composite-separable", "Positive†", "6"],
    ["McKinnon et al. (2023)", "UK", "261", "Neonatal", "CS", "sMRI", "Maternal education (categorical); edu-only", "Positive", "9"],
    ["Zhu et al. (2023)", "USA/UK/Norway", "373", "Birth–8 years", "L", "sMRI", "Parental education (years); composite-separable", "Positive", "7"],
    ["Konrad et al. (2024)", "Canada/Germany", "105", "Neonatal", "CS", "sMRI", "Maternal education (years); edu-only", "Positive", "7"],
    ["Demir-Lira et al. (2021)", "USA", "42", "6–13 years", "CS", "fMRI", "Parental education (years); composite-separable", "Positive", "7"],
    ["Ramphal et al. (2020)", "USA", "112", "Neonatal → 2 years", "L", "fMRI", "Parental education (composite-separable)", "Positive", "8"],
    ["Ozernov-Palchik et al. (2019)", "USA", "125", "5–8 years", "CS", "DTI", "Parental education (years); edu-only", "Positive", "7"],
    ["Turesky et al. (2022)", "USA", "38", "~8.6 months", "CS", "DTI", "Maternal education (years); composite-separable", "Positive", "7"],
    ["Maguire & Schneider (2019)", "USA", "90", "8–15 years", "CS", "rsEEG", "Maternal education (years); composite-separable", "Positive", "7"],
    ["Shephard et al. (2019)", "Brazil", "31", "6 months", "CS", "rsEEG", "Maternal education (categorical); edu-only", "Positive", "7"],
    ["Conejero et al. (2018)", "Spain", "56", "12–30 months", "CS", "ERP", "Parental education (years/categorical); edu-only", "Positive", "7"],
    ["Ursache & Noble (2016)", "USA", "107", "3–21 years (focus 6–9y)", "CS", "DTI", "Parental education (years); composite-separable", "Positive", "8"],
    ["Lange et al. (2010)", "UK", "309", "4–18 years", "CS", "sMRI", "Parental education (categorical); edu-only", "Positive", "7"],
]

TABLE1_COL_WIDTHS_CM = [3.2, 1.8, 0.9, 3.0, 1.2, 1.4, 4.0, 1.8, 0.8]
# 合计 = 18.1 cm（略超，可按比例缩放至 16 cm）
```

---

## 五、Supplementary Table S1 格式

标题页：`Supplementary Materials`（居中，加粗，12pt）

表格标题：`Supplementary Table S1.`（加粗）+ ` Newcastle–Ottawa Scale domain scores for included studies (N = 16)`

三线表，列定义：

| 列 | 内容 |
|----|------|
| Study | 作者年份 |
| Selection (0–4) | 选择域得分 |
| Comparability (0–2) | 可比性域得分 |
| Outcome (0–3) | 结局域得分 |
| Total (0–9) | 总分 |
| Quality | High / Moderate / Low |

数据从 `文档_3_Supplementary_TableS1_NOS.md` 提取。

---

## 六、执行与验证

脚本完成后，请 cc 验证以下内容并汇报：

1. **页面顺序**：标题页 → Abstract → 正文 → References → Figure Captions → Figure 1–4（各单页）→ Table 1 → Supplementary Table S1
2. **三线表**：Table 1 顶线/中线/底线可见，无竖线，无内部横线
3. **图片**：四张图均正确插入，无变形，宽度不超过页面
4. **占位符**：正文中 `[INSERT FIGURE X ABOUT HERE]` 和 `[INSERT TABLE 1 ABOUT HERE]` 均存在且居中
5. **References**：悬挂缩进正确，双倍行距
6. **字数统计**：运行后报告正文字数（不含 Abstract/References/Tables/Figure Captions）

---

## 七、注意事项

1. **不要**从 Markdown 解析 Table 1——直接用上面的硬编码数据，避免解析错误
2. **不要**把图嵌入正文——图统一放在文档末尾，正文只有占位符
3. **斜体统计符号**：正文中 `*p*`、`*β*`、`*r*` 等在 Word 里需要用斜体 run 实现，不能保留星号
4. **†脚注标记**：Brito 行的 "Positive†" 中，† 需要用上标（`run.font.superscript = True`）
5. **References 悬挂缩进**：用 `paragraph_format.first_line_indent = Cm(-1.27)` + `paragraph_format.left_indent = Cm(1.27)` 实现
6. **双倍行距**：用 `paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE` 实现，需 `from docx.enum.text import WD_LINE_SPACING`
7. **页码**：在页脚插入页码字段，右对齐

---

*cc 完成后 push 并汇报：文件大小、页数、字数统计、三线表截图确认。*
