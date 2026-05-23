# LegacyNote Bitcointalk Initial Post Draft

- Status: draft PRE-ANN initial post
- Use: post only after public repository, whitepaper, supply, and launch-process links are ready
- Mainnet status: not launched
- Testnet status: not launched
- Supply status: selected for public review; not mainnet-final until build, test, and release artifacts exist

## Recommended Thread Title

`[PRE-ANN][LGN] LegacyNote - no-premine Monero-codebase fair launch`

Use `PRE-ANN` while LegacyNote is in the whitepaper and public-review stage. Do not switch to `ANN` until public testnet or mainnet release artifacts justify it.

## Before Posting

- Replace all placeholder links.
- Confirm the repository is public.
- Confirm the whitepaper, supply document, and launch process are public.
- Confirm the post says testnet and mainnet are not launched near the top.
- Confirm the project account, GitHub account, and Git commit metadata do not expose a personal identity.
- Do not include price, exchange, listing, bounty, airdrop, donation, giveaway, or investment language.
- Do not imply Bitcointalk endorsement.
- Do not call LegacyNote the first fair-launch CryptoNote coin.
- Do not claim that the founder is 100% anonymous.

## Suggested First Reply Reservations

If the forum flow allows it, reserve the next replies for:

- public review log and changelog,
- supply calculation and zero-premine proof,
- build and test status,
- common questions and project responses.

## BBCode Initial Post

```bbcode
[center][b][size=18pt]LegacyNote (LGN)[/size][/b][/center]
[center]A conservative CryptoNote-style fair-launch project based on the maintained Monero codebase[/center]

[b]Status:[/b] whitepaper / public review stage
[b]Mainnet:[/b] not launched
[b]Testnet:[/b] not launched
[b]Mining:[/b] not available yet
[b]Premine:[/b] 0
[b]Founder allocation:[/b] 0
[b]Founder identity:[/b] pseudonymous; not part of the trust model
[b]ICO / presale:[/b] none
[b]Dev fee / treasury / donation wallet:[/b] none
[b]Supply under review:[/b] 36,902,026 LGN reference supply; 0.6 LGN tail reward per 2-minute block; no hard cap
[b]Activation timestamp under review:[/b] proposed 2026-07-04 16:00:00 UTC; not final

[hr]

[b]Important launch status[/b]

LegacyNote is not launched. There is no mainnet, no testnet, no public mining, no release binary, and no official pool.

This thread is a PRE-ANN for public review of the whitepaper, source changes, supply parameters, and launch process before any testnet begins.

Official LegacyNote posts will not discuss price, exchanges, paid listings, market expectations, donations, bounties, or investment claims.

[hr]

[b]What is LegacyNote?[/b]

LegacyNote is a conservative CryptoNote-style chain based on Monero v0.18.5.0. The project is intended as a modern no-extraction fair launch: no premine, no sale, no dev fee, no treasury, no donation wallet, no paid insider access, and no founder allocation.

LegacyNote is not claimed to be the first fair-launch CryptoNote coin. The claim is narrower and should be directly reviewable: public launch mechanics, public artifacts, no privileged mining window, zero spendable genesis allocation, and a planned handoff from founder control to community maintainers.

The founder is pseudonymous. This is not a claim of perfect anonymity. The launch should be judged by source, chain state, timestamps, hashes, and access rules rather than by founder identity.

[hr]

[b]Core commitments[/b]

[list]
[li]Zero premine, ICO, presale, dev fee, treasury, donation wallet, founder allocation, and paid insider access.[/li]
[li]Founder may mine only after public mainnet activation, using the same public software and rules as everyone else.[/li]
[li]After public launch, founder participation is limited to the same ordinary rights as everyone else: mining, running nodes, or building independent tools without privileged access or gatekeeping power.[/li]
[li]Founder identity is not part of the trust model; the no-extraction claims must be verifiable without trusting a person.[/li]
[li]No private mainnet binaries, private seed access, hidden node list, or private mining window.[/li]
[li]No gatekeeping over pools, explorers, exchanges, wallets, marketing, or community initiatives.[/li]
[li]Source, build instructions, release hashes, and binaries must be public before mainnet.[/li]
[li]Mainnet activation must use a fixed public timestamp with a consensus guard against early non-genesis blocks.[/li]
[li]After launch stability, repository, admin, and infrastructure control are intended to move to community maintainers.[/li]
[/list]

[hr]

[b]Founder and community participation[/b]

The founder is not asking for permanent control or special restrictions on others. Pools, explorers, wallets, mining tools, documentation, and other ecosystem work are open for anyone to build.

The founder may also build independent tools after public launch, under the same rules as everyone else. Such tools must not receive private launch access, protocol-level fees, hidden fees, official default donation streams, or special gatekeeping power.

Independent tools may ask for voluntary support, but any support mechanism should be transparent and opt-in. Default-on mining donations are not part of the LegacyNote launch plan.

[hr]

[b]Development disclosure[/b]

LegacyNote used AI-assisted coding and documentation workflows. No launch claim depends on trusting any AI system. The source, build process, genesis state, supply constants, activation guard, release hashes, and launch timeline must be independently verifiable.

If the community rejects AI-authored or AI-assisted materials, credible community maintainers may take over, rewrite, fork, or replace those materials before testnet or mainnet while preserving the no-extraction fair-launch principles.

[hr]

[b]Technical posture[/b]

[list]
[li][b]Baseline:[/b] Monero v0.18.5.0[/li]
[li][b]V1 software:[/b] daemon, wallet CLI, wallet RPC[/li]
[li][b]Daemon:[/b] legacynoted[/li]
[li][b]Wallet CLI:[/b] legacynote-wallet-cli[/li]
[li][b]Wallet RPC:[/b] legacynote-wallet-rpc[/li]
[li][b]Ticker:[/b] LGN[/li]
[li][b]Proof of work:[/b] RandomX[/li]
[li][b]Block target:[/b] 2 minutes[/li]
[li][b]Privacy model:[/b] RingCT, stealth addresses, ring signatures[/li]
[li][b]Emission:[/b] 36,902,026 LGN reference supply with ongoing tail emission[/li]
[li][b]Tail subsidy:[/b] 0.6 LGN per 2-minute block[/li]
[li][b]Hard cap:[/b] none, because tail emission continues indefinitely[/li]
[/list]

[b]Default ports[/b]

[list]
[li]Mainnet: P2P 19580 / RPC 19581 / ZMQ 19582[/li]
[li]Testnet: P2P 29580 / RPC 29581 / ZMQ 29582[/li]
[li]Stagenet: P2P 39580 / RPC 39581 / ZMQ 39582[/li]
[/list]

[hr]

[b]Supply parameters selected for review[/b]

The current source constants select:

[list]
[li]36,902,026 LGN reference supply[/li]
[li]0.6 LGN tail reward per 2-minute block[/li]
[li]0 premine[/li]
[li]0 founder allocation[/li]
[li]no hard cap[/li]
[li]11 display decimals, so the selected reference supply fits the inherited uint64 amount type[/li]
[/list]

These parameters must be verified through builds, tests, and a reproducible public supply table before any mainnet release candidate.

[hr]

[b]Launch sequence[/b]

[list=1]
[li]Publish whitepaper, source, implementation notes, and public review thread.[/li]
[li]Hold at least 7 public review days before any testnet.[/li]
[li]Start public testnet only after visible independent interest and no unresolved critical launch-mechanics objections.[/li]
[li]Publish source tag, build instructions, release hashes, and binaries at least 7 days before mainnet.[/li]
[li]Publish final supply parameters, zero-premine proof, and activation-guard proof.[/li]
[li]Activate mainnet at a fixed public UTC timestamp.[/li]
[li]Move repository, admin, and infrastructure control to community maintainers after launch stability.[/li]
[/list]

[hr]

[b]Current review request[/b]

Review is requested on:

[list]
[li]whether the no-premine claim is directly provable from genesis state,[/li]
[li]whether the activation guard prevents early mainnet mining,[/li]
[li]whether LegacyNote is sufficiently separated from Monero network identity,[/li]
[li]whether the selected 36,902,026 LGN / 0.6 LGN tail supply contract is clear and reproducible,[/li]
[li]whether the launch process prevents private access or founder advantage,[/li]
[li]whether the founder/community participation language preserves no-extraction while allowing independent tools,[/li]
[li]whether the pseudonymous-founder posture is framed honestly and does not replace technical proof,[/li]
[li]whether official materials avoid market and investment framing,[/li]
[li]whether the founder handoff plan is credible and specific enough.[/li]
[/list]

[hr]

[b]Links[/b]

[list]
[li]Repository: [url=https://github.com/ShinjukuNakamoto/LegacyNote]https://github.com/ShinjukuNakamoto/LegacyNote[/url][/li]
[li]Whitepaper: [url=https://github.com/ShinjukuNakamoto/LegacyNote/blob/main/docs/LEGACYNOTE_WHITEPAPER.md]https://github.com/ShinjukuNakamoto/LegacyNote/blob/main/docs/LEGACYNOTE_WHITEPAPER.md[/url][/li]
[li]Supply document: [url=https://github.com/ShinjukuNakamoto/LegacyNote/blob/main/docs/SUPPLY.md]https://github.com/ShinjukuNakamoto/LegacyNote/blob/main/docs/SUPPLY.md[/url][/li]
[li]Launch process: [url=https://github.com/ShinjukuNakamoto/LegacyNote/blob/main/docs/LAUNCH_PROCESS.md]https://github.com/ShinjukuNakamoto/LegacyNote/blob/main/docs/LAUNCH_PROCESS.md[/url][/li]
[/list]

[b]Please keep this thread focused on source review, launch mechanics, supply reproducibility, and testnet readiness. There is nothing to mine yet, and official posts will not discuss price, exchanges, listings, donations, bounties, or investment expectations.[/b]
```
