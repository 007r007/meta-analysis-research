"""
Figure 4: Age Timeline of Included Studies
Paper-02: Parental education and early childhood neural development

Each study shown as a horizontal bar spanning the age range of neural measurement.
- Y-axis: studies sorted by age_min then age_max
- X-axis: child age in months (0–220), with year labels
- Color: neural modality (6 colors)
- Bar edge style: solid = positive association, dashed = negative
- Bar height proportional to log(N) for visual emphasis
- Shaded background regions for age-group windows
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

# Sort: by age_min ascending, then age_max ascending
studies_sorted = sorted(studies, key=lambda s: (s["age_min_mo"], s["age_max_mo"]))

# ── Modality color palette (Nature-adjacent) ──────────────────────────────
MOD_COL = {
    "rsEEG": "#4E9A8C",   # teal
    "ERP":   "#E07B54",   # coral
    "fNIRS": "#9467BD",   # purple
    "fMRI":  "#3A7ABF",   # blue
    "DTI":   "#D4A017",   # amber
    "sMRI":  "#6A9E5B",   # green
}

# ── Age-group background bands (months) ───────────────────────────────────
AGE_BANDS = [
    (0,   1,   "#F0F4FA", "Neonatal"),
    (1,   12,  "#FAF0F0", "Infant"),
    (12,  36,  "#F0FAF2", "Toddler"),
    (36,  60,  "#FAFAF0", "Preschool"),
    (60,  220, "#F5F0FA", "School-age"),
]

# ── Figure ────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(13, 8))

n_studies = len(studies_sorted)

# background bands
for xlo, xhi, col, label in AGE_BANDS:
    ax.axvspan(xlo, xhi, facecolor=col, alpha=0.6, zorder=0)
    mid = (xlo + xhi) / 2
    ax.text(mid, n_studies + 0.3, label,
            ha="center", va="bottom", fontsize=8, color="#888888",
            fontstyle="italic")

# draw bars
BAR_H_BASE = 0.55  # base half-height of each bar
for i, s in enumerate(studies_sorted):
    y       = i
    xlo     = s["age_min_mo"]
    xhi     = max(s["age_max_mo"], xlo + 0.8)   # minimum visible width
    mod     = s["modality"]
    col     = MOD_COL[mod]
    pos     = s["effect_direction"] == "positive"
    n       = s["N"]

    # bar height scales gently with log(N): range ~0.3–0.5
    h = 0.22 + 0.18 * (np.log(n) - np.log(26)) / (np.log(373) - np.log(26))

    # filled bar
    bar = mpatches.FancyBboxPatch(
        (xlo, y - h), xhi - xlo, 2 * h,
        boxstyle="round,pad=0.3",
        facecolor=col, alpha=0.82,
        edgecolor=col if pos else "#333333",
        linewidth=1.0 if pos else 2.0,
        linestyle="-" if pos else "--",
        zorder=3
    )
    ax.add_patch(bar)

    # author label inside or to the right of bar
    bar_width = xhi - xlo
    label_text = s["author_year"]
    if bar_width >= 18:
        ax.text((xlo + xhi) / 2, y, label_text,
                ha="center", va="center", fontsize=7.2,
                color="white", fontweight="bold", zorder=4)
    else:
        ax.text(xhi + 1.5, y, label_text,
                ha="left", va="center", fontsize=7.2,
                color="#333333", zorder=4)

    # N label to the left of bar
    ax.text(xlo - 1, y, f"N={n}",
            ha="right", va="center", fontsize=6.5, color="#666666", zorder=4)

# ── x-axis: months → labelled in years ─────────────────────────────────
year_ticks_mo = [0, 6, 12, 24, 36, 48, 60, 96, 120, 156, 180, 216]
year_labels   = ["0", "6m", "1y", "2y", "3y", "4y", "5y", "8y", "10y", "13y", "15y", "18y"]
ax.set_xticks(year_ticks_mo)
ax.set_xticklabels(year_labels, fontsize=9)
ax.set_xlim(-22, 222)

# ── y-axis: study labels ────────────────────────────────────────────────
ax.set_yticks(range(n_studies))
ax.set_yticklabels(
    [f"{s['modality']}" for s in studies_sorted],
    fontsize=9, fontstyle="italic"
)
ax.set_ylim(-0.8, n_studies + 0.8)

ax.set_xlabel("Child age at neural measurement", fontsize=11, labelpad=7)
ax.set_title("Figure 4.  Age range of neural measurement across included studies",
             fontsize=11.5, fontweight="bold", pad=10, loc="left")

# light horizontal gridlines
for i in range(n_studies):
    ax.axhline(i, color="#eeeeee", linewidth=0.5, zorder=1)

# vertical gridlines at year marks
for mo in [12, 24, 36, 48, 60, 96, 120, 156]:
    ax.axvline(mo, color="#dddddd", linewidth=0.6, linestyle=":", zorder=1)

ax.set_facecolor("white")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#cccccc")
ax.spines["bottom"].set_color("#cccccc")

# ── legends ─────────────────────────────────────────────────────────────
# Modality legend
mod_handles = [mpatches.Patch(color=c, label=m, alpha=0.82)
               for m, c in MOD_COL.items()]
leg_mod = ax.legend(handles=mod_handles, title="Neural modality",
                    loc="lower right", fontsize=8.5, title_fontsize=9,
                    frameon=True, framealpha=0.95, edgecolor="#cccccc",
                    ncol=2, handlelength=1.0)
ax.add_artist(leg_mod)

# Direction legend
dir_handles = [
    Line2D([0], [0], color="#555555", linewidth=1.0, linestyle="-",
           label="Positive association"),
    Line2D([0], [0], color="#333333", linewidth=2.0, linestyle="--",
           label="Negative association (k = 1)"),
]
ax.legend(handles=dir_handles, title="Effect direction",
          loc="upper right", fontsize=8.5, title_fontsize=9,
          frameon=True, framealpha=0.95, edgecolor="#cccccc",
          handlelength=1.8)

# footnote
fig.text(0.07, 0.01,
         "Bar width = age range of neural measurement. Bar height reflects sample size (log scale). "
         "Dashed border = negative association. "
         "Ramphal (2020): neonatal fMRI scan; bar extended to 24 months to indicate longitudinal follow-up.",
         fontsize=7, color="#666666", va="bottom")

plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Saved: {out_path}")
