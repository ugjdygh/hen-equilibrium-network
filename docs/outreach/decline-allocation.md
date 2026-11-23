# If someone offers a genesis allocation

Written for one situation: an implementation, a fork or a community reaches a stage where it could launch, and someone proposes to put the author's name on a genesis allocation, a founder share or a wallet address.

## 1. Decide before it happens

Answer is fixed: **decline**. Not "later", not "if it is small", not "only to support research". Deciding now is the whole point — a refusal given after the allocation exists reads as a negotiating position, a refusal given before it exists is a boundary.

Why, in four lines:

1. **It makes the author an issuer.** A genesis allocation is the clearest possible evidence of issuing, promoting or distributing an asset — the exact conduct every document in this repository says does not happen.
2. **It breaks anonymity permanently.** A byline plus an address is a two-record join; the first movement links them, and chain analysis does the rest.
3. **It turns disclaimers into evidence.** `DISCLAIMER.md` §2.1 already says the boundaries lapse if a deployable contract, prototype, token allocation or funding entry appears. Accepting a genesis share is that triggering event, personally.
4. **It is usually a scam.** "Genesis allocation for the founder" is a standard opening move: it asks for a wallet, then for a signature, then for a "small gas prepayment". No legitimate implementation needs the whitepaper author's address to launch.

## 2. Reply template (English, safe to post verbatim)

> Thank you, but I decline.
>
> I hold no genesis allocation, no founder share and no vesting position in any implementation of this design, and I will not accept one. This is not modesty: HEN is published as research, and every document states that there is no issuance and no operating entity. Accepting an allocation would make me an issuer, which is precisely what the documents say does not happen.
>
> I also do not publish, accept or use a wallet address in connection with this project, and I will not sign with keys supplied by anyone else. Please do not reserve an address "for the author" — there is none.
>
> You are free to implement, fork or abandon this design under the MIT licence. That freedom creates no obligation toward me, and gives me no authority over your project either.

Short form, if a one-liner is needed:

> No allocation, no address, no keys — I decline, and this predates your offer.

## 3. Handling steps, in order

1. **Do not reply privately first.** Answer in the same channel where the offer was made, so the refusal is visible and dated; a private refusal can later be described as consent.
2. **Record it.** Screenshot, then timestamp the screenshot's hash with `python3 tools/stamp.py <file> --label decline-<date>`; the receipt goes in `docs/legal/stamps/`. A dated refusal is the asset here.
3. **Never send a wallet address**, not even "just to receive a donation" — the address is the join key.
4. **Never sign anything**, including a "proof of authorship" message with a key you did not generate, and never install a wallet on a device that holds the repository credentials.
5. **Do not touch unsolicited value.** If assets arrive at an address associated with you anyway, do not move them, do not claim them, do not convert them. Movement is the act that creates the issuer appearance.
6. **Update the public record** if the offer was public: one line in `CHANGELOG.md` under the date, and a matching entry in `GOVERNANCE.md` §7A if the situation is new.
7. **If it is a scam** — a claim link, a "must sign to receive", a request for seed phrase, gas money or KYC — report it to the platform and post the same short warning, without repeating the link.

## 4. What is acceptable instead

If the intent is genuinely to support the research, the acceptable forms cost the author nothing and create no issuer relationship:

- a citation, a review, a replication of the simulation, or an implementation that credits the design;
- a public issue or PR against this repository;
- payment to a **third party** — an auditor, a translator, an independent reviewer — never to the author's address.

None of these require a wallet, a name, or a signature.

## 5. The uncomfortable case

If the author ever wants the allocation, the honest route is: stop being anonymous, become a named person, register whatever entity is required, and accept the full regulatory consequence of being an issuer. That is a different project with a different byline, and it cannot be reached by quietly accepting one address. Choosing the pen name means choosing not to be paid by the protocol.
