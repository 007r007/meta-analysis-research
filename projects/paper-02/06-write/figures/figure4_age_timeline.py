"""
Figure 4: Age Timeline of Included Studies  (v3 — oo redesign, fixed)

Layout:
- Y-axis: one row per study, sorted youngest-at-top, labelled "Author (Year)"
- X-axis: child age in months (0–220), tick labels in months / years
- Color: neural modality (6 colors, consistent with Figure 2/3)
- Bar style: solid fill = positive; hatch + white fill = negative (Wienke only)
- Vertical background bands: age-group zones
- Age-group labels: placed via ax.text in data coords BEFORE invert_yaxis,
  then drawn above the top study row (y = n + 0.6)
- N= labels right of bar; [−] marker for negative
- Legend: lower-right quadrant (avoids data)
"""

import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
data_path  = os.path.join(script_dir, "figure4_data.json")
out_path   = os.path.join(script_dir, "figure4_age_timeline.png")

with open(data_path, encoding="utf-8") as f:
    meta = json.load(f)

studies = meta["studies"]

# ── Sort: age_min ascending, then age_max ascending (index 0 = youngest) ──────
studies_sorted = sorted(studies, key=lambda s: (s["age_min_mo"], s["age_max_mo"]))

# ── Modality color palette (consistent with Figure 2/3) ──────────────────────
MOD_COL = {
    "rsEEG": "#4C9BE8",
    "ERP":   "#E8834C",
    "fNIRS": "#4CBE8A",
    "fMRI":  "#9B4CE8",
    "DTI":   "#E8C84C",
    "sMRI":  "#4C6EE8",
}

# ── Vertical age-band zones (months) ─────────────────────────────────────────
AGE_BANDS = [
    (0,    1,   "#F0F4FB", "Neo."),
    (1,    12,  "#EBF7EE", "Infant\n(1–12 mo)"),
    (12,   36,  "#FFF8E7", "Toddler\n(1–3 yr)"),
    (36,   60,  "#FEF0EF", "Pre-\nschool"),
    (60,   220, "#F5F0FA", "School-age  (5+ yr)"),
]

# ── Figure ───────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 9))
plt.subplots_adjust(left=0.20, right=0.96, top=0.93, bottom=0.20)

n     = len(studies_sorted)
BAR_H = 0.42   # half-height of each bar
X_MAX = 220

# ── Vertical background bands ─────────────────────────────────────────────────
for xlo, xhi, col, label in AGE_BANDS:
    ax.axvspan(xlo, xhi, facecolor=col, alpha=0.65, zorder=0)

# Age-group labels: placed at y = -1.5 in data coords (below row 0 after invert).
# We draw them BEFORE invert_yaxis so we can reason in natural coords.
# After invert: row-0 is at top, row-(n-1) is at bottom;
# y = -1.5 ends up ABOVE row-0, which is wrong.
# Solution: place them at y = n + 0.8  (below the last row after invert).
for xlo, xhi, col, label in AGE_BANDS:
    mid = (xlo + xhi) / 2
    ax.text(mid, n + 0.9, label,
            ha="center", va="top", fontsize=8, color="#555555",
            fontstyle="italic", multialignment="center", zorder=5)

# ── Draw bars ────────────────────────────────────────────────────────────────
for i, s in enumerate(studies_sorted):
    y   = i
    xlo = s["age_min_mo"]
    xhi = s["age_max_mo"]
    if xhi - xlo < 2:        # minimum visible width
        xhi = xlo + 2
    col = MOD_COL[s["modality"]]
    neg = s["effect_direction"] == "negative"
    N   = s["N"]

    if neg:
        rect = mpatches.FancyBboxPatch(
            (xlo, y - BAR_H), xhi - xlo, 2 * BAR_H,
            boxstyle="round,pad=0.15",
            facecolor="white", edgecolor=col,
            linewidth=2.0, linestyle="--", hatch="///",
            zorder=3
        )
    else:
        rect = mpatches.FancyBboxPatch(
            (xlo, y - BAR_H), xhi - xlo, 2 * BAR_H,
            boxstyle="round,pad=0.15",
            facecolor=col, edgecolor="white",
            linewidth=0.7, alpha=0.88,
            zorder=3
        )
    ax.add_patch(rect)

    # N= label right of bar
    ax.text(xhi + 3, y, f"N={N}",
            ha="left", va="center", fontsize=6.8, color="#555555", zorder=4)
    if neg:
        ax.text(xhi + 3, y + 0.25, "[−]",
                ha="left", va="center", fontsize=6.5, color="#C0392B", zorder=4)

# ── Horizontal grid lines ────────────────────────────────────────────────────
for i in range(n):
    ax.axhline(i, color="#e0e0e0", linewidth=0.5, zorder=1)

# ── Vertical year gridlines ──────────────────────────────────────────────────
for mo in [12, 24, 36, 48, 60, 96, 120, 156, 180]:
    ax.axvline(mo, color="#cccccc", linewidth=0.6, linestyle=":", zorder=1)

# ── X-axis ───────────────────────────────────────────────────────────────────
tick_mo  = [0, 6, 12, 24, 36, 48, 60, 96, 120, 156, 180, 216]
tick_lbl = ["0", "6 mo", "1 yr", "2 yr", "3 yr", "4 yr",
             "5 yr", "8 yr", "10 yr", "13 yr", "15 yr", "18 yr"]
ax.set_xticks(tick_mo)
ax.set_xticklabels(tick_lbl, fontsize=8.5)
ax.set_xlim(-5, X_MAX + 26)

# ── Y-axis ───────────────────────────────────────────────────────────────────
ax.set_yticks(range(n))
ax.set_yticklabels([s["author_year"] for s in studies_sorted], fontsize=9.0)
ax.set_ylim(-1.5, n + 1.8)
ax.invert_yaxis()   # row 0 (youngest) at top

ax.set_xlabel("Child age at neural measurement", fontsize=11, labelpad=10)
ax.set_title(
    "Figure 4.  Age range of neural measurement across included studies",
    fontsize=11.5, fontweight="bold", pad=10, loc="left"
)

ax.set_facecolor("white")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#cccccc")
ax.spines["bottom"].set_color("#cccccc")

# ── Legend: lower-right (clears all bars) ────────────────────────────────────
mod_handles = [
    mpatches.Patch(facecolor=c, edgecolor="white", label=m, alpha=0.88)
    for m, c in MOD_COL.items()
]
dir_handles = [
    mpatches.Patch(facecolor="#aaaaaa", edgecolor="white",
                   alpha=0.88, label="Positive association"),
    mpatches.Patch(facecolor="white", edgecolor="#aaaaaa",
                   hatch="///", linewidth=1.5,
                   label="Negative association (Wienke, 2024)"),
]

leg1 = ax.legend(
    handles=mod_handles, title="Neural modality",
    loc="lower right", fontsize=8.0, title_fontsize=8.5,
    frameon=True, framealpha=0.95, edgecolor="#cccccc",
    ncol=2, handlelength=1.2,
    bbox_to_anchor=(0.99, 0.01)
)
ax.add_artist(leg1)

ax.legend(
    handles=dir_handles, title="Effect direction",
    loc="lower right", fontsize=8.0, title_fontsize=8.5,
    frameon=True, framealpha=0.95, edgecolor="#cccccc",
    handlelength=1.5,
    bbox_to_anchor=(0.99, 0.22)
)

# ── Footnote ─────────────────────────────────────────────────────────────────
fig.text(
    0.20, 0.005,
    "Bar width = age range at neural measurement.  "
    "Ramphal (2020): neonatal fMRI scan; bar extended to 24 months (longitudinal behavioural follow-up).  "
    "Stiver (2015): preterm sample; bar starts at term-equivalent age.  "
    "Shephard (2019): point measurement at 6 months; bar shown at minimum width.",
    fontsize=6.5, color="#777777", va="bottom", wrap=True
)

plt.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Saved: {out_path}")
