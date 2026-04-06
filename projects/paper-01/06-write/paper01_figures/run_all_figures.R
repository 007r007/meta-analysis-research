# ============================================================
# 一键生成 Paper-01 全部三张图
# 使用方法：在 RStudio Console 粘贴以下全部内容，回车运行
# ============================================================

# Step 1: 安装缺失的包（已安装则跳过）
pkgs <- c("ggplot2", "dplyr", "tidyr")
install.packages(pkgs[!pkgs %in% installed.packages()[,"Package"]],
                 repos = "https://cloud.r-project.org")

# Step 2: 运行三个图脚本
base_dir <- "E:/Meta-analysis writing project/projects/paper-01/06-write/paper01_figures"

cat(">>> 生成 Figure 1 (PRISMA)...\n")
source(file.path(base_dir, "figure1_prisma.R"))

cat(">>> 生成 Figure 2 (年份分布)...\n")
source(file.path(base_dir, "figure2_year_dist.R"))

cat(">>> 生成 Figure 3 (调节因素)...\n")
source(file.path(base_dir, "figure3_moderator_summary.R"))

cat("\n✓ 全部完成！PNG 已保存到：\n", base_dir, "\n")
