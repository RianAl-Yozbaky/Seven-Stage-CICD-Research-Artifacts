# Provenance status
- Tables in `results/` and `datasets-metadata/` were transcribed from the user's 19-page PDF `A_Seven_Stage_Serverless_Security_Framework_for_CICD_Pipelines (29).pdf` (Tables 2, 6–10 and accompanying text).
- Figures 1–6 were copied without alteration from `media/Fig 1.png` ... `media/Fig 6.png` in user-provided `A_Seven_Stage_Serverless_Security_Framework_for_CICD_Pipelines (3).zip`.
- The evaluation script is new transparent reproducibility helper code, **not** the script used in the original experiment.
- Missing: raw independent evidence and detector source; source-to-artifact lineage is incomplete in the underlying paper.
- All summary metrics must be compared to the final paper and run logs before public deposit.

## Reproduction scopes
A) Summary-level arithmetic: supported by this package.
B) Per-pipeline agreement and confusion-matrix verification: NOT supported until 1,000 raw results per orchestrator are added.
C) Replay of 1,000 pipelines: NOT supported until original manifests and frozen detector implementations plus environment instructions are provided.
D) Independent generalization: NOT established; no independent holdout evaluation is recorded.

## Current release boundary
This is v1.0, an aggregate-verification release. In particular, the manuscript-reported 100% cross-orchestration agreement cannot be independently proved from the aggregate tables alone. Original per-scenario decision exports would be required to validate that claim.
