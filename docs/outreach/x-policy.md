# X (Twitter) posting policy

**Purpose**: share research on X without turning a research account into a token account.

## 1. Four statements that must appear in every post about this project

Any post that mentions HEN, the whitepaper or a simulation result carries, in the post itself or in the immediately following reply:

> Draft research only. No token, no mainnet, no fundraising. Not investment advice.

Shortened form for a single post is acceptable only if all four elements remain: **no token / no mainnet / no fundraising / not investment advice**.

## 2. What may be posted

- A simulation result with its number and the command to reproduce it.
- A design defect found, with the mechanism that fails and why.
- A revised parameter rule, with the before/after comparison.
- A new document or release, with a link and a one-line statement of what changed.
- A correction to something previously posted.

## 3. What may not be posted

- Price, market capitalisation, "potential", "upside", "early", "watch this".
- Any implication of a launch date, a listing, an airdrop, a whitelist, a waitlist.
- Recruiting developers, validators, node operators, or an "official team".
- Screenshots of charts presented as performance.
- Replies to price-prediction or airdrop accounts, even to correct them — engaging amplifies them.
- Any use of cashtags or ticker-style formatting for the name.

## 4. Account hygiene

- Bio states: research, drafting, no token, no network, not investment advice.
- No paid promotion, no follow-for-follow, no engagement pods.
- Quote-posting a critic is allowed; brigading them is not.
- If an impersonation account appears, report it to the platform and post a short factual notice — no drama.

## 5. Ready-to-post templates

**Simulation result**

> Simulated the difficulty controller on a 1.8x compute step. The "3 consecutive moves" breaker froze at target 13.31 of 18.00 needed; a windowed cumulative rule with cooldown converged to 18.00, interval 10.00.
> Reproduce: `python3 examples/sim/mechanism_sim.py`
> Draft research only. No token, no mainnet, no fundraising. Not investment advice.

**Design defect**

> Found a defect in my own draft: freezing after N same-direction parameter moves contradicts the adjustment budget needed for a compute step. Fix is cumulative amplitude plus a time window, not a counter.
> Whitepaper §10.1.1, simulation in `examples/sim/`.
> Draft research only. No token, no mainnet, no fundraising. Not investment advice.

**Release note**

> Whitepaper v0.4.x: breaker rule replaced, dormancy handled by opt-in burn only, English surface completed. No mechanism is claimed to be settled.
> Draft research only. No token, no mainnet, no fundraising. Not investment advice.

## 6. If a post goes wrong

1. Delete or correct within the hour; corrections get their own post, not a silent edit.
2. Record what was said and why it was wrong in `CHANGELOG.md` if it concerned a mechanism.
3. Do not argue in threads; link the document and stop.
