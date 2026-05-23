# LegacyNote Pseudonymous Operations

- Status: working checklist
- Mainnet status: not launched
- Testnet status: not launched

LegacyNote may be launched by a pseudonymous founder. That is different from a promise of perfect anonymity. Public materials should not claim that the founder is untraceable or 100% anonymous.

The launch claim must remain mechanical and verifiable:

- zero premine,
- zero founder allocation,
- no private launch access,
- public source and hashes,
- public activation timestamp,
- reproducible artifacts,
- community handoff.

The founder identity is not part of the trust model. Reviewers should be able to verify the launch process without knowing who the founder is.

## Public Wording

Use:

- "The founder is pseudonymous."
- "The founder receives no allocation."
- "The launch should be verifiable without trusting the founder's identity."
- "The project does not make a claim of perfect anonymity."

Avoid:

- "100% anonymous founder."
- "Untraceable founder."
- "Trust me."
- Any personal backstory or identity hints.

## Account Separation Checklist

Before making the repository public or posting the Bitcointalk PRE-ANN:

- [ ] Create a project-only email account.
- [ ] Create a project-only GitHub account or organization.
- [ ] Create a project-only Bitcointalk account.
- [ ] Use unique passwords stored in a password manager.
- [ ] Avoid personal recovery email, personal phone number, personal avatar, reused username, or reused profile text.
- [ ] Use project-only SSH keys for GitHub.
- [ ] Use a project-only release signing key.
- [ ] Do not reuse personal SSH, GPG, age, minisign, or code-signing keys.

## Git Metadata Checklist

Before the first public commit:

- [ ] Set repository-local `user.name` to the project pseudonym.
- [ ] Set repository-local `user.email` to the project email or GitHub noreply address for the project account.
- [ ] Confirm local repository config overrides any global personal Git config.
- [ ] Confirm commits do not expose a personal name or personal email.
- [ ] Confirm tags, release notes, and signatures use project-controlled identity material.

Example commands, after the project identity exists:

```bash
git config user.name "LegacyNote"
git config user.email "<PROJECT_GITHUB_NOREPLY_OR_EMAIL>"
git config --show-origin --get-regexp "^user\\."
```

## Artifact Scrub

Before posting public links:

- [ ] Search public docs for local paths, personal usernames, personal email addresses, private URLs, and temporary hostnames.
- [ ] Search release scripts and generated files for local machine paths.
- [ ] Confirm no wallet files, seed phrases, private keys, API tokens, cookies, `.env` files, or personal config files are present.
- [ ] Confirm placeholder links in the Bitcointalk post are replaced with public URLs.
- [ ] View the repository as a logged-out or private-browser visitor.

## Infrastructure Notes

For the initial public review stage, avoid infrastructure that creates unnecessary identity or payment trails. A public GitHub repository plus static documentation is enough for the PRE-ANN.

If domains, seed nodes, or VPS infrastructure are used later, document what is project-controlled and what will be handed to community maintainers. Do not make anonymity claims about third-party infrastructure.
