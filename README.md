# Myanmar OCR Project

## Project direction

This project investigates Myanmar text recognition using the `chuuhtetnaing/myanmar-ocr-dataset` dataset as the main training dataset. The project focuses on the optical OCR recognition stage, not post-OCR correction.

For Phase 2, the coding target is:

| Phase | Experiment | Train | Test | Submit |
|---|---|---|---|---|
| Phase 2 | E1 pilot | CHN subset | CHN test subset | Yes |
| Final | E1 scaled | Larger CHN subset | CHN test subset | Yes |

Optional final extension:
- Evaluate the best CHN-trained model on the myOCR test set as an external benchmark.

## Main implementation idea

We use a PaddleOCR-style text recognition model with a custom Myanmar character dictionary. The dataset is converted into recognition format:

```text
image_path<TAB>label
```

Example:

```text
train_images/img_000001.png	မြန်မာစာ...
```

## Folder structure

```text
Myanmar-OCR-Project/
├── data/
│   ├── raw/
│   └── chn_subset/
│       ├── train_images/
│       ├── test_images/
│       ├── rec_gt_train.txt
│       ├── rec_gt_test.txt
│       └── myanmar_dict.txt
├── scripts/
├── configs/
├── outputs/
├── results/
└── docs/
```

## Phase 2 minimum result to report

Fill these values after training:

```text
Dataset:
- Train subset size:
- Test subset size:

Model:
- Framework:
- Base config/model:
- Custom dictionary size:

Compute:
- GPU:
- Training time:
- Epochs/iterations:
- Batch size:

Metrics:
- CER:
- WER:
- chrF++:

Notes:
- Did the model converge?
- Main error types:
- Limitations:
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

For PaddleOCR training, follow the commands in `docs/PUFFER_SETUP.md`.
