#!/usr/bin/env python3
"""生成仓库内全部受版本控制文件的 SHA-256 清单。

用途：为 docs/legal/provenance.md §3.1 提供可复现的存证材料。
用法：python3 tools/provenance_manifest.py > docs/legal/provenance.sha256
"""
import hashlib
import subprocess
import sys

def tracked_files():
    out = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True)
    return [p for p in out.stdout.splitlines() if p.strip() and p != "docs/legal/provenance.sha256"]

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    files = tracked_files()
    print(f"# Horizon Equilibrium Network — provenance manifest")
    print("# regenerate together with each release tag; see docs/legal/provenance.md §3.1")
    print(f"# files: {len(files)}")
    print(f"# algorithm: sha256(file bytes)")
    print("#")
    for p in sorted(files):
        try:
            print(f"{sha256(p)}  {p}")
        except OSError as e:
            print(f"# SKIP {p}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
