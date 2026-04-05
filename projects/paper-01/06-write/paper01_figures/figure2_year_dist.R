# Figure 2: Publication Year Distribution
# Paper 01 — WM Training Systematic Review
# Requires: ggplot2

library(ggplot2)
library(dplyr)

# ─────────────────────────────────────────────────
# DATA: Publication years for all 56 included studies
# ─────────────────────────────────────────────────
years_data <- data.frame(
  seq = c(1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,
          27,28,29,30,31,32,34,35,36,39,40,41,43,44,45,46,47,48,49,50,51,52,
          53,54,55,57,59,60,61,62,63,67),
  year = c(2020,2019,2016,2015,2018,2020,2025,2017,2022,2016,2016,2019,2021,
           2019,2020,2014,2013,2020,2018,2022,2024,2022,2014,2020,2024,2020,
           2014,2017,2013,2014,2022,2003,2014,2008,2023,2017,2017,2025,2016,
           2013,2018,2025,2017,2012,2016,2023,2017,2021,2022,2014,2021,2026,
           2021,2020,2015,2026)
)

# Count by year
year_counts <- years_data %>%
  group_by(year) %>%
  summarise(n = n()) %>%
  arrange(year)

# Add any missing years as 0 (for continuous x-axis)
all_years <- data.frame(year = seq(min(year_counts$year), max(year_counts$year), by = 1))
year_counts_full <- left_join(all_years, year_counts, by = "year") %>%
  mutate(n = ifelse(is.na(n), 0, n))

# ─────────────────────────────────────────────────
# PLOT
# ─────────────────────────────────────────────────
p2 <- ggplot(year_counts_full, aes(x = year, y = n)) +
  geom_col(fill = "#4472C4", color = "white", width = 0.8) +
  geom_text(data = subset(year_counts_full, n > 0),
            aes(label = n), vjust = -0.4, size = 3.2, color = "#333333") +
  scale_x_continuous(
    breaks = seq(2003, 2026, by = 2),
    labels = seq(2003, 2026, by = 2),
    expand = c(0.01, 0.01)
  ) +
  scale_y_continuous(
    breaks = 0:8,
    limits = c(0, 8.5),
    expand = c(0, 0)
  ) +
  labs(
    title = "Figure 2. Distribution of Included Studies by Publication Year",
    x = "Publication Year",
    y = "Number of Studies (k)",
    caption = paste0("Note. Total k = 56 studies (2003–2026).",
                     " Peak years: 2020 (k = 7), 2014 (k = 6), 2017 (k = 6).")
  ) +
  theme_classic(base_size = 11) +
  theme(
    plot.title = element_text(face = "bold", hjust = 0.5, size = 12,
                               margin = margin(b = 8)),
    plot.caption = element_text(hjust = 0, size = 8.5, color = "#555555",
                                 margin = margin(t = 8)),
    axis.text.x = element_text(angle = 45, hjust = 1, size = 9),
    axis.text.y = element_text(size = 9),
    panel.grid.major.y = element_line(color = "#DDDDDD", linewidth = 0.4),
    plot.margin = margin(15, 20, 10, 15)
  )

# Save
ggsave(
  filename = "E:/Meta-analysis writing project/projects/paper-01/06-write/paper01_figures/figure2_year_dist.png",
  plot = p2,
  width = 9, height = 5, dpi = 300, bg = "white"
)

cat("Figure 2 (year distribution) saved.\n")
cat("Year summary:\n")
print(year_counts_full[year_counts_full$n > 0, ])
