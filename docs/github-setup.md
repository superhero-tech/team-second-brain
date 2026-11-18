# Configure GitHub review

Use a GitHub plan that supports repository rules for your repository's visibility. Two people need their own accounts and write access. Choose visibility with the team. See [ruleset availability](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets).

1. Run `team-init` to propose the [profile](../01-Team/team.md), [ownership](../01-Team/owners.md) and [CODEOWNERS](../.github/CODEOWNERS). Use real logins with write access. The last matching CODEOWNERS pattern wins. Cover the rules, skills and CODEOWNERS file itself. [Code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
2. Review the setup Draft PR and explicitly mark it ready before requesting review. In a new repository, manually arrange review for this first PR: proposed CODEOWNERS entries are not yet on the base branch. Merge the reviewed setup, then verify owner assignment on a subsequent ready-for-review PR. Wait for `knowledge-check` to run.
3. An administrator enables a ruleset on the default branch. Import [the supplied ruleset](../.github/knowledge-ruleset.json) in repository settings, or run the following from the clone after substituting `OWNER/REPO`. Update an equivalent existing rule instead of adding duplicates.

   ```sh
   gh api -X POST repos/OWNER/REPO/rulesets --input .github/knowledge-ruleset.json
   ```

   Require a PR, at least one approval, code-owner review, renewed approval after changes, approval from someone other than the last pusher, resolved conversations and `knowledge-check`. Bind the expected check to GitHub Actions in the rules UI and keep the bypass list empty. [Available rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
4. Follow the [manual test](manual-test.md). In a disposable repository, verify that missing approval, changed content after approval and failing checks block merge, and that direct pushes to the default branch are rejected. Record the test PR and observed result.

Template files do not grant access or enable protection. The active GitHub configuration and observed behavior establish enforcement. `knowledge-check` validates structure; people assess the content.
