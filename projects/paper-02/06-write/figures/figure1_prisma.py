"""
Figure 1: PRISMA 2020 Flow Diagram
Paper-02: Parental education and early childhood neural development

Output: figures/figure1_prisma.png

PRISMA 2020 four-column layout:
  Left column:  Identification → Screening → Included
  Right column: Exclusion boxes at each stage

Confirmed numbers (oo, 2026-04-10):
  PubMed=521, PsycINFO=296, WoS=1011, Scopus=1269  → total=3097
  After deduplication: 1827
  Stage 1 auto-excluded: 1314 → retained: 513
  Stage 2 title/abstract excluded: 380 → retained: 133
  Pre-full-text excluded: 24 (abstract-based=22, retracted=1, unavailable=1)
  Full-text reviewed: 109
  Full-text excluded: 93 (E2=87, E7=4, E4=1, E6=1)
  Included: 16

Style: Nature-inspired (clean lines, muted palette, no chartjunk)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
out_path   = os.path.join(script_dir, "figure1_prisma.png")

# ── colour palette (Nature-style) ─────────────────────────────────────────
C_ID    = dict(fc="#EBF4FA", ec="#2E6DA4", tc="#1A3A5C")  # identification
C_SC    = dict(fc="#EBF7EE", ec="#1A7D3E", tc="#0D4A22")  # screening / included
C_EX    = dict(fc="#FEF0EF", ec="#C0392B", tc="#7B1E1E")  # exclusion
C_LABEL = dict(fc="#E8EFF7", ec="#2E6DA4", tc="#2E6DA4")  # stage labels
ARROW   = "#444444"

fig, ax = plt.subplots(figsize=(10, 13))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis("off")
ax.set_facecolor("white")
fig.patch.set_facecolor("white")

# ── helper functions ───────────────────────────────────────────────────────
def box(ax, x, y, w, h, text, style, fontsize=8.5, bold_first=False):
    rect = mpatches.FancyBboxPatch(
        (x - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.3",
        facecolor=style["fc"], edgecolor=style["ec"], linewidth=1.2, zorder=3
    )
    ax.add_patch(rect)
    if bold_first:
        lines = text.split("\n", 1)
        ax.text(x, y + h * 0.18, lines[0],
                ha="center", va="center", fontsize=fontsize,
                color=style["tc"], fontweight="bold", zorder=4)
        if len(lines) > 1:
            ax.text(x, y - h * 0.18, lines[1],
                    ha="center", va="center", fontsize=fontsize - 0.5,
                    color=style["tc"], zorder=4)
    else:
        ax.text(x, y, text,
                ha="center", va="center", fontsize=fontsize,
                color=style["tc"], zorder=4,
                multialignment="center")

def arrow_down(ax, x, y_start, y_end):
    ax.annotate("", xy=(x, y_end), xytext=(x, y_start),
                arrowprops=dict(arrowstyle="-|>", color=ARROW,
                                lw=1.3, mutation_scale=12),
                zorder=2)

def arrow_right(ax, x_start, x_end, y):
    ax.annotate("", xy=(x_end, y), xytext=(x_start, y),
                arrowprops=dict(arrowstyle="-|>", color=ARROW,
                                lw=1.3, mutation_scale=12),
                zorder=2)

def stage_label(ax, x, y, text):
    rect = mpatches.FancyBboxPatch(
        (x - 5, y - 1.8), 10, 3.6,
        boxstyle="round,pad=0.2",
        facecolor=C_LABEL["fc"], edgecolor=C_LABEL["ec"],
        linewidth=1.0, zorder=3
    )
    ax.add_patch(rect)
    ax.text(x, y, text, ha="center", va="center",
            fontsize=9, color=C_LABEL["tc"], fontweight="bold", zorder=4)

# ══════════════════════════════════════════════════════════════════════════
# Layout: main column at x=38, exclusion column at x=75
# y positions (top→bottom): 95, 83, 71, 59, 47, 37, 25
# ══════════════════════════════════════════════════════════════════════════

MAIN_X = 38
EXCL_X = 75
BW     = 40   # box width, main
BH     = 9    # box height
EBW    = 28   # exclusion box width
EBH    = 9

# ── Stage labels (left margin) ─────────────────────────────────────────────
stage_label(ax,  5, 91, "Identification")
stage_label(ax,  5, 74, "Screening")
stage_label(ax,  5, 57, "")            # spacer
stage_label(ax,  5, 46, "Eligibility")
stage_label(ax,  5, 29, "Included")

# fix stage labels properly
for child in ax.get_children():
    pass  # already drawn via stage_label calls above

# ── Row 1: Database hits ───────────────────────────────────────────────────
y1 = 93
box(ax, MAIN_X, y1, BW, 10,
    "Records identified from databases\n"
    "PubMed (n = 521)  PsycINFO (n = 296)\n"
    "Web of Science (n = 1,011)  Scopus (n = 1,269)\n"
    "Total: n = 3,097",
    C_ID, fontsize=8)

# ── Row 2: After deduplication ─────────────────────────────────────────────
y2 = 79
arrow_down(ax, MAIN_X, y1 - 5, y2 + 4.5)
box(ax, MAIN_X, y2, BW, BH,
    "Records after deduplication\n(n = 1,827)",
    C_ID, fontsize=9, bold_first=True)

# exclusion: duplicates removed
box(ax, EXCL_X, y2, EBW, BH,
    "Duplicates removed\n(n = 1,270)",
    C_EX, fontsize=8.5)
arrow_right(ax, MAIN_X + BW/2, EXCL_X - EBW/2, y2)

# ── Row 3: After Stage 1 (auto-screening) ─────────────────────────────────
y3 = 66
arrow_down(ax, MAIN_X, y2 - 4.5, y3 + 4.5)
box(ax, MAIN_X, y3, BW, BH,
    "Records after automated pre-screening\n(n = 513)",
    C_SC, fontsize=9, bold_first=True)

box(ax, EXCL_X, y3, EBW, BH,
    "Excluded at Stage 1\n(keyword algorithm)\nn = 1,314",
    C_EX, fontsize=8.5)
arrow_right(ax, MAIN_X + BW/2, EXCL_X - EBW/2, y3)

# ── Row 4: After Stage 2 (title/abstract) ──────────────────────────────────
y4 = 53
arrow_down(ax, MAIN_X, y3 - 4.5, y4 + 4.5)
box(ax, MAIN_X, y4, BW, BH,
    "Records after title/abstract screening\n(n = 133)",
    C_SC, fontsize=9, bold_first=True)

box(ax, EXCL_X, y4, EBW, BH,
    "Excluded at Stage 2\n(title/abstract)\nn = 380",
    C_EX, fontsize=8.5)
arrow_right(ax, MAIN_X + BW/2, EXCL_X - EBW/2, y4)

# ── Row 5: Full-text sought ────────────────────────────────────────────────
y5 = 40
arrow_down(ax, MAIN_X, y4 - 4.5, y5 + 4.5)
box(ax, MAIN_X, y5, BW, BH,
    "Full texts assessed for eligibility\n(n = 109)",
    C_SC, fontsize=9, bold_first=True)

box(ax, EXCL_X, y5, EBW, 10,
    "Excluded before full-text review\n(n = 24)\n"
    "  Abstract-based: n = 22\n"
    "  Confirmed retraction: n = 1\n"
    "  Full text unavailable: n = 1",
    C_EX, fontsize=7.8)
arrow_right(ax, MAIN_X + BW/2, EXCL_X - EBW/2, y5)

# ── Row 6: Included ────────────────────────────────────────────────────────
y6 = 24
arrow_down(ax, MAIN_X, y5 - 4.5, y6 + 4.5)
box(ax, MAIN_X, y6, BW, 9,
    "Studies included in review\n(n = 16)",
    C_SC, fontsize=10, bold_first=True)

box(ax, EXCL_X, y6, EBW, 12,
    "Excluded at full-text review\n(n = 93)\n"
    "  E2 – education not independently\n"
    "          estimable: n = 87\n"
    "  E7 – duplicate/superseded: n = 4\n"
    "  E4 – non-empirical: n = 1\n"
    "  E6 – full text inaccessible: n = 1",
    C_EX, fontsize=7.5)
arrow_right(ax, MAIN_X + BW/2, EXCL_X - EBW/2, y6)

# ── Title ──────────────────────────────────────────────────────────────────
ax.text(50, 99.5,
        "Figure 1. PRISMA 2020 Flow Diagram",
        ha="center", va="top", fontsize=11, fontweight="bold", color="#1A1A1A")

# ── Stage labels (vertical, left) ─────────────────────────────────────────
for (yc, label) in [(y1, "Identification"), (y3, "Screening"),
                    (y5, "Eligibility"), (y6, "Included")]:
    ax.text(1, yc, label, ha="left", va="center",
            fontsize=8, color="#555555", style="italic",
            rotation=90)

plt.tight_layout(pad=0.5)
plt.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Saved: {out_path}")
