"""
Paper-02 文献合并去重脚本
输入：四库原始导出文件（RIS格式 + PubMed MEDLINE格式）
输出：数据_2_四库合并去重后.ris、结果_1_检索统计数据.json
"""

import re
import json
from pathlib import Path

BASE_DIR = Path(r"E:\Meta-analysis writing project\projects\paper-02\02-search")

# ── 1. 解析函数 ──────────────────────────────────────────────

def parse_ris(filepath):
    """解析 RIS 格式，返回记录列表"""
    records = []
    current = {}
    with open(filepath, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("ER  -") or line.startswith("ER -"):
                if current:
                    records.append(current)
                    current = {}
            elif len(line) >= 6 and line[2:6] == "  - ":
                tag = line[:2].strip()
                val = line[6:].strip()
                if tag in current:
                    if isinstance(current[tag], list):
                        current[tag].append(val)
                    else:
                        current[tag] = [current[tag], val]
                else:
                    current[tag] = val
    if current:
        records.append(current)
    return records


def parse_pubmed_medline(filepath):
    """解析 PubMed MEDLINE/nbib 格式"""
    records = []
    current = {}
    last_tag = None
    with open(filepath, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.strip() == "":
                if current:
                    records.append(current)
                    current = {}
                    last_tag = None
                continue
            if len(line) > 6 and line[4] == "-":
                tag = line[:4].strip()
                val = line[6:].strip()
                last_tag = tag
                if tag in current:
                    if isinstance(current[tag], list):
                        current[tag].append(val)
                    else:
                        current[tag] = [current[tag], val]
                else:
                    current[tag] = val
            elif line.startswith("      ") and last_tag:
                val = line.strip()
                if isinstance(current.get(last_tag), list):
                    current[last_tag][-1] += " " + val
                elif last_tag in current:
                    current[last_tag] += " " + val
    if current:
        records.append(current)
    return records


# ── 2. 标准化字段提取 ────────────────────────────────────────

def get_doi(rec, source):
    doi = None
    if source in ("psycinfo", "scopus"):
        doi = rec.get("DO") or rec.get("M3")
    elif source == "pubmed":
        doi = rec.get("LID") or rec.get("AID")
        if isinstance(doi, list):
            for d in doi:
                if "10." in str(d):
                    doi = d
                    break
    elif source == "wos":
        doi = rec.get("DO") or rec.get("DI")
    if doi and isinstance(doi, list):
        doi = doi[0]
    if doi:
        doi = re.sub(r'\s+', '', str(doi).lower())
        doi = doi.replace("[doi]", "").strip()
        if doi.startswith("10."):
            return doi
    return None


def get_title(rec, source):
    title = None
    if source in ("psycinfo", "scopus", "wos"):
        title = rec.get("TI") or rec.get("T1")
    elif source == "pubmed":
        title = rec.get("TI")
    if title and isinstance(title, list):
        title = title[0]
    if title:
        title = re.sub(r'[^\w\s]', '', str(title).lower())
        title = re.sub(r'\s+', ' ', title).strip()
        return title[:120]
    return None


def get_year(rec, source):
    if source in ("psycinfo", "scopus", "wos"):
        y = rec.get("PY") or rec.get("Y1")
    elif source == "pubmed":
        y = rec.get("DP")
    if y and isinstance(y, list):
        y = y[0]
    if y:
        m = re.search(r'\d{4}', str(y))
        if m:
            return m.group()
    return None


# ── 3. 加载文件 ──────────────────────────────────────────────

print("=" * 60)
print("加载文件...")

pubmed_recs = parse_pubmed_medline(BASE_DIR / "pubmed-parentaled-set.txt")
print(f"PubMed:    {len(pubmed_recs)} 条")

psycinfo_recs = parse_ris(BASE_DIR / "psycinfo_raw.ris.ris")
print(f"PsycINFO:  {len(psycinfo_recs)} 条")

wos1 = parse_ris(BASE_DIR / "wos_raw_1.ris")
wos2 = parse_ris(BASE_DIR / "wos_raw_2.ris")
wos_recs = wos1 + wos2
print(f"WoS:       {len(wos1)} + {len(wos2)} = {len(wos_recs)} 条")

scopus_recs = parse_ris(BASE_DIR / "scopus_raw.ris.ris")
print(f"Scopus:    {len(scopus_recs)} 条")

total_raw = len(pubmed_recs) + len(psycinfo_recs) + len(wos_recs) + len(scopus_recs)
print(f"\n合并前总计: {total_raw} 条")
print("=" * 60)

# ── 4. 去重 ──────────────────────────────────────────────────

print("\n开始去重...")

all_records = []
for rec in pubmed_recs:
    all_records.append(("pubmed", rec))
for rec in psycinfo_recs:
    all_records.append(("psycinfo", rec))
for rec in wos_recs:
    all_records.append(("wos", rec))
for rec in scopus_recs:
    all_records.append(("scopus", rec))

seen_doi = {}
seen_title = {}
unique_records = []
duplicate_count = 0

for source, rec in all_records:
    doi = get_doi(rec, source)
    title = get_title(rec, source)
    year = get_year(rec, source)
    title_year = f"{title}_{year}" if title and year else None

    is_dup = False
    if doi and doi in seen_doi:
        is_dup = True
    elif title_year and title_year in seen_title:
        is_dup = True

    if not is_dup:
        idx = len(unique_records)
        unique_records.append((source, rec))
        if doi:
            seen_doi[doi] = idx
        if title_year:
            seen_title[title_year] = idx
    else:
        duplicate_count += 1

print(f"重复记录:   {duplicate_count} 条")
print(f"去重后总计: {len(unique_records)} 条")

# ── 5. 输出 RIS ──────────────────────────────────────────────

def rec_to_ris(source, rec):
    lines = []

    def add(tag, val):
        if val:
            if isinstance(val, list):
                for v in val:
                    if v:
                        lines.append(f"{tag}  - {v}")
            else:
                lines.append(f"{tag}  - {val}")

    if source in ("psycinfo", "scopus", "wos"):
        add("TY", rec.get("TY", "JOUR"))
        add("TI", rec.get("TI") or rec.get("T1"))
        add("AU", rec.get("AU") or rec.get("A1"))
        add("PY", rec.get("PY") or rec.get("Y1"))
        add("JO", rec.get("JO") or rec.get("JF") or rec.get("T2"))
        add("VL", rec.get("VL"))
        add("IS", rec.get("IS"))
        add("SP", rec.get("SP"))
        add("EP", rec.get("EP"))
        add("DO", rec.get("DO") or rec.get("DI") or rec.get("M3"))
        add("AB", rec.get("AB") or rec.get("N2"))
        add("KW", rec.get("KW"))
        add("DB", source.upper())
    elif source == "pubmed":
        add("TY", "JOUR")
        add("TI", rec.get("TI"))
        add("AU", rec.get("AU") or rec.get("FAU"))
        add("PY", rec.get("DP"))
        add("JO", rec.get("JT") or rec.get("TA"))
        add("VL", rec.get("VI"))
        add("IS", rec.get("IP"))
        add("SP", rec.get("PG"))
        doi_raw = rec.get("LID") or rec.get("AID")
        if isinstance(doi_raw, list):
            for d in doi_raw:
                if "10." in str(d):
                    doi_raw = d
                    break
        add("DO", doi_raw)
        add("AB", rec.get("AB"))
        add("KW", rec.get("MH") or rec.get("OT"))
        add("DB", "PUBMED")

    lines.append("ER  - ")
    lines.append("")
    return "\n".join(lines)


out_ris = BASE_DIR / "数据_2_四库合并去重后.ris"
with open(out_ris, "w", encoding="utf-8") as f:
    for source, rec in unique_records:
        f.write(rec_to_ris(source, rec))
        f.write("\n")

print(f"\n已输出RIS: {out_ris}")

# ── 6. 统计 ──────────────────────────────────────────────────

print("\n" + "=" * 60)
print("检索统计摘要")
print("=" * 60)
print(f"{'数据库':<12} {'条数':>8}")
print("-" * 22)
print(f"{'PubMed':<12} {len(pubmed_recs):>8}")
print(f"{'PsycINFO':<12} {len(psycinfo_recs):>8}")
print(f"{'WoS':<12} {len(wos_recs):>8}")
print(f"{'Scopus':<12} {len(scopus_recs):>8}")
print("-" * 22)
print(f"{'合并前总计':<12} {total_raw:>8}")
print(f"{'重复':<12} {duplicate_count:>8}")
print(f"{'去重后':<12} {len(unique_records):>8}")
print("=" * 60)

stats = {
    "pubmed": len(pubmed_recs),
    "psycinfo": len(psycinfo_recs),
    "wos": len(wos_recs),
    "scopus": len(scopus_recs),
    "total_raw": total_raw,
    "duplicates": duplicate_count,
    "unique": len(unique_records),
}
out_json = BASE_DIR / "结果_1_检索统计数据.json"
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)
print(f"统计数据已保存: {out_json}")
