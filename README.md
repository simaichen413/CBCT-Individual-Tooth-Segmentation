# CBCT Individual Tooth Segmentation

This repository documents a **3D nnU-Net v2 model** for multiclass segmentation of teeth, maxilla, and mandible in cone-beam computed tomography (CBCT). The model generates individual tooth labels following the FDI numbering system and provides three-dimensional segmentation masks for visualization and quantitative image analysis.

## Segmentation examples

The images below illustrate the predicted segmentation overlaid on CBCT slices and reconstructed as three-dimensional tooth and jawbone surfaces.

| CBCT segmentation: axial, coronal, sagittal, and 3D views |  CBCT segmentation: axial, coronal, sagittal, and 3D views |
| :-------------------------------------------------------: | :--------------------------------------------------------: |
| Multiplanar CBCT segmentation with a frontal 3D rendering | Multiplanar CBCT segmentation with an oblique 3D rendering |

|            Tooth and jawbone reconstruction           |                 Individual teeth: frontal view                |
| :---------------------------------------------------: | :-----------------------------------------------------------: |
| Three-dimensional CBCT tooth and jawbone segmentation | Color-coded individually segmented teeth shown from the front |

## Model overview

| Property                     | Value                                                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Framework                    | nnU-Net v2                                                                                                               |
| Dataset                      | `Dataset413_byscm` (ID `413`)                                                                                            |
| Configuration                | `3d_fullres`                                                                                                             |
| Trainer                      | `nnUNetTrainerNoMirroring`                                                                                               |
| Available fold               | `0` (`checkpoint_final.pth`)                                                                                             |
| Input                        | Single-channel CBCT, NIfTI `.nii.gz`                                                                                     |
| Preprocessing target spacing | 0.25 × 0.25 × 0.25 mm                                                                                                    |
| Segmentation labels          | Maxilla, mandible, 32 FDI tooth classes, and mandibular canal (label 35, stored as `seg5` in the training configuration) |
| Development dataset          | 55 annotated CBCT scans (44 training / 11 internal validation)                                                           |

The exact integer-to-FDI mapping is provided in [Label definitions](docs/LABELS.md). Label 35 corresponds to the **mandibular canal**. Its original configuration key, `seg5`, is retained for compatibility with the trained model.

## Model availability

**The trained model weights are available upon reasonable request for academic and research purposes.**

To request the pretrained nnU-Net model, please email **<simaichen413@gmail.com>** with a brief description of your research purpose.

The model is provided as an nnU-Net v2-compatible ZIP archive (`nnUNet_413.zip`). Once received, install the ZIP directly using:

```bash
nnUNetv2_install_pretrained_model_from_zip /path/to/nnUNet_413.zip
```

## Installation and inference

Install nnU-Net v2 in a compatible Python / PyTorch environment:

```bash
pip install nnunetv2
```

Set a writable nnU-Net results directory (macOS/Linux example):

```bash
export nnUNet_results="$HOME/nnUNet_results"
mkdir -p "$nnUNet_results"
```

After importing the model archive, place single-channel CBCT images in a folder using the standard nnU-Net naming convention:

```text
imagesTs/
├── case001_0000.nii.gz
└── case002_0000.nii.gz
```

Run segmentation using Fold 0:

```bash
nnUNetv2_predict \
  -i ./imagesTs \
  -o ./predictions \
  -d 413 \
  -c 3d_fullres \
  -f 0 \
  -tr nnUNetTrainerNoMirroring
```

For additional instructions on macOS, Linux, and Windows, see [Installation](docs/INSTALLATION.md) and [中文使用说明](docs/使用说明_中文.md). Helper scripts are available in [`scripts/`](scripts/).

## Internal validation

Internal validation was performed on 11 CBCT scans. Metrics below are calculated against reference segmentation labels.

| Target                                              |  Mean Dice |   Mean IoU |
| --------------------------------------------------- | ---------: | ---------: |
| 32 individual tooth classes (unweighted class mean) | **0.9670** | **0.9494** |
| Maxilla                                             |     0.9696 |     0.9410 |
| Mandible                                            |     0.9852 |     0.9709 |
| All 35 foreground classes (unweighted class mean)   |     0.9667 |     0.9478 |

These values are from internal Fold 0 validation. See [Validation](docs/VALIDATION.md) and [per-class metrics](metadata/validation_by_label.csv) for the full results.

## Repository structure

```text
CBCT-Individual-Tooth-Segmentation/
├── README.md
├── .gitignore
├── assets/
│   └── segmentation/         # CBCT overlays and 3D visualizations
├── model/
│   └── README.md             # Model access information
├── docs/
│   ├── INSTALLATION.md
│   ├── LABELS.md
│   ├── MODEL.md
│   ├── VALIDATION.md
│   └── 使用说明_中文.md
├── metadata/
│   ├── dataset.json
│   ├── model.json
│   └── validation_by_label.csv
└── scripts/
    ├── check_model_zip.py
    ├── predict.sh
    └── predict.ps1
```

## Reference

Isensee F, Jaeger PF, Kohl SAA, Petersen J, Maier-Hein KH. nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. *Nature Methods*. 2021;18:203–211. <https://doi.org/10.1038/s41592-020-01008-z>
