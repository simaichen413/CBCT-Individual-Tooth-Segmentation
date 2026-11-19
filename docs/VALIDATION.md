# Segmentation validation

The model export includes internal validation results for **11 cases** evaluated with Fold 0. Values below are derived from the exported `fold_0/validation/summary.json`.

| Segmentation result | Dice | IoU |
|---|---:|---:|
| Maxilla | 0.969574 | 0.941003 |
| Mandible | 0.985217 | 0.970875 |
| 32 FDI tooth labels (unweighted mean) | 0.967007 | 0.949415 |
| 35 foreground labels (unweighted mean) | 0.966673 | 0.947756 |

The per-label Dice and IoU values are available in [`metadata/validation_by_label.csv`](../metadata/validation_by_label.csv). The reported `foreground_mean` covers 35 foreground labels (including both jaws and `seg5`). The tooth-only average is calculated separately over the 32 individual FDI tooth labels.
