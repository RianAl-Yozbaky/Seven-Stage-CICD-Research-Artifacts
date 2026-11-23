# Publication disclosure checklist

## Public candidates (after verification and sanitization)
- Published aggregate confusion matrices and calculations.
- Original per-pipeline IDs, ground truth, decisions for each orchestration, stage decisions and skip flags (once extracted).
- Exact scenario assignment manifests, after removing private bucket paths/identifiers.
- Dataset inventory with original origin URL, license, hash, selection and deduplication method, and source splits.
- Original evaluation scripts, tables, figure files, and version metadata.

## Conditional — consult IST editorial requirements, coauthors, and IP office
- Detector source, regex/heuristics, thresholds, metadata/path features, and exact code versions.
- State machine JSON/ASL, Boto3 orchestration code, GitHub workflow YAML.
- Third-party vulnerable or malicious samples: redistribution license and safeguards required.

## Never publish
- AWS access/secret keys, GitHub tokens, IAM credentials, signed URLs, private keys, proprietary endpoints, personal records.

## Scientific caution
The Build detector in the paper used dataset-context information. Retain this disclosure. A summary-only archive cannot establish independent evaluation on unseen artifacts. Protecting implementation details must not lead to misleading reproducibility claims.
