"""
文献去重合并脚本
统计各数据库条数，合并去重，输出结果
"""

import os
import re
from pathlib import Path

RAW_DIR = Path(r"E:\Meta-analysis writing project\projects\paper-01\02-search\raw-exports")
OUT_DIR = Path(r"E:\Meta-analysis writing project\projects\paper-01\02-search")

# ── 1. 解析函数 ──────────────────────────────────────────────

def parse_ris(filepath):
    """解析 RIS 格式，返回记录列表，每条记录为 dict"""
    records = []
    current = {}
    with open(filepath, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("ER  -"):
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


def parse_pubmed_nbib(filepath):
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


def parse_bib(filepath):
    """解析 BibTeX 格式，返回记录列表"""
    records = []
    with open(filepath, encoding="utf-8", errors="replace") as f:
        content = f.read()
    # 每条记录以 @type{ 开头
    entries = re.split(r'\n(?=@)', content)
    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue
        rec = {}
        # 提取类型和 key
        m = re.match(r'@(\w+)\{([^,]+),', entry)
        if m:
            rec['_type'] = m.group(1).lower()
            rec['_key'] = m.group(2).strip()
        # 提取字段
        for field_m in re.finditer(r'(\w+)\s*=\s*\{(.*?)\}(?:\s*,|\s*\}?\s*$)', entry, re.DOTALL):
            key = field_m.group(1).lower()
            val = field_m.group(2).strip().replace('\n', ' ')
            rec[key] = val
        if rec:
            records.append(rec)
    return records


# ── 2. 提取标准化字段用于去重 ────────────────────────────────

def get_doi(rec, source):
    """从记录中提取 DOI（小写，去空格）"""
    doi = None
    if source in ("psycinfo", "scopus"):
        doi = rec.get("DO") or rec.get("M3") or rec.get("UR")
    elif source == "pubmed":
        doi = rec.get("LID") or rec.get("AID")
        if isinstance(doi, list):
            for d in doi:
                if "[doi]" in d.lower() or "10." in d:
                    doi = d
                    break
    elif source == "wos":
        doi = rec.get("doi") or rec.get("DO")
    if doi and isinstance(doi, list):
        doi = doi[0]
    if doi:
        doi = re.sub(r'\s+', '', str(doi).lower())
        doi = doi.replace("[doi]", "").strip()
        if doi.startswith("10."):
            return doi
    return None


def get_title(rec, source):
    """提取标题，用于 DOI 缺失时的模糊去重"""
    title = None
    if source in ("psycinfo", "scopus"):
        title = rec.get("TI") or rec.get("T1")
    elif source == "pubmed":
        title = rec.get("TI")
    elif source == "wos":
        title = rec.get("title")
    if title and isinstance(title, list):
        title = title[0]
    if title:
        # 标准化：小写，去标点，去多余空格
        title = re.sub(r'[^\w\s]', '', str(title).lower())
        title = re.sub(r'\s+', ' ', title).strip()
        return title[:120]  # 前120字符
    return None


def get_year(rec, source):
    if source in ("psycinfo", "scopus"):
        y = rec.get("PY") or rec.get("Y1")
    elif source == "pubmed":
        y = rec.get("DP")
    elif source == "wos":
        y = rec.get("year")
    if y and isinstance(y, list):
        y = y[0]
    if y:
        m = re.search(r'\d{4}', str(y))
        if m:
            return m.group()
    return None


# ── 3. 加载所有文件 ──────────────────────────────────────────

print("=" * 60)
print("加载文件...")

# PubMed
pubmed_file = RAW_DIR / "pubmed-workingmem-set.txt"
pubmed_recs = parse_pubmed_nbib(pubmed_file)
print(f"PubMed:    {len(pubmed_recs)} 条")

# PsycINFO
psy1 = parse_ris(RAW_DIR / "psycinfo_raw\u20141.ris.ris")
psy2 = parse_ris(RAW_DIR / "psycinfo_raw\u20142.ris.ris")
psycinfo_recs = psy1 + psy2
print(f"PsycINFO:  {len(psy1)} + {len(psy2)} = {len(psycinfo_recs)} 条")

# WoS
wos1 = parse_bib(RAW_DIR / "wos_raw_1.bib")
wos2 = parse_bib(RAW_DIR / "wos_raw_2.bib")
wos3 = parse_bib(RAW_DIR / "wos_raw_3.bib")
wos_recs = wos1 + wos2 + wos3
print(f"WoS:       {len(wos1)} + {len(wos2)} + {len(wos3)} = {len(wos_recs)} 条")

# Scopus
scopus_recs = parse_ris(RAW_DIR / "scopus_raw.ris.ris")
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

seen_doi = {}      # doi -> index
seen_title = {}    # title_year -> index
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

# ── 5. 输出去重后的 RIS 文件 ─────────────────────────────────

def rec_to_ris(source, rec):
    """将记录转为 RIS 格式输出"""
    lines = []

    def add(tag, val):
        if val:
            if isinstance(val, list):
                for v in val:
                    lines.append(f"{tag}  - {v}")
            else:
                lines.append(f"{tag}  - {val}")

    if source in ("psycinfo", "scopus"):
        ty = rec.get("TY", "JOUR")
        add("TY", ty)
        add("TI", rec.get("TI") or rec.get("T1"))
        add("AU", rec.get("AU") or rec.get("A1"))
        add("PY", rec.get("PY") or rec.get("Y1"))
        add("JO", rec.get("JO") or rec.get("JF") or rec.get("T2"))
        add("VL", rec.get("VL"))
        add("IS", rec.get("IS"))
        add("SP", rec.get("SP"))
        add("EP", rec.get("EP"))
        add("DO", rec.get("DO") or rec.get("M3"))
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
    elif source == "wos":
        add("TY", "JOUR")
        add("TI", rec.get("title"))
        author = rec.get("author")
        add("AU", author)
        add("PY", rec.get("year"))
        add("JO", rec.get("journal") or rec.get("booktitle"))
        add("VL", rec.get("volume"))
        add("IS", rec.get("number"))
        add("SP", rec.get("pages"))
        add("DO", rec.get("doi"))
        add("AB", rec.get("abstract"))
        add("KW", rec.get("keywords"))
        add("DB", "WOS")

    lines.append("ER  - ")
    lines.append("")
    return "\n".join(lines)


out_file = OUT_DIR / "merged_deduplicated.ris"
with open(out_file, "w", encoding="utf-8") as f:
    for source, rec in unique_records:
        f.write(rec_to_ris(source, rec))
        f.write("\n")

print(f"\n已输出: {out_file}")

# ── 6. 统计摘要 ──────────────────────────────────────────────

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

# 保存统计结果供后续使用
stats = {
    "pubmed": len(pubmed_recs),
    "psycinfo": len(psycinfo_recs),
    "wos": len(wos_recs),
    "scopus": len(scopus_recs),
    "total_raw": total_raw,
    "duplicates": duplicate_count,
    "unique": len(unique_records),
}
import json
with open(OUT_DIR / "search_stats.json", "w", encoding="utf-8") as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)
print("统计数据已保存至 search_stats.json")
