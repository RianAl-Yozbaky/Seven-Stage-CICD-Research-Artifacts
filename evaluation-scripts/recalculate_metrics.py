#!/usr/bin/env python3
"""Recalculate reported confusion-matrix metrics from the summary CSVs.
This is NOT an original experimental runner.
"""
import csv
from pathlib import Path
base = Path(__file__).resolve().parents[1]
def pct(x): return f'{100*x:.2f}%'
def run(path):
    with (base/path).open(newline='',encoding='utf-8') as f:
        for row in csv.DictReader(f):
            tp,tn,fp,fn=[int(row[k]) for k in ('tp','tn','fp','fn')]
            total=tp+tn+fp+fn
            precision=tp/(tp+fp) if tp+fp else 0
            recall=tp/(tp+fn) if tp+fn else 0
            f1=(2*precision*recall/(precision+recall)) if precision+recall else 0
            label=row.get('stage') or row.get('orchestration') or 'Overall'
            print(label, 'n=',total,'accuracy=',pct((tp+tn)/total),'precision=',pct(precision),'recall=',pct(recall),'f1=',pct(f1))
if __name__=='__main__':
    run('results/artifact_level/stage_confusion_matrices.csv')
    run('results/artifact_level/overall_confusion_matrix.csv')
    run('results/pipeline_level/cross_orchestration_summary.csv')
