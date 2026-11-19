#!/usr/bin/env python3
"""Validate the structure and integrity of a received nnU-Net model ZIP."""
from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

PREFIX = 'Dataset413_byscm/nnUNetTrainerNoMirroring__nnUNetPlans__3d_fullres/'
REQUIRED = [PREFIX + name for name in ('dataset.json', 'plans.json', 'fold_0/checkpoint_final.pth')]


def main() -> int:
    parser = argparse.ArgumentParser(description='Check nnU-Net Dataset413 model archive')
    parser.add_argument('archive', type=Path, help='Path to the received model ZIP')
    parser.add_argument('--full', action='store_true', help='Verify CRC of all ZIP members')
    parser.add_argument('--sha256', help='Optional expected SHA-256 supplied with the model')
    args = parser.parse_args()

    digest = hashlib.sha256()
    with args.archive.open('rb') as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b''):
            digest.update(chunk)
    observed = digest.hexdigest()
    print('SHA-256:', observed)
    if args.sha256 and observed.lower() != args.sha256.lower():
        raise SystemExit('SHA-256 does not match the expected value.')

    with zipfile.ZipFile(args.archive) as z:
        missing = sorted(set(REQUIRED) - set(z.namelist()))
        if missing:
            raise SystemExit('Missing required nnU-Net files: ' + ', '.join(missing))
        dataset = json.loads(z.read(PREFIX + 'dataset.json'))
        plans = json.loads(z.read(PREFIX + 'plans.json'))
        if dataset.get('file_ending') != '.nii.gz':
            raise SystemExit('Unexpected input file extension in dataset.json')
        if '3d_fullres' not in plans.get('configurations', {}):
            raise SystemExit('3d_fullres configuration missing from plans.json')
        if args.full:
            bad = z.testzip()
            if bad:
                raise SystemExit('Archive integrity check failed for: ' + bad)
    print('OK: required Dataset413 nnU-Net model files are present.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
