# LegacyNote Supply

- Status: selected for public review
- Mainnet status: not launched
- Testnet status: not launched

LegacyNote uses a Monero-style emission curve with LegacyNote-specific constants. The goal is a simple, non-promotional supply contract that can be reproduced from source.

These parameters are selected for review, not finalized for mainnet. They must survive public review, build verification, testnet checks, and a reproducible supply-table pass before any release candidate.

## Constants

The selected constants in `src/cryptonote_config.h` are:

| Parameter | Value |
| --- | ---: |
| Display decimals | `11` |
| Atomic units per LGN | `100,000,000,000` |
| Reference supply | `36,902,026` LGN |
| Reference supply in atomic units | `3,690,202,600,000,000,000` |
| Emission speed factor per minute | `20` |
| Block target | `120` seconds |
| Tail subsidy | `0.6` LGN per block |

The reference supply is not a hard cap. Tail emission continues indefinitely.

The 11-decimal display precision is an implementation constraint: it allows the selected reference supply to fit Monero's inherited `uint64_t` amount type. It should not be treated as a promotional feature.

## Tail Emission

At 2-minute blocks, the selected tail subsidy is:

- `0.6` LGN per block,
- `432` LGN per day,
- `157,680` LGN per 365-day year.

## Estimated Tail Transition

Using the current CryptoNote reward formula and selected constants, tail emission begins around block `2,498,130`, roughly `9.51` years after the first non-genesis block at the 2-minute target.

The approximate generated supply before the first tail block is:

- `36,587,453.59983037809` LGN generated,
- `314,572.40016962191` LGN remaining against the reference supply.

These figures should be regenerated from source before any public release candidate.

## Review Notes

The supply design intentionally avoids scarcity framing. The important public claims are:

- no premine,
- no founder allocation,
- no dev fee,
- no treasury,
- predictable emission from source constants,
- ongoing tail emission for long-term miner incentives.

The supply document should not be used to imply future price, exchange interest, investment value, or scarcity marketing.
