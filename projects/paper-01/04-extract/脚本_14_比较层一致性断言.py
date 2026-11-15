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

# ── 断言 1：独立 trial_id 数 = 51 ─────────────────────────────
n_trial = len(trial)
tids = [r[T["trial_id"]] for r in trial]
n_unique = len(set(tids))
if n_trial == 51 and n_unique == 51:
    print(f"[PASS] 断言1：独立 trial_id 数 = 51（行数={n_trial}, 唯一={n_unique}）")
else:
    failures.append(f"断言1：trial行数={n_trial}, 唯一={n_unique}, 期望51")

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

# ── 断言 6：核心元分析池（in_core_ma=True）计数 = 38（cx 裁定）──
n_core = sum(1 for r in comp if r[C["in_core_ma"]] is True or r[C["in_core_ma"]] == "True")
# 精确计数 + 分布
from collections import Counter
core_types = Counter(r[C["comp_type"]] for r in comp if r[C["in_core_ma"]] is True or r[C["in_core_ma"]] == "True")
print(f"[INFO] 断言6：in_core_ma=True 精确计数 = {n_core}（分布 {dict(core_types)}）")
# ①+② 应为 core；校验 in_core_ma 与 comp_type 一致性
core_by_def = sum(1 for r in comp if r[C["comp_type"]] in ("①", "②"))
if n_core != core_by_def:
    failures.append(f"断言6：in_core_ma计数({n_core}) ≠ ①+②计数({core_by_def})")
if n_core == 38 and core_by_def == 38:
    print("[PASS] 断言6：核心元分析池 = 38（cx 裁定 ①36 + ②2），与 ①+② 计数一致")
else:
    failures.append(f"断言6：核心池={n_core}（①+②={core_by_def}），期望 38（cx 裁定）")

# ── 汇总 ──────────────────────────────────────────────────────
print()
print("=" * 60)
if failures:
    print(f"❌ 失败 {len(failures)} 项：")
    for f in failures:
        print("  -", f)
else:
    print("✅ 全部 6 项断言通过")
if notes:
    print()
    print("⚠️ 审计提示（非失败，请 cx 复核）：")
    for n in notes:
        print("  -", n)
print("=" * 60)
sys.exit(1 if failures else 0)
