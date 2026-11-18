# Working agreements

Keep knowledge that helps another person make a decision or do work. The [team profile](../01-Team/team.md) defines the scope and working language. Personal profiles and scratch notes belong in private repositories.

## Accepted knowledge

The accepted version is the default branch after merge. Verify the repository identity and commit using [Git reads](git-read.md), then read selected files from that commit. Local edits, open PRs and private material are proposals or context, not accepted knowledge.

Cite the pages and revision used. Distinguish observations, hypotheses, decisions and gaps. For conflicting claims, show both sources and identify the owner who must resolve them. Link to an external authoritative source when the repository is not its owner.

## Changes and review

Use [team-update](../.agents/skills/team-update/SKILL.md) to deliver requested changes on a team branch in a GitHub Draft PR, unless the user explicitly asks for a plan, preview or local-only work. Include affected indexes, sources and links. A direct request to save identified private material in the team repository authorizes publishing that material. Follow [private sharing](../.agents/skills/team-update/references/private-sharing.md) for unresolved disclosure scope or a requested preview; do not ask again solely because the source is private.

The author is responsible for disclosure; the area's owner is responsible for content. The [backup or steward](../01-Team/owners.md) resolves reviewer assignment. A person other than the author reviews the evidence. Passing checks is necessary, but does not establish truth or replace review.

Creating a Draft PR is separate from marking it ready or merging it. Follow the user's authorization and the [repository rules](github-setup.md). Do not claim a Draft PR requested review automatically; check its actual review state. Missing reviewers leave the PR pending.

Update `reviewed_at` only after actual content review. After merge, the private author may link to the accepted shared page. Do not copy private preferences into shared team policy.
