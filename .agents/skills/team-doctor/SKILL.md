---
name: team-doctor
description: Check a Team Second Brain clone after cloning or setup, or diagnose problems with its tools, skills, knowledge validation or GitHub access.
---
# Diagnose Team Second Brain setup

Run `python3 scripts/doctor.py` from the team clone. If it cannot start, identify the missing prerequisite.

Open with a verdict on local setup and a separate verdict on access to shared knowledge and publishing. Explain findings in the user's language. For each confirmed problem give the evidence, exact next step and who can act. Label conditional setup notes and checks that could not run.

If terminal access is unverified and a GitHub connector is available, verify the remote branch and commit read-only through that connector. Compare with the cached SHA when available. Keep the connector result separate from local Git connectivity and `gh` permissions.

Finish with either the required changes or that the checks found no changes to make. Apply fixes only when asked.
