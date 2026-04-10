"""
Figure 2: Modality × Age Group Bubble Chart  (v4 — all overlap issues fixed)
Paper-02: Parental education and early childhood neural development

Fixes vs v3:
1. Direction legend moved to LOWER-LEFT (was upper-left, covered Neonatal/sMRI)
2. ax_leg (size legend) shifted right to 0.84, no overlap with main axes
3. Brito label visibility: rsEEG/Infant label forced BELOW bubble (into row space)
4. Neonatal sMRI two bubbles: direction legend no longer covers them

Data source: figures/figure2_data.json
Output:      figures/figure2_modality_age_bubble.png
"""

import json, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from collections import defaultdict
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
data_path  = os.path.join(script_dir, "figure2_data.json")
out_path   = os.path.join(script_dir, "figure2_modality_age_bubble.png")

with open(data_path, encoding="utf-8") as f:
    meta = json.load(f)

age_order      = meta["age_group_order"]
modality_order = meta["modality_order"]   # rsEEG=0, ERP=1, fNIRS=2, fMRI=3, DTI=4, sMRI=5
studies        = meta["studies"]

COL = {"positive": "#3A7ABF", "negative": "#D45F5F"}

age_idx = {a: i for i, a in enumerate(age_order)}
ROW_SPACING = 1.5
mod_y = {m: i * ROW_SPACING for i, m in enumerate(modality_order)}

def bsize(n):
    n_eff = min(n, 250)
    return (4.0 ** 2) * n_eff

# ── group & layout ─────────────────────────────────────────────────────────
cell_studies = defaultdict(list)
for s in studies:
    key = (age_idx.get(s["age_group"]), s["modality"])
    cell_studies[key].append(s)

xs, ys, sizes, colors, labels, label_va = [], [], [], [], [], []

for key, group in cell_studies.items():
    xi, mod = key
    yi_center = mod_y[mod]
    n = len(group)
    if n == 1:
        x_offsets = [0.0]
    elif n == 2:
        x_offsets = [-0.26, 0.26]
    elif n == 3:
        x_offsets = [-0.32, 0.0, 0.32]
    else:
        x_offsets = np.linspace(-0.42, 0.42, n).tolist()

    mi = modality_order.index(mod)
    for s, dx in zip(group, x_offsets):
        author = s["author_year"].split(" ")[0]
        year   = s["author_year"].split("(")[1].rstrip(")")
        xs.append(xi + dx)
        ys.append(yi_center)
        sizes.append(bsize(s["N"]))
        colors.append(COL[s["effect_direction"]])
        labels.append(f"{author}\n({year})")
        # Label placement rules:
        # sMRI (mi=5, top row): label BELOW to avoid top edge clipping
        # rsEEG (mi=0, bottom row): label ABOVE (into its own row, away from bottom)
        # ERP (mi=1): label ABOVE (away from rsEEG row below)
        # others: alternate
        if mi == 5:
            label_va.append("below")
        elif mi == 0:
            label_va.append("above")
        elif mi == 1:
            label_va.append("above")
        else:
            label_va.append("above" if mi % 2 == 0 else "below")

# ── figure: wider right margin for size legend ────────────────────────────
fig = plt.figure(figsize=(14, 9.5))
# Main axes ends at 0.78; ax_leg starts at 0.84 — guaranteed no overlap
ax     = fig.add_axes([0.06, 0.10, 0.75, 0.84])
ax_leg = fig.add_axes([0.84, 0.22, 0.14, 0.60])
ax_leg.axis("off")

# scatter
ax.scatter(xs, ys, s=sizes, c=colors,
           alpha=0.82, edgecolors="white", linewidths=1.6, zorder=3)

# labels
pts_per_unit = 72.5
for x, y, lbl, va_dir, sz in zip(xs, ys, labels, label_va, sizes):
    r_data = math.sqrt(sz) / 2 / pts_per_unit
    dy = r_data + 0.10
    if va_dir == "above":
        ax.text(x, y + dy, lbl, ha="center", va="bottom",
                fontsize=6.8, color="#333333", zorder=5, linespacing=1.3)
    else:
        ax.text(x, y - dy, lbl, ha="center", va="top",
                fontsize=6.8, color="#333333", zorder=5, linespacing=1.3)

# ── axes ───────────────────────────────────────────────────────────────────
y_tick_pos    = [mod_y[m] for m in modality_order]

ax.set_xticks(range(len(age_order)))
ax.set_xticklabels(age_order, fontsize=10)
ax.set_yticks(y_tick_pos)
ax.set_yticklabels(modality_order, fontsize=10.5, fontstyle="italic")
ax.set_xlim(-0.75, len(age_order) - 0.25)
ax.set_ylim(-1.0, max(y_tick_pos) + 1.2)

ax.set_xlabel("Age group at neural measurement", fontsize=11, labelpad=7)
ax.set_ylabel("Neural modality", fontsize=11, labelpad=7)
ax.set_title("Figure 2.  Included studies by neural modality and age group",
             fontsize=11.5, fontweight="bold", pad=10, loc="left")

for ytp in y_tick_pos:
    ax.axhline(ytp, color="#ebebeb", linewidth=0.6, zorder=0)
for xtp in range(len(age_order)):
    ax.axvline(xtp, color="#ebebeb", linewidth=0.6, zorder=0)

ax.set_facecolor("white")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#cccccc")
ax.spines["bottom"].set_color("#cccccc")

# ── direction legend — LOWER LEFT to avoid covering sMRI/Neonatal ─────────
legend_handles = [
    mpatches.Patch(color=COL["positive"], label="Positive association (k = 15)"),
    mpatches.Patch(color=COL["negative"], label="Negative association (k = 1)"),
]
ax.legend(handles=legend_handles, loc="lower left", fontsize=9,
          frameon=True, framealpha=0.95, edgecolor="#cccccc",
          handlelength=1.2, handleheight=1.0)

# ── size legend (right panel, no overlap) ─────────────────────────────────
ax_leg.set_xlim(0, 1)
ax_leg.set_ylim(0, 1)
ax_leg.text(0.5, 0.97, "Sample\nsize (N)", ha="center", va="top",
            fontsize=9, fontweight="bold", color="#333333")

ref_ns    = [30, 100, 250, 373]
ref_pos_y = [0.78, 0.57, 0.33, 0.10]
max_r = math.sqrt(bsize(373)) / 2

for n_ref, yp in zip(ref_ns, ref_pos_y):
    r_rel  = math.sqrt(bsize(n_ref)) / max_r
    r_disp = r_rel * 0.10
    circ = mpatches.Circle((0.35, yp), r_disp,
                            color="#3A7ABF", alpha=0.75,
                            transform=ax_leg.transAxes, zorder=3)
    ax_leg.add_patch(circ)
    ax_leg.text(0.62, yp, f"N = {n_ref}", ha="left", va="center",
                fontsize=8.5, color="#333333", transform=ax_leg.transAxes)

# ── footnote ──────────────────────────────────────────────────────────────
fig.text(0.05, 0.005,
         "† Brito & Noble (2020): p = .025, did not survive FDR correction.  "
         "Ramphal et al. (2020): neural measurement at neonatal period; longitudinal follow-up to 2 yr for behavioural outcomes.  "
         "Lange et al. (2010): IQ as neural-cognitive proxy; brain volume as covariate.",
         fontsize=7, color="#666666", va="bottom")

plt.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Saved: {out_path}")
