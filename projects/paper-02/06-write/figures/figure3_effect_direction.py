"""
Figure 3: Effect Direction by Neural Modality — Horizontal Stacked Bar  (v2 Nature style)
Paper-02: Parental education and early childhood neural development

Changes from v1:
- Nature palette: blue #3A7ABF positive, red #D45F5F negative
- Thinner bars, more breathing room
- Remove redundant "(total k = N)" text; show k inside segments + modality total on right
- Clean spines (top/right removed)

Data source: figures/figure3_data.json
Output:      figures/figure3_effect_direction.png
"""

import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
data_path  = os.path.join(script_dir, "figure3_data.json")
out_path   = os.path.join(script_dir, "figure3_effect_direction.png")

with open(data_path, encoding="utf-8") as f:
    meta = json.load(f)

row_order = meta["modality_order_bottom_to_top"]
data_map  = {d["modality"]: d for d in meta["data"]}

COL = {"positive": "#3A7ABF", "negative": "#D45F5F"}

modalities = row_order
pos_vals   = [data_map[m]["positive"] for m in modalities]
neg_vals   = [data_map[m]["negative"] for m in modalities]
k_totals   = [data_map[m]["k_total"]  for m in modalities]
y_pos      = np.arange(len(modalities))

fig, ax = plt.subplots(figsize=(8, 4.8))

# ── bars ───────────────────────────────────────────────────────────────────
ax.barh(y_pos, pos_vals, color=COL["positive"], height=0.50,
        label="Positive association", zorder=3, edgecolor="white", linewidth=0.5)
ax.barh(y_pos, neg_vals, left=pos_vals, color=COL["negative"], height=0.50,
        label="Negative association", zorder=3, edgecolor="white", linewidth=0.5)

# ── segment labels ─────────────────────────────────────────────────────────
for i, (p, n, kt) in enumerate(zip(pos_vals, neg_vals, k_totals)):
    if p > 0:
        ax.text(p / 2, i, f"k = {p}", ha="center", va="center",
                fontsize=10.5, color="white", fontweight="bold", zorder=4)
    if n > 0:
        ax.text(p + n / 2, i, f"k = {n}", ha="center", va="center",
                fontsize=10.5, color="white", fontweight="bold", zorder=4)
    # total to the right
    ax.text(kt + 0.07, i, f"k = {kt}", ha="left", va="center",
            fontsize=9, color="#555555")

# ── axes ───────────────────────────────────────────────────────────────────
ax.set_yticks(y_pos)
ax.set_yticklabels(modalities, fontsize=11, fontstyle="italic")
ax.set_xlim(0, max(k_totals) + 1.5)
ax.set_xlabel("Number of studies (k)", fontsize=10.5, labelpad=6)
ax.set_title("Figure 3.  Effect direction by neural modality",
             fontsize=11.5, fontweight="bold", pad=10, loc="left")

ax.set_axisbelow(True)
ax.grid(axis="x", color="#e8e8e8", linestyle="-", linewidth=0.7, zorder=0)
ax.set_facecolor("white")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#cccccc")
ax.spines["bottom"].set_color("#cccccc")
ax.tick_params(axis="both", colors="#555555")

ax.legend(loc="lower right", fontsize=9, frameon=True,
          framealpha=0.95, edgecolor="#cccccc", handlelength=1.2)

fig.text(0.05, 0.00,
         "Negative finding (ERP, k = 1): Wienke et al. (2024); attributed to migration-related linguistic exposure heterogeneity.",
         fontsize=7.5, color="#666666", va="bottom")

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Saved: {out_path}")
