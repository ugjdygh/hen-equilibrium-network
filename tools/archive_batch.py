#!/usr/bin/env python3
"""Submit the batch in docs/legal/web-archive-urls.txt to the Wayback Machine and
record the snapshots. Needs outbound access to web.archive.org (not available in
every sandbox; run it locally if it fails here).

Usage:
  python3 tools/archive_batch.py --dry-run          # print the batch
  python3 tools/archive_batch.py --limit 5          # archive the first 5 P0 URLs
  python3 tools/archive_batch.py --out docs/legal/web-archive.md

Each successful save is written as a dated row: url | snapshot | status.
"""
import argparse, os, sys, time, urllib.request

SPN = "https://web.archive.org/save/"
CDX = "https://web.archive.org/cdx/search/cdx?url={}&output=json&limit=1&filter=statuscode:200&from={}"


def load(path):
    rows = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("\t")]
        if len(parts) < 2:
            continue
        rows.append({"priority": parts[0], "url": parts[1], "label": parts[2] if len(parts) > 2 else ""})
    return rows


def save(url, timeout=90):
    req = urllib.request.Request(SPN + url, headers={"User-Agent": "HEN-deposit/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.geturl(), r.status


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", default="docs/legal/web-archive-urls.txt")
    ap.add_argument("--out", default="docs/legal/web-archive.md")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    rows = load(a.list)
    if a.dry_run:
        for r in rows:
            print(f"{r['priority']}\t{r['url']}\t{r['label']}")
        print(f"\n{len(rows)} URLs")
        return

    if a.limit:
        rows = rows[: a.limit]
    results, failures = [], []
    for r in rows:
        try:
            snap, status = save(r["url"])
            results.append((r, snap, status))
            print(f"ok   {r['url']} -> {snap}")
        except Exception as e:  # network or rate limit
            failures.append((r, str(e)))
            print(f"fail {r['url']} {e}", file=sys.stderr)
        time.sleep(3)  # be polite; SPN rate-limits aggressively

    if not os.path.exists(a.out):
        open(a.out, "w", encoding="utf-8").write(
            "# Web archive record\n\nBatch source: `docs/legal/web-archive-urls.txt`.\n\n"
            "| Priority | Page | Snapshot | Status |\n|---|---|---|---|\n")
    with open(a.out, "a", encoding="utf-8") as fh:
        for r, snap, status in results:
            fh.write(f"| {r['priority']} | {r['label'] or r['url']} | {snap} | {status} |\n")
    print(f"\n{len(results)} saved, {len(failures)} failed. Rows appended to {a.out}")
    if failures:
        print("Failed URLs keep their place in the batch; re-run the same command later.")


if __name__ == "__main__":
    main()
