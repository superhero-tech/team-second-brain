---
name: team-garden
description: Review team knowledge for contradictions, duplicates, stale claims, missing owners or evidence gaps, and route selected repairs through PRs.
---
# Maintain shared knowledge

## Review

- Establish scope and [revision](../../../docs/git-read.md). Run `ruby scripts/check.rb` on a copy of that revision. Check sources, contradictions, duplicates, ownership, review needs, completed-project summaries and the [maintenance queue](../../../docs/maintenance.md). State any unavailable Issue or PR coverage.
- Rank findings by impact. For each, provide evidence, a proposed action and an [owner](../../../01-Team/owners.md); send missing assignments to the steward. Keep the report in conversation unless asked to save it.

## Selected repair

- Send conflicting claims and their evidence to the owner for resolution. For duplicates, propose a successor while preserving unique content. Deliver the agreed repair through [team-update](../team-update/SKILL.md).
- When authorized to file an Issue, check for an existing one and use the [maintenance template](../../../.github/ISSUE_TEMPLATE/knowledge-maintenance.md).
