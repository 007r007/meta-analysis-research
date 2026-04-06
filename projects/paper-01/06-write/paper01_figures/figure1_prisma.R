# Figure 1: PRISMA 2020 Flow Diagram
# Paper 01 — WM Training Systematic Review
# Requires: ggplot2, ggforce (or DiagrammeR or gridExtra)
# Simpler approach: use the 'PRISMAstatement' package or base ggplot2 boxes
# Here we use ggplot2 + annotation for full control

library(ggplot2)
library(grid)

# ─────────────────────────────────────────────────
# DATA (from actual screening statistics)
# ─────────────────────────────────────────────────
# Identification
n_pubmed     <- NA   # To be filled from search logs
n_psycinfo   <- NA
n_wos        <- NA
n_cnki       <- NA
n_identified <- 4168  # After deduplication

# Screening
n_title_abs_screened   <- 4168
n_title_abs_excluded   <- 4168 - 445   # = 3723
n_reasons_automation   <- 2379         # Stage 1 (automated keyword filter)
n_reasons_manual       <- 1344         # Stage 2 (title/abstract review)

# Full-text eligibility
n_fulltext_assessed    <- 445
n_fulltext_excluded    <- 15
n_excluded_population  <- 12           # E1: age/population
n_excluded_intervention<- 2            # E2: not WM-focused
n_excluded_design      <- 1            # E4: design criteria
n_included             <- 56

# ─────────────────────────────────────────────────
# DRAW PRISMA BOXES using ggplot2
# ─────────────────────────────────────────────────

draw_prisma <- function() {

  # Set up blank canvas
  p <- ggplot() +
    xlim(0, 10) + ylim(0, 20) +
    theme_void() +
    theme(plot.margin = margin(10, 10, 10, 10))

  # Helper: draw a labeled box
  box <- function(p, x, y, w, h, label, fill = "white", color = "black", size = 3) {
    p + annotate("rect",
                 xmin = x - w/2, xmax = x + w/2,
                 ymin = y - h/2, ymax = y + h/2,
                 fill = fill, color = color) +
      annotate("text",
               x = x, y = y, label = label,
               size = size, hjust = 0.5, vjust = 0.5, lineheight = 0.9)
  }

  add_arrow <- function(p, x1, y1, x2, y2) {
    p + annotate("segment",
                 x = x1, xend = x2, y = y1, yend = y2,
                 arrow = grid::arrow(length = unit(0.2, "cm"), type = "closed"),
                 color = "black")
  }

  # ── IDENTIFICATION ──────────────────────────────
  p <- box(p, 5, 19, 8, 1.2,
           sprintf("Records identified through database searching\n(n = 4,168 after deduplication)"),
           fill = "#E8F4F8")

  p <- add_arrow(p, 5, 18.4, 5, 17.2)

  # ── SCREENING ───────────────────────────────────
  p <- box(p, 5, 16.8, 8, 1.2,
           sprintf("Records screened\n(title/abstract; n = %d)", n_title_abs_screened),
           fill = "#E8F4F8")

  # Excluded box (right side)
  p <- box(p, 8.5, 15.8, 2.8, 1.2,
           sprintf("Records excluded\n(n = %d)\n  Stage 1 (keyword): %d\n  Stage 2 (review): %d",
                   n_title_abs_excluded, n_reasons_automation, n_reasons_manual),
           fill = "#FFF3E0", size = 2.5)

  p <- p + annotate("segment",
                    x = 9, xend = 7.2, y = 16.8, yend = 16.8,
                    arrow = grid::arrow(length = unit(0.2, "cm"), type = "closed"),
                    color = "black")

  p <- add_arrow(p, 5, 16.2, 5, 15)

  # ── ELIGIBILITY ─────────────────────────────────
  p <- box(p, 5, 14.6, 8, 1.2,
           sprintf("Full-text articles assessed for eligibility\n(n = %d)", n_fulltext_assessed),
           fill = "#E8F4F8")

  # Excluded full-text box
  p <- box(p, 8.5, 13.3, 2.8, 1.8,
           sprintf("Full-text articles excluded\n(n = %d)\n  Population (E1): n = %d\n  Intervention (E2): n = %d\n  Design (E4): n = %d",
                   n_fulltext_excluded,
                   n_excluded_population, n_excluded_intervention, n_excluded_design),
           fill = "#FFF3E0", size = 2.5)

  p <- p + annotate("segment",
                    x = 9, xend = 7.2, y = 14.6, yend = 14.6,
                    arrow = grid::arrow(length = unit(0.2, "cm"), type = "closed"),
                    color = "black")

  p <- add_arrow(p, 5, 14.0, 5, 12.8)

  # ── INCLUDED ────────────────────────────────────
  p <- box(p, 5, 12.4, 8, 1.2,
           sprintf("Studies included in narrative synthesis\n(n = %d)", n_included),
           fill = "#E8F5E9", color = "#2E7D32")

  # ── TITLE ───────────────────────────────────────
  p <- p + labs(title = "Figure 1. PRISMA 2020 Flow Diagram") +
    theme(plot.title = element_text(size = 12, face = "bold", hjust = 0.5,
                                    margin = margin(b = 10)))

  return(p)
}

p_prisma <- draw_prisma()

# Save
ggsave(
  filename = "E:/Meta-analysis writing project/projects/paper-01/06-write/paper01_figures/figure1_prisma.png",
  plot = p_prisma,
  width = 8, height = 10, dpi = 300, bg = "white"
)

cat("Figure 1 (PRISMA) saved.\n")
