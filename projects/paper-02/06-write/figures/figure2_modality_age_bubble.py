"""
Figure 2: Modality × Age Group Bubble Chart
Paper-02: Parental education and early childhood neural development

Data source: figures/figure2_data.json
Output: figures/figure2_modality_age_bubble.png

Design decisions (oo-cc confirmed 2026-04-10):
- X-axis: age group at NEURAL MEASUREMENT (not follow-up behavioral outcome)
- Ramphal 2020 → Neonatal (neural measurement at birth, not follow-up to 2y)
- Lange 2010 → sMRI / School-age (IQ as proxy, noted in bubble label)
- Bubble size: proportional to sqrt(N) for visual clarity
- Color: positive=#2E6DA4 (DCN blue), negative=#C0392B (red)
"""

import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import os

# ── paths ──────────────────────────────────────────────────────────────────
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path  = os.path.join(script_dir, "figure2_data.json")
out_path   = os.path.join(script_dir, "figure2_modality_age_bubble.png")

# ── load data ──────────────────────────────────────────────────────────────
with open(data_path, encoding="utf-8") as f:
    meta = json.load(f)

age_order     = meta["age_group_order"]        # X axis categories
modality_order = meta["modality_order"]         # Y axis categories (bottom → top)
color_map     = meta["color_mapping"]
studies       = meta["studies"]

# ── coordinate mapping ─────────────────────────────────────────────────────
age_idx     = {a: i for i, a in enumerate(age_order)}
mod_idx     = {m: i for i, m in enumerate(modality_order)}

# bubble size: area proportional to N, scaled for readability
def bubble_size(n):
    return (np.sqrt(n) * 8) ** 2  # tuned so N=373 ≈ 2000, N=26 ≈ 400

# ── build arrays ───────────────────────────────────────────────────────────
xs, ys, sizes, colors, labels = [], [], [], [], []
for s in studies:
    x = age_idx.get(s["age_group"])
    y = mod_idx.get(s["modality"])
    if x is None or y is None:
        continue
    xs.append(x)
    ys.append(y)
    sizes.append(bubble_size(s["N"]))
    colors.append(color_map[s["effect_direction"]])
    # short label: first author + year
    author = s["author_year"].split(" ")[0]
    year   = s["author_year"].split("(")[1].rstrip(")")
    labels.append(f"{author}\n{year}")

# ── figure ─────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 6))

scatter = ax.scatter(xs, ys, s=sizes, c=colors,
                     alpha=0.80, edgecolors="white", linewidths=1.5, zorder=3)

# author labels inside / near bubbles
for x, y, lbl in zip(xs, ys, labels):
    ax.text(x, y, lbl, ha="center", va="center",
            fontsize=6.5, color="white", fontweight="bold", zorder=4)

# ── axes ───────────────────────────────────────────────────────────────────
ax.set_xticks(range(len(age_order)))
ax.set_xticklabels(age_order, fontsize=10)
ax.set_yticks(range(len(modality_order)))
ax.set_yticklabels(modality_order, fontsize=10)
ax.set_xlim(-0.7, len(age_order) - 0.3)
ax.set_ylim(-0.7, len(modality_order) - 0.3)

ax.set_xlabel("Age Group at Neural Measurement", fontsize=11, labelpad=8)
ax.set_ylabel("Neural Modality", fontsize=11, labelpad=8)
ax.set_title(
    "Figure 2. Distribution of Included Studies by Neural Modality and Age Group\n"
    "(bubble size proportional to sample size N)",
    fontsize=11, pad=12
)

# light grid
ax.set_axisbelow(True)
ax.grid(True, color="#e0e0e0", linestyle="--", linewidth=0.7, zorder=1)
ax.set_facecolor("#fafafa")

# ── legends ────────────────────────────────────────────────────────────────
# direction legend
patches = [
    mpatches.Patch(color=color_map["positive"], label="Positive association (k = 15)"),
    mpatches.Patch(color=color_map["negative"], label="Negative association (k = 1)"),
]

# size legend (N reference bubbles)
size_ref = [50, 150, 373]
size_handles = [
    Line2D([0], [0], marker='o', color='w',
           markerfacecolor='#888888', markersize=np.sqrt(bubble_size(n)) / np.pi,
           label=f"N = {n}", alpha=0.8)
    for n in size_ref
]

leg1 = ax.legend(handles=patches,     loc="upper left",  fontsize=9,
                 framealpha=0.9, title="Effect direction", title_fontsize=9)
leg2 = ax.legend(handles=size_handles, loc="lower right", fontsize=9,
                 framealpha=0.9, title="Sample size",      title_fontsize=9)
ax.add_artist(leg1)

# ── footnote ──────────────────────────────────────────────────────────────
fig.text(0.01, 0.01,
         "† Brito & Noble (2020): p = .025 for rsEEG; did not survive FDR correction.\n"
         "  Ramphal et al. (2020): neural measurement at neonatal period; longitudinal follow-up to 2 years for behavioral outcomes.\n"
         "  Lange et al. (2010): IQ used as neural-cognitive proxy; brain volume included as covariate.",
         fontsize=7, color="#555555", va="bottom")

plt.tight_layout(rect=[0, 0.08, 1, 1])
plt.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Saved: {out_path}")
