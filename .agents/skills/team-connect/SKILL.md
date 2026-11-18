---
name: team-connect
description: Run in a team clone to connect a private Super Brain, install or update team-share, and add context-reading rules to its agent instructions.
---
# Connect a private brain

1. Use the current clone as the team repository. Obtain the private repository's path if missing; confirm it is a separate repository root and writable. Verify `origin`, a `verified` SHA and `01-Team/context-entry.md` using [Git reads](../../../docs/git-read.md). Report the specific inaccessible repository or directory.
2. Add or update this team's entry in the private `8-System/team-context.md` using the [connection template](../../../05-Templates/team-context.md). Read identity and clone path from the team repository, and scope from its profile and the user's request. Preserve other connections. The private `8-System/` path is intentional; do not rename private folders to match the team layout.
3. Install or update [team-share](../../../05-Templates/private-skills/team-share/SKILL.md) at the private `.agents/skills/team-share/SKILL.md`, preserving local customizations; resolve incompatible customizations with the user. Add the relative `.claude/skills/team-share` symlink for Claude Code. Apply the [private instruction block](../../../docs/private-connection.md) in `AGENTS.md` and an independently maintained `CLAUDE.md`. Include the snapshot-reading rule even on an existing connection. Preserve unrelated instructions.
4. Verify the connection using [team-query](../team-query/SKILL.md) on a question grounded in an accepted team source. An initialized profile is enough when the knowledge index is empty. Report the source, SHA and private files changed. Connecting does not publish private material.
