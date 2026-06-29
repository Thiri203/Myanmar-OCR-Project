"""
Inspect the CHN Myanmar OCR dataset from Hugging Face.

Run:
    python scripts/01_inspect_chn_dataset.py

This script prints dataset split names, columns, row counts, and saves one sample image
if the image column can be detected.
"""

from datasets import load_dataset
from pathlib import Path
from PIL import Image

DATASET_NAME = "chuuhtetnaing/myanmar-ocr-dataset"
OUT_DIR = Path("results")
OUT_DIR.mkdir(exist_ok=True)

def main():
    print(f"Loading dataset: {DATASET_NAME}")
    ds = load_dataset(DATASET_NAME, streaming=True)

    print("Splits:", list(ds.keys()))
    for split_name, split in ds.items():
        print(f"\nSplit: {split_name}")
        sample = next(iter(split))
        print("Columns:", list(sample.keys()))
        for k, v in sample.items():
            print(f"  {k}: {type(v)}")
            if isinstance(v, str):
                print(f"    preview: {v[:120]}")

        # Try to save image sample
        for k, v in sample.items():
            if isinstance(v, Image.Image):
                out_path = OUT_DIR / f"sample_{split_name}.png"
                v.save(out_path)
                print(f"Saved sample image to {out_path}")
                break

        break

if __name__ == "__main__":
    main()
