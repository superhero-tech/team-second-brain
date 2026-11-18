# Document templates

- [Knowledge or definition](knowledge.md)
- [Decision](decision.md)
- [Experiment and outcome](experiment.md)
- [Project brief or summary](project.md)
- [Practice](practice.md)
- [Shareable source extract](source-extract.md)
- [Private team connection](team-context.md)

## Page contract

Markdown pages in `02-Knowledge/` and `03-Projects/`, except their root `index.md`, require YAML frontmatter. List every page exactly once in its root index, including historical pages. Store non-page attachments in `04-Sources/` or a project's assets directory.

| Field | Meaning |
| --- | --- |
| `id` | Stable, unique lowercase ASCII letters, digits and hyphens. |
| `type` | `knowledge`, `definition`, `decision`, `practice`, `questions`, `project`, `experiment` or `summary`. |
| `area` | A key from [ownership](../01-Team/owners.md). Active pages need an owner and a different backup for their area. |
| `owner` | Optional person responsible for this specific page. |
| `status` | `active`, `needs_review`, `superseded` or `archived`. |
| `reviewed_at` | Date of actual content review as a quoted `YYYY-MM-DD`, or `null` while awaiting the first review. |
| `sources` | Non-empty list of `access` and `ref` entries. `team` is a relative path to a shared file; `external` is an HTTPS URL; `restricted` is a relative path to a shareable extract or account whose original has restricted access. |
| `superseded_by` | Required for `superseded`: the successor's ID. Also link to that page in the body. |
| `next_review_at` / `review_when` | Optional review date or condition appropriate for the content. |

Source paths are relative to the page containing them. Replace template IDs, areas and source paths before adding a page. New pages start as `needs_review`; do not invent a review date. A merge does not automatically change the page's content status.

Distinguish observations, hypotheses and actual decisions in the body. Source material in [04-Sources](../04-Sources/README.md) records provenance and limitations.
