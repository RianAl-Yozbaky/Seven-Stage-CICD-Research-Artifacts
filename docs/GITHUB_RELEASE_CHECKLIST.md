# GitHub publication checklist

1. Create a NEW repository with the name `seven-stage-cicd-security-framework-artifacts` (private during initial review).
2. Extract this ZIP; upload the **files and directories inside**, so `README.md` appears at the repository root. Do not upload the ZIP alone if you want GitHub to display the files.
3. Check `README.md`, `LICENSE_AND_REUSE.md`, `CITATION.cff` and all six figures with coauthors.
4. Run `python evaluation-scripts/verify_release.py`; compare the numbers against the accepted manuscript.
5. Search for secrets: AWS access keys, GitHub tokens, SSH/private keys, cloud account IDs, personal identifiers, and internal paths; do not publish them.
6. This release has NO original raw per-pipeline JSON records or detector implementations. Do not describe it as complete experimental replication materials.
7. Confirm the journal's current material-sharing requirements and any restrictions with the editor and university IP office before selecting Public.
8. Add a repository release tag (e.g. `v1.0`) and, if appropriate, archive with Zenodo to create a stable DOI.
9. Once public, replace `[Repository URL]` in your paper with the actual link, and preferably archive DOI. If your Data Availability Statement promises raw materials, either supply them or revise the statement to fit the release.

