# Connect a private Super Brain

Open the team clone in Codex or Claude Code after its initial configuration is merged. The session needs read access to the team repository and write access to the private clone.

```text
$team-connect Connect my private repo at /absolute/path/to/private-brain
```

Use `/team-connect` in Claude Code. The skill adds a connection, installs `team-share` and updates the private agent instructions. It leaves the private repository's layout intact.

## Private instruction block

Add this to the private `AGENTS.md`, preserving existing content. An independently maintained `CLAUDE.md` needs the same rule, or can import `AGENTS.md` with `@AGENTS.md`.

```markdown
## Team knowledge

- When a question concerns a connected team, read `8-System/team-context.md` and use `team-query` from the configured team clone.
- When asked to share private material with a team, use `.agents/skills/team-share/SKILL.md` in this private repository.
- Before using or editing shared claims in a note with `knowledge_role: personal_snapshot`, follow "Read a handed-off note" in `.agents/skills/team-share/SKILL.md`: resolve its PR state and current team page, keeping private sections as personal context.
```

## Manual installation

If installing without `team-connect`:

1. Add a team entry to private `8-System/team-context.md` using the [connection template](../05-Templates/team-context.md). Preserve existing connections. Set the team entry points to `01-Team/context-entry.md` and `01-Team/team.md`.
2. Copy [team-share](../05-Templates/private-skills/team-share/SKILL.md) into the private `.agents/skills/team-share/SKILL.md`. If already installed, merge updates with local customizations.
3. Create `.claude/skills/team-share` as a symlink to `../../.agents/skills/team-share` for Claude Code, preserving a valid existing link.
4. Add the instruction block above. Start a fresh private session and ask a question requiring a team source. Check its cited source and SHA.

## Sharing and updates

In the private session, run `team-share` on a selected note. Expect a disclosure preview followed, after approval, by a GitHub Draft PR. Sharing also needs write access to the team clone and permission to push branches and create PRs. No team patch package is stored in the private brain. After publication, `team-share` marks the editable author note as `personal_snapshot` with `team_pr` and `team_path`, plus a visible handoff link. It preserves the note and private sections. Agents resolve the PR state when reading the note; no post-merge synchronization or cached lifecycle status is needed.

After updating the team template in an existing repository, rerun `team-connect` to update the installed private skill and entry points. Updating the template on GitHub does not automatically update independent repositories.
