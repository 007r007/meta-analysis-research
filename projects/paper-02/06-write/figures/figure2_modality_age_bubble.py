"""
Figure 2: Modality × Age Group Bubble Chart  (v6 — strict vertical separation)

Fixes vs v5:
- Three layout zones strictly separated:
    main axes:   [left=0.07, bottom=0.27, width=0.90, height=0.67]
    size legend: [left=0.07, bottom=0.11, width=0.90, height=0.13]
    footnote:     fig.text at y=0.005, well below size legend
- Size legend: NO set_aspect("equal") — instead use transform-aware radius
  approach: draw circles via scatter with fixed s values, place at y=0.5 in
  a dedicated axes whose ylim is set so circles don't overflow
- Footnote text: wrapped to two lines so it never reaches legend area
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
modality_order = meta["modality_order"]
studies        = meta["studies"]

COL = {"positive": "#3A7ABF", "negative": "#D45F5F"}

age_idx     = {a: i for i, a in enumerate(age_order)}
ROW_SPACING = 1.5
mod_y       = {m: i * ROW_SPACING for i, m in enumerate(modality_order)}

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
        if mi == 5:          # sMRI top row → label below
            label_va.append("below")
        elif mi in (0, 1):   # rsEEG, ERP bottom rows → label above
            label_va.append("above")
        else:
            label_va.append("above" if mi % 2 == 0 else "below")

# ── figure ────────────────────────────────────────────────────────────────
# Zone map (figure fraction):
#   0.000 – 0.030  : bottom margin
#   0.030 – 0.095  : footnote text  (fig.text y≈0.03–0.09)
#   0.095 – 0.100  : gap
#   0.100 – 0.240  : size legend axes
#   0.240 – 0.260  : gap / x-axis label of main axes
#   0.260 – 0.950  : main scatter axes
#   0.950 – 1.000  : title

fig = plt.figure(figsize=(13, 11))

# ── main axes ──────────────────────────────────────────────────────────────
ax = fig.add_axes([0.07, 0.26, 0.90, 0.69])

ax.scatter(xs, ys, s=sizes, c=colors,
           alpha=0.82, edgecolors="white", linewidths=1.6, zorder=3)

pts_per_unit = 72.0
for x, y, lbl, va_dir, sz in zip(xs, ys, labels, label_va, sizes):
    r_data = math.sqrt(sz) / 2 / pts_per_unit
    dy = r_data + 0.10
    if va_dir == "above":
        ax.text(x, y + dy, lbl, ha="center", va="bottom",
                fontsize=6.8, color="#333333", zorder=5, linespacing=1.3)
    else:
        ax.text(x, y - dy, lbl, ha="center", va="top",
                fontsize=6.8, color="#333333", zorder=5, linespacing=1.3)

y_tick_pos = [mod_y[m] for m in modality_order]
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

legend_handles = [
    mpatches.Patch(color=COL["positive"], label="Positive association (k = 15)"),
    mpatches.Patch(color=COL["negative"], label="Negative association (k = 1)"),
]
ax.legend(handles=legend_handles, loc="lower left", fontsize=9,
          frameon=True, framealpha=0.95, edgecolor="#cccccc",
          handlelength=1.2, handleheight=1.0)

# ── size legend axes ────────────────────────────────────────────────────────
# Dedicated axes occupying [0.07, 0.10, 0.90, 0.14] in figure fraction.
# xlim(0,13) keeps same x-scale logic; ylim(0,3) gives enough vertical room.
# NO set_aspect("equal") — circles rendered via scatter always look round
# in screen space; minor ellipse distortion acceptable in legend.

ax_sz = fig.add_axes([0.07, 0.10, 0.90, 0.14])
ax_sz.set_xlim(0, 13)
ax_sz.set_ylim(0, 3)
ax_sz.axis("off")

# horizontal separator line
ax_sz.plot([0, 13], [2.75, 2.75], color="#cccccc", linewidth=0.8,
           transform=ax_sz.transData)

# heading text
ax_sz.text(0.3, 2.60, "Bubble size = sample size (N):",
           ha="left", va="top", fontsize=9, fontweight="bold", color="#333333")

# reference bubbles: positioned at y=1.5 (centre of the axes middle zone)
ref_ns     = [30, 100, 250, 373]
ref_labels = ["N = 30", "N = 100", "N = 250", "N = 373 (max)"]
x_pos_data = [1.5,  4.5,  8.0,  11.5]

for n_ref, xp, lbl in zip(ref_ns, x_pos_data, ref_labels):
    ax_sz.scatter([xp], [1.5], s=bsize(n_ref),
                  color="#3A7ABF", alpha=0.75,
                  edgecolors="white", linewidths=1.2, zorder=3)
    ax_sz.text(xp, 0.35, lbl,
               ha="center", va="top", fontsize=8.5, color="#444444")

# ── footnote — placed below size legend, well clear ───────────────────────
# fig.text in figure fraction: y=0.03 puts it at ~3% from bottom,
# size legend bottom edge is at 10% → separation ≥ 7% of figure height = ~7cm clear
fig.text(0.07, 0.065,
         "† Brito & Noble (2020): p = .025, did not survive FDR correction.\n"
         "  Ramphal et al. (2020): neural measurement at neonatal period; longitudinal follow-up to 2 yr.\n"
         "  Lange et al. (2010): IQ as neural-cognitive proxy; brain volume as covariate.",
         fontsize=7, color="#666666", va="top", linespacing=1.5)

plt.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Saved: {out_path}")
