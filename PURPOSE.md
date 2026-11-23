# Purpose

One sentence: **to make a specific design for a decentralised ledger reviewable and refutable by strangers, in public, before anyone builds it.**

Everything in this repository serves that sentence. Nothing in it serves anything else.

## 1. Why "reviewable" is the whole point

A design that is only described in private cannot be attacked. A design that is published with runnable simulations, stated parameters, explicit open questions and an acceptance test suite can be attacked — and that is the intent. The value is not that the design is right; the value is that its failures are findable by someone who owes the author nothing.

The repository is therefore built to be *used against* the author:

- the simulation is runnable, so a reader can change a parameter and break the conclusion;
- the open questions are listed, including the ones the design does not solve (Q4 has no answer);
- the whitepaper text is frozen with a hash and a timestamp, so a later revision cannot quietly claim to have said something else;
- the acceptance cases are written for an implementer who does not exist yet.

## 2. Who it is for, and what each of them should be able to do

| Reader | What they should be able to do after reading |
|---|---|
| A protocol researcher | Name the three weakest assumptions and say which experiment would refute them |
| A cryptoeconomics reviewer | Reproduce or contradict the incentive simulation in under an hour |
| A future implementer | Start a client from `api-sketch.md` without guessing, or refuse to, with reasons |
| A sceptic | Establish that no token, no network and no entity exist — from the documents, not from a promise |

## 3. Success, stated falsifiably

Success is **not** adoption, funding, a launch or a market. It is:

1. an outside reviewer publishes a specific technical objection that the documents did not already contain;
2. someone reproduces a simulation result and reports a different number;
3. a reader uses the acceptance cases to argue that a design detail is unimplementable;
4. the documents are cited by someone with no relationship to the author.

Any of the four counts. Volume of stars, forks, followers or citations does not.

## 4. Failure

1. The repository is read but never contradicted — meaning nobody engaged, not that it was right.
2. It is absorbed into a product or offering whose promoters imply endorsement.
3. The author starts treating the design as an asset, a position or a claim on future value.

## 5. What is explicitly not the purpose

- Not to launch a network, and not to prepare to.
- Not to issue, distribute, price or promote any asset.
- Not to raise money, form an entity, hire a team or recruit developers.
- Not to establish priority over the idea, or to own the mechanism.
- Not to earn anything: no allocation, no advisory grant, no share of any implementation. MIT already means an implementation owes the author nothing, and that is accepted, not resented.

## 6. Drift test

Purpose drift is not a feeling; it has symptoms. Answer these honestly, once a year:

| Question | Signal that the purpose has drifted |
|---|---|
| Am I writing to be reviewed, or to be believed? | Removing open questions, softening limits, adding confidence to the abstract |
| Do I want a reader to check the numbers? | Making the simulation harder to run, or dropping parameters from the text |
| Am I tracking attention or objections? | Counting stars and followers, ignoring issues and replies |
| Have I thought about a wallet, an allocation or a price? | Any of the three appearing in a plan is drift, whether or not it is carried out |
| Would I still publish this if nobody ever read it? | If no, the motive is external, and the boundaries will bend next |

## 7. What stays true if the project dies

The documents remain readable, citable and refutable; the licence keeps them usable; the timestamps keep them datable. A research project that ends with a findable record of what was claimed and what was not has done its job. That is the only outcome being aimed at.
