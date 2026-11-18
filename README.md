# Team Second Brain

Shared product knowledge that your team and its AI agents can use, question and improve through pull requests.

A useful discovery often lives in one person's notes. A decision survives in a chat, but its reasoning does not. The next person asks an agent for help and has to reconstruct the context before any work can begin.

Team Second Brain gives that context a shared home: a Git repository of sources, findings, decisions and project records. Agents read the accepted version, prepare changes on branches and open real Draft PRs. People review the evidence and decide what becomes shared knowledge.

It works on its own or alongside a [private Super Brain](https://github.com/superhero-tech/super-brain). Your private notes stay private; selected material becomes a self-contained contribution to the team.

## Start with an empty brain

1. Choose **Use this template → Create a new repository** on GitHub. Choose visibility appropriate for your team's knowledge.
2. Clone your new repository, run the configuration check below, then open the repository root in Codex or Claude Code.
3. Run `$team-init` in Codex or `/team-init` in Claude Code. Provide your product, team scope, working language, steward, and owners and backups for the areas the team uses. Reviewers are selected for each PR based on its scope and author.
4. The agent prepares the configuration and opens a Draft PR. Review it, then explicitly ask to mark it ready and merge after the required review. Configure repository access and protection using [GitHub setup](docs/github-setup.md).
5. Share a source or a recent decision with `team-update`. This becomes your first knowledge contribution.

```sh
git clone https://github.com/YOUR-ACCOUNT/YOUR-TEAM-BRAIN.git
cd YOUR-TEAM-BRAIN
python3 scripts/doctor.py
```

The template includes structure and workflows, not sample company knowledge. Template instructions are in English. `working_language` in [the team profile](01-Team/team.md) controls the language of new team content; conversations can follow the user's language.

You need Git, Python 3 and Ruby for the included checks, plus access to GitHub to publish branches and PRs. `doctor` checks the skill files, runs the local knowledge check and verifies the accepted revision on `origin`. If `gh` is available, it also reports the CLI account's repository role for a GitHub.com origin.

The report gives separate verdicts for local configuration and repository access. Exit code 1 means there is a confirmed issue to fix. An unavailable network or unverified GitHub role is reported separately and does not fail the local setup check. On a fresh template, the note about `CODEOWNERS` is expected. The command can fetch Git objects without changing the working tree or pushing changes. Use [GitHub setup](docs/github-setup.md) to verify live review enforcement.

An editor or Obsidian can open the same folder; neither is required for the workflows.

## What belongs here

| Folder | Keep here | Example |
| --- | --- | --- |
| [01-Team](01-Team/context-entry.md) | Team context and responsibility | What the product does and who reviews research |
| [02-Knowledge](02-Knowledge/index.md) | Findings, definitions, decisions and practices | What counts as an activated account, and why |
| [03-Projects](03-Projects/index.md) | Briefs, experiments and project summaries | The onboarding pilot and what it taught us |
| [04-Sources](04-Sources/README.md) | Shareable evidence and extracts | Interview findings with scope and limitations |
| [05-Templates](05-Templates/README.md) | Document starting points and the page contract | A decision with its rationale and revisit condition |

A source records the evidence; a knowledge page explains what the team can conclude from it. A project connects that knowledge to work with a specific goal. Task tracking stays in the team's existing tool. Private scratch notes stay in private repositories.

Agent skills live in `.agents/skills/`, with Claude Code symlinks in `.claude/skills/`. Operating instructions live in `docs/`; checks and repository configuration live in `scripts/` and `.github/`.

## The workflows

Use these names directly or describe the work you want done. In Codex, invoke a skill with `$`; in Claude Code, use `/`.

| Skill | When to use it | Result |
| --- | --- | --- |
| [team-doctor](.agents/skills/team-doctor/SKILL.md) | You want to check your clone or understand a setup problem | Separate verdicts for local setup and repository access, with next steps |
| [team-init](.agents/skills/team-init/SKILL.md) | You have just created a team repository | Team profile, ownership and starting context in a Draft PR |
| [team-query](.agents/skills/team-query/SKILL.md) | You need an answer grounded in team knowledge | An answer with sources, the accepted commit and explicit gaps |
| [team-update](.agents/skills/team-update/SKILL.md) | Research, an experiment or a decision changes what the team knows | Updated pages, evidence and indexes in a GitHub Draft PR |
| [capture-meeting](.agents/skills/capture-meeting/SKILL.md) | A meeting produces decisions, open questions or changes to team knowledge | Select evidenced items first; `team-update` records them in one Draft PR |
| [team-garden](.agents/skills/team-garden/SKILL.md) | You want to check what needs attention | Ranked findings with evidence and owners; selected repairs go through PRs |
| [team-connect](.agents/skills/team-connect/SKILL.md) | You also use a private Super Brain | A private connection and an installed `team-share` skill |
| [team-share](05-Templates/private-skills/team-share/SKILL.md) | A private note contains something useful to the team | A shareable version in a Draft PR, after you approve what leaves your private repo |

`team-share` runs from the private brain after connection. It continues through the team's `team-update` workflow in the same session. There is no patch package to carry between repositories. After publication, it links the private author note to the PR as a personal snapshot. On later reads, the agent resolves that PR and uses the current team page after merge; private working notes remain local.

## Try one complete loop

Start with one useful research note. Ask `team-update` to turn it into shared knowledge, keeping the evidence and uncertainty visible. Open the resulting Draft PR and inspect what changed.

Have another person review it. Once the change has been accepted and merged, ask `team-query` a question from a separate clone with no access to the original author's private notes. The answer should cite the shared material and the accepted commit.

If the PR is still open, the proposed conclusion is not yet accepted knowledge. A successful automated check does not replace a person's assessment of the evidence.

## Connect your private brain

From the team repository, run:

```text
$team-connect Connect my private Super Brain at /absolute/path/to/my-brain
```

The skill records the connection in the private brain, installs `team-share` and adds a context-reading rule. It does not upload private notes. When you later share a note, the agent prepares a self-contained contribution and shows exactly what will be published before the first push.

See [private connection](docs/private-connection.md) for installation, permissions and updating an existing connection. The private brain keeps its own folder layout.

## Keep it useful

- Before work, check existing decisions and evidence with `team-query`.
- After an event changes knowledge, use `team-update` to record what changed and why.
- After a meeting, run `$capture-meeting /path/to/notes.md` in Codex or `/capture-meeting /path/to/notes.md` in Claude Code, or paste the text. Select the proposed items before any write; only short evidence excerpts are shared.
- At project closure, save the outcome and move reusable findings into knowledge pages.
- Regularly run `team-garden` to find contradictions, stale claims, duplicates and ownership gaps. Resolve the highest-impact findings with the people responsible.

[Ownership](01-Team/owners.md) names the steward, owners and backups. [Working agreements](docs/working-agreements.md) distinguish proposals, accepted decisions and historical pages. [Maintenance](docs/maintenance.md) describes the routine.

## Checks and review

```sh
ruby scripts/check.rb
ruby scripts/check_test.rb
```

`knowledge-check` runs on pull requests. It validates page metadata, indexes, local sources, links and ownership requirements. It cannot establish that a claim is true or that a metric is useful.

The repository includes a CODEOWNERS example and a ruleset configuration. Files alone do not enforce review: a repository administrator must configure access and enable the rules. Follow [GitHub setup](docs/github-setup.md), then verify the behavior with the [manual test](docs/manual-test.md).

Updating this template does not update repositories already created from it. For the previous numbered layout, use the [migration guide](docs/migration.md).
