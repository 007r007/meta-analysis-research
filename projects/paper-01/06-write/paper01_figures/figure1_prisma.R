# Figure 1: PRISMA 2020 Flow Diagram — Redesigned
# Paper 01 — WM Training Systematic Review
# Clean professional layout matching published PRISMA standards

library(ggplot2)
library(grid)

# ─────────────────────────────────────────────────
# DATA
# If per-database counts are available, fill in below.
# Currently using merged total only (n_per_db = NA).
# ─────────────────────────────────────────────────
n_pubmed    <- NA   # fill if known, e.g. 1823
n_psycinfo  <- NA
n_wos       <- NA
n_cnki      <- NA
n_total_raw <- NA   # total before deduplication (if known)
n_identified <- 4168  # after deduplication

n_screened          <- 4168
n_excluded_screen   <- 3723   # 4168 - 445
n_stage1            <- 2379   # automated keyword filter
n_stage2            <- 1344   # title/abstract review

n_fulltext          <- 445
n_fulltext_excluded <- 389    # 445 - 56
n_excl_population   <- 12
n_excl_intervention <- 2
n_excl_design       <- 1
n_excl_other        <- 389 - 12 - 2 - 1   # remaining (other reasons)

n_included          <- 56

# ─────────────────────────────────────────────────
# Build identification label based on available data
# ─────────────────────────────────────────────────
if (!is.na(n_pubmed)) {
  id_label <- sprintf(
    "Records identified from databases\nPubMed (n=%d), PsycINFO (n=%d)\nWeb of Science (n=%d), CNKI (n=%d)\nTotal after deduplication: n=%s",
    n_pubmed, n_psycinfo, n_wos, n_cnki,
    format(n_identified, big.mark=","))
} else {
  id_label <- sprintf(
    "Records identified from 4 databases\n(PubMed, PsycINFO, Web of Science, CNKI)\nAfter deduplication: n = %s",
    format(n_identified, big.mark=","))
}

# ─────────────────────────────────────────────────
# COORDINATE SYSTEM: x 0–100, y 0–100
# Main column center: x = 38
# Excluded boxes center: x = 78
# Phase labels: x = 6
# Row y-centers: 88, 74, 58, 36
# ─────────────────────────────────────────────────

BOX_W   <- 44   # main box width
BOX_H   <- 10   # main box height
EX_W    <- 30   # excluded box width
EX_H_1  <- 12   # excluded box height (screening)
EX_H_2  <- 16   # excluded box height (full-text)
CX      <- 38   # main column x
EX_CX   <- 78   # excluded column x

draw_prisma <- function() {

  p <- ggplot() +
    xlim(0, 100) + ylim(0, 100) +
    theme_void() +
    theme(
      plot.background = element_rect(fill = "white", color = NA),
      plot.margin = margin(8, 8, 8, 8),
      plot.title = element_text(size = 13, face = "bold",
                                hjust = 0.5, margin = margin(b = 10))
    )

  # ── helpers ──────────────────────────────────────

  dbox <- function(p, cx, cy, w, h, txt,
                   fill = "white", border = "#2C3E50",
                   tsize = 3.1, bold = FALSE) {
    face <- ifelse(bold, "bold", "plain")
    p +
      annotate("rect",
               xmin=cx-w/2, xmax=cx+w/2,
               ymin=cy-h/2, ymax=cy+h/2,
               fill=fill, color=border, linewidth=0.6) +
      annotate("text", x=cx, y=cy, label=txt,
               size=tsize, hjust=0.5, vjust=0.5,
               lineheight=1.05, fontface=face)
  }

  varrow <- function(p, x, y1, y2) {
    p + annotate("segment", x=x, xend=x, y=y1, yend=y2,
                 arrow=grid::arrow(length=unit(0.22,"cm"), type="closed"),
                 color="#2C3E50", linewidth=0.55)
  }

  harrow <- function(p, x1, x2, y) {
    p + annotate("segment", x=x1, xend=x2, y=y, yend=y,
                 arrow=grid::arrow(length=unit(0.22,"cm"), type="closed"),
                 color="#2C3E50", linewidth=0.55)
  }

  hline <- function(p, x1, x2, y) {
    p + annotate("segment", x=x1, xend=x2, y=y, yend=y,
                 color="#2C3E50", linewidth=0.55)
  }

  vline <- function(p, x, y1, y2) {
    p + annotate("segment", x=x, xend=x, y=y1, yend=y2,
                 color="#2C3E50", linewidth=0.55)
  }

  phase_label <- function(p, y, txt) {
    p +
      annotate("rect", xmin=0.5, xmax=11, ymin=y-5, ymax=y+5,
               fill="#D6EAF8", color="#2980B9", linewidth=0.5) +
      annotate("text", x=5.8, y=y, label=txt,
               size=3.0, fontface="bold", color="#1A5276",
               hjust=0.5, vjust=0.5)
  }

  # ── Phase labels ─────────────────────────────────
  p <- phase_label(p, 88, "Identification")
  p <- phase_label(p, 72, "Screening")
  p <- phase_label(p, 54, "Eligibility")
  p <- phase_label(p, 32, "Included")

  # ── ROW 1: Identification (y=88) ─────────────────
  p <- dbox(p, CX, 88, BOX_W, BOX_H, id_label,
            fill="#EBF5FB", border="#2980B9")

  # arrow down
  p <- varrow(p, CX, 83, 77.5)

  # ── ROW 2: Screened (y=72) ───────────────────────
  p <- dbox(p, CX, 72, BOX_W, BOX_H,
            sprintf("Records screened\n(n = %s)", format(n_screened, big.mark=",")),
            fill="#EBF5FB", border="#2980B9")

  # elbow to excluded: horizontal line + downward arrow into box
  p <- hline(p, CX + BOX_W/2, EX_CX - EX_W/2, 72)
  p <- harrow(p, CX + BOX_W/2, EX_CX - EX_W/2 + 0.1, 72)
  p <- dbox(p, EX_CX, 68, EX_W, EX_H_1,
            sprintf("Records excluded (n = %s)\n  Stage 1 – automated: %s\n  Stage 2 – title/abstract: %s",
                    format(n_excluded_screen, big.mark=","),
                    format(n_stage1, big.mark=","),
                    format(n_stage2, big.mark=",")),
            fill="#FDFEFE", border="#E74C3C", tsize=2.85)

  # arrow down main
  p <- varrow(p, CX, 67, 59.5)

  # ── ROW 3: Full-text eligibility (y=54) ──────────
  p <- dbox(p, CX, 54, BOX_W, BOX_H,
            sprintf("Full-text articles assessed\nfor eligibility (n = %d)", n_fulltext),
            fill="#EBF5FB", border="#2980B9")

  # elbow to excluded: horizontal arrow
  p <- harrow(p, CX + BOX_W/2, EX_CX - EX_W/2, 54)
  p <- dbox(p, EX_CX, 46, EX_W, EX_H_2,
            sprintf(paste0("Full-text excluded (n = %d)\n",
                           "  Population criteria: n = %d\n",
                           "  Intervention criteria: n = %d\n",
                           "  Study design: n = %d\n",
                           "  Other reasons: n = %d"),
                    n_fulltext_excluded,
                    n_excl_population,
                    n_excl_intervention,
                    n_excl_design,
                    n_excl_other),
            fill="#FDFEFE", border="#E74C3C", tsize=2.85)

  # arrow down main
  p <- varrow(p, CX, 49, 37.5)

  # ── ROW 4: Included (y=32) ───────────────────────
  p <- dbox(p, CX, 32, BOX_W, 11,
            sprintf("Studies included in narrative synthesis\n(n = %d)", n_included),
            fill="#EAFAF1", border="#27AE60", tsize=3.5, bold=TRUE)

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
