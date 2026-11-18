---
name: team-update
description: Update team knowledge, setup or operating rules and deliver the change as a GitHub Draft PR, including contributions from team-share.
---
# Update shared knowledge

The result is a team branch and a real GitHub Draft PR. A request to make a change includes delivering that result without a separate push or PR confirmation. An explicit request for a plan, preview or local-only work takes precedence. A local branch, commit, patch or PR description is not completion; finish with a verified GitHub Draft PR URL or report the concrete blocker.

1. Read the input and affected pages at a [verified SHA](../../../docs/git-read.md). For private input, including `team-share`, apply [private sharing](references/private-sharing.md). A direct request to save an identified plan, note or result in the team repository authorizes publishing that material; a private file or chat as its source does not by itself require another confirmation.
2. Use a separate `codex/` team branch based on that SHA; use a worktree if unrelated edits are present. Continue an existing task branch and PR when applicable. Follow the [page contract](../../../05-Templates/README.md), update affected sources and indexes, and use the team's `working_language`. Record decisions people actually made. Run `ruby scripts/check.rb`.
3. Prepare the diff, rationale and limitations. Select reviewers from the [owners of the affected areas](../../../01-Team/owners.md), covering each area changed. Use a backup when its owner is the author or unavailable; never select the author to review their own PR. If no eligible reviewer is available, record the assignment gap for the steward and leave review pending; this does not block creating the Draft PR. Ask before pushing only when the disclosure scope is unresolved or the user explicitly requested a preview first. Do not store team patches or PR drafts in the private brain.
4. Commit only this change, push the branch and create a Draft PR to the verified repository's default branch using the [PR template](../../../.github/PULL_REQUEST_TEMPLATE.md). Update an existing PR for this task instead of duplicating it. Read back and report its URL, Draft state and checks. If access or publication fails, report the blocker and preserved branch state; a local diff is not a PR. If nothing changed, report that without creating an empty PR.

A Draft PR is a proposal, not accepted knowledge. Do not mark it ready or merge without a request; follow the [review process](../../../docs/github-setup.md).
