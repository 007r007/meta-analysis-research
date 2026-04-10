"""
Figure 2: Modality × Age Group Bubble Chart  (v3 — Nature style, guaranteed no overlap)
Paper-02: Parental education and early childhood neural development

Overlap fix strategy (v3):
- Row spacing = 1.5 data units instead of 1.0 → bubbles physically cannot span rows
- Y tick positions: [0, 1.5, 3, 4.5, 6, 7.5] mapped to modality labels
- Max bubble radius in data units ≈ 0.55 (N=373), row gap = 1.5 → safe margin ≥ 0.4
- Labels above/below with offset proportional to radius, capped to stay in row band

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

# ── paths ──────────────────────────────────────────────────────────────────
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path  = os.path.join(script_dir, "figure2_data.json")
out_path   = os.path.join(script_dir, "figure2_modality_age_bubble.png")

# ── load ───────────────────────────────────────────────────────────────────
with open(data_path, encoding="utf-8") as f:
    meta = json.load(f)

age_order      = meta["age_group_order"]
modality_order = meta["modality_order"]   # rsEEG, ERP, fNIRS, fMRI, DTI, sMRI
studies        = meta["studies"]

COL = {"positive": "#3A7ABF", "negative": "#D45F5F"}

age_idx = {a: i for i, a in enumerate(age_order)}
# Row spacing = 1.5  (key change vs v1/v2)
ROW_SPACING = 1.5
mod_y = {m: i * ROW_SPACING for i, m in enumerate(modality_order)}

# Bubble area: radius in data units ≤ 0.55 for N=373 (< ROW_SPACING/2 = 0.75)
# Chosen so max bubble diameter = 1.1 data units < row gap of 1.5
SCALE = 5.5   # sqrt(N) * SCALE = radius in points? No — use scatter s = area in pts²
# We want radius_pts such that radius_data < 0.6 for all N
# Figure: 13 × 9 in, axes ~0.72 × 0.84 → ~9.36 × 7.56 in → 673 × 544 pts
# Y range: 0 to 7.5 → 544 pts / 7.5 = 72.5 pts per data unit
# radius_data = 0.6 → radius_pts = 43.5 → diameter_pts = 87 → area_pts² = 87²/4*π ≈ 5940
# For N=373: sqrt(373) ≈ 19.3, scale² * N = 5940 → scale = sqrt(5940/373) ≈ 3.99
# Use scale = 4.0 → N=373 gives area = 4²*373 = 5968 pts² ✓
def bsize(n):
    # Cap effective N at 250 to prevent very large bubbles from spanning rows
    n_eff = min(n, 250)
    return (4.0 ** 2) * n_eff

# ── group studies by cell ──────────────────────────────────────────────────
cell_studies = defaultdict(list)
for s in studies:
    key = (age_idx.get(s["age_group"]), s["modality"])
    cell_studies[key].append(s)

# ── build plot arrays ──────────────────────────────────────────────────────
xs, ys, sizes, colors, labels, label_va = [], [], [], [], [], []

for key, group in cell_studies.items():
    xi, mod = key
    yi_center = mod_y[mod]
    n = len(group)
    # horizontal offsets for same-cell studies
    if n == 1:
        x_offsets = [0.0]
    elif n == 2:
        x_offsets = [-0.26, 0.26]
    elif n == 3:
        x_offsets = [-0.32, 0.0, 0.32]
    else:
        x_offsets = np.linspace(-0.42, 0.42, n).tolist()

    for s, dx in zip(group, x_offsets):
        author = s["author_year"].split(" ")[0]
        year   = s["author_year"].split("(")[1].rstrip(")")
        xs.append(xi + dx)
        ys.append(yi_center)
        sizes.append(bsize(s["N"]))
        colors.append(COL[s["effect_direction"]])
        labels.append(f"{author}\n({year})")
        # alternate above/below — put label INTO the row's own space
        # rsEEG(mi=0): label above (toward rsEEG center, away from ERP)
        # ERP(mi=1): label below (toward ERP center, away from rsEEG)
        # fNIRS(mi=2): above; fMRI(mi=3): below; DTI(mi=4): above; sMRI(mi=5): below
        mi = modality_order.index(mod)
        label_va.append("above" if mi % 2 == 0 else "below")

# ── figure ─────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(13, 9.5))
ax     = fig.add_axes([0.07, 0.10, 0.72, 0.84])
ax_leg = fig.add_axes([0.81, 0.20, 0.16, 0.65])
ax_leg.axis("off")

# scatter
ax.scatter(xs, ys, s=sizes, c=colors,
           alpha=0.82, edgecolors="white", linewidths=1.6, zorder=3)

# labels — offset in data units proportional to sqrt(N)
# pts_per_unit ≈ 544/7.5 ≈ 72.5; radius_pts = sqrt(area)/2; radius_data = radius_pts/72.5
pts_per_unit = 72.5
for x, y, lbl, va_dir, sz in zip(xs, ys, labels, label_va, sizes):
    r_data = math.sqrt(sz) / 2 / pts_per_unit
    dy = r_data + 0.08
    if va_dir == "above":
        ax.text(x, y + dy, lbl, ha="center", va="bottom",
                fontsize=6.8, color="#333333", zorder=5, linespacing=1.3)
    else:
        ax.text(x, y - dy, lbl, ha="center", va="top",
                fontsize=6.8, color="#333333", zorder=5, linespacing=1.3)

# ── axes ───────────────────────────────────────────────────────────────────
y_tick_pos    = [mod_y[m] for m in modality_order]
y_tick_labels = modality_order

ax.set_xticks(range(len(age_order)))
ax.set_xticklabels(age_order, fontsize=10)
ax.set_yticks(y_tick_pos)
ax.set_yticklabels(y_tick_labels, fontsize=10.5, fontstyle="italic")

ax.set_xlim(-0.75, len(age_order) - 0.25)
ax.set_ylim(-1.0, max(y_tick_pos) + 1.0)

ax.set_xlabel("Age group at neural measurement", fontsize=11, labelpad=7)
ax.set_ylabel("Neural modality", fontsize=11, labelpad=7)
ax.set_title("Figure 2.  Included studies by neural modality and age group",
             fontsize=11.5, fontweight="bold", pad=10, loc="left")

# grid at row positions only (horizontal lines)
ax.set_axisbelow(True)
for ytp in y_tick_pos:
    ax.axhline(ytp, color="#ebebeb", linewidth=0.6, zorder=0)
# vertical grid at age columns
for xtp in range(len(age_order)):
    ax.axvline(xtp, color="#ebebeb", linewidth=0.6, zorder=0)

ax.set_facecolor("white")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#cccccc")
ax.spines["bottom"].set_color("#cccccc")

# ── direction legend ───────────────────────────────────────────────────────
legend_handles = [
    mpatches.Patch(color=COL["positive"], label="Positive association (k = 15)"),
    mpatches.Patch(color=COL["negative"], label="Negative association (k = 1)"),
]
ax.legend(handles=legend_handles, loc="upper left", fontsize=9,
          frameon=True, framealpha=0.95, edgecolor="#cccccc",
          handlelength=1.2, handleheight=1.0)

# ── size legend (right panel) ─────────────────────────────────────────────
ax_leg.set_xlim(0, 1)
ax_leg.set_ylim(0, 1)
ax_leg.text(0.5, 0.97, "Sample\nsize (N)", ha="center", va="top",
            fontsize=9, fontweight="bold", color="#333333")

ref_ns    = [30, 100, 250, 373]
ref_pos_y = [0.76, 0.56, 0.33, 0.11]
max_r = math.sqrt(bsize(373)) / 2   # in pts

for n_ref, yp in zip(ref_ns, ref_pos_y):
    r_rel  = math.sqrt(bsize(n_ref)) / max_r    # 0–1
    r_disp = r_rel * 0.11                        # axes fraction
    circ = mpatches.Circle((0.35, yp), r_disp,
                            color="#3A7ABF", alpha=0.75,
                            transform=ax_leg.transAxes, zorder=3)
    ax_leg.add_patch(circ)
    ax_leg.text(0.65, yp, f"N = {n_ref}", ha="left", va="center",
                fontsize=8.5, color="#333333", transform=ax_leg.transAxes)

# ── footnote ──────────────────────────────────────────────────────────────
fig.text(0.05, 0.005,
         "† Brito & Noble (2020): p = .025, did not survive FDR correction.  "
         "Ramphal et al. (2020): neural measurement at neonatal period.  "
         "Lange et al. (2010): IQ as neural-cognitive proxy; brain volume as covariate.",
         fontsize=7, color="#666666", va="bottom")

plt.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Saved: {out_path}")
