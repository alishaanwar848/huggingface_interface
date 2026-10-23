# Tuesday: Trying a hosted open-source model on the Hugging Face website (no code)

## Step 1: Model page

I opened `distilbert/distilbert-base-uncased-finetuned-sst-2-english` and tried its inference widget. It showed "You have no remaining credits for Inference Providers", because hosted inference uses credits and my free credits were zero.

![Credits error](error_fa0a7e.PNG)

## Step 2: Hosted Space instead

Spaces run on community hardware, so I used the Space [`zama-fhe/encrypted_sentiment_analysis`](https://huggingface.co/spaces/zama-fhe/encrypted_sentiment_analysis). It runs sentiment analysis on encrypted data. Steps in the app: generate keys, enter a message, encode and encrypt it, run the evaluation on the server, then decrypt the prediction.

| Input | Prediction | Confidence |
|---|---|---|
| I love this product, it works perfectly! | Positive | 90% |
| This was the worst experience ever | Negative | 84% |
| The package arrived on Tuesday. | Neutral | 75% |

**Positive**

![Positive input](1_94e7df.PNG)
![Positive result](2_0eb3be.PNG)

**Negative**

![Negative input](3_5caded.PNG)
![Negative result](4_ee0682.PNG)

**Neutral**

![Neutral input](5_87336b.PNG)
![Neutral result](6_efbf8b.PNG)

## Observations

- All three sentences were classified correctly.
- This Space has three labels (positive, negative, neutral). DistilBERT SST-2 only has two, so it cannot give a neutral answer.
- Encryption makes it slower than a normal widget, but the server never sees the original text.
- Spaces worked without credits and without any code.
