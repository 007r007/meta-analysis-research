# Figure 3: Moderator Summary Visualization
# Paper 01 — WM Training Systematic Review
# Requires: ggplot2, dplyr, tidyr

# This figure presents a visual summary of outcome distributions (Positive/Null/Mixed)
# across key moderator subgroups, using stacked bar charts.

library(ggplot2)
library(dplyr)
library(tidyr)

# ─────────────────────────────────────────────────
# DATA: Outcome counts by moderator subgroup
# Based on narrative synthesis from 56 studies
# (Exact counts should be verified from Excel data)
# ─────────────────────────────────────────────────

moderator_data <- data.frame(
  moderator = c(
    # Control group type
    "Active control", "Active control",  "Active control",
    "Passive/no control", "Passive/no control", "Passive/no control",
    # Training type
    "N-back", "N-back", "N-back",
    "Span/Other", "Span/Other", "Span/Other",
    # Combined intervention
    "Pure WM only", "Pure WM only", "Pure WM only",
    "WM + tDCS/stim", "WM + tDCS/stim", "WM + tDCS/stim",
    # Adaptive
    "Adaptive", "Adaptive", "Adaptive",
    "Non-adaptive", "Non-adaptive", "Non-adaptive",
    # Dose (sessions)
    "≤10 sessions", "≤10 sessions", "≤10 sessions",
    "11-25 sessions", "11-25 sessions", "11-25 sessions",
    ">25 sessions", ">25 sessions", ">25 sessions"
  ),
  group = c(
    "Control type", "Control type", "Control type",
    "Control type", "Control type", "Control type",
    "Training type", "Training type", "Training type",
    "Training type", "Training type", "Training type",
    "Co-intervention", "Co-intervention", "Co-intervention",
    "Co-intervention", "Co-intervention", "Co-intervention",
    "Adaptivity", "Adaptivity", "Adaptivity",
    "Adaptivity", "Adaptivity", "Adaptivity",
    "Training dose", "Training dose", "Training dose",
    "Training dose", "Training dose", "Training dose",
    "Training dose", "Training dose", "Training dose"
  ),
  outcome = rep(c("Positive", "Mixed", "Null"), 11),
  # Approximate counts — verify against final cross-tabulation
  k = c(
    # Active control (n=46): Positive=6, Mixed=8, Null=32
    6, 8, 32,
    # Passive/no control (n=10): Positive=2, Mixed=5, Null=3  [Seq3 Salminen → Mixed]
    2, 5, 3,
    # N-back (n=44): Positive=5, Mixed=13, Null=26  [Seq3 Salminen → Mixed]
    5, 13, 26,
    # Span/Other (n=12): Positive=3, Mixed=0, Null=9
    3, 0, 9,
    # Pure WM only (n=15): Positive=1, Mixed=2, Null=12
    1, 2, 12,
    # WM + stimulation (n=14): Positive=3, Mixed=5, Null=6
    3, 5, 6,
    # Adaptive (n=46): Positive=3, Mixed=11, Null=32  [Seq3 Salminen → Mixed]
    3, 11, 32,
    # Non-adaptive (n=10): Positive=5, Mixed=2, Null=3
    5, 2, 3,
    # ≤10 sessions (n=23): Positive=3, Mixed=5, Null=15
    3, 5, 15,
    # 11-25 sessions (n=25): Positive=5, Mixed=7, Null=13  [Seq3 Salminen → Mixed]
    5, 7, 13,
    # >25 sessions (n=3): Positive=0, Mixed=0, Null=3
    0, 0, 3
  )
)

# Calculate percentages within each moderator
moderator_data <- moderator_data %>%
  group_by(moderator) %>%
  mutate(
    total = sum(k),
    pct = k / total * 100
  ) %>%
  ungroup()

# Factor ordering
moderator_data$outcome <- factor(moderator_data$outcome,
                                  levels = c("Positive", "Mixed", "Null"))

# Ordering of moderator labels (within each group)
moderator_data$moderator <- factor(moderator_data$moderator,
  levels = c(
    "Active control", "Passive/no control",
    "N-back", "Span/Other",
    "Pure WM only", "WM + tDCS/stim",
    "Adaptive", "Non-adaptive",
    "≤10 sessions", "11-25 sessions", ">25 sessions"
  )
)

# Group factor (for facet)
moderator_data$group <- factor(moderator_data$group,
  levels = c("Control type", "Training type", "Co-intervention", "Adaptivity", "Training dose")
)

# ─────────────────────────────────────────────────
# COLORS
# ─────────────────────────────────────────────────
outcome_colors <- c(
  "Positive" = "#2E7D32",   # Dark green
  "Mixed"    = "#F9A825",   # Amber
  "Null"     = "#C62828"    # Dark red
)

# ─────────────────────────────────────────────────
# PLOT: Faceted horizontal stacked bar chart
# ─────────────────────────────────────────────────
p3 <- ggplot(moderator_data,
             aes(x = moderator, y = pct, fill = outcome)) +
  geom_col(width = 0.7, position = "stack") +
  geom_text(
    aes(label = ifelse(k >= 2, paste0(k), "")),
    position = position_stack(vjust = 0.5),
    size = 2.8, color = "white", fontface = "bold"
  ) +
  scale_fill_manual(
    values = outcome_colors,
    name = "Transfer outcome",
    breaks = c("Positive", "Mixed", "Null")
  ) +
  scale_y_continuous(
    labels = function(x) paste0(x, "%"),
    breaks = seq(0, 100, by = 25),
    expand = c(0, 0)
  ) +
  facet_wrap(~ group, scales = "free_y", ncol = 1, strip.position = "left") +
  coord_flip() +
  labs(
    title = "Figure 3. Distribution of Transfer Outcomes by Moderator Subgroup",
    x = NULL,
    y = "Percentage of Studies",
    caption = paste0(
      "Note. Numbers within bars = k (number of studies).\n",
      "Positive = statistically significant between-group transfer advantage;\n",
      "Null = no significant between-group differences;\n",
      "Mixed = significant effects on some outcomes only.\n",
      "Based on 56 included studies. Counts are approximate; see Table 3 for details."
    )
  ) +
  theme_classic(base_size = 10) +
  theme(
    plot.title = element_text(face = "bold", hjust = 0.5, size = 11,
                               margin = margin(b = 8)),
    strip.text.y.left = element_text(angle = 0, face = "bold", size = 9,
                                      hjust = 1),
    strip.placement = "outside",
    strip.background = element_rect(fill = "#F5F5F5", color = NA),
    legend.position = "bottom",
    legend.title = element_text(size = 9, face = "bold"),
    legend.text = element_text(size = 9),
    panel.spacing.y = unit(0.4, "cm"),
    plot.caption = element_text(hjust = 0, size = 8, color = "#555555",
                                 margin = margin(t = 8)),
    plot.margin = margin(15, 20, 10, 15),
    axis.text.y = element_text(size = 9),
    axis.text.x = element_text(size = 9)
  )

# Save
ggsave(
  filename = "E:/Meta-analysis writing project/projects/paper-01/06-write/paper01_figures/figure3_moderator_summary.png",
  plot = p3,
  width = 8, height = 10, dpi = 300, bg = "white"
)

cat("Figure 3 (moderator summary) saved.\n")

# ─────────────────────────────────────────────────
# NOTE ON DATA ACCURACY
# ─────────────────────────────────────────────────
# The k counts above are APPROXIMATE, derived from the narrative summary in the
# paper draft (Section 3.4). Before final submission, these should be verified
# against the cross-tabulation of the raw Excel data:
#   04-extract/数据_6_数据提取表_v3_research.xlsx
# Fields used: col40 (总体结论), col24 (主动对照), col17 (训练类型),
#              col19 (自适应), col26 (结合干预), col20 (训练总次数)
