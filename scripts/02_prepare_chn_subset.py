"""
Prepare a CHN subset in PaddleOCR recognition format.

Default:
    train: 5000 samples
    test: 500 samples

Run:
    python scripts/02_prepare_chn_subset.py --train_size 5000 --test_size 500

Output:
    data/chn_subset/train_images/
    data/chn_subset/test_images/
    data/chn_subset/rec_gt_train.txt
    data/chn_subset/rec_gt_test.txt

Important:
    The CHN dataset column names may differ. If this script fails, first run
    01_inspect_chn_dataset.py, then update IMAGE_COLUMN and TEXT_COLUMN below.
"""

from datasets import load_dataset
from pathlib import Path
from PIL import Image
from tqdm import tqdm
import argparse
import re

DATASET_NAME = "chuuhtetnaing/myanmar-ocr-dataset"

# Update these after inspecting the dataset.
# Common possibilities: "image", "text", "label"
IMAGE_COLUMN = "image"
TEXT_COLUMN = "text"

OUT_ROOT = Path("data/chn_subset")

def safe_label(label: str) -> str:
    label = str(label).replace("\n", " ").replace("\r", " ").strip()
    # Keep tabs out of PaddleOCR label file.
    label = label.replace("\t", " ")
    return label

def save_split(split, split_name: str, limit: int):
    img_dir = OUT_ROOT / f"{split_name}_images"
    img_dir.mkdir(parents=True, exist_ok=True)

    gt_path = OUT_ROOT / f"rec_gt_{split_name}.txt"

    count = 0
    with gt_path.open("w", encoding="utf-8") as f:
        for idx, sample in enumerate(tqdm(split, total=limit, desc=f"Preparing {split_name}")):
            if count >= limit:
                break

            if IMAGE_COLUMN not in sample or TEXT_COLUMN not in sample:
                raise KeyError(
                    f"Expected columns {IMAGE_COLUMN=} and {TEXT_COLUMN=}, "
                    f"but got columns {list(sample.keys())}. "
                    "Run 01_inspect_chn_dataset.py and update this script."
                )

            image = sample[IMAGE_COLUMN]
            label = safe_label(sample[TEXT_COLUMN])

            if not label:
                continue

            if not isinstance(image, Image.Image):
                # Some HF datasets store images as dicts or paths. Try common forms.
                if isinstance(image, dict) and "bytes" in image:
                    from io import BytesIO
                    image = Image.open(BytesIO(image["bytes"])).convert("RGB")
                elif isinstance(image, dict) and "path" in image:
                    image = Image.open(image["path"]).convert("RGB")
                else:
                    raise TypeError(f"Unsupported image type: {type(image)}")

            image = image.convert("RGB")
            img_name = f"{split_name}_{count:06d}.png"
            img_path = img_dir / img_name
            image.save(img_path)

            # PaddleOCR paths should be relative to the dataset root.
            rel_path = f"{split_name}_images/{img_name}"
            f.write(f"{rel_path}\t{label}\n")
            count += 1

    print(f"Saved {count} samples to {gt_path}")
    return count

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_size", type=int, default=5000)
    parser.add_argument("--test_size", type=int, default=500)
    args = parser.parse_args()

    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    print(f"Loading {DATASET_NAME} with streaming=True")
    ds = load_dataset(DATASET_NAME, streaming=True)

    split_names = list(ds.keys())
    print("Available splits:", split_names)

    if "train" not in ds:
        raise ValueError("No train split found. Check dataset splits with 01_inspect_chn_dataset.py.")

    train_split = ds["train"]

    # Prefer test split if available, otherwise split from train stream is not ideal but ok for pilot.
    test_split = ds["test"] if "test" in ds else ds["train"].skip(args.train_size)

    train_count = save_split(train_split, "train", args.train_size)
    test_count = save_split(test_split, "test", args.test_size)

    print("\nDONE")
    print(f"Train samples: {train_count}")
    print(f"Test samples: {test_count}")
    print(f"Next: python scripts/03_build_dictionary.py")

if __name__ == "__main__":
    main()
