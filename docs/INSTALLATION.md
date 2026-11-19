# Installation and inference

This model runs with nnU-Net v2. The trained weights are available upon reasonable request by email at [simaichen413@gmail.com](mailto:simaichen413@gmail.com). Please include a brief description of the intended research use.

## Environment

Install an nnU-Net v2 and PyTorch environment appropriate for your hardware:

```bash
pip install nnunetv2
```

Configure a writable results directory (macOS/Linux):

```bash
export nnUNet_results="$HOME/nnUNet_results"
mkdir -p "$nnUNet_results"
```

Windows PowerShell:

```powershell
$env:nnUNet_results = "$HOME\nnUNet_results"
New-Item -ItemType Directory -Force $env:nnUNet_results
```

## Import the pretrained model

The pretrained model is supplied upon request as `nnUNet_413.zip`, in the standard nnU-Net v2 model-export structure. Install it directly without unpacking:

```bash
nnUNetv2_install_pretrained_model_from_zip /path/to/nnUNet_413.zip
```

The ZIP provides `Dataset413_byscm`, `nnUNetTrainerNoMirroring`, `nnUNetPlans`, `3d_fullres`, and Fold 0. See [Model description](MODEL.md) for configuration details.

You can inspect a received model archive before installation with:

```bash
python scripts/check_model_zip.py /path/to/nnUNet_413.zip --full
```

## Input images

Use a single `.nii.gz` CBCT image per case, with the channel suffix `_0000`:

```text
imagesTs/
├── case001_0000.nii.gz
└── case002_0000.nii.gz
```

## Inference

```bash
nnUNetv2_predict -i ./imagesTs -o ./predictions -d 413 -c 3d_fullres -f 0 -tr nnUNetTrainerNoMirroring
```

The output folder contains multiclass NIfTI masks (`case001.nii.gz`, etc.). Only Fold 0 is supplied. The numeric segmentation IDs and their associated anatomical names are documented in [LABELS.md](LABELS.md).

Helper scripts:

```bash
bash scripts/predict.sh ./imagesTs ./predictions
```

```powershell
.\scripts\predict.ps1 -InputDir .\imagesTs -OutputDir .\predictions
```

System RAM and GPU memory requirements depend on the input image dimensions and inference configuration.
