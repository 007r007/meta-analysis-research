# Figure 1: PRISMA 2020 Flow Diagram
# Paper 01 — WM Training Systematic Review
# Nature-style color palette, publication-quality layout

library(ggplot2)
library(grid)

# ─────────────────────────────────────────────────
# DATA (verified from 03-screen Excel files)
# ─────────────────────────────────────────────────
# Per-database counts (from 数据_2_第一轮标题摘要筛选_v2.xlsx)
n_pubmed   <- 2403
n_psycinfo <- 372
n_wos      <- 575
n_scopus   <- 818
n_total    <- 4168  # after deduplication (sum = 4168)

# Stage 1: automated keyword filter (结果_2_筛选统计_v2.json)
n_screened       <- 4168
n_excl_stage1    <- 3723   # total excluded title/abstract
n_stage1_auto    <- 2379   # automated (v1 → v2 diff)
n_stage2_manual  <- 1344

# Stage 3: full-text (数据_5_第三轮全文筛选.xlsx)
n_fulltext       <- 445
n_ft_excluded    <- 15
n_ft_E1          <- 12   # population criteria (age/diagnosis)
n_ft_E2          <- 2    # intervention criteria
n_ft_E4          <- 1    # study design criteria

n_included       <- 56

# ─────────────────────────────────────────────────
# Nature color palette
# ─────────────────────────────────────────────────
# Main boxes:   Nature blue  #4DBBD5 (light fill) / #2E6DA4 (border)
# Excluded:     Nature red   #F9B9B7 (fill)       / #C0392B (border)
# Included:     Nature green #B7E0C4 (fill)       / #1A7D3E (border)
# Phase labels: #E8EFF7 (fill) / #2E6DA4 (border/text)
# Background:   white

COL_MAIN_FILL   <- "#EBF4FA"
COL_MAIN_BORDER <- "#2E6DA4"
COL_MAIN_TEXT   <- "#1A3A5C"
COL_EXCL_FILL   <- "#FEF0EF"
COL_EXCL_BORDER <- "#C0392B"
COL_EXCL_TEXT   <- "#7B1E1E"
COL_INCL_FILL   <- "#EBF7EE"
COL_INCL_BORDER <- "#1A7D3E"
COL_INCL_TEXT   <- "#0D4A22"
COL_PHASE_FILL  <- "#E8EFF7"
COL_PHASE_BORD  <- "#2E6DA4"
COL_PHASE_TEXT  <- "#2E6DA4"
COL_ARROW       <- "#444444"

# ─────────────────────────────────────────────────
# LAYOUT (coordinate 0–100 x 0–100)
# Phase label column:  x_phase = 8  (width 14)
# Main flow column:    cx = 42  (width 46)
# Excluded column:     ex_cx = 83  (width 28)
# Row centers (y):     90, 75, 58, 35
# ─────────────────────────────────────────────────
cx     <- 42
bw     <- 46   # main box width
bh     <- 9    # main box height
ex_cx  <- 83
ex_w   <- 28
x_ph   <- 8    # phase label center x
ph_w   <- 14   # phase label width
ph_h   <- 7    # phase label height

draw_prisma <- function() {

  p <- ggplot() +
    xlim(0, 100) + ylim(0, 100) +
    theme_void() +
    theme(
      plot.background  = element_rect(fill = "white", color = NA),
      panel.background = element_rect(fill = "white", color = NA),
      plot.margin = margin(10, 8, 8, 8),
      plot.title  = element_text(size = 13, face = "bold",
                                  hjust = 0.5, color = "#1A3A5C",
                                  margin = margin(b = 6))
    )

  # ── helpers ──────────────────────────────────────

  dbox <- function(p, cx, cy, w, h, txt,
                   fill, border, tcol = "#222222",
                   tsize = 3.0, bold = FALSE) {
    p +
      annotate("rect",
               xmin = cx-w/2, xmax = cx+w/2,
               ymin = cy-h/2, ymax = cy+h/2,
               fill = fill, color = border, linewidth = 0.65) +
      annotate("text", x = cx, y = cy, label = txt,
               size = tsize, hjust = 0.5, vjust = 0.5,
               lineheight = 1.1, color = tcol,
               fontface = ifelse(bold, "bold", "plain"))
  }

  phase <- function(p, cy, txt) {
    p +
      annotate("rect",
               xmin = x_ph - ph_w/2, xmax = x_ph + ph_w/2,
               ymin = cy - ph_h/2,   ymax = cy + ph_h/2,
               fill = COL_PHASE_FILL, color = COL_PHASE_BORD, linewidth = 0.6) +
      annotate("text", x = x_ph, y = cy, label = txt,
               size = 2.7, fontface = "bold", color = COL_PHASE_TEXT,
               hjust = 0.5, vjust = 0.5, lineheight = 1.0)
  }

  varrow <- function(p, x, y1, y2) {
    p + annotate("segment", x = x, xend = x, y = y1, yend = y2,
                 arrow = grid::arrow(length = unit(0.2, "cm"),
                                     type = "closed"),
                 color = COL_ARROW, linewidth = 0.55)
  }

  harrow <- function(p, x1, x2, y) {
    p + annotate("segment", x = x1, xend = x2, y = y, yend = y,
                 arrow = grid::arrow(length = unit(0.2, "cm"),
                                     type = "closed"),
                 color = COL_ARROW, linewidth = 0.55)
  }

  # ── Phase labels ─────────────────────────────────
  p <- phase(p, 91, "Identification")
  p <- phase(p, 76, "Screening")
  p <- phase(p, 50, "Eligibility")
  p <- phase(p, 28, "Included")

  # ── ROW 1: Identification (y=91) ─────────────────
  id_txt <- sprintf(
    paste0("Records identified from 4 databases\n",
           "(N = %s after deduplication)\n",
           "PubMed: %s  |  PsycINFO: %s  |  WoS: %s  |  Scopus: %s"),
    format(n_total, big.mark=","),
    format(n_pubmed, big.mark=","),
    format(n_psycinfo, big.mark=","),
    format(n_wos, big.mark=","),
    format(n_scopus, big.mark=",")
  )
  p <- dbox(p, cx, 91, bw, 11, id_txt,
            fill = COL_MAIN_FILL, border = COL_MAIN_BORDER,
            tcol = COL_MAIN_TEXT, tsize = 2.9)

  p <- varrow(p, cx, 85.4, 81.0)

  # ── ROW 2: Screened (y=76) ───────────────────────
  p <- dbox(p, cx, 76, bw, bh,
            sprintf("Records screened\n(title and abstract; n = %s)",
                    format(n_screened, big.mark=",")),
            fill = COL_MAIN_FILL, border = COL_MAIN_BORDER,
            tcol = COL_MAIN_TEXT, tsize = 3.0)

  p <- harrow(p, cx + bw/2, ex_cx - ex_w/2, 76)

  p <- dbox(p, ex_cx, 71.5, ex_w, 11,
            sprintf("Records excluded (n = %s)\n  Stage 1 – automated filter: n = %s\n  Stage 2 – title/abstract review: n = %s",
                    format(n_excl_stage1, big.mark=","),
                    format(n_stage1_auto, big.mark=","),
                    format(n_stage2_manual, big.mark=",")),
            fill = COL_EXCL_FILL, border = COL_EXCL_BORDER,
            tcol = COL_EXCL_TEXT, tsize = 2.7)

  # Screening → Eligibility 之间留出足够间隔（3723框底部约y=66，全文框顶部y=58）
  p <- varrow(p, cx, 71.4, 59.5)

  # ── ROW 3: Full-text eligibility (y=55) ──────────
  p <- dbox(p, cx, 55, bw, bh,
            sprintf("Full-text articles assessed for eligibility (n = %d)",
                    n_fulltext),
            fill = COL_MAIN_FILL, border = COL_MAIN_BORDER,
            tcol = COL_MAIN_TEXT, tsize = 3.0)

  # 水平箭头从全文框引到右侧
  p <- harrow(p, cx + bw/2, ex_cx - ex_w/2, 55)

  # 全文阶段排除框：合并374篇（无详细记录）+ 15篇（有理由）
  n_ft_no_record <- n_fulltext - n_ft_excluded - n_included  # 445 - 15 - 56 = 374
  p <- dbox(p, ex_cx, 50, ex_w, 21,
            sprintf(paste0(
              "Full-text articles excluded (n = %d)\n",
              "  Not entering detailed review: n = %d\n",
              "    (did not meet ≥1 PICOS criterion;\n",
              "    reasons not individually recorded)\n",
              "  Reviewed with reasons (n = %d):\n",
              "    E1 – population criteria: n = %d\n",
              "    E2 – intervention: n = %d\n",
              "    E4 – study design: n = %d"),
              n_ft_no_record + n_ft_excluded,
              n_ft_no_record,
              n_ft_excluded, n_ft_E1, n_ft_E2, n_ft_E4),
            fill = COL_EXCL_FILL, border = COL_EXCL_BORDER,
            tcol = COL_EXCL_TEXT, tsize = 2.55)

  p <- varrow(p, cx, 50.4, 34.5)

  # ── ROW 4: Included (y=28) ───────────────────────
  p <- dbox(p, cx, 28, bw, 10,
            sprintf("Studies included in narrative synthesis\n(n = %d)", n_included),
            fill = COL_INCL_FILL, border = COL_INCL_BORDER,
            tcol = COL_INCL_TEXT, tsize = 3.3, bold = TRUE)

  p <- p + labs(title = "Figure 1. PRISMA 2020 Flow Diagram")

  return(p)
}

p_prisma <- draw_prisma()

ggsave(
  filename = "E:/Meta-analysis writing project/projects/paper-01/06-write/paper01_figures/figure1_prisma.png",
  plot = p_prisma,
  width = 9, height = 10, dpi = 300, bg = "white"
)

cat("Figure 1 (PRISMA) saved.\n")
