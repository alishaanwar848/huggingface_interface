# Wednesday: Using the Hugging Face Inference API for a simple text task

**Task:** run sentiment analysis through the Hugging Face Inference API.

## Attempt: Inference API

I created a read-only access token and, in Google Colab, called the API with `InferenceClient.text_classification`. The token was typed in with `getpass`, so it is not stored in the notebook.

```python
from huggingface_hub import InferenceClient

client = InferenceClient(provider="hf-inference", token=HF_TOKEN)

result = client.text_classification(
    "I love this product, it works perfectly!",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
)
print(result)
```

I tried two models. Both returned **402 Payment Required**.

| Attempt | Model | Result |
|---|---|---|
| 1 | `cardiffnlp/twitter-roberta-base-sentiment-latest` | 402 Payment Required |
| 2 | `distilbert/distilbert-base-uncased-finetuned-sst-2-english` | 402 Payment Required |

![First 402 error (cardiffnlp)](error.PNG)
![Second 402 error (distilbert)](error2.PNG)

## Why the API did not work

The Inference API runs the model on Hugging Face servers and uses account credits. My account has **$0.00 in credits** (billing page below), so every API call was rejected with 402. The code and token were fine. The limit is on credits, not on the code.

![Billing page showing $0.00 credits](credits.PNG)

## Fallback: same task with a local pipeline

Since the API was blocked, I ran the same sentiment analysis locally in Colab with `transformers`. This downloads the model into Colab, so it needs no token and no credits.

```python
from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
)

for s in [
    "I love this product, it works perfectly!",
    "This was the worst experience ever.",
    "The package arrived on Tuesday.",
]:
    r = classifier(s)[0]
    print(s, "->", r["label"], f"{r['score']:.2f}")
```

| Sentence | Label | Score |
|---|---|---|
| I love this product, it works perfectly! | positive | 0.99 |
| This was the worst experience ever. | negative | 0.94 |
| The package arrived on Tuesday. | neutral | 0.68 |

![Code and model download](a.PNG)
![Local pipeline output](c.PNG)

## What I learned

- **Inference API:** model runs on Hugging Face servers, needs a token, uses credits.
- **Local pipeline:** model runs in my own Colab, needs no token and is free, but has to be downloaded first.
