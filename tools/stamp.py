#!/usr/bin/env python3
"""Request an RFC 3161 trusted timestamp for a file and store the receipt.

Usage:
  python3 tools/stamp.py FILE [--out docs/legal/stamps] [--label name]

Requires only openssl and curl. The default TSA is DigiCert's public service
(policy 2.16.840.1.114412.7.1); any RFC 3161 responder works via --tsa.
The receipt proves the file existed at the stamped time and is unaltered since.
"""
import argparse, hashlib, os, subprocess, sys

TSA = "http://timestamp.digicert.com"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--out", default="docs/legal/stamps")
    ap.add_argument("--label", default=None)
    ap.add_argument("--tsa", default=TSA)
    a = ap.parse_args()

    label = a.label or os.path.basename(a.file).replace("/", "_")
    os.makedirs(a.out, exist_ok=True)
    tsq = os.path.join(a.out, label + ".tsq")
    tsr = os.path.join(a.out, label + ".tsr")

    subprocess.run(["openssl", "ts", "-query", "-data", a.file, "-no_nonce",
                    "-sha256", "-cert", "-out", tsq], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["curl", "-sS", "-o", tsr, "--max-time", "60",
                    "-H", "Content-Type: application/timestamp-query",
                    "--data-binary", "@" + tsq, a.tsa], check=True)

    txt = subprocess.run(["openssl", "ts", "-reply", "-in", tsr, "-text"],
                         capture_output=True, text=True).stdout
    if "Granted" not in txt:
        sys.exit("timestamp not granted:\n" + txt)
    h = hashlib.sha256(open(a.file, "rb").read()).hexdigest()
    line = next((l.strip() for l in txt.splitlines() if l.strip().startswith("Time stamp:")), "")
    serial = next((l.strip() for l in txt.splitlines() if l.strip().startswith("Serial number:")), "")
    print(f"{a.file}\n  sha256: {h}\n  {serial}\n  {line}\n  receipt: {tsr}")

if __name__ == "__main__":
    main()
