# LegacyNote Whitepaper

- Status: public review draft
- Date: 2026-05-23
- Mainnet status: not launched
- Testnet status: not launched
- Mining status: not available
- Supply status: selected for public review

## Abstract

LegacyNote is a conservative CryptoNote-style chain based on the maintained Monero codebase. It is a no-extraction fair launch: no premine, no ICO, no presale, no dev fee, no treasury, no donation wallet, no paid insider access, and no founder allocation.

LegacyNote is not presented as the first fair-launch CryptoNote coin. The claim is narrower and easier to verify: a modern Monero-codebase fair launch with public mechanics, public artifacts, no privileged launch access, and a planned handoff from founder control to community maintainers.

## Current Review Status

This whitepaper is a public-review anchor, not a launch announcement. LegacyNote has no public mainnet, no public testnet, no public mining, no official pool, and no release binary at this stage.

The selected supply contract and proposed activation timestamp are review parameters. They are not final mainnet parameters until public review, build verification, testnet results, release artifacts, and published hashes support them.

Official LegacyNote materials should not discuss price, exchanges, paid listings, donations, bounties, giveaways, or investment expectations.

The founder may operate pseudonymously. LegacyNote does not make a claim of perfect anonymity. The project should be judged by public source, public artifacts, chain state, activation mechanics, and handoff process rather than by founder identity.

## Purpose

LegacyNote exists to show that a CryptoNote-style chain can be launched without insider enrichment, private launch windows, or founder-controlled extraction. The project does not ask reviewers to trust a personality, brand, or marketing campaign. It asks reviewers to inspect the launch mechanics.

The intended proof is procedural and technical:

- the source is public before mainnet,
- build instructions and release hashes are public before mainnet,
- mainnet has a fixed public activation timestamp,
- consensus rejects non-genesis mainnet blocks before that timestamp,
- genesis creates no spendable founder output,
- the founder has no allocation and no special mining window,
- control is intended to pass to community maintainers after launch stability.

Founder identity is intentionally outside the proof model. A reviewer should not need to know who the founder is to verify whether the launch is clean.

## Public Commitments

LegacyNote official materials and launch infrastructure are bound by the following commitments:

- No premine.
- No ICO, presale, private sale, or paid insider access.
- No dev fee, founder fee, treasury, donation wallet, or automatic funding address.
- No founder allocation.
- Founder identity is not part of the trust model.
- No market promotion, price discussion, exchange promises, paid listing promises, or investment framing.
- No gatekeeping over pools, exchanges, explorers, wallets, marketing, or community initiatives.
- Founder mining, if any, begins only after the public mainnet activation timestamp and uses the same public software as everyone else.
- After public launch, the founder may participate like any other community member, including mining or building independent tools, but receives no privileged access, allocation, official fee stream, or gatekeeping power.
- Future protocol changes are community decisions, not founder decrees.

These commitments are intentionally restrictive. They remove common ways a launch can quietly become extractive.

## Technical Baseline

LegacyNote begins from Monero `v0.18.5.0` and keeps a conservative protocol posture. Version 1 is limited to core command-line software:

- `legacynoted`
- `legacynote-wallet-cli`
- `legacynote-wallet-rpc`

Preserved Monero-style properties include:

- RandomX proof of work,
- 2-minute target blocks,
- RingCT,
- stealth addresses,
- ring signatures,
- dynamic block weight,
- tail emission as a long-term miner-incentive principle.

LegacyNote does not seek protocol novelty at launch. The main technical work is identity separation, launch integrity, supply clarity, and auditability.

LegacyNote uses deliberately selected emission constants rather than copying Monero's monetary contract by accident.

Selected supply parameters:

- `MONEY_SUPPLY = 36,902,026` LGN at 11 decimals.
- `MONEY_SUPPLY = 3,690,202,600,000,000,000` atomic units.
- `EMISSION_SPEED_FACTOR_PER_MINUTE = 20`.
- `FINAL_SUBSIDY_PER_MINUTE = 30000000000` atomic units, or `0.3` LGN per minute.
- With 2-minute blocks, tail emission is `0.6` LGN per block, about `432` LGN per day.
- There is no hard cap because tail emission continues indefinitely.

These values are selected for review and must be verified through builds, tests, and a reproducible public supply table before mainnet. LegacyNote uses 11 display decimals so the selected reference supply fits Monero's existing `uint64_t` amount type.

## Network Identity Separation

LegacyNote must not accidentally join Monero networks or reuse Monero address space. The implementation resets network identity at the chain, network, wallet, and user-visible layers.

| Network | P2P | RPC | ZMQ |
| --- | ---: | ---: | ---: |
| Mainnet | `19580` | `19581` | `19582` |
| Testnet | `29580` | `29581` | `29582` |
| Stagenet | `39580` | `39581` | `39582` |

Identity separation includes network IDs, address prefixes, genesis data, checkpoints, DNS seeds, update endpoints, data paths, wallet cache magic, OpenAlias marker, URI scheme, and public binary names.

## Launch Mechanics

The public sequence is:

1. Publish this whitepaper, source, implementation notes, and a public PRE-ANN review thread.
2. Hold at least 7 public review days before testnet.
3. Open public testnet only after visible independent interest and no unresolved critical objections.
4. Publish source, build instructions, release hashes, and binaries at least 7 days before mainnet.
5. Publish final supply parameters, a reproducible supply table, zero-premine proof, and activation-guard proof.
6. Activate mainnet at a fixed public timestamp.
7. Permit no valid non-genesis mainnet block before that timestamp.
8. Transfer repository, admin, and infrastructure control to community maintainers after launch stability.

No private mainnet binaries, private seed access, private mining window, or privileged launch instructions should exist.

The current implementation contains a proposed activation timestamp of `2026-07-04T16:00:00Z`. It must be reviewed and deliberately finalized before any public mainnet release candidate.

## Zero Premine Proof

LegacyNote genesis is configured with no spendable outputs. The genesis miner transaction must have:

- zero outputs,
- zero fee,
- zero base reward.

Any release candidate must include an independently reproducible proof from chain state showing that the genesis transaction creates no founder allocation.

The proof obligation should remain simple. A reviewer should be able to read the source, rebuild the binaries, inspect the genesis state, and confirm that the first non-genesis mainnet block cannot be valid before the public activation time.

## Public Review Gate

The whitepaper is published before testnet so objections can surface while the project is still easy to change. Review should focus on launch integrity, not market interest.

The Bitcointalk post should remain a `PRE-ANN` while this gate is active. Its purpose is to request technical and process review, not to announce mining availability.

Reviewers are asked to check:

- whether the no-premine claim is directly provable,
- whether the activation guard prevents early mainnet mining,
- whether LegacyNote is separated from Monero network identity,
- whether the selected supply parameters are explicit, reviewed, and reproducible from source,
- whether inherited Monero infrastructure has been removed or replaced where necessary,
- whether official materials avoid investment framing,
- whether the handoff plan is credible enough for a project that intends to become community-maintained.

If review identifies unresolved critical issues, testnet should wait.

## Testnet Gate

Testnet should begin only after the public review period has passed, visible independent interest exists, and no launch-critical objections remain unresolved.

Testnet must verify at minimum:

- daemon startup and sync behavior,
- wallet creation and restore,
- mining on testnet,
- send and receive flows,
- daemon RPC and wallet RPC,
- seed failover,
- short reorg recovery,
- address isolation from Monero tooling,
- rejection of Monero network identity,
- mainnet pre-activation mining rejection.

## Mainnet Gate

Mainnet should not be treated as ready until the project has:

- a finalized activation timestamp,
- finalized supply parameters matching the reviewed contract,
- a public supply table generated from source constants,
- public source tag,
- public build instructions,
- published release hashes,
- public binaries,
- zero-premine proof,
- activation-guard proof,
- no unresolved critical review objections.

The founder should not receive private mainnet binaries or mine before the public activation timestamp.

## Governance And Handoff

The founder role is temporary. Before mainnet, credible community takeover may happen immediately if independent maintainers step forward and the public process remains intact. If not, the founder continues only through launch stability, then transfers repository, admin, and infrastructure keys to community maintainers.

Protocol changes after launch should come from public discussion, review, and community consent. LegacyNote should not depend on founder decrees.

## Community Participation And Tool Funding

No one should be blocked from building around LegacyNote. That includes pools, explorers, wallets, documentation, mining tools, and other ecosystem work. The founder may also build such tools after public launch under the same rules as everyone else.

The line is privilege. Founder-built tools must not receive private launch access, hidden advantages, protocol-level fees, official default donation streams, or special endorsement that prevents competing tools.

Funding for independent tools should be transparent and opt-in. A GUI wallet or pool may ask users for voluntary support, but official LegacyNote materials should not include a donation wallet, and default-on mining donations are not recommended because they can look like a disguised dev fee. If a community tool adds a donation option later, it should be clearly disclosed, easy to disable, and never required for normal use.

## Pseudonymous Founder Policy

The founder may use project-only accounts, keys, and public identities. That pseudonymity should not become a substitute for proof. The launch process must still publish enough source, metadata, hashes, and chain-state evidence for reviewers to verify no premine, no founder allocation, no private launch window, and no privileged access.

Public materials should say "pseudonymous founder" if the subject comes up. They should not claim "100% anonymous founder" or imply that operational anonymity can be proven.

## Non-Goals

LegacyNote version 1 does not include a GUI, explorer, pool, faucet, exchange integration, mobile wallet, paid listing, paid marketing campaign, paid community management, or official donation address.

Community members may build those things independently. Official materials should not promise them.

## Communication Tone

Official LegacyNote communication should stay calm and factual. It should not claim moral superiority, promise future value, attack other projects, encourage speculation, or use price-oriented language.

LegacyNote is open-source software and a clean launch process. The proof is in the mechanics: public source, public review, fixed timestamps, reproducible artifacts, zero-premine chain state, and community handoff.
