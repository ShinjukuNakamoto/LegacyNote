# Contributing To LegacyNote

LegacyNote welcomes public review and contributions that improve the code, launch mechanics, documentation, testing, and handoff process.

## Ground Rules

- Keep discussion public whenever possible.
- Keep official project language factual and calm.
- Do not use official spaces for price, market, listing, or investment promotion.
- Do not ask for a founder allocation, dev fee, treasury, donation wallet, or paid insider access.
- Do not gatekeep independent pools, explorers, wallets, exchanges, or community work.
- Do not use founder identity as evidence for launch integrity. The project may use a pseudonymous founder identity, but the proof must come from source, artifacts, and chain state.
- Do not add default-on donation, mining donation, hidden fee, or protocol-level funding behavior to official launch software.
- Preserve the no-extraction launch commitments unless the community explicitly replaces this project with something else.

## Preferred Changes

- Network identity separation from Monero.
- Build and test fixes.
- Reproducible release improvements.
- Zero-premine proof tooling.
- Mainnet activation guard tests.
- Documentation that makes the launch easier to audit.
- Security review and conservative upstream compatibility fixes.

## Protocol Changes

LegacyNote starts conservatively from Monero `v0.18.5.0`. Protocol changes after launch should require public discussion, review, and community consent. Founder preference is not a governance mechanism.

## Independent Tools

Pools, explorers, GUI wallets, mining helpers, documentation, and other ecosystem tools can be built independently by anyone, including the founder after public launch. They should not be represented as privileged official launch infrastructure unless the community maintainers explicitly adopt them.

Funding for independent tools should be transparent and opt-in. A donation prompt is different from a default-on mining donation or hidden fee. The latter conflicts with the no-extraction launch posture.

## Reporting Security Issues

Until community maintainers publish a formal security process, report suspected vulnerabilities privately to the current repository administrators, then coordinate a public disclosure timeline that protects users. This temporary process should be replaced during the maintainer handoff.
