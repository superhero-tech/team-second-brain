---
name: team-update
description: Update team knowledge, setup or operating rules and deliver the change as a GitHub Draft PR, including contributions from team-share.
---
# Update shared knowledge

The result is a team branch and a real GitHub Draft PR. A request to make a change includes delivering that result without a separate push or PR confirmation. An explicit request for a plan, preview or local-only work takes precedence.

1. Read the input and affected pages at a [verified SHA](../../../docs/git-read.md). For private input, including `team-share`, apply [private sharing](references/private-sharing.md), honoring approval already given for that exact scope.
2. Use a separate `codex/` team branch based on that SHA; use a worktree if unrelated edits are present. Continue an existing task branch and PR when applicable. Follow the [page contract](../../../05-Templates/README.md), update affected sources and indexes, and use the team's `working_language`. Record decisions people actually made. Run `ruby scripts/check.rb`.
3. Prepare the diff, rationale and limitations. Select reviewers from the [owners of the affected areas](../../../01-Team/owners.md), covering each area changed. Use a backup when its owner is the author or unavailable; never select the author to review their own PR. Ask the steward to resolve missing assignments and leave review pending if no eligible reviewer is available. Obtain any missing disclosure approval for private input before pushing. Do not store team patches or PR drafts in the private brain.
4. Commit only this change, push the branch and create a Draft PR to the verified repository's default branch using the [PR template](../../../.github/PULL_REQUEST_TEMPLATE.md). Update an existing PR for this task instead of duplicating it. Read back and report its URL, Draft state and checks. If access or publication fails, report the blocker and preserved branch state; a local diff is not a PR. If nothing changed, report that without creating an empty PR.

A Draft PR is a proposal, not accepted knowledge. Do not mark it ready or merge without a request; follow the [review process](../../../docs/github-setup.md).
