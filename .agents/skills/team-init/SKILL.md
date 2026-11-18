---
name: team-init
description: Configure a newly created Team Second Brain with team context, working language, ownership and a GitHub Draft PR.
---
# Initialize the team brain

1. Read the current [profile](../../../01-Team/team.md), [ownership](../../../01-Team/owners.md) and [context map](../../../01-Team/context-entry.md). Use existing answers; ask only for missing product and audience context, scope, working language, the steward, and an owner and a different backup for each area in use, with their GitHub logins. Adapt the areas to the team; do not ask for a permanent repository-wide reviewer. Do not invent goals, sources or people.
2. Use [team-update](../team-update/SKILL.md) to prepare the setup on a separate team branch. Fill the profile, adapt ownership areas and link the available entry points. Activate [CODEOWNERS](../../../.github/CODEOWNERS) entries only for supplied, verified logins with write access; otherwise record the access check as pending. Leave content indexes empty until actual knowledge is supplied.
3. Select reviewers for this setup PR from the owners of the areas it changes. Use the backup when the owner authored the PR or is unavailable; cover all affected areas for a cross-area change. For an initial setup without accepted ownership, propose reviewers from the new ownership map and confirm the assignment with the user. If no eligible person is available, ask the steward to assign one and leave review pending. This assignment belongs to the PR, not a global reviewer setting.
4. Run `ruby scripts/check.rb` and open or update the setup Draft PR through `team-update`. Report its URL and any missing ownership or access configuration. Do not claim setup is accepted before merge or review is enforced before verification.

Creating files does not configure GitHub permissions or protection. Point to [GitHub setup](../../../docs/github-setup.md); change access or rules only when separately requested. On rerun, update the existing setup without resetting content, owners or local customizations. Do not create an empty PR when nothing changed.
