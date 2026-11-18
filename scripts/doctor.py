"""Check local Team Second Brain setup and report what GitHub access was verified."""

import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from typing import NamedTuple

sys.dont_write_bytecode = True
from team_revision import git, revision

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ("team-init", "team-query", "team-update", "team-garden", "team-connect", "team-doctor", "capture-meeting")
GITHUB_REMOTE = re.compile(
    r"(?:https?://(?:[^/@]+@)?github\.com/|ssh://(?:[^/@]+@)?github\.com(?::\d+)?/"
    r"|(?:[^/@:]+@)?github\.com:)"
    r"([A-Za-z0-9-]+/[A-Za-z0-9_.-]+?)(?:\.git)?/?",
    re.IGNORECASE,
)
DNS_ERRORS = ("could not resolve host", "no such host", "name resolution")
NETWORK_ERRORS = (
    "network is unreachable", "failed to connect", "error connecting",
    "connection timed out", "connection refused",
)


class Finding(NamedTuple):
    status: str
    check: str
    detail: str
    action: str = ""


def command(*args):
    return subprocess.run(
        args,
        cwd=ROOT,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        check=True,
        env={**os.environ, "GH_PROMPT_DISABLED": "1"},
        timeout=30,
    )


def access_issue(error, fallback):
    # Classify stderr without printing it. It can contain a credential-bearing URL.
    if isinstance(error, subprocess.TimeoutExpired):
        return "The connection attempt timed out.", "Retry from a session with network access."
    message = (getattr(error, "stderr", None) or "").lower()
    if any(fragment in message for fragment in DNS_ERRORS):
        return (
            "This shell could not resolve the remote hostname (DNS).",
            "If live access is needed, retry from a network-enabled session.",
        )
    if any(fragment in message for fragment in NETWORK_ERRORS):
        return (
            "This shell could not reach the remote host.",
            "If live access is needed, retry from a network-enabled session.",
        )
    if "terminal prompts disabled" in message or "permission denied (publickey)" in message:
        return "Git needs credentials that this shell could not use.", "Check Git credentials for origin."
    if "gh auth login" in message or "authentication failed" in message or "http 401" in message:
        return "The remote request could not authenticate.", fallback
    if "repository not found" in message or "http 403" in message:
        return "The remote request was denied or the repository could not be accessed.", fallback
    return "The remote request failed and its cause could not be identified here.", fallback


def check_skills():
    entry_points = [Path("AGENTS.md"), Path("CLAUDE.md")]
    for directory in (".agents", ".claude"):
        entry_points.extend(Path(directory, "skills", name, "SKILL.md") for name in SKILLS)
    missing = [str(path) for path in entry_points if not (ROOT / path).is_file()]
    if missing:
        return Finding("FIX", "Agent entry points", "\n".join(missing), "Restore these files or symlinks.")
    return Finding("OK", "Agent entry points", f"Codex and Claude Code files found for all {len(SKILLS)} team skills.")


def check_knowledge():
    try:
        result = command("ruby", "scripts/check.rb")
    except subprocess.CalledProcessError as error:
        errors = [line for line in error.stderr.splitlines() if line.startswith("ERROR: ")]
        detail = "\n".join(errors) or f"The validator exited with code {error.returncode}."
        return Finding("FIX", "Knowledge validation", detail, "Run ruby scripts/check.rb and fix the reported errors.")
    except (OSError, subprocess.TimeoutExpired):
        return Finding("FIX", "Knowledge validation", "The Ruby validator could not complete.", "Run ruby scripts/check.rb directly.")
    lines = result.stdout.strip().splitlines()
    if any(line.startswith("WARNING: ") for line in lines):
        return Finding("NOTE", "Knowledge validation", "\n".join(lines), "Review the warnings in the listed pages.")
    return Finding("OK", "Knowledge validation", "\n".join(lines) or "The validator passed.")


def check_codeowners():
    path = ROOT / ".github/CODEOWNERS"
    if path.is_file() and any(
        line.strip() and not line.lstrip().startswith("#")
        for line in path.read_text(encoding="utf-8").splitlines()
    ):
        return Finding("OK", "Local CODEOWNERS", "Active entries found. Live branch protection was not tested.")
    return Finding(
        "NOTE", "Local CODEOWNERS", "No active entries. This is expected in a fresh template.",
        "For a new team run team-init. To enforce review, an administrator can follow docs/github-setup.md.",
    )


def check_origin():
    label = "Read accepted team knowledge from origin"
    errors = []
    result = revision(ROOT, on_remote_error=errors.append)
    if result["status"] == "verified":
        branch = result["ref"][len("refs/heads/"):]
        sha = result["sha"]
        for path in ("01-Team/context-entry.md", "01-Team/team.md"):
            if git(ROOT, "cat-file", "-e", f"{sha}:{path}") is None:
                return Finding("FIX", label, f"{path} is missing on {branch}.", "Check that origin points to your team repository.")
        return Finding("OK", label, f"Verified {branch} at {sha}. The team profile and context map are available.")
    if result["reason"] == "not_clone_root":
        return Finding("FIX", label, "The repository is not a Git clone.", "Run from your cloned team repository.")
    if result["reason"] == "no_origin":
        return Finding("FIX", label, "Git remote origin is missing.", "Set origin to your team repository.")
    fallback = "Run git ls-remote --symref origin HEAD in a network-enabled terminal for details."
    if errors:
        detail, action = access_issue(errors[-1], fallback)
    elif result["reason"] == "commit_unavailable":
        detail, action = "The advertised commit could not be read locally.", "Fetch the default branch and retry."
    else:
        detail, action = "The default branch and commit could not be determined from origin.", fallback
    if result["status"] == "cached":
        detail += f"\nCached commit {result['sha']} is available for offline reading."
    return Finding("UNVERIFIED", label, detail, action)


def check_github_role():
    label = "GitHub account for publishing"
    origin = git(ROOT, "remote", "get-url", "origin") or ""
    match = GITHUB_REMOTE.fullmatch(origin)
    if not match:
        return Finding("UNVERIFIED", label, "The CLI role probe applies to GitHub.com origins.")
    repository = match[1]
    if not shutil.which("gh"):
        return Finding("UNVERIFIED", label, f"GitHub CLI is unavailable for checking {repository}.", "If you use gh to publish, install it and sign in.")
    try:
        result = command(
            "gh", "repo", "view", f"github.com/{repository}",
            "--json", "viewerPermission", "--jq", ".viewerPermission",
        )
    except (OSError, subprocess.SubprocessError) as error:
        detail, action = access_issue(error, "If you publish via gh, check gh auth status and the repository role.")
        return Finding("UNVERIFIED", label, detail, action)
    role = result.stdout.strip()
    if role in ("ADMIN", "MAINTAIN", "WRITE"):
        return Finding("OK", label, f"The gh account has {role} on {repository}. Push and PR creation were not tested.")
    if role in ("TRIAGE", "READ"):
        return Finding("NOTE", label, f"The gh account has {role} on {repository}.", "Ask for write access if this account needs to publish changes.")
    return Finding("UNVERIFIED", label, f"GitHub did not return a role for {repository}.")


def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    local = [check_skills(), check_codeowners()]
    if shutil.which("ruby"):
        local.append(check_knowledge())
    else:
        local.append(Finding("FIX", "Knowledge validation", "Ruby is missing.", "Install Ruby and rerun."))
    if shutil.which("git"):
        access = [check_origin(), check_github_role()]
    else:
        local.append(Finding("FIX", "Git tooling", "Git is missing.", "Install Git and rerun."))
        access = [Finding("UNVERIFIED", "Repository access", "Git is required for the local access checks.")]

    needs_local_fix = any(finding.status == "FIX" for finding in local)
    has_local_notes = any(finding.status == "NOTE" for finding in local)
    local_status = "OK WITH NOTES" if has_local_notes else "OK"
    if needs_local_fix:
        local_status = "NEEDS CHANGES"
    if any(finding.status == "FIX" for finding in access):
        access_status = "SETUP NEEDED"
    elif any(finding.status == "UNVERIFIED" for finding in access):
        access_status = "NOT FULLY VERIFIED IN THIS SESSION"
    elif any(finding.status == "NOTE" for finding in access):
        access_status = "LIMITED"
    else:
        access_status = "CHECKS PASSED"
    print(f"Local configuration: {local_status}")
    print(f"Repository access: {access_status}")
    for heading, findings in (("Local checks", local), ("Access checks", access)):
        print(f"\n{heading}")
        for finding in findings:
            print(f"[{finding.status}] {finding.check}")
            for line in finding.detail.splitlines():
                print(f"  {line}")
            if finding.action:
                print(f"  Next step: {finding.action}")
    return int(needs_local_fix or access_status == "SETUP NEEDED")


if __name__ == "__main__":
    raise SystemExit(main())
