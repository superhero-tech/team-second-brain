---
name: team-share
description: Share selected private Super Brain material through a GitHub Draft PR and mark the author note as a personal snapshot with a durable handoff link.
---
# Share with the team

1. Read the selected material and choose the team from private `8-System/team-context.md`. Verify repository identity and default-branch SHA using `docs/git-read.md` in the team clone. Read affected pages, indexes and owners. If the note already has a handoff, resolve it below before acting: reuse its open PR, or report the existing accepted contribution unless a new change is requested. Before creating a PR, also check the current task for a verified existing PR whose private annotation is missing. Do not silently replace a handoff to another contribution.
2. In the same session, use `.agents/skills/team-update/SKILL.md` from that team clone. Prepare self-contained shared material with context, sources and limitations on a team branch. Exclude private scratch notes and follow the private-sharing rules linked by `team-update`.
3. Show the exact publication scope and obtain any missing approval. Continue `team-update` until a real Draft PR is created or updated, then verify its URL and the primary shared page's repository-relative path. Do not require switching sessions or handing off a patch file.
4. After publication is confirmed, update the editable private author note with the handoff below. Preserve its content, private sections and unrelated metadata; do not replace its existing `status` or invent a review date. Keep this annotation out of the published team contribution. Maintain affected private indexes/logs according to the vault's rules. Report the PR URL and the private note changed; if annotation fails, report that partial result and repair it on retry without creating another PR.

Do not store team patches or PR drafts in the private brain. Preview-only requests and failed publication create no handoff annotation. Do not alter immutable raw sources; record the handoff on an editable author note and report its location.

## Record the handoff

Merge these fields into the note's YAML frontmatter using actual values; update an existing matching annotation instead of adding duplicates:

```yaml
knowledge_role: personal_snapshot
team_pr: https://github.com/OWNER/REPO/pull/123
team_path: 02-Knowledge/path-to-primary-page.md
```

Add a visible callout in the note's language, replacing `PR_URL` with the verified URL:

```markdown
> This analysis was submitted to the team: [pull request](PR_URL). This note preserves the author's snapshot and private working notes. Before using or updating the shared analysis, check the PR and team version.
```

The marker describes the shared analysis, not unrelated personal sections. It neither deletes the original nor labels it obsolete. Do not persist a PR lifecycle status or schedule a post-merge rewrite; the link stays useful after merge.

## Read a handed-off note

Before using or editing shared claims from a `personal_snapshot`, match `team_pr` to the configured team and check its current state on GitHub:

- **Open:** the PR's current version is a proposal. Distinguish it from accepted team knowledge and the author's snapshot; continue changes through that PR.
- **Merged:** read `team_path` from the currently verified default-branch SHA, not the old PR head or merge snapshot. Follow verified successor links where present. Maintain shared claims through `team-update`; use private sections only as personal context.
- **Closed without merge:** no shared contribution was accepted through this PR. Treat the original as personal material; do not reopen or republish it without a request.
- **Unavailable, mismatched repository or missing shared page:** state what could not be verified. The private snapshot may provide historical context, but must not be presented as the current team version.

Reading the note resolves the current state; it does not require rewriting the private note after merge.
