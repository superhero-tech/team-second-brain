# Read a verified Git revision

1. Confirm the clone root with `git -C <clone> rev-parse --show-toplevel`. Read `origin` and compare its host, owner and repository with the connection configuration. HTTPS and SSH may identify the same repository. For a local bare origin, compare resolved absolute paths. Do not display credentials in remote URLs. Stop on an identity mismatch.
2. Run `python3 scripts/team_revision.py <clone>` from a trusted copy. `verified` means the observed default-branch commit exists locally; `cached` means only a cached remote HEAD is available; `unavailable` means no usable revision. Require `verified` for new connections and PR bases. Report stale or unavailable reads honestly.
3. Read files from one SHA with `git -C <clone> show <SHA>:01-Team/context-entry.md`. Search that tree with `git -C <clone> grep -in -e '<term>' <SHA> -- 02-Knowledge 03-Projects`. Cite `https://github.com/OWNER/REPO/blob/<SHA>/<path>` or the path and SHA if no web URL exists.

Fetching a commit does not require switching the user's branch or overwriting their working tree.
