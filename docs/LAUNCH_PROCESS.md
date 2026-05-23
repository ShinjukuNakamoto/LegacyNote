# LegacyNote Launch Process

This document defines the public launch sequence for LegacyNote. Dates and hashes must be filled in publicly before each phase begins.

## Phase 1: Whitepaper Review

- Publish the whitepaper and implementation notes.
- Publish the Bitcointalk post only as a `PRE-ANN` public review thread.
- Use project-only public accounts and project-local Git metadata before any public commit or post.
- Keep selected supply parameters visible and reviewable until the code and public supply table are final.
- Keep discussion public.
- State clearly that mainnet, testnet, mining, and official pools are not launched.
- Do not claim that LegacyNote is the first fair-launch CryptoNote coin.
- Do not claim that the founder is 100% anonymous. Use pseudonymous-founder language if founder identity is discussed.
- Do not discuss price, markets, listings, donations, bounties, giveaways, or investment expectations.
- Wait at least 7 public review days before testnet.

Exit criteria:

- At least 7 full days of public review have passed.
- No unresolved critical launch-mechanics objection remains.
- There is visible independent interest in reviewing or running the software.

## Phase 2: Public Testnet

- Publish testnet source and build instructions.
- Publish testnet seed configuration.
- Publish release hashes for any test binaries.
- Run only public testnet binaries.
- Encourage independent nodes, wallets, mining, and RPC testing.

Required testnet checks:

- Daemon sync and peer discovery.
- Wallet create and restore.
- Send and receive.
- Daemon RPC and wallet RPC.
- Mining and reward maturity.
- Seed failover.
- Short reorg recovery.
- LegacyNote cannot connect to Monero networks.
- Monero tooling rejects LegacyNote addresses.

## Phase 3: Mainnet Candidate

- Freeze the intended mainnet source.
- Publish exact build commands.
- Publish release hashes and binaries at least 7 days before activation.
- Publish the activation timestamp in UTC.
- Publish final supply parameters and a reproducible supply table generated from source constants.
- Publish the genesis and zero-premine proof.
- Publish the activation-guard proof.
- Publish the maintainers and key-handoff plan.
- Confirm release signatures and Git metadata use project-controlled identity material, not personal keys.

No privileged access is permitted:

- No private mainnet binaries.
- No private seed access.
- No hidden node list.
- No private mining window.
- No founder allocation.

## Phase 4: Mainnet Activation

- Mainnet activation occurs at the fixed public UTC timestamp.
- The daemon must reject non-genesis mainnet blocks before activation.
- Founder mining, if any, begins only after activation and only with public software.
- Official channels should continue to avoid market language.

## Phase 5: Stability And Handoff

- Monitor chain stability, seed behavior, and release reproducibility.
- Resolve critical launch defects publicly.
- Transfer repository, admin, domain, DNS, seed, and infrastructure access to community maintainers.
- Document who holds which keys and what the rotation process is.
- Founder steps back from control after handoff.
- Founder may continue as an ordinary community participant, including mining or building independent tools, with no special access or gatekeeping authority.
- Any independent tool funding should be transparent and opt-in. Default-on mining donations are not part of the official launch process.
