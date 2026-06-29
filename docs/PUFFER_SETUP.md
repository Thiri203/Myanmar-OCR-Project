# Puffer Setup Guide

This is the practical setup guide for the RTX 2080 Ti Puffer environment.

## 1. SSH into Puffer

Use your normal Puffer login method.

## 2. Clone project repo

```bash
cd ~
git clone https://github.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>.git
cd <YOUR_REPO_NAME>
```

## 3. Create Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Check CUDA:

```bash
nvidia-smi
python - <<'PY'
import torch
print("torch available?", "torch" in globals())
PY
```

PaddleOCR may require PaddlePaddle GPU installation depending on CUDA version.
Check the CUDA version from:

```bash
nvidia-smi
```

Then install PaddlePaddle GPU from the official PaddlePaddle install selector.

## 4. Inspect CHN dataset

```bash
python scripts/01_inspect_chn_dataset.py
```

If the dataset column names are not `image` and `text`, edit:

```text
scripts/02_prepare_chn_subset.py
```

and update:

```python
IMAGE_COLUMN = "..."
TEXT_COLUMN = "..."
```

## 5. Prepare Phase 2 subset

For first Puffer pilot:

```bash
python scripts/02_prepare_chn_subset.py --train_size 5000 --test_size 500
python scripts/03_build_dictionary.py
```

For larger final training later:

```bash
python scripts/02_prepare_chn_subset.py --train_size 50000 --test_size 2000
python scripts/03_build_dictionary.py
```

## 6. PaddleOCR training workflow

Clone PaddleOCR beside this repo:

```bash
cd ~
git clone https://github.com/PaddlePaddle/PaddleOCR.git
cd PaddleOCR
```

Install PaddleOCR requirements according to the official docs.

Then copy or adapt a recognition config from PaddleOCR:

```bash
cp configs/rec/PP-OCRv3/en_PP-OCRv3_rec.yml ~/YOUR_REPO_NAME/configs/myanmar_rec_config.yml
```

Edit the config paths:
- dictionary path
- training label file
- evaluation label file
- data root
- output directory
- epochs / batch size

Then train:

```bash
python tools/train.py -c ~/YOUR_REPO_NAME/configs/myanmar_rec_config.yml
```

Evaluate:

```bash
python tools/eval.py -c ~/YOUR_REPO_NAME/configs/myanmar_rec_config.yml \
  -o Global.checkpoints=~/YOUR_REPO_NAME/outputs/puffer_2080ti_run1/best_accuracy
```

## 7. Save report values

Create:

```text
results/phase2_summary.txt
results/sample_predictions.csv
```

Send these values to the report teammate:
- train subset size
- test subset size
- model config name
- dictionary size
- GPU name
- training time
- epochs/iterations
- batch size
- CER
- WER
- chrF++
- sample predictions
