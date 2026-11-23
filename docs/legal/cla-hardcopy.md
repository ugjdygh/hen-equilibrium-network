# Hard-copy sign-off template

**Use when** you need a written licence that can be produced in evidence and enforced, rather than a sentence in a thread. Typical cases: internal compliance requirements, a defined rights holder, or genuine litigation risk.

**The cost, stated first**: this document requires the signatory's **real name, entity type and contact address** — it is incompatible with anonymity. If you choose anonymity, the electronic record in `CLA-SIGNATURES.md` is your only option, and it is weaker than a written instrument.

---

## Steps

1. Copy the template below into a document (Word or plain text), fill the blanks.
2. Print, sign by hand (companies: company seal plus an authorised representative's signature).
3. Scan to PDF (keep a text copy too).
4. Open a new issue in the sign-off thread labelled `cla-hardcopy`, attach the PDF, and state in the body: "written signature submitted, version v1.0".
5. The maintainer checks it, appends a row to `CLA-SIGNATURES.md` marked `hardcopy`.

---

## Template

> **Contributor License Agreement — signed confirmation**
>
> To: the maintainers of Horizon Equilibrium Network (HEN)
>
> Name / entity: ________________________________
> Entity type: ☐ natural person　☐ company or other organisation
> Registration or identification number: ____________________
> GitHub account: ____________
> Address: ________________________________
> Email: ________________________________
>
> I confirm that:
>
> 1. I have read `CLA.md` in the repository root in full (version: ______; SHA-256: ____________), and understand that it is a **licence grant**, not a copyright assignment;
> 2. I agree to all its terms, and they apply to every contribution I make to this repository;
> 3. I hold the rights needed to submit and license my contributions, and have declared any generative-AI output under `CLA.md` §6;
> 4. I understand that the agreement creates no employment, partnership, agency or payment relationship;
> 5. This confirmation is governed by the law of ____________, with disputes in ____________.
>
> Signed: ____________
> Date: ____________
> (Companies additionally: company seal, authorised representative, authority documents attached.)

---

## Maintainer checklist

- [ ] Version and hash match `CLA.md` at the time (`sha256sum CLA.md`)
- [ ] The signatory's identity is linked to the GitHub account in writing
- [ ] Company signatures have authority documents attached
- [ ] Ledger row marked `hardcopy` with the issue link
- [ ] Original stored at a location recorded in the deposit list in `docs/legal/provenance.md`

**Note**: this template is not a legal instrument; have counsel review it under the applicable law before use.
