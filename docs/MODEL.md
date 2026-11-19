# Model description

## Overview

The model segments individual permanent teeth, maxilla, and mandible from CBCT volumes using nnU-Net v2 3D full-resolution inference. The predicted multiclass masks can be visualized or used as an upstream input for quantitative dental image analyses.

## Technical details

| Property | Value |
|---|---|
| Dataset ID | 413 |
| Dataset name | `Dataset413_byscm` |
| Planning identifier | `nnUNetPlans` |
| Network | 3D PlainConvUNet |
| Trainer | `nnUNetTrainerNoMirroring` |
| Fold | 0 |
| Development cases | 55 annotated CBCT scans |
| Training / internal validation | 44 / 11 |
| Target spacing | 0.25 mm isotropic |
| Channel | CT |
| Input file format | NIfTI `.nii.gz` |
| Output | Multiclass segmentation mask |

## Model access

The pretrained nnU-Net v2 model is available upon reasonable request for academic and research purposes. Contact **[simaichen413@gmail.com](mailto:simaichen413@gmail.com)** with a brief description of the research purpose.

The model package is supplied as `nnUNet_413.zip` with the standard nnU-Net directory structure, including `dataset.json`, `plans.json`, and `fold_0/checkpoint_final.pth`. Install the archive directly:

```bash
nnUNetv2_install_pretrained_model_from_zip /path/to/nnUNet_413.zip
```

## Labels and evaluation

The label mapping includes background, maxilla, mandible, 32 FDI tooth classes, and the mandibular canal (label 35, recorded under the original configuration key `seg5`). This key is retained for compatibility with the trained model. See [label definitions](LABELS.md) and [internal validation metrics](VALIDATION.md).

## Reference

Isensee F, Jaeger PF, Kohl SAA, Petersen J, Maier-Hein KH. nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. *Nature Methods*. 2021;18:203–211. https://doi.org/10.1038/s41592-020-01008-z
