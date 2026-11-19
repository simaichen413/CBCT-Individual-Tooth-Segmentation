param(
  [Parameter(Mandatory=$true)][string]$InputDir,
  [Parameter(Mandatory=$true)][string]$OutputDir
)
& nnUNetv2_predict -i $InputDir -o $OutputDir -d 413 -c 3d_fullres -f 0 -tr nnUNetTrainerNoMirroring
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
