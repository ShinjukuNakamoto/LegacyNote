# LegacyNote Release Checklist

This checklist is for LegacyNote v1 CLI releases. It intentionally excludes market, exchange, listing, and donation tasks.

## Before Testnet

- [ ] Public forum post is a `PRE-ANN`, not an `ANN`.
- [ ] Public materials state that mainnet, testnet, mining, and official pools are not launched.
- [ ] Public materials use "pseudonymous founder" language if founder identity is discussed.
- [ ] Public materials do not claim perfect founder anonymity.
- [ ] Repository-local Git author metadata uses the project identity, not personal global Git config.
- [ ] Public source has been scrubbed for personal paths, personal emails, private URLs, and secrets.
- [ ] Public materials state that founder post-launch participation is ordinary community participation only.
- [ ] No official default-on donation, mining donation, or hidden fee is present in launch materials or release artifacts.
- [ ] Whitepaper has been public for at least 7 full days.
- [ ] No unresolved critical launch-mechanics objection remains.
- [ ] Testnet source is public.
- [ ] Testnet build instructions are public.
- [ ] Testnet seed configuration is public.
- [ ] Testnet binaries, if published, have SHA256 hashes.

## Before Mainnet Candidate

- [ ] Mainnet activation timestamp is final and public in UTC.
- [ ] `LEGACYNOTE_MAINNET_ACTIVATION_TIMESTAMP` matches the public timestamp.
- [ ] Final supply parameters are documented in public.
- [ ] Public supply parameters specify `36,902,026` LGN reference supply, `0.6` LGN tail reward per 2-minute block, no premine, no founder allocation, and no hard cap.
- [ ] Public supply parameters specify 11 display decimals and `3,690,202,600,000,000,000` atomic units.
- [ ] Emission constants in `src/cryptonote_config.h` match the public supply parameters.
- [ ] A reproducible supply table is published from source constants.
- [ ] `LEGACYNOTE_ZERO_PREMINE_GENESIS` is enabled.
- [ ] Genesis transaction has no outputs.
- [ ] Embedded Monero checkpoints are absent.
- [ ] Monero DNS seeds are absent.
- [ ] Monero update endpoints are absent or disabled.
- [ ] LegacyNote ports and address prefixes are verified.
- [ ] CLI binaries are named `legacynoted`, `legacynote-wallet-cli`, and `legacynote-wallet-rpc`.

## Build Verification

- [ ] Linux daemon, wallet CLI, and wallet RPC build.
- [ ] Windows daemon, wallet CLI, and wallet RPC build.
- [ ] macOS daemon, wallet CLI, and wallet RPC build.
- [ ] Unit tests pass.
- [ ] Functional tests pass.
- [ ] Daemon tests pass.
- [ ] Wallet tests pass.
- [ ] RPC tests pass.
- [ ] Mining tests pass.
- [ ] Reproducible build notes are published.
- [ ] Release hashes are published at least 7 days before activation.
- [ ] Release signatures use project-controlled signing keys, not personal keys.

## Launch Verification

- [ ] Mainnet mining is impossible before activation.
- [ ] Non-genesis mainnet blocks before activation are rejected.
- [ ] First post-activation block can be mined with public software.
- [ ] Zero premine proof is published from chain state.
- [ ] Founder has no allocation and no private mining window.
- [ ] Public seed/node list contains no private privileged entries.

## Handoff

- [ ] Community maintainers are identified publicly.
- [ ] Repository permissions are transferred or made multi-maintainer.
- [ ] Domain, DNS, seed, and infrastructure access are transferred or made multi-maintainer.
- [ ] Release signing custody is documented.
- [ ] Founder post-launch role is documented as non-controlling.
