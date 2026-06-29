# Phase 2 Inference Examples

Model: PaddleOCR CRNN recognition model  
Checkpoint: puffer_2080ti_scaled_20k/best_accuracy  
Dataset: CHN Myanmar OCR test subset  
Input type: cropped Myanmar text-line images  

| Image | Ground Truth | Prediction | Confidence | Result |
|---|---|---|---:|---|
| test_000000.png | သည် | သည် | 0.9998 | Correct |
| test_000001.png | မှာငြိပါ ပါလိမ့်။ | မှာပြီပါ ပါလိမ်း | 0.9326 | Partial |
| test_000002.png | သေတ္တာကို မရဲတ | သေတ္တာကို မရဲ့တ | 0.8922 | Near |
| test_000003.png | ၃၅၃ ဖြစ်သည်။ ၂၀၁၄ သန်းခေါင်စာရင်းအရ တောင်နီကျေးရွာအုပ်စုတွင် ကျား ၁၁၀ | ၄၅၃ ဖြစ်သည်။ ၂၀၁၄ သန်းခခါစ်စာရင်းအရ တောစ်မီခကျေးရွာအုပ်ခုတွင် ကျား ၁၁၀ | 0.8919 | Partial |
| test_000004.png | ပုသိမ်မြို့သည် ၁၂ စ | ပုသိမ်မြို့သည် ၁၂ | 0.9288 | Near |
| test_000005.png | ပုန်း | ပှန်း | 0.9037 | Incorrect |
| test_000006.png | ရင်မ အားပြန်၍ လက် | ရင်မ အားပြန်၍ လက် | 0.9715 | Correct |
| test_000007.png | မလာသေး | မလာသေး | 0.9172 | Correct |
| test_000008.png | ခဲ့သော | ခဲ့သော | 0.9495 | Correct |
| test_000009.png | အ | အ | 0.9998 | Correct |

Summary: The trained recognition model can perform inference on cropped Myanmar text-line images. Short words are often recognized correctly, while longer sentences still contain character-level and punctuation-level errors.
