# Output labels

The model predicts an integer label image. The numeric IDs in the output are mapped to anatomical and dental labels as follows (from `dataset.json`):

| Label ID | Dataset label | Structure |
|---:|---|---|
| 0 | `background` | Background |
| 1 | `Maxilla` | Maxilla |
| 2 | `Mandible` | Mandible |
| 3 | `11` | Tooth 11 (FDI notation) |
| 4 | `12` | Tooth 12 (FDI notation) |
| 5 | `13` | Tooth 13 (FDI notation) |
| 6 | `14` | Tooth 14 (FDI notation) |
| 7 | `15` | Tooth 15 (FDI notation) |
| 8 | `16` | Tooth 16 (FDI notation) |
| 9 | `17` | Tooth 17 (FDI notation) |
| 10 | `18` | Tooth 18 (FDI notation) |
| 11 | `21` | Tooth 21 (FDI notation) |
| 12 | `22` | Tooth 22 (FDI notation) |
| 13 | `23` | Tooth 23 (FDI notation) |
| 14 | `24` | Tooth 24 (FDI notation) |
| 15 | `25` | Tooth 25 (FDI notation) |
| 16 | `26` | Tooth 26 (FDI notation) |
| 17 | `27` | Tooth 27 (FDI notation) |
| 18 | `28` | Tooth 28 (FDI notation) |
| 19 | `31` | Tooth 31 (FDI notation) |
| 20 | `32` | Tooth 32 (FDI notation) |
| 21 | `33` | Tooth 33 (FDI notation) |
| 22 | `34` | Tooth 34 (FDI notation) |
| 23 | `35` | Tooth 35 (FDI notation) |
| 24 | `36` | Tooth 36 (FDI notation) |
| 25 | `37` | Tooth 37 (FDI notation) |
| 26 | `38` | Tooth 38 (FDI notation) |
| 27 | `41` | Tooth 41 (FDI notation) |
| 28 | `42` | Tooth 42 (FDI notation) |
| 29 | `43` | Tooth 43 (FDI notation) |
| 30 | `44` | Tooth 44 (FDI notation) |
| 31 | `45` | Tooth 45 (FDI notation) |
| 32 | `46` | Tooth 46 (FDI notation) |
| 33 | `47` | Tooth 47 (FDI notation) |
| 34 | `48` | Tooth 48 (FDI notation) |
| 35 | `seg5` | Additional segmentation label (`seg5`) |

`seg5` is listed as an auxiliary class in the original model configuration; its anatomical definition is not included in the supplied metadata.
