# Figure 1: PRISMA 2020 Flow Diagram
# Paper 01 — WM Training Systematic Review
# Requires: ggplot2, grid

library(ggplot2)
library(grid)

# ─────────────────────────────────────────────────
# DATA (from actual screening statistics)
# ─────────────────────────────────────────────────
n_identified        <- 4168
n_title_abs_screened <- 4168
n_title_abs_excluded <- 3723
n_reasons_automation <- 2379
n_reasons_manual     <- 1344
n_fulltext_assessed  <- 445
n_fulltext_excluded  <- 15
n_excluded_population   <- 12
n_excluded_intervention <- 2
n_excluded_design       <- 1
n_included           <- 56

# ─────────────────────────────────────────────────
# LAYOUT: coordinate system 0-100 x 0-100
# Left column (main flow): x=35, right column (excluded): x=78
# Rows from top: y = 92, 78, 64, 50, 36
# ─────────────────────────────────────────────────

draw_prisma <- function() {

  p <- ggplot() +
    xlim(0, 100) + ylim(0, 100) +
    theme_void() +
    theme(plot.margin = margin(5, 5, 5, 5),
          plot.title = element_text(size = 13, face = "bold",
                                    hjust = 0.5, margin = margin(b = 8)))

  # ── helper: filled rectangle + text ────────────
  draw_box <- function(p, cx, cy, w, h, txt,
                       fill = "white", border = "#333333", tsize = 3.2) {
    p + annotate("rect",
                 xmin = cx - w/2, xmax = cx + w/2,
                 ymin = cy - h/2, ymax = cy + h/2,
                 fill = fill, color = border, linewidth = 0.5) +
      annotate("text", x = cx, y = cy, label = txt,
               size = tsize, hjust = 0.5, vjust = 0.5, lineheight = 1.0)
  }

  # ── helper: vertical arrow ──────────────────────
  v_arrow <- function(p, x, y1, y2) {
    p + annotate("segment", x = x, xend = x, y = y1, yend = y2,
                 arrow = grid::arrow(length = unit(0.25, "cm"), type = "closed"),
                 color = "#333333", linewidth = 0.5)
  }

  # ── helper: horizontal line (no arrow) ─────────
  h_line <- function(p, x1, x2, y) {
    p + annotate("segment", x = x1, xend = x2, y = y, yend = y,
                 color = "#333333", linewidth = 0.5)
  }

  # ── helper: horizontal arrow ───────────────────
  h_arrow <- function(p, x1, x2, y) {
    p + annotate("segment", x = x1, xend = x2, y = y, yend = y,
                 arrow = grid::arrow(length = unit(0.25, "cm"), type = "closed"),
                 color = "#333333", linewidth = 0.5)
  }

  # ── Section labels (left margin) ───────────────
  p <- p +
    annotate("text", x = 3, y = 89, label = "Identification",
             size = 3.2, fontface = "bold", angle = 90, hjust = 0.5, color = "#555555") +
    annotate("text", x = 3, y = 72, label = "Screening",
             size = 3.2, fontface = "bold", angle = 90, hjust = 0.5, color = "#555555") +
    annotate("text", x = 3, y = 53, label = "Eligibility",
             size = 3.2, fontface = "bold", angle = 90, hjust = 0.5, color = "#555555") +
    annotate("text", x = 3, y = 30, label = "Included",
             size = 3.2, fontface = "bold", angle = 90, hjust = 0.5, color = "#555555")

  # ── ROW 1: Identification (y=89) ───────────────
  p <- draw_box(p, cx=40, cy=89, w=50, h=8,
                sprintf("Records identified through\ndatabase searching\n(n = %s after deduplication)",
                        format(n_identified, big.mark=",")),
                fill="#E3F2FD")

  # arrow down
  p <- v_arrow(p, x=40, y1=85, y2=81)

  # ── ROW 2: Screening (y=77) ────────────────────
  p <- draw_box(p, cx=40, cy=77, w=50, h=8,
                sprintf("Records screened\n(title/abstract; n = %s)",
                        format(n_title_abs_screened, big.mark=",")),
                fill="#E3F2FD")

  # horizontal line from main box to excluded box
  p <- h_line(p, x1=65, x2=75, y=77)
  p <- h_arrow(p, x1=75, x2=91, y=77)

  # excluded box (right, y=77)
  p <- draw_box(p, cx=91, cy=72, w=16, h=14,
                sprintf("Records excluded\n(n = %s)\n  Stage 1: %s\n  Stage 2: %s",
                        format(n_title_abs_excluded, big.mark=","),
                        format(n_reasons_automation, big.mark=","),
                        format(n_reasons_manual, big.mark=",")),
                fill="#FFF8E1", tsize=2.8)

  # arrow down
  p <- v_arrow(p, x=40, y1=73, y2=69)

  # ── ROW 3: Eligibility (y=65) ──────────────────
  p <- draw_box(p, cx=40, cy=65, w=50, h=8,
                sprintf("Full-text articles assessed\nfor eligibility (n = %d)",
                        n_fulltext_assessed),
                fill="#E3F2FD")

  # horizontal to excluded
  p <- h_line(p, x1=65, x2=75, y=65)
  p <- h_arrow(p, x1=75, x2=91, y=65)

  # excluded full-text box (right, y=55)
  p <- draw_box(p, cx=91, cy=53, w=16, h=18,
                sprintf("Full-text excluded\n(n = %d)\n  Population: n = %d\n  Intervention: n = %d\n  Design: n = %d",
                        n_fulltext_excluded,
                        n_excluded_population,
                        n_excluded_intervention,
                        n_excluded_design),
                fill="#FFF8E1", tsize=2.8)

  # arrow down
  p <- v_arrow(p, x=40, y1=61, y2=38)

  # ── ROW 4: Included (y=30) ─────────────────────
  p <- draw_box(p, cx=40, cy=30, w=50, h=10,
                sprintf("Studies included in\nnarrative synthesis\n(n = %d)", n_included),
                fill="#E8F5E9", border="#2E7D32")

  # title
  p <- p + labs(title = "Figure 1. PRISMA 2020 Flow Diagram")

  return(p)
}

p_prisma <- draw_prisma()

ggsave(
  filename = "E:/Meta-analysis writing project/projects/paper-01/06-write/paper01_figures/figure1_prisma.png",
  plot = p_prisma,
  width = 9, height = 11, dpi = 300, bg = "white"
)

cat("Figure 1 (PRISMA) saved.\n")
