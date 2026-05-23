# LegacyNote Launch Constants Verifier

- Status: first source-level verification artifact
- Mainnet status: not launched
- Testnet status: not launched

This verifier checks the launch constants that support the current no-extraction review claims. It is intentionally small and uses only the Python standard library.

Run from the repository root:

```powershell
python utils/verify_launch_constants.py
```

On Linux or macOS:

```sh
python3 utils/verify_launch_constants.py
```

## What It Checks

The script reads `src/cryptonote_config.h` and `src/cryptonote_core/blockchain.cpp` and verifies:

- `MONEY_SUPPLY = 3,690,202,600,000,000,000` atomic units,
- `CRYPTONOTE_DISPLAY_DECIMAL_POINT = 11`,
- derived reference supply is `36,902,026` LGN,
- `FINAL_SUBSIDY_PER_MINUTE = 30,000,000,000` atomic units,
- `DIFFICULTY_TARGET_V2 = 120` seconds,
- derived tail reward is `0.6` LGN per 2-minute block,
- `LEGACYNOTE_MAINNET_ACTIVATION_TIMESTAMP = 1783180800`,
- derived activation UTC time is `2026-07-04T16:00:00Z`,
- each configured genesis transaction blob is `013c01ff000000`,
- the parsed genesis transaction has zero outputs,
- source-level activation guard hooks are present for mining templates and incoming mainnet blocks.

## Limits

This is not a substitute for build verification, functional tests, release hashes, or a chain-state proof. It is the first public-review artifact for checking whether the source currently matches the selected supply, activation, and zero-premine parameters.

Before any mainnet release candidate, this should be followed by:

- a successful daemon and wallet build,
- unit and functional tests,
- a reproducible supply table,
- a chain-state zero-premine proof,
- release hashes generated from public binaries.
