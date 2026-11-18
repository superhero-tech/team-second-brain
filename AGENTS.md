# Team Second Brain

- Read [working agreements](docs/working-agreements.md), the [context map](01-Team/context-entry.md) and [team profile](01-Team/team.md). Use `working_language` for new team content; follow the user's language in conversation.
- For a new team's setup, use [team-init](.agents/skills/team-init/SKILL.md). Do not invent product facts or people.
- Ground accepted knowledge in a verified commit of the team's default branch. Use [team-query](.agents/skills/team-query/SKILL.md), including when access is unavailable or evidence conflicts.
- Changes to knowledge, rules and skills go through a branch and a GitHub Draft PR via [team-update](.agents/skills/team-update/SKILL.md). Human review and merge establish the accepted version.
- For meeting notes or transcripts, use [capture-meeting](.agents/skills/capture-meeting/SKILL.md). Show extracted items and wait for selection before any writes; hand selected items to `team-update`.
- Use [team-garden](.agents/skills/team-garden/SKILL.md) for maintenance findings and selected repairs.
- Before editing, read the relevant index; update affected links and indexes. Run `ruby scripts/check.rb`. When changing the checker, also run `ruby scripts/check_test.rb`.
