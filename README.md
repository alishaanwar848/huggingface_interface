# Hugging Face Explorer

A week of hands-on work with Hugging Face. Every test uses the same three sentences so results can be compared across days:

1. `I love this product, it works perfectly!`
2. `This was the worst experience ever.`
3. `The package arrived on Tuesday.`

## Summary

| Day | Task | Result |
|---|---|---|
| [Monday](#monday-intro-to-hugging-face) | Intro: Hub, Models, Datasets, Spaces | What each one is for |
| [Tuesday](tuesday/) | Hosted open-source model on the website (no code) | Positive 90%, negative 84%, neutral 75% |
| [Wednesday](wednesday/) | Inference API for sentiment analysis | API blocked (402, $0.00 credits), ran locally instead |
| [Thursday](thursday/) | Open-source vs proprietary model | Both correct on all 3 sentences |
| [Friday](friday/) | Ready-made `pipeline()` | POSITIVE, score 0.97 |

---

## Monday: Intro to Hugging Face

Hugging Face is like GitHub for machine learning. People and companies share models, datasets and demo apps there, so nobody has to build everything from scratch.

- **Hub:** the whole platform. Every model, dataset and Space is a repository with files, version history and documentation.
- **Models:** pretrained AI models for text, images, audio and more. Each has a model card explaining what it does and its limits. Use when you need a ready-made model.
- **Datasets:** collections of data used to train, fine-tune or test models. Use when you need data to train or evaluate a model.
- **Spaces:** small hosted apps (Gradio or Streamlit) that let you try a model in the browser. Use to test a model quickly or show a demo to someone who does not code.
- **How they fit together:** find a model on the Hub, test it on a dataset, show it in a Space.

---

## Tuesday: Hosted model on the website (no code)

- Tried `distilbert/distilbert-base-uncased-finetuned-sst-2-english` on its model page. The widget showed "no remaining credits", because hosted inference uses credits.
- Used the Space `zama-fhe/encrypted_sentiment_analysis` instead. It runs sentiment analysis on encrypted data.
- Results:
  - Positive sentence: **positive 90%**
  - Negative sentence: **negative 84%**
  - Neutral sentence: **neutral 75%**
- This Space has three labels, while DistilBERT SST-2 has only two, so it handles neutral text better.
- Spaces worked without credits and without code.

Details and screenshots: [tuesday/](tuesday/)

---

## Wednesday: Hugging Face Inference API

- Called `InferenceClient.text_classification` from Google Colab with a read-only token (entered with `getpass`, never saved).
- Tried two models (`cardiffnlp/twitter-roberta-base-sentiment-latest` and `distilbert/distilbert-base-uncased-finetuned-sst-2-english`). Both returned **402 Payment Required**.
- **Reason:** the API runs on Hugging Face servers and uses credits. The account has $0.00 credits (billing page screenshot included).
- **Fallback:** ran the same task locally with `pipeline("sentiment-analysis")`:
  - positive 0.99
  - negative 0.94
  - neutral 0.68
- API: needs a token and credits. Local pipeline: free and no token, but the model must be downloaded first.

Details and screenshots: [wednesday/](wednesday/)

---

## Thursday: Open-source vs proprietary model

- Open-source: `cardiffnlp/twitter-roberta-base-sentiment-latest` (local, Colab). Proprietary: Google Gemini.

| Sentence | RoBERTa | Gemini |
|---|---|---|
| Positive sentence | Positive 0.99 | Positive 0.99 |
| Negative sentence | Negative 0.94 | Negative 0.99 |
| Neutral sentence | Neutral 0.68 | Neutral 0.98 |

- Both classified all 3 sentences correctly.
- Gemini also gave reasons. RoBERTa gave only a label and score.
- Gemini's scores are written by the model, not true probabilities. RoBERTa's are real probabilities, so its 0.68 is the more honest number.
- Cost: RoBERTa is free. Gemini has a limited free tier and a paid API.
- Ease: Gemini needs only a prompt. RoBERTa needs code and setup.
- Control: RoBERTa runs locally and data stays with me. Gemini sends data to Google's servers.
- **Conclusion:** Gemini is easier and explains itself. The open-source model is free, private and under my control.

Details and screenshots: [thursday/](thursday/)

---

## Friday: `pipeline()`

- Used `pipeline("text-classification")` with the DistilBERT SST-2 model.
- Three lines of code: the pipeline downloaded the model, processed the text and returned **POSITIVE** with a score of **0.97**.
- The `summarization` task was not available in this version of the library, so I used classification instead.

Details and screenshot: [friday/](friday/)

---

## Note on credentials

No access token is stored in this repo. The token was typed into Colab with `getpass` and never saved in a notebook or file.
