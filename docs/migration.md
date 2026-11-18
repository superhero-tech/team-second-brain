# Migrate an existing team repository

Repositories created from a template do not receive its updates automatically. Prepare migration on a separate branch and review it as a PR. Preserve team content, ownership assignments, working language and history; do not replace them with empty template files.

| Previous team path | New team path |
| --- | --- |
| `8-System/team.md`, `owners.md`, `context-entry.md` | Same filenames under `01-Team/` |
| `4-Knowledge/` | `02-Knowledge/` |
| `3-Projects/` | `03-Projects/` |
| `5-Raw/` | `04-Sources/` |
| `6-Templates/` | `05-Templates/` |
| `7-Skills/README.md` | Workflow overview in root `README.md` |
| `8-System/brain.md`, `git-read.md`, `maintenance.md` | `docs/working-agreements.md`, `docs/git-read.md`, `docs/maintenance.md` |
| `9-Outputs/` | Move useful files into the relevant project or knowledge area; do not discard existing artifacts |

1. Use `git mv` for tracked paths. Translate operating instructions and template filenames; preserve existing source wording and team content unless translation is requested.
2. Update Markdown links, YAML source references, indexes, CODEOWNERS paths, skills and checker paths together. Keep stable page IDs. Existing ownership area keys can remain if every page and ownership record agrees; do not translate keys in only one place.
3. Add `working_language` to `01-Team/team.md`, using the team's actual language. Install `team-init` and its Claude symlink. Keep the checker, regression tests and CI workflow from the same version.
4. Run both commands from the README, then review actual content and source paths. An existing artifact moved into knowledge or projects needs page metadata and an index entry if it is Markdown.
5. After the migration PR is accepted and merged, run `team-connect` for each private brain. Refresh its team entry points and installed skill. Do not rename the private `8-System/` folder: it still holds the private connection configuration.

The new default is a real GitHub Draft PR for requested changes. Old local patch packages do not become accepted knowledge merely because the workflow changed.
