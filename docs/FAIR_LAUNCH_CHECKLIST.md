# LegacyNote Fair Launch Checklist

## Source Identity

- [ ] Monero baseline tag documented as `v0.18.5.0`.
- [ ] Project rebranded to LegacyNote / LGN for v1 CLI binaries.
- [ ] Mainnet, testnet, and stagenet network IDs reset.
- [ ] Mainnet, testnet, and stagenet address prefixes reset.
- [ ] Mainnet ports set to `19580`, `19581`, `19582`.
- [ ] Testnet ports set to `29580`, `29581`, `29582`.
- [ ] Stagenet ports set to `39580`, `39581`, `39582`.
- [ ] DNS seeds use LegacyNote-controlled or community-published domains only.
- [ ] Embedded checkpoints do not inherit Monero chain data.
- [ ] Update checks do not query Monero infrastructure.

## No Extraction

- [ ] No premine.
- [ ] No founder allocation.
- [ ] No ICO, presale, private sale, or paid insider access.
- [ ] No dev fee.
- [ ] No treasury.
- [ ] No donation wallet.
- [ ] No bounty, giveaway, or airdrop promise in official launch materials.
- [ ] No official paid listing or exchange promise.
- [ ] No official market or investment language.
- [ ] Bitcointalk thread is posted as `PRE-ANN` while testnet and mainnet are not launched.
- [ ] Founder is described as pseudonymous only if needed; no claim of perfect anonymity is made.
- [ ] Founder identity is not used as evidence for any launch-integrity claim.
- [ ] Founder post-launch participation is documented as ordinary community participation only.
- [ ] Founder-built or community-built pools, wallets, and tools receive no privileged access or official gatekeeping power.
- [ ] Independent tool funding is opt-in and transparent; no default-on mining donation is included in official launch materials.

## Pseudonymous Operations

- [ ] Project-only email account created.
- [ ] Project-only GitHub account or organization created.
- [ ] Project-only Bitcointalk account created.
- [ ] Repository-local Git `user.name` and `user.email` use the project identity.
- [ ] Public commits do not expose personal Git author metadata.
- [ ] Public tags and release signatures use project-controlled keys.
- [ ] Public docs are scrubbed for personal names, personal emails, local paths, private URLs, and temporary hostnames.
- [ ] No wallet files, seed phrases, private keys, API tokens, cookies, `.env` files, or personal config files are present.

## Activation Guard

- [ ] Mainnet activation timestamp published in UTC.
- [ ] Source constant matches the published timestamp.
- [ ] Mining template creation fails before activation.
- [ ] Received non-genesis mainnet blocks before activation are rejected.
- [ ] Genesis remains valid with zero outputs and zero reward.

## Supply Contract

- [ ] Main-emission reference supply is documented as `36,902,026` LGN unless changed by public review.
- [ ] Reference supply atomic value is documented as `3,690,202,600,000,000,000`.
- [ ] Tail emission is documented as `0.6` LGN per 2-minute block unless changed by public review.
- [ ] No hard cap is documented because tail emission continues indefinitely.
- [ ] Display precision is documented as 11 decimals because of the inherited `uint64_t` amount type.
- [ ] Source emission constants match the public supply document.
- [ ] Supply table can be regenerated from source constants.
- [ ] Supply language avoids scarcity, price, and investment framing.

## Release Artifacts

- [ ] Source tag published.
- [ ] Build instructions published.
- [ ] Linux binary hash published.
- [ ] Windows binary hash published.
- [ ] macOS binary hash published.
- [ ] Reproducible build notes published.
- [ ] Release signed by the documented release key.

## Public Testing

- [ ] Daemon builds and starts.
- [ ] Wallet CLI builds and starts.
- [ ] Wallet RPC builds and starts.
- [ ] Unit tests run.
- [ ] Functional tests run.
- [ ] Daemon tests run.
- [ ] Wallet tests run.
- [ ] RPC tests run.
- [ ] Mining tests run.
- [ ] Testnet send and receive verified.
- [ ] Short reorg recovery verified.
- [ ] Seed failover verified.
- [ ] LegacyNote cannot connect to Monero networks.
- [ ] Monero tooling rejects LegacyNote addresses.

## Handoff

- [ ] Community maintainer criteria published.
- [ ] Repository ownership transfer plan published.
- [ ] Domain and DNS transfer plan published.
- [ ] Seed node access plan published.
- [ ] Release signing key plan published.
- [ ] Founder post-launch role documented as non-controlling.
