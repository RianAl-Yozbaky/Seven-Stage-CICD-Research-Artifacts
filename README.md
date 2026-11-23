# Seven-Stage Serverless Security Framework for CI/CD Pipelines — Research Artifacts

**Research article:** *A Seven-Stage Serverless Security Framework for CI/CD Pipelines: Multi-Level Evaluation and Cross-Orchestration Decision Reproducibility*  
**Intended journal:** Information and Software Technology (Elsevier)  
**Release:** v1.0 — summary-level research artifacts

## Scope and limitations
This release provides **published/manuscript-reported aggregate experimental tables**, the six supplied manuscript figures, and a **new independent metrics-recalculation utility**. The aggregate CSV rows were transcribed from the author's uploaded manuscript, not exported from original AWS execution logs. Consequently, this is an **aggregate-results verification package, not a complete reproduction archive**.

**Not included:** Original 32,120 artifact files; complete source-to-artifact inventory; 1,000 original pipeline manifest JSON files; 1,000 per-pipeline decision records from each orchestration mechanism; detector Lambda source or pinned versions; actual Python/Boto3, Step Functions, or GitHub Actions workflow implementation. No placeholder has been represented as genuine original evidence.

## Repository contents
- `results/artifact_level/`: seven detector confusion matrices and overall counts from the manuscript.
- `results/pipeline_level/`: cross-orchestration aggregate results, attack multiplicity, execution counts.
- `results/ablation/`: retrospective ablation tables reported in the paper.
- `figures/`: original manuscript PNG figures 1–6 (supplied in the author Overleaf ZIP).
- `datasets-metadata/`: stage sizes, labels, categories and artifact type descriptions; NOT raw datasets.
- `evaluation-scripts/`: independent, transparent script for metric recalculation and consistency checks; NOT the original experiment runner.
- `orchestration-comparison/`, `pipeline-manifests/`: documentation for the original records not yet deposited.
- `docs/`: provenance, data-availability wording, disclosure and publication checklists.
- `CITATION.cff`: software/archive citation metadata; adjust repository URL after publication.
- `SHA256_MANIFEST.csv`: hashes of all packaged files (other than itself).


## Reported headline findings
- 32,120 stage artifacts; 16,060 clean and 16,060 attacked; 46 attack categories.
- Artifact-level confusion matrix: TP 15,618; TN 15,479; FP 581; FN 442; accuracy 96.82%.
- 1,000 pipeline scenarios (500 clean; 500 attacked), each orchestration: TP 473, TN 496, FP 4, FN 27; accuracy 96.90%; recall 94.60%.
- The manuscript reports identical decisions across all three orchestration mechanisms for all 1,000 pipelines. 



