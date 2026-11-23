#!/usr/bin/env python3
"""Build a deposit bundle for copyright evidence and print its hash.

The bundle stays outside the repository (default: /tmp/hen-deposit/) so binaries
never enter git history. Record the printed hash in docs/legal/deposit-record.md.

Usage:
  python3 tools/make_deposit.py [--out DIR] [--tag v0.4.0]
"""
import argparse, hashlib, os, subprocess, tarfile, time

FILES = [
    "docs/whitepaper/en/whitepaper.md",
    "docs/whitepaper/zh/whitepaper.md",
    "DISCLAIMER.md", "NOTICE.md", "AUTHORS.md", "LICENSE",
    "CLA-SIGNATURES.md", "docs/legal/provenance.sha256",
]

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="/tmp/hen-deposit")
    ap.add_argument("--tag", default="")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    name = f"HEN-deposit-{a.tag or 'worktree'}-{stamp}"
    tar_path = os.path.join(a.out, name + ".tar.gz")

    missing = [f for f in FILES if not os.path.exists(f)]
    if missing:
        raise SystemExit(f"missing files: {missing}")

    commit = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()

    with tarfile.open(tar_path, "w:gz") as tar:
        for f in FILES:
            tar.add(f, arcname=os.path.join(name, f))
        readme = os.path.join(a.out, "README.txt")
        with open(readme, "w", encoding="utf-8") as fh:
            fh.write(
                "Horizon Equilibrium Network — copyright deposit bundle\n"
                f"created_utc: {stamp}\ncommit: {commit}\n"
                "contents: whitepaper (en, zh), boundary and notice files, byline, licence, "
                "CLA ledger, provenance manifest\n"
                "note: this is evidence that the text existed at this time; it is not a "
                "copyright registration and proves nothing about priority of ideas.\n"
            )
        tar.add(readme, arcname=os.path.join(name, "README.txt"))

    h = sha256(tar_path)
    print(f"bundle: {tar_path}")
    print(f"size:   {os.path.getsize(tar_path)} bytes")
    print(f"sha256: {h}")
    print(f"commit: {commit}")
    print("\nNext: store the hash in docs/legal/deposit-record.md and, for a timestamp, "
          "submit it to an RFC 3161 service or publish it on an independent platform.")

if __name__ == "__main__":
    main()
