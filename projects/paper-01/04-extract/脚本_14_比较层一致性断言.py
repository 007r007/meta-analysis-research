# -*- coding: utf-8 -*-
"""
Paper-01 比较层一致性断言脚本
================================
读取 数据_7_比较层新表.xlsx，跑 schema 第四节「一致性检查断言」6 项。
任何一项不通过 → exit(1)；全部通过 → exit(0)。
"""
import sys
import openpyxl

sys.stdout.reconfigure(encoding='utf-8')

XLSX = r"E:\Meta-analysis writing project\projects\paper-01\04-extract\数据_7_比较层新表.xlsx"

wb = openpyxl.load_workbook(XLSX)
trial = list(wb["trial"].iter_rows(min_row=2, values_only=True))
dedup = list(wb["dedup"].iter_rows(min_row=2, values_only=True))
comp  = list(wb["comparison"].iter_rows(min_row=2, values_only=True))

# 列索引
T = {h: i for i, h in enumerate(next(wb["trial"].iter_rows(min_row=1, max_row=1, values_only=True)))}
C = {h: i for i, h in enumerate(next(wb["comparison"].iter_rows(min_row=1, max_row=1, values_only=True)))}
D = {h: i for i, h in enumerate(next(wb["dedup"].iter_rows(min_row=1, max_row=1, values_only=True)))}

def cidx(h, idxmap): return idxmap[h]

# trial 表查询
def trial_by_seq(seq):
    for r in trial:
        if r[T["main_report_seq"]] == seq:
            return r
    return None

failures = []
notes = []

# ── 断言 1：登记 trial 记录数 = 57（53 主报告[Seq6/61拆2] + 4 不在册/恢复[Borella2010/Borella2017∧/WOME/Zając2016]）──
n_trial = len(trial)
tids = [r[T["trial_id"]] for r in trial]
n_unique = len(set(tids))
if n_trial == 57 and n_unique == 57:
    print(f"[PASS] 断言1：登记 trial 记录数 = 57（行数={n_trial}, 唯一={n_unique}）")
else:
    failures.append(f"断言1：trial行数={n_trial}, 唯一={n_unique}, 期望57")

# ── 断言 2：Seq10 恰好 2 条 comparison ────────────────────────
seq10 = [r for r in comp if r[C["trial_id"]] == trial_by_seq(10)[T["trial_id"]]]
if len(seq10) == 2:
    types = [r[C["comp_type"]] for r in seq10]
    print(f"[PASS] 断言2：Seq10 恰好 2 条 comparison（类型={types}）")
    if set(types) != {"②", "③"}:
        notes.append(f"Seq10 两比较类型={types}，期望 {{②, ③}}")
else:
    failures.append(f"断言2：Seq10 comparison 数={len(seq10)}, 期望2")

# ── 断言 3：Seq24 无 comparison、exclusion_status=excluded ────
t24 = trial_by_seq(24)
seq24_comp = [r for r in comp if r[C["trial_id"]] == t24[T["trial_id"]]]
if len(seq24_comp) == 0 and t24[T["exclusion_status"]] == "excluded":
    print(f"[PASS] 断言3：Seq24 无 comparison 且 exclusion_status=excluded")
else:
    failures.append(f"断言3：Seq24 comp数={len(seq24_comp)}, status={t24[T['exclusion_status']]}")

# ── 断言 4：Seq1/35 comp_type=N、无 comparison ────────────────
for seq in (1, 35):
    tr = trial_by_seq(seq)
    tc = [r for r in comp if r[C["trial_id"]] == tr[T["trial_id"]]]
    ok_type = tr[T["comp_type"]] == "N"
    ok_nocomp = len(tc) == 0
    if ok_type and ok_nocomp:
        print(f"[PASS] 断言4：Seq{seq} comp_type=N 且无 comparison")
    else:
        failures.append(f"断言4：Seq{seq} comp_type={tr[T['comp_type']]}, comp数={len(tc)}")

# ── 断言 5：5 重复（16/43/47/53/28）正确映射到主报告（cx 裁定：43/53 双挂）──
expected_map = {16: [13], 43: [4, 12], 47: [49], 53: [19, 31], 28: [52]}
expected_status = {16: "duplicate", 43: "duplicate", 47: "duplicate",
                   53: "duplicate", 28: "nested"}
if len(dedup) == 5:
    ok = True
    for r in dedup:
        seq = r[D["seq"]]
        main_raw = str(r[D["maps_to_main_seq"]]).replace(" ", "")
        mains = [int(x) for x in main_raw.split(",") if x]
        st = r[D["exclusion_status"]]
        if seq not in expected_map:
            failures.append(f"断言5：dedup 出现未知 seq={seq}"); ok = False; continue
        if expected_map[seq] != mains:
            failures.append(f"断言5：Seq{seq} 映射到 {mains}，期望 {expected_map[seq]}"); ok = False
        if expected_status[seq] != st:
            failures.append(f"断言5：Seq{seq} status={st}，期望 {expected_status[seq]}"); ok = False
        # 每个主报告的 secondary_report_seq 都应包含该 seq
        for m in expected_map[seq]:
            mt = trial_by_seq(m)
            secs = str(mt[T["secondary_report_seq"]]).replace(" ", "")
            if str(seq) not in secs.split(","):
                failures.append(f"断言5：主报告 Seq{m} 的 secondary_report_seq 未含 {seq}"); ok = False
    if ok:
        print("[PASS] 断言5：5 重复正确映射（16→13; 43→4,12; 47→49; 53→19,31; 28→52）")
else:
    failures.append(f"断言5：dedup 行数={len(dedup)}, 期望5")

# ── 断言 7：不在册/恢复样本（Borella 2010 / Borella 2017∧ / WOME / Zając 2016）──
ext_rows = [r for r in trial if isinstance(r[T["main_report_seq"]], str) and r[T["main_report_seq"]].startswith("ext-")]
if len(ext_rows) == 4:
    ok = True
    for r in ext_rows:
        tid = r[T["trial_id"]]
        tc = [c for c in comp if c[C["trial_id"]] == tid]
        if r[T["author_year"]] == "Borella 2010":
            # cx 恢复纳入：正式 ①×1，链接 Seq53
            secs = str(r[T["secondary_report_seq"]]).replace(" ", "")
            if "53" not in secs.split(","):
                failures.append(f"断言7：Borella 2010 secondary_report_seq 未含 53"); ok = False
            if r[T["comp_type"]] != "①" or len(tc) != 1 or tc[0][C["comp_type"]] != "①":
                failures.append(f"断言7：Borella 2010 comp_type={r[T['comp_type']]}, comp数={len(tc)}，期望 ①×1"); ok = False
        elif r[T["author_year"]] == "Zając-Lamparska 2016":
            # cx 恢复纳入：①+①（WM vs waiting / WM vs AC），共用 WM 臂
            if len(tc) != 2 or {c[C["comp_type"]] for c in tc} != {"①"}:
                failures.append(f"断言7：Zając 2016 comp数={len(tc)} 类型={[c[C['comp_type']] for c in tc]}，期望 ①×2"); ok = False
            if tc[0][C["arm_a"]] != tc[1][C["arm_a"]]:
                failures.append(f"断言7：Zając 2016 两比较未共用 WM 臂"); ok = False
        else:
            # Borella 2017∧ / WOME：①-pending，无 comparison
            if r[T["comp_type"]] != "①-pending":
                failures.append(f"断言7：{r[T['author_year']]} comp_type={r[T['comp_type']]}，期望 ①-pending"); ok = False
            if len(tc) != 0:
                failures.append(f"断言7：{r[T['author_year']]} 有 {len(tc)} 条 comparison，期望 0"); ok = False
    if ok:
        print("[PASS] 断言7：Borella 2010 ①×1(链Seq53)；Zając 2016 ①×2(共用WM臂)；Borella 2017∧/WOME ①-pending")
else:
    failures.append(f"断言7：ext trial 行数={len(ext_rows)}, 期望4")

# ── 断言 6：核心候选比较池（in_core_ma=True）计数 = 39（cx 裁定：Seq6拆2）──
n_core = sum(1 for r in comp if r[C["in_core_ma"]] is True or r[C["in_core_ma"]] == "True")
# 精确计数 + 分布
from collections import Counter
core_types = Counter(r[C["comp_type"]] for r in comp if r[C["in_core_ma"]] is True or r[C["in_core_ma"]] == "True")
print(f"[INFO] 断言6：in_core_ma=True 精确计数 = {n_core}（分布 {dict(core_types)}）")
# ①+② 应为 core；校验 in_core_ma 与 comp_type 一致性
core_by_def = sum(1 for r in comp if r[C["comp_type"]] in ("①", "②"))
if n_core != core_by_def:
    failures.append(f"断言6：in_core_ma计数({n_core}) ≠ ①+②计数({core_by_def})")
if n_core == 43 and core_by_def == 43:
    print("[PASS] 断言6：核心候选比较池 = 43（①41[含Borella2010恢复+Zając2016双①] + ②2），与 ①+② 计数一致")
    notes.append("术语提示（cx）：43 是候选比较数，非最终能算效应量的数量；Borella 2017∧/WOME 编码后→45")
else:
    failures.append(f"断言6：核心池={n_core}（①+②={core_by_def}），期望 43（cx 裁定）")

# ── 断言 8：Seq6（Brum 2020）与 Seq61（Cantarella 2017）各拆两个子研究，各 1 条 ① ──
sub_prefixes = {"6-S": "Seq6(Brum 2020)", "61-E": "Seq61(Cantarella 2017)"}
for prefix, label in sub_prefixes.items():
    sub_rows = [r for r in trial if isinstance(r[T["main_report_seq"]], str) and r[T["main_report_seq"]].startswith(prefix)]
    if len(sub_rows) == 2:
        ok = True
        for r in sub_rows:
            tid = r[T["trial_id"]]
            tc = [c for c in comp if c[C["trial_id"]] == tid]
            if len(tc) != 1 or tc[0][C["comp_type"]] != "①":
                failures.append(f"断言8：{r[T['author_year']]} comparison 数={len(tc)}，期望 1 条 ①"); ok = False
        if ok:
            print(f"[PASS] 断言8：{label} 拆为 2 子研究，各 1 条 ①")
    else:
        failures.append(f"断言8：{label} 子研究 trial 行数={len(sub_rows)}, 期望2")

# ── 汇总 ──────────────────────────────────────────────────────
print()
print("=" * 60)
if failures:
    print(f"❌ 失败 {len(failures)} 项：")
    for f in failures:
        print("  -", f)
else:
    print("✅ 全部断言通过（1-8 项，含 Seq6拆2 / 2不在册 / 双挂校验）")
if notes:
    print()
    print("⚠️ 审计提示（非失败，请 cx 复核）：")
    for n in notes:
        print("  -", n)
print("=" * 60)
sys.exit(1 if failures else 0)
