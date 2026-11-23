# Provenance

**Horizon Equilibrium Network (HEN)**

Three questions: how these documents came to exist, what can be claimed in them, and how to fix evidence that a text existed at a point in time.

**Not legal advice.** Registration, litigation or trademark filing require counsel.

---

## 1. How the text was produced (stated plainly)

The documents and the simulation script are **neither purely human-written nor purely machine-generated**. The actual split:

| Layer | Who | What |
|---|---|---|
| Conception | author | problem framing (steady-state circulation, recoverable assets, controllable privacy, reversible evolution), structure, terminology, the boundary stance (no issuance, no fundraising, no operation), which conclusions to keep |
| Drafting | AI-assisted | chapter drafts generated from the author's framing and outline, tables, examples, English rewriting, first version of the simulation script |
| Review | author | judging which arguments hold, what must be deleted, which wording to change; deciding what can be published; checking citations and compliance statements |
| Finalisation | author | version numbers, change records, external wording, boundary statements, release cadence |

**Why this is stated.** Readers deserve to know what they are reading; and because **copyright protects concrete expression, while the treatment of purely AI-generated material varies by jurisdiction** — recording which layer is human is more reliable than asserting "original". The simulation script follows the same rule: drafted with AI assistance, reviewed by the author for whether its conclusions hold, and the author does not write implementation code (see `AUTHORS.md`).

## 2. What can and cannot be claimed

| Object | Claimable? | Note |
|---|---|---|
| The **wording** of the whitepaper and protocol drafts | Yes (author and contributors, see `LICENSE`) | Provided the human contribution is demonstrable; this file plus git history is part of that proof |
| Diagrams, SVG, simulation script | Yes | Same; the script also carries usage notes in `examples/sim/README.md` |
| **Mechanism ideas, parameter intentions, economic model** | **No** | Copyright protects no idea, method, algorithm or mathematical concept. Anyone rewriting an implementation from scratch after reading the whitepaper infringes nothing |
| The name "HEN / Horizon Equilibrium Network" | Depends on trademark status | Currently unregistered; only source identification is claimed (see `NOTICE.md`) |
| Third-party quoted material | No | Rights remain with the original authors |

**This is the key point**: what this repository can hold is the wording and the name; it cannot hold the idea. Anyone may build another chain on the same idea. That is not a defect — it is the normal condition of open-source public chains, as the history of Bitcoin and its forks shows.

## 3. Deposit methods (actionable)

A deposit proves that a text existed at a point in time and has not changed since. It does not prove who conceived it first. Three methods, increasing in cost:

### 3.1 In-repository hash manifest (done, zero cost)

Each release produces a SHA-256 manifest of every file:

```bash
python3 tools/provenance_manifest.py > docs/legal/provenance.sha256
git add docs/legal/provenance.sha256 && git commit -m "chore: refresh provenance manifest"
```

Together with commit history this fixes, for a given commit, the exact contents of every file. **Limit**: it cannot prove anything earlier than repository creation, and it is not externally verifiable.

### 3.2 Third-party timestamping (low cost)

- Submit the manifest and the release tag hash to a trusted timestamping service (RFC 3161 class) and store the receipt in `docs/legal/stamps/`;
- or publish the same hash on several independent platforms (release page, personal site, public archive) to allow cross-verification of the time.

### 3.3 Voluntary copyright registration (moderate cost)

Register the work as a literary work with the competent authority (in mainland China, the Copyright Protection Center). Registration is in the **name of a real, verifiable person** — **this step is directly incompatible with anonymity**: registration requires an identifiable rights holder.

**So this is a trade-off only the author can make**: stronger enforceability means giving up anonymity; keeping anonymity means relying on 3.1 and 3.2, which are verifiable but unofficial. Both cannot be had.

## 4. Current status

| Item | Status |
|---|---|
| Hash manifest | Generated, see `docs/legal/provenance.sha256` |
| Release tags | Tagged from `v0.4.0` onward (see Releases) |
| Third-party timestamps | Not done |
| Copyright registration | Not done (incompatible with anonymity; author's decision) |
| Trademark search and filing | Not done (see `NOTICE.md` §3 for the scope of searches performed) |

## 5. Working with a technical lead

If a technical lead is later brought in to deliver the full implementation, copyright and fork restraint **cannot be handled by the CLA** (the CLA governs contributions, not "starting another chain"). A separate written agreement is required. Clause checklist: `docs/legal/lead-agreement-checklist.md`.

The same fact runs the other way: **an agreement binds only its counterparty, never third parties on the internet**.
