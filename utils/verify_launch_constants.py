#!/usr/bin/env python3
"""Verify LegacyNote launch constants from source files.

This is a source-level verifier. It does not replace a build, runtime test,
chain-state proof, or release hash verification.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
from decimal import Decimal
from pathlib import Path


EXPECTED = {
    "display_decimals": 11,
    "money_supply_atoms": 3_690_202_600_000_000_000,
    "money_supply_lgn": Decimal("36902026"),
    "final_subsidy_per_minute_atoms": 30_000_000_000,
    "difficulty_target_seconds": 120,
    "tail_reward_atoms_per_block": 60_000_000_000,
    "tail_reward_lgn_per_block": Decimal("0.6"),
    "activation_timestamp": 1_783_180_800,
    "activation_utc": "2026-07-04T16:00:00Z",
    "genesis_tx_hex": "013c01ff000000",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def macro_value(text: str, name: str) -> int:
    pattern = re.compile(rf"^\s*#define\s+{re.escape(name)}\s+(.+?)(?://.*)?$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        raise ValueError(f"Missing macro {name}")

    value = re.sub(r"\(\s*uint64_t\s*\)", "", match.group(1))
    value = re.sub(r"\b(?:ull|ULL|ul|UL|u|U|l|L)\b", "", value)
    number = re.search(r"\d+", value)
    if not number:
        raise ValueError(f"Could not parse numeric value for {name}: {match.group(1)!r}")
    return int(number.group(0))


def genesis_tx_values(text: str) -> list[str]:
    return re.findall(r'GENESIS_TX\s*=\s*"([0-9a-fA-F]+)"', text)


def read_varint(data: bytes, offset: int) -> tuple[int, int]:
    value = 0
    shift = 0
    while True:
        if offset >= len(data):
            raise ValueError("Unexpected end while reading varint")
        byte = data[offset]
        offset += 1
        value |= (byte & 0x7F) << shift
        if not byte & 0x80:
            return value, offset
        shift += 7


def parse_genesis_tx(blob_hex: str) -> dict[str, int]:
    data = bytes.fromhex(blob_hex)
    offset = 0
    version, offset = read_varint(data, offset)
    unlock_time, offset = read_varint(data, offset)
    input_count, offset = read_varint(data, offset)
    if offset >= len(data):
        raise ValueError("Missing input tag")
    input_tag = data[offset]
    offset += 1
    input_height, offset = read_varint(data, offset)
    output_count, offset = read_varint(data, offset)
    extra_size, offset = read_varint(data, offset)

    if offset + extra_size != len(data):
        raise ValueError("Genesis transaction has trailing or truncated extra data")

    return {
        "version": version,
        "unlock_time": unlock_time,
        "input_count": input_count,
        "input_tag": input_tag,
        "input_height": input_height,
        "output_count": output_count,
        "extra_size": extra_size,
    }


def normalized(text: str) -> str:
    return " ".join(text.split())


def pass_fail(name: str, actual, expected) -> dict[str, object]:
    return {
        "name": name,
        "actual": actual,
        "expected": expected,
        "pass": actual == expected,
    }


def main() -> int:
    root = repo_root()
    config_path = root / "src" / "cryptonote_config.h"
    blockchain_path = root / "src" / "cryptonote_core" / "blockchain.cpp"

    config = read_text(config_path)
    blockchain = read_text(blockchain_path)

    display_decimals = macro_value(config, "CRYPTONOTE_DISPLAY_DECIMAL_POINT")
    atomic_units_per_lgn = 10 ** display_decimals
    money_supply_atoms = macro_value(config, "MONEY_SUPPLY")
    final_subsidy_per_minute_atoms = macro_value(config, "FINAL_SUBSIDY_PER_MINUTE")
    difficulty_target_seconds = macro_value(config, "DIFFICULTY_TARGET_V2")
    activation_timestamp = macro_value(config, "LEGACYNOTE_MAINNET_ACTIVATION_TIMESTAMP")
    activation_utc = dt.datetime.fromtimestamp(
        activation_timestamp,
        tz=dt.timezone.utc,
    ).strftime("%Y-%m-%dT%H:%M:%SZ")

    tail_reward_atoms_per_block = final_subsidy_per_minute_atoms * difficulty_target_seconds // 60
    money_supply_lgn = Decimal(money_supply_atoms) / Decimal(atomic_units_per_lgn)
    tail_reward_lgn_per_block = Decimal(tail_reward_atoms_per_block) / Decimal(atomic_units_per_lgn)

    genesis_values = genesis_tx_values(config)
    genesis_unique = sorted(set(genesis_values))
    genesis_parsed = parse_genesis_tx(EXPECTED["genesis_tx_hex"])

    chain_source = normalized(blockchain)
    activation_guard_checks = {
        "mining_template_time_guard": "m_nettype == MAINNET && height > 0 && time(NULL) < LEGACYNOTE_MAINNET_ACTIVATION_TIMESTAMP" in chain_source,
        "incoming_block_timestamp_guard": "m_nettype == MAINNET && blockchain_height > 0 && bl.timestamp < LEGACYNOTE_MAINNET_ACTIVATION_TIMESTAMP" in chain_source,
        "incoming_block_wallclock_guard": "m_nettype == MAINNET && blockchain_height > 0 && time(NULL) < LEGACYNOTE_MAINNET_ACTIVATION_TIMESTAMP" in chain_source,
    }

    checks = [
        pass_fail("display_decimals", display_decimals, EXPECTED["display_decimals"]),
        pass_fail("money_supply_atoms", money_supply_atoms, EXPECTED["money_supply_atoms"]),
        pass_fail("money_supply_lgn", str(money_supply_lgn), str(EXPECTED["money_supply_lgn"])),
        pass_fail("final_subsidy_per_minute_atoms", final_subsidy_per_minute_atoms, EXPECTED["final_subsidy_per_minute_atoms"]),
        pass_fail("difficulty_target_seconds", difficulty_target_seconds, EXPECTED["difficulty_target_seconds"]),
        pass_fail("tail_reward_atoms_per_block", tail_reward_atoms_per_block, EXPECTED["tail_reward_atoms_per_block"]),
        pass_fail("tail_reward_lgn_per_block", str(tail_reward_lgn_per_block), str(EXPECTED["tail_reward_lgn_per_block"])),
        pass_fail("activation_timestamp", activation_timestamp, EXPECTED["activation_timestamp"]),
        pass_fail("activation_utc", activation_utc, EXPECTED["activation_utc"]),
        pass_fail("genesis_tx_values", genesis_unique, [EXPECTED["genesis_tx_hex"]]),
        pass_fail("genesis_output_count", genesis_parsed["output_count"], 0),
        pass_fail("genesis_input_count", genesis_parsed["input_count"], 1),
        pass_fail("genesis_input_tag", genesis_parsed["input_tag"], 0xFF),
        pass_fail("genesis_input_height", genesis_parsed["input_height"], 0),
        pass_fail("activation_guard_checks", activation_guard_checks, {
            "mining_template_time_guard": True,
            "incoming_block_timestamp_guard": True,
            "incoming_block_wallclock_guard": True,
        }),
    ]

    report = {
        "repository": ".",
        "source_files": [
            config_path.relative_to(root).as_posix(),
            blockchain_path.relative_to(root).as_posix(),
        ],
        "status": "pass" if all(item["pass"] for item in checks) else "fail",
        "checks": checks,
        "derived": {
            "atomic_units_per_lgn": atomic_units_per_lgn,
            "tail_emission_continues": tail_reward_atoms_per_block > 0,
            "genesis_tx_parsed": genesis_parsed,
        },
        "limits": [
            "Source-level verification only.",
            "Does not compile the daemon or wallet.",
            "Does not prove runtime chain state.",
            "Does not verify release binaries or hashes.",
        ],
    }

    print("LegacyNote launch constants verifier")
    print(f"Status: {report['status'].upper()}")
    for item in checks:
        mark = "PASS" if item["pass"] else "FAIL"
        print(f"{mark} {item['name']}: {item['actual']}")
    print()
    print(json.dumps(report, indent=2))

    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
