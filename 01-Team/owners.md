---
steward: null
areas:
  product:
    owner: null
    backup: null
  domain:
    owner: null
    backup: null
  research:
    owner: null
    backup: null
  maintenance:
    owner: null
    backup: null
---
# Ownership

Assign a `steward` before adding knowledge or project pages. For each area in use, assign an `owner` and a different `backup`. Use real GitHub logins when mapping these responsibilities to [CODEOWNERS](../.github/CODEOWNERS). A file does not grant repository access.

| Area | Typical content |
| --- | --- |
| `product` | Projects, decisions and open questions |
| `domain` | Definitions and metrics |
| `research` | Customer knowledge and research practices |
| `maintenance` | Repository instructions and skills |

The backup reviews when the owner authored the change or is unavailable. The steward resolves missing assignments. A page can name its own `owner`; the area's backup still applies. Adapt the areas to the actual team. Reviewer is a role on a specific PR, not a permanent repository-wide assignment; a change spanning several areas needs review coverage for those areas.
