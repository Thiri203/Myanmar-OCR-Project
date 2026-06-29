"""
Evaluate OCR predictions using CER, WER, and chrF++.

Expected CSV:
    results/sample_predictions.csv

Columns:
    ground_truth,prediction

Run:
    python scripts/04_evaluate_predictions.py --input results/sample_predictions.csv
"""

import argparse
import pandas as pd
from jiwer import wer, cer
import sacrebleu

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="results/sample_predictions.csv")
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    refs = df["ground_truth"].fillna("").astype(str).tolist()
    hyps = df["prediction"].fillna("").astype(str).tolist()

    corpus_cer = cer(refs, hyps)
    corpus_wer = wer(refs, hyps)
    chrf = sacrebleu.corpus_chrf(hyps, [refs], word_order=2)

    print("Evaluation results")
    print(f"CER: {corpus_cer:.4f}")
    print(f"WER: {corpus_wer:.4f}")
    print(f"chrF++: {chrf.score:.2f}")

if __name__ == "__main__":
    main()
