"""Check a Team Second Brain clone before running the team workflows."""

import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True
from team_revision import git, revision

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ("team-init", "team-query", "team-update", "team-garden", "team-connect")
GITHUB_REMOTE = re.compile(
    r"(?:https?://(?:[^/@]+@)?github\.com/|ssh://(?:[^/@]+@)?github\.com(?::\d+)?/"
    r"|(?:[^/@:]+@)?github\.com:)"
    r"([A-Za-z0-9-]+/[A-Za-z0-9_.-]+?)(?:\.git)?/?",
    re.IGNORECASE,
)


def command(*args):
    try:
        return subprocess.run(
            args,
            cwd=ROOT,
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
            env={**os.environ, "GH_PROMPT_DISABLED": "1"},
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None


def check_origin():
    result = revision(ROOT)
    status = result["status"]
    if status == "verified":
        branch = result["ref"][len("refs/heads/"):]
        sha = result["sha"]
        for path in ("01-Team/context-entry.md", "01-Team/team.md"):
            if git(ROOT, "cat-file", "-e", f"{sha}:{path}") is None:
                print(f"FAIL Accepted revision: {path} is missing on {branch}. Check the origin team repository.")
                return False
        print(f"OK   Accepted revision: {branch} at {sha}")
        return True
    if status == "cached":
        print(f"FAIL Accepted revision: cached {result['sha']}. Restore access to origin and rerun.")
    else:
        fixes = {
            "not_clone_root": "Run from a clone of your team repository.",
            "no_origin": "Set origin to your team repository and rerun.",
            "commit_unavailable": "Fetch the default branch from origin and rerun.",
            "origin_head_not_verified": "Check network, Git credentials, and the default branch on origin.",
        }
        print(f"FAIL Accepted revision: {fixes[result['reason']]}")
    return False


def check_github_role():
    origin = git(ROOT, "remote", "get-url", "origin") or ""
    match = GITHUB_REMOTE.fullmatch(origin)
    if not match:
        print("WARN GitHub role: unknown. Check repository access with your team administrator.")
        return
    repository = match[1]
    if not shutil.which("gh"):
        print(f"WARN GitHub role for {repository}: unknown. Use an authenticated gh or check GitHub access.")
        return
    result = command(
        "gh", "repo", "view", f"github.com/{repository}",
        "--json", "viewerPermission", "--jq", ".viewerPermission",
    )
    role = result.stdout.strip() if result and result.returncode == 0 else ""
    if role in ("ADMIN", "MAINTAIN", "WRITE"):
        print(f"OK   GitHub repository role for {repository}: {role} (gh account)")
    elif role in ("TRIAGE", "READ"):
        print(f"WARN GitHub role for {repository}: {role}. Ask for write access to publish team branches.")
    else:
        print(f"WARN GitHub role for {repository}: unknown. Check gh auth status and repository access.")


def check_skills():
    entry_points = [Path("AGENTS.md"), Path("CLAUDE.md")]
    for directory in (".agents", ".claude"):
        entry_points.extend(Path(directory, "skills", name, "SKILL.md") for name in SKILLS)
    missing = [str(path) for path in entry_points if not (ROOT / path).is_file()]
    for path in missing:
        print(f"FAIL Agent entry point missing: {path}. Restore it from the team repository.")
    if not missing:
        print("OK   Codex and Claude Code skill files")
    return not missing


def check_knowledge():
    result = command("ruby", "scripts/check.rb")
    if result and result.returncode == 0:
        print("OK   Local knowledge check passed")
        return True
    print("FAIL Local knowledge check. Run ruby scripts/check.rb for details.")
    return False


def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    checks = [check_skills()]
    if shutil.which("git"):
        checks.append(check_origin())
        check_github_role()
    else:
        checks.append(False)
        print("FAIL Git is missing. Install Git and rerun.")
    if shutil.which("ruby"):
        checks.append(check_knowledge())
    else:
        checks.append(False)
        print("FAIL Ruby is missing. Install Ruby and rerun.")

    codeowners = ROOT / ".github/CODEOWNERS"
    if not codeowners.is_file() or not any(
        line.strip() and not line.lstrip().startswith("#")
        for line in codeowners.read_text(encoding="utf-8").splitlines()
    ):
        print("WARN No active local CODEOWNERS entries. Run team-init if this is a new brain.")
    print("INFO For live review enforcement, have an administrator follow docs/github-setup.md.")
    return int(not all(checks))


if __name__ == "__main__":
    raise SystemExit(main())
