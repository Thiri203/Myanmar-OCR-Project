"""
Build a Myanmar OCR character dictionary from PaddleOCR label files.

Run:
    python scripts/03_build_dictionary.py

Output:
    data/chn_subset/myanmar_dict.txt
"""

from pathlib import Path

DATA_ROOT = Path("data/chn_subset")
LABEL_FILES = [
    DATA_ROOT / "rec_gt_train.txt",
    DATA_ROOT / "rec_gt_test.txt",
]
DICT_PATH = DATA_ROOT / "myanmar_dict.txt"

def main():
    chars = set()

    for label_file in LABEL_FILES:
        if not label_file.exists():
            print(f"Skipping missing file: {label_file}")
            continue

        with label_file.open("r", encoding="utf-8") as f:
            for line in f:
                if "\t" not in line:
                    continue
                _, label = line.rstrip("\n").split("\t", 1)
                for ch in label:
                    # PaddleOCR can handle space separately if use_space_char=True.
                    if ch != " ":
                        chars.add(ch)

    sorted_chars = sorted(chars)
    with DICT_PATH.open("w", encoding="utf-8") as f:
        for ch in sorted_chars:
            f.write(ch + "\n")

    print(f"Dictionary size: {len(sorted_chars)}")
    print(f"Saved dictionary to: {DICT_PATH}")

if __name__ == "__main__":
    main()
