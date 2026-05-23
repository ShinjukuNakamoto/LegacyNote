# LegacyNote

LegacyNote is a conservative CryptoNote-style chain based on the maintained Monero codebase. It is not claimed to be the first fair-launch CryptoNote coin. The intended claim is narrower and easier to verify: a modern no-extraction launch with public process, no privileged access, and a planned founder handoff.

This repository currently tracks an implementation pass based on Monero `v0.18.5.0`. Mainnet and testnet are not launched, and mining is not available yet.

The founder may operate pseudonymously. LegacyNote does not claim perfect anonymity for the founder; the point is that the launch should be verifiable without trusting or identifying the founder.

## Commitments

- Zero premine, zero ICO, zero presale, zero dev fee, zero treasury, zero donation wallet, and zero founder allocation.
- The founder receives no allocation and may mine only after public mainnet activation, using the same public software and rules as everyone else.
- Founder identity is not part of the trust model. The no-extraction claims must be proven from public source, public artifacts, and chain state.
- No market promotion, price talk, exchange promises, paid listings, donations, bounties, giveaways, hype language, or investment framing.
- No gatekeeping over pools, exchanges, explorers, wallets, marketing, or community initiatives.
- After public launch, the founder keeps the same ordinary rights as everyone else to mine and build independent tools, including pools or wallets, without privileged access or official gatekeeping power.
- Source, build instructions, release hashes, and binaries are public before mainnet.
- Mainnet activation is guarded by a fixed public timestamp. No valid non-genesis mainnet block should exist before that time.
- After launch stability, repository, admin, and infrastructure control are intended to move to community maintainers.
- Future protocol changes are community decisions, not founder decrees.

## Scope

V1 is core CLI only:

- `legacynoted`
- `legacynote-wallet-cli`
- `legacynote-wallet-rpc`

V1 excludes GUI, explorer, pool, faucet, exchange integrations, mobile wallets, paid listings, paid marketing, and paid community management.

Independent post-launch tools may be built by anyone, including the founder after the public launch. Funding for those tools should be explicit and opt-in. Default-on mining donations, protocol-level fees, hidden fees, or official donation addresses would conflict with the no-extraction posture.

## Network Identity

LegacyNote resets the network identity inherited from Monero:

| Network | P2P | RPC | ZMQ |
| --- | ---: | ---: | ---: |
| Mainnet | `19580` | `19581` | `19582` |
| Testnet | `29580` | `29581` | `29582` |
| Stagenet | `39580` | `39581` | `39582` |

The implementation also resets network IDs, address prefixes, genesis data, DNS seeds, embedded checkpoints, update URLs, OpenAlias marker, wallet cache magic, and public binary names.

## Consensus Posture

LegacyNote intentionally preserves Monero-style consensus unless identity separation requires otherwise:

- RandomX proof of work
- 2-minute target blocks
- RingCT
- Stealth addresses
- Ring signatures
- Dynamic block weight
- Tail emission

The current mainnet activation guard is set in `src/cryptonote_config.h` as `LEGACYNOTE_MAINNET_ACTIVATION_TIMESTAMP`. In this implementation pass it is `1783180800`, which is `2026-07-04 16:00:00 UTC`. Treat that value as a public launch parameter that must be deliberately reviewed before any release.

## Supply

LegacyNote uses a deliberately selected Monero-style emission contract, not an inherited default:

- `MONEY_SUPPLY = 36,902,026` LGN at 11 decimals.
- `MONEY_SUPPLY = 3,690,202,600,000,000,000` atomic units.
- `EMISSION_SPEED_FACTOR_PER_MINUTE = 20`.
- `FINAL_SUBSIDY_PER_MINUTE = 30000000000` atomic units, or `0.3` LGN per minute.
- With 2-minute blocks, tail emission is `0.6` LGN per block, about `432` LGN per day.

The reference supply is not a hard cap because tail emission continues indefinitely. LegacyNote uses 11 display decimals so the selected reference supply fits Monero's existing `uint64_t` amount type. The selected constants still need build verification and a reproducible public supply table before any mainnet release candidate.

## Zero Premine

The genesis transaction is configured with no outputs. The chain validation path special-cases height `0` so the genesis miner transaction is valid only when it has:

- no outputs,
- zero fee,
- zero base reward.

That means there is no spendable founder allocation in the genesis state. The planned release process requires publishing a simple chain-state proof before mainnet binaries are treated as launch candidates.

## Build

The upstream Monero build system is retained. A typical Linux build is:

```bash
git submodule update --init --recursive
make release
```

The resulting v1 binaries are expected under the release build directory with the LegacyNote names:

```bash
legacynoted
legacynote-wallet-cli
legacynote-wallet-rpc
```

For reproducible release work, use the pinned source tree, clean build environments, published build commands, and published SHA256 hashes.

## Launch Documents

- [Whitepaper](docs/LEGACYNOTE_WHITEPAPER.md)
- [Supply](docs/SUPPLY.md)
- [Pseudonymous operations](docs/PSEUDONYMOUS_OPERATIONS.md)
- [Bitcointalk initial post draft](docs/BITCOINTALK_ANNOUNCEMENT.md)
- [Launch process](docs/LAUNCH_PROCESS.md)
- [Fair launch checklist](docs/FAIR_LAUNCH_CHECKLIST.md)
- [Release checklist](docs/RELEASE_CHECKLIST.md)

## Upstream

LegacyNote is based on the Monero source tree and keeps Monero's copyright and license history. Upstream technical references:

- [Monero source](https://github.com/monero-project/monero)
- [Monero releases](https://github.com/monero-project/monero/releases)
- [Monero technical specs](https://docs.getmonero.org/technical-specs/)

Inherited technical documents may still mention Monero where they describe upstream internals. Public LegacyNote launch materials should remain calm, factual, and free of investment framing.
