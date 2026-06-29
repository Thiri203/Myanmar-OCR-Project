# Myanmar OCR Project

## Project Direction

This project investigates Myanmar text recognition using the `chuuhtetnaing/myanmar-ocr-dataset` dataset as the main training dataset.

The current implementation focuses on the optical OCR recognition stage. This means the model takes cropped Myanmar text-line images as input and predicts the corresponding Myanmar text sequence.

This project does not yet implement full-page OCR, text detection, or post-OCR correction.

---

## Framework and Model

Framework: PaddleOCR  
Task type: Text recognition  
Training style: From scratch  
Dataset: CHN Myanmar OCR dataset  
Model architecture: CRNN + MobileNetV3 + RNN SequenceEncoder + CTCHead  
Loss function: CTCLoss  
Dictionary: Custom Myanmar character dictionary  

PaddleOCR is used as the OCR training framework. The model does not use a pretrained Burmese OCR model. Instead, it learns Myanmar text recognition from CHN image-label pairs.

---

## Phase 2 Experiments

| Run | GPU | Train Size | Test Size | Epochs | Batch Size | Checkpoint | Accuracy | Normalized Edit Distance | FPS |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| E1 Pilot | RTX 2080 Ti | 5,000 | 500 | 5 | 32 | latest | 0.0220 | 0.2627 | 775.05 |
| E1 Scaled | RTX 2080 Ti | 20,000 | 2,000 | 20 | 32 | best_accuracy | 0.2825 | 0.5067 | 1592.95 |

The E1 Pilot experiment was used to verify that the complete PaddleOCR training and evaluation pipeline worked. The E1 Scaled experiment increased both the dataset size and the training duration, which improved the model performance.

---

## Inference

The trained scaled model can perform inference on cropped Myanmar text-line images.

Example inference result:

| Image | Ground Truth | Prediction | Confidence | Result |
|---|---|---|---:|---|
| test_000000.png | သည် | သည် | 0.9998 | Correct |

More examples are saved in:

```text
results/phase2_inference_examples.md
```

---

## Main Implementation Idea

The CHN dataset is converted into PaddleOCR recognition format:

```text
image_path<TAB>label
```

Example:

```text
train_images/train_000001.png     မြန်မာစာ...
```

A custom Myanmar character dictionary is built from the training and test labels. PaddleOCR uses this dictionary to encode and decode Myanmar text labels during training and inference.

---

## Folder Structure

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

Important note: `outputs/` is ignored by Git because it contains large training logs, checkpoints, and model files.

---

## Important Files

```text
configs/myanmar_rec_config.yml
configs/myanmar_rec_config_scaled_20k.yml
results/phase2_summary.txt
results/phase2_inference_examples.md
scripts/02_prepare_chn_subset.py
scripts/03_build_dictionary.py
scripts/05_make_paddle_config.py
scripts/06_make_phase2_summary.py
```

---

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

For PaddleOCR training, follow the setup notes in:

```text
docs/PUFFER_SETUP.md
```

---

## Current Limitations

1. The current model is recognition-only and requires cropped text-line images.
2. The model was trained from scratch on a subset of the full CHN dataset.
3. Longer Myanmar text sequences still contain character-level and punctuation-level errors.
4. Confidence score is not always equal to correctness.
5. Full-page OCR would require an additional text detection stage.

---

## Next Steps

Possible final-stage extensions:

1. Train on a larger CHN subset, such as 50k or 100k images.
2. Evaluate the best CHN-trained model on the myOCR dataset as an external test.
3. Compare an alternative architecture, such as a ResNet backbone.
4. Study the effect of dataset size, number of epochs, or dictionary settings.
5. Explore Myanmar post-OCR correction to reduce character-level errors.
