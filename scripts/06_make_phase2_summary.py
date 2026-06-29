"""
Create Phase 2 summary template with real dataset counts and GPU name.

Run:
    python scripts/06_make_phase2_summary.py --gpu "RTX 2080 Ti" --run_name "puffer_2080ti_run1"
"""

import argparse
from pathlib import Path


def count_lines(path):
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu", default="[FILL]")
    parser.add_argument("--run_name", default="puffer_2080ti_run1")
    args = parser.parse_args()

    data_root = Path("data/chn_subset")
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    train_count = count_lines(data_root / "rec_gt_train.txt")
    test_count = count_lines(data_root / "rec_gt_test.txt")
    dict_count = count_lines(data_root / "myanmar_dict.txt")

    out_path = results_dir / "phase2_summary.txt"
    text = f"""Phase 2 E1 Pilot Result

Dataset:
- Main dataset: chuuhtetnaing/myanmar-ocr-dataset
- Train subset size: {train_count}
- Test subset size: {test_count}

Model:
- Framework: PaddleOCR recognition
- Base config/model: [FILL after training config is finalized]
- Custom dictionary size: {dict_count} characters, plus space character enabled

Compute:
- GPU: {args.gpu}
- Run name: {args.run_name}
- Training time: [FILL]
- Epochs/iterations: [FILL]
- Batch size: [FILL]

Metrics:
- CER: [FILL]
- WER: [FILL]
- chrF++: [FILL]

Sample predictions:
1. GT: [FILL]
   Pred: [FILL]

2. GT: [FILL]
   Pred: [FILL]

Notes:
- Did the model converge? [yes/no]
- Main error types observed: [FILL]
- Limitations: small subset, short training time, synthetic data only
"""
    out_path.write_text(text, encoding="utf-8")
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
