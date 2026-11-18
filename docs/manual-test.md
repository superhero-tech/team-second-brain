# Manual acceptance test

## Fresh template and setup

1. Run `ruby scripts/check.rb` and `ruby scripts/check_test.rb`. An empty template should report 0 pages, 0 errors and 0 warnings.
2. Open a fresh session in a clone created from the template. Confirm `team-init`, `team-query`, `team-update`, `team-garden` and `team-connect` are discoverable in Codex and through Claude Code symlinks.
3. Run `team-init` with a product, audience, scope, working language and real logins for the steward and each area's owner and backup. Expect a setup Draft PR with no invented knowledge, no default-branch write and no automatic permission changes. For the first setup, expect a proposed reviewer assignment based on the new ownership map and confirmation from the user, not a permanent reviewer setting. Rerun without new input: no duplicate or empty PR should appear.
4. Review and merge the setup; verify [GitHub review](github-setup.md) in a disposable repository. Create one sourced page through `team-update`; expect an actual Draft PR and a successful check. Mark it ready when instructed. Missing human review should still prevent merge when protection is enabled.

## Reviewer selection

Use at least two areas with different owners and backups. A change in one area should select that area's owner; when the owner is the author or unavailable, select the backup. A cross-area PR should cover both areas. If no eligible reviewer exists, expect a request to the steward and pending review, not self-review or a fabricated assignment.

## Direct team-update from a private result

Ask `team-update` to save a specific plan from a private file or referenced chat in the team project. Expect a real GitHub Draft PR without another publication confirmation. Only the plan and shareable evidence may be published, not the full conversation, private-only sections or local links. Missing reviewers leave review pending without blocking PR creation. Repeat with an explicit preview-only request: expect no push. If the requested material includes private-only content or the scope is ambiguous, expect a focused disclosure question before publication.

## Private connection and sharing

1. Run `team-connect` from the initialized team clone. Check private `8-System/team-context.md`, installed `team-share`, agent instructions and the Claude symlink. The private folder layout must remain unchanged. Ask a team question in a fresh private session; expect a team source and accepted SHA.
2. Provide a private note containing a shareable finding and a marked private-only fragment. Run `team-share`. Before disclosure approval, nothing should be pushed. After approval, expect a Draft PR without switching sessions. Inspect all outgoing commits and the PR text: no private-only fragment or private file link may be published. No patch package should appear in the private brain.
3. Continue the same change: update its existing PR. Ask explicitly for a preview only: no push or PR. Remove GitHub access in a test environment: expect a blocker report, not a claim that a PR was created.
4. After review and merge, ask from a second clone with no private access. Expect the accepted finding, source and merged SHA. While the PR is open, its content must remain a proposal.
5. Rerun `team-connect` with an older installed skill. Confirm updated entry points and sharing workflow while preserving other connections and local customizations.

## Private handoff

After sharing an editable private note, expect exactly one `personal_snapshot` annotation with the actual PR URL, primary team-page path and a readable link. The original content, private sections and unrelated metadata remain intact; the annotation is absent from the published contribution. A preview or failed publication must not create this annotation. Retrying after a private-write failure must reuse the existing PR.

Read the note while the PR is open, merged, closed without merge and inaccessible. Expect proposal, current verified default-branch page, personal-only material and an explicit verification gap respectively. After a later team-page update, expect the current page rather than the original PR version. No post-merge rewrite is needed. If the target page disappears, expect an unresolved handoff rather than invented current knowledge.

## Meeting capture

Run `capture-meeting` once with pasted notes and once with the same content in a `.md` or `.txt` file. Include an explicit named decision, an undecided suggestion, an assigned question, a claim that changes an existing page and a private-only aside. Omit the date. Expect a numbered preview with short exact evidence, existing/proposed targets and an unknown date; no files, branches or commits before selection. The suggestion must stay proposed or become a question, and the private aside must be absent.

Accept only selected item numbers. Expect one real Draft PR through `team-update`, containing only those changes and short excerpts, with title/date (unknown where absent) and `needs_review` page status. The original transcript stays unchanged and unpublished. Repeat the capture: reuse its PR or report no changes. Check both Codex and the Claude Code symlink; no meeting-service integration is required for text/file input.

## Maintenance

Create a sourced contradiction, a duplicate and an unassigned area in test content. Run `team-garden`; expect evidence, proposed actions and responsible people, with no unsolicited edits. Have the owner resolve the contradiction and request a repair. Expect a Draft PR retaining historical context and a valid successor link.

For migration from the previous structure, follow [migration](migration.md) and run both automated checks again.
