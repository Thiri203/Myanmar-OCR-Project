# Local RTX 4060 Setup Guide

The local RTX 4060 machine should be used for debugging and backup runs.

Recommended local run:
- 1,000 train images
- 200 test images
- 1 to 3 epochs

The goal is not the final metric. The goal is to confirm:
- CHN dataset can be loaded
- PaddleOCR label format is correct
- Myanmar dictionary works
- training command runs
- prediction output can be evaluated
