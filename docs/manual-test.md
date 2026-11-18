# Manual acceptance test

## Fresh template and setup

1. Run `ruby scripts/check.rb` and `ruby scripts/check_test.rb`. An empty template should report 0 pages, 0 errors and 0 warnings.
2. Open a fresh session in a clone created from the template. Confirm `team-init`, `team-query`, `team-update`, `team-garden` and `team-connect` are discoverable in Codex and through Claude Code symlinks.
3. Run `team-init` with a product, audience, scope, working language and real steward/reviewer logins. Expect a setup Draft PR with no invented knowledge, no default-branch write and no automatic permission changes. Rerun without new input: no duplicate or empty PR should appear.
4. Review and merge the setup; verify [GitHub review](github-setup.md) in a disposable repository. Create one sourced page through `team-update`; expect an actual Draft PR and a successful check. Mark it ready when instructed. Missing human review should still prevent merge when protection is enabled.

## Private connection and sharing

1. Run `team-connect` from the initialized team clone. Check private `8-System/team-context.md`, installed `team-share`, agent instructions and the Claude symlink. The private folder layout must remain unchanged. Ask a team question in a fresh private session; expect a team source and accepted SHA.
2. Provide a private note containing a shareable finding and a marked private-only fragment. Run `team-share`. Before disclosure approval, nothing should be pushed. After approval, expect a Draft PR without switching sessions. Inspect all outgoing commits and the PR text: no private-only fragment or private file link may be published. No patch package should appear in the private brain.
3. Continue the same change: update its existing PR. Ask explicitly for a preview only: no push or PR. Remove GitHub access in a test environment: expect a blocker report, not a claim that a PR was created.
4. After review and merge, ask from a second clone with no private access. Expect the accepted finding, source and merged SHA. While the PR is open, its content must remain a proposal.
5. Rerun `team-connect` with an older installed skill. Confirm updated entry points and sharing workflow while preserving other connections and local customizations.

## Maintenance

Create a sourced contradiction, a duplicate and an unassigned area in test content. Run `team-garden`; expect evidence, proposed actions and responsible people, with no unsolicited edits. Have the owner resolve the contradiction and request a repair. Expect a Draft PR retaining historical context and a valid successor link.

For migration from the previous structure, follow [migration](migration.md) and run both automated checks again.
