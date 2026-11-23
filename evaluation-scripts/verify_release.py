#!/usr/bin/env python3
"""Validate arithmetic consistency of MANUSCRIPT-REPORTED aggregates.
This does NOT verify the underlying AWS executions or per-pipeline agreement.
"""
import csv
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def load(rel):
    with (ROOT / rel).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))
def assert_equal(actual, expected, what):
    if actual != expected:
        raise AssertionError(f"{what}: expected {expected}, got {actual}")
    print(f"OK: {what} = {actual}")

def main():
    stage=load('results/artifact_level/stage_confusion_matrices.csv')
    overall=load('results/artifact_level/overall_confusion_matrix.csv')[0]
    for key in ('tp','tn','fp','fn'):
        assert_equal(sum(int(r[key]) for r in stage),int(overall[key]),f'Artifact {key.upper()} sum')
    assert_equal(sum(int(r['total']) for r in stage),32120,'Total evaluated artifacts')
    assert_equal(sum(int(r['attack_categories']) for r in stage),46,'Attack categories')
    assert_equal(sum(int(overall[x]) for x in ('tp','tn','fp','fn')),32120,'Artifact confusion matrix total')
    inventory=load('datasets-metadata/stage_dataset_inventory.csv')
    assert_equal(sum(int(r['clean']) for r in inventory),16060,'Inventory clean artifacts')
    assert_equal(sum(int(r['attacked']) for r in inventory),16060,'Inventory attacked artifacts')
    assert_equal(sum(int(r['total']) for r in inventory),32120,'Inventory total artifacts')
    pipeline=load('results/pipeline_level/cross_orchestration_summary.csv')
    assert_equal(len(pipeline),3,'Number of orchestration summaries')
    for r in pipeline:
        label=r['orchestration']
        assert_equal(sum(int(r[k]) for k in ('tp','tn','fp','fn')),1000,label+' total pipelines')
        assert_equal(int(r['tp'])+int(r['fn']),500,label+' attacked pipelines')
        assert_equal(int(r['tn'])+int(r['fp']),500,label+' clean pipelines')
    attacked=load('results/pipeline_level/attack_multiplicity_summary.csv')
    assert_equal(sum(int(r['total']) for r in attacked),500,'Attack scenario groups total')
    assert_equal(sum(int(r['tp']) for r in attacked),473,'Attack scenario groups TP')
    assert_equal(sum(int(r['fn']) for r in attacked),27,'Attack scenario groups FN')
    executions=load('results/pipeline_level/orchestration_execution_summary.csv')
    for r in executions:
        assert_equal(int(r['executed_stage_evaluations'])+int(r['skipped_stage_evaluations']),7000,r['orchestration']+' stage slots')
    print('PASS: all checked aggregate summaries are internally consistent.')
    print('CAUTION: No original execution files were checked.')
if __name__=='__main__': main()
