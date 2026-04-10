"""
Figure 3: Effect Direction by Neural Modality (Horizontal Stacked Bar)
Paper-02: Parental education and early childhood neural development

Data source: figures/figure3_data.json
Output: figures/figure3_effect_direction.png

Design (oo-cc confirmed 2026-04-10):
- Horizontal stacked bars, one bar per modality
- Ordered bottom-to-top: fNIRS, ERP, rsEEG, DTI, fMRI, sMRI
- Positive=#2E6DA4 (DCN blue), Negative=#C0392B (red)
- Annotate k counts inside bar segments
"""

import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# ── paths ──────────────────────────────────────────────────────────────────
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path  = os.path.join(script_dir, "figure3_data.json")
out_path   = os.path.join(script_dir, "figure3_effect_direction.png")

# ── load data ──────────────────────────────────────────────────────────────
with open(data_path, encoding="utf-8") as f:
    meta = json.load(f)

row_order = meta["modality_order_bottom_to_top"]  # bottom → top in chart
data_map  = {d["modality"]: d for d in meta["data"]}
colors    = meta["color_mapping"]

# ── build arrays ───────────────────────────────────────────────────────────
modalities = row_order
pos_vals   = [data_map[m]["positive"] for m in modalities]
neg_vals   = [data_map[m]["negative"] for m in modalities]
k_totals   = [data_map[m]["k_total"]  for m in modalities]
y_pos      = np.arange(len(modalities))

# ── figure ─────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5))

bar_pos = ax.barh(y_pos, pos_vals, color=colors["positive"],
                  height=0.55, label="Positive association", zorder=3)
bar_neg = ax.barh(y_pos, neg_vals, left=pos_vals, color=colors["negative"],
                  height=0.55, label="Negative association", zorder=3)

# ── annotate k counts ──────────────────────────────────────────────────────
for i, (p, n, kt) in enumerate(zip(pos_vals, neg_vals, k_totals)):
    # positive segment label
    if p > 0:
        ax.text(p / 2, i, f"k = {p}", ha="center", va="center",
                fontsize=10, color="white", fontweight="bold", zorder=4)
    # negative segment label
    if n > 0:
        ax.text(p + n / 2, i, f"k = {n}", ha="center", va="center",
                fontsize=10, color="white", fontweight="bold", zorder=4)
    # total label to the right of the bar
    ax.text(kt + 0.05, i, f"(total k = {kt})", ha="left", va="center",
            fontsize=9, color="#444444")

# ── axes ───────────────────────────────────────────────────────────────────
ax.set_yticks(y_pos)
ax.set_yticklabels(modalities, fontsize=11)
ax.set_xlim(0, max(k_totals) + 1.8)
ax.set_xlabel("Number of Studies (k)", fontsize=10)
ax.set_title(
    "Figure 3. Effect Direction of Included Studies by Neural Modality",
    fontsize=11, pad=10
)

ax.set_axisbelow(True)
ax.grid(axis="x", color="#e0e0e0", linestyle="--", linewidth=0.7, zorder=1)
ax.set_facecolor("#fafafa")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# ── legend ─────────────────────────────────────────────────────────────────
ax.legend(loc="lower right", fontsize=9, framealpha=0.9)

# ── footnote ──────────────────────────────────────────────────────────────
fig.text(0.01, 0.01,
         "Negative finding (ERP, k = 1): Wienke et al. (2024); attributed to migration-related linguistic exposure heterogeneity.",
         fontsize=8, color="#555555", va="bottom")

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Saved: {out_path}")
