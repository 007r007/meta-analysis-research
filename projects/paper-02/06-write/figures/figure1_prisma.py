"""
Figure 1: PRISMA 2020 Flow Diagram  (v2 — fixed left overlap)
Paper-02: Parental education and early childhood neural development

Fix: removed duplicate vertical text labels; stage labels moved to left margin
     with no overlap to main flow boxes; MAIN_X shifted right to 45.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
out_path   = os.path.join(script_dir, "figure1_prisma.png")

C_ID    = dict(fc="#EBF4FA", ec="#2E6DA4", tc="#1A3A5C")
C_SC    = dict(fc="#EBF7EE", ec="#1A7D3E", tc="#0D4A22")
C_EX    = dict(fc="#FEF0EF", ec="#C0392B", tc="#7B1E1E")
C_LABEL = dict(fc="#E8EFF7", ec="#2E6DA4", tc="#2E6DA4")
ARROW   = "#444444"

fig, ax = plt.subplots(figsize=(11, 14))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis("off")
ax.set_facecolor("white")
fig.patch.set_facecolor("white")

# ── layout constants ───────────────────────────────────────────────────────
MAIN_X = 46     # centre of main flow column (shifted right vs v1)
EXCL_X = 82     # centre of exclusion column
BW     = 36     # main box width  → left edge at 46-18=28, right at 64
BH     = 9
EBW    = 28     # exclusion box width → left edge at 82-14=68  (gap=4 from main right)
LABEL_X = 8     # stage label centre (right edge at 8+6=14, well left of 28)
LABEL_W = 12    # label box half-width → 8±6 = 2 to 14

# ── helpers ────────────────────────────────────────────────────────────────
def box(ax, x, y, w, h, text, style, fontsize=8.5, bold_first=False):
    rect = mpatches.FancyBboxPatch(
        (x - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.4",
        facecolor=style["fc"], edgecolor=style["ec"], linewidth=1.3, zorder=3
    )
    ax.add_patch(rect)
    if bold_first:
        lines = text.split("\n", 1)
        ax.text(x, y + h * 0.18, lines[0],
                ha="center", va="center", fontsize=fontsize,
                color=style["tc"], fontweight="bold", zorder=4)
        if len(lines) > 1:
            ax.text(x, y - h * 0.20, lines[1],
                    ha="center", va="center", fontsize=fontsize - 0.5,
                    color=style["tc"], zorder=4)
    else:
        ax.text(x, y, text, ha="center", va="center", fontsize=fontsize,
                color=style["tc"], zorder=4, multialignment="center")

def arrow_down(ax, x, y_start, y_end):
    ax.annotate("", xy=(x, y_end), xytext=(x, y_start),
                arrowprops=dict(arrowstyle="-|>", color=ARROW,
                                lw=1.4, mutation_scale=13), zorder=2)

def arrow_right(ax, x_start, x_end, y):
    ax.annotate("", xy=(x_end, y), xytext=(x_start, y),
                arrowprops=dict(arrowstyle="-|>", color=ARROW,
                                lw=1.4, mutation_scale=13), zorder=2)

def stage_label(ax, y, text):
    """Draw a rotated stage label in the left margin."""
    rect = mpatches.FancyBboxPatch(
        (LABEL_X - LABEL_W/2, y - 3.5), LABEL_W, 7,
        boxstyle="round,pad=0.3",
        facecolor=C_LABEL["fc"], edgecolor=C_LABEL["ec"],
        linewidth=1.0, zorder=3
    )
    ax.add_patch(rect)
    ax.text(LABEL_X, y, text, ha="center", va="center",
            fontsize=8.5, color=C_LABEL["tc"], fontweight="bold",
            rotation=90, zorder=4)

# ── row y-positions ────────────────────────────────────────────────────────
y1 = 92   # database hits
y2 = 78   # after dedup
y3 = 64   # after stage 1
y4 = 50   # after stage 2
y5 = 36   # full-text
y6 = 20   # included

# ── stage labels (left margin, no overlap with main boxes) ─────────────────
stage_label(ax, (y1 + y2) / 2,       "Identification")
stage_label(ax, (y2 + y3 + y4) / 3,  "Screening")
stage_label(ax, (y4 + y5) / 2,       "Eligibility")
stage_label(ax, y6,                   "Included")

# ── Row 1: Database hits ───────────────────────────────────────────────────
box(ax, MAIN_X, y1, BW, 10,
    "Records identified from databases\n"
    "PubMed (n = 521)  ·  PsycINFO (n = 296)\n"
    "Web of Science (n = 1,011)  ·  Scopus (n = 1,269)\n"
    "Total: n = 3,097",
    C_ID, fontsize=8)

# ── Row 2: After deduplication ─────────────────────────────────────────────
arrow_down(ax, MAIN_X, y1 - 5, y2 + 4.5)
box(ax, MAIN_X, y2, BW, BH,
    "Records after deduplication\n(n = 1,827)",
    C_ID, fontsize=9, bold_first=True)
box(ax, EXCL_X, y2, EBW, BH,
    "Duplicates removed\n(n = 1,270)", C_EX, fontsize=8.5)
arrow_right(ax, MAIN_X + BW/2, EXCL_X - EBW/2, y2)

# ── Row 3: After Stage 1 ───────────────────────────────────────────────────
arrow_down(ax, MAIN_X, y2 - 4.5, y3 + 4.5)
box(ax, MAIN_X, y3, BW, BH,
    "Records after automated pre-screening\n(n = 513)",
    C_SC, fontsize=9, bold_first=True)
box(ax, EXCL_X, y3, EBW, BH,
    "Excluded at Stage 1\n(keyword algorithm)\nn = 1,314",
    C_EX, fontsize=8.5)
arrow_right(ax, MAIN_X + BW/2, EXCL_X - EBW/2, y3)

# ── Row 4: After Stage 2 ───────────────────────────────────────────────────
arrow_down(ax, MAIN_X, y3 - 4.5, y4 + 4.5)
box(ax, MAIN_X, y4, BW, BH,
    "Records after title/abstract screening\n(n = 133)",
    C_SC, fontsize=9, bold_first=True)
box(ax, EXCL_X, y4, EBW, BH,
    "Excluded at Stage 2\n(title/abstract)\nn = 380",
    C_EX, fontsize=8.5)
arrow_right(ax, MAIN_X + BW/2, EXCL_X - EBW/2, y4)

# ── Row 5: Full-text ───────────────────────────────────────────────────────
arrow_down(ax, MAIN_X, y4 - 4.5, y5 + 4.5)
box(ax, MAIN_X, y5, BW, BH,
    "Full texts assessed for eligibility\n(n = 109)",
    C_SC, fontsize=9, bold_first=True)
box(ax, EXCL_X, y5, EBW, 11,
    "Excluded before full-text review\n(n = 24)\n"
    "  Abstract-based exclusion: n = 22\n"
    "  Confirmed retraction: n = 1\n"
    "  Full text unavailable: n = 1",
    C_EX, fontsize=7.8)
arrow_right(ax, MAIN_X + BW/2, EXCL_X - EBW/2, y5)

# ── Row 6: Included ────────────────────────────────────────────────────────
arrow_down(ax, MAIN_X, y5 - 4.5, y6 + 4.5)
box(ax, MAIN_X, y6, BW, 9,
    "Studies included in review\n(n = 16)",
    C_SC, fontsize=10, bold_first=True)
box(ax, EXCL_X, y6, EBW, 13,
    "Excluded at full-text review\n(n = 93)\n"
    "  E2 – education not independently\n"
    "          estimable: n = 87\n"
    "  E7 – duplicate/superseded: n = 4\n"
    "  E4 – non-empirical: n = 1\n"
    "  E6 – full text inaccessible: n = 1",
    C_EX, fontsize=7.5)
arrow_right(ax, MAIN_X + BW/2, EXCL_X - EBW/2, y6)

# ── Title ──────────────────────────────────────────────────────────────────
ax.text(50, 99.2,
        "Figure 1.  PRISMA 2020 Flow Diagram",
        ha="center", va="top", fontsize=12, fontweight="bold", color="#1A1A1A")

plt.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Saved: {out_path}")
