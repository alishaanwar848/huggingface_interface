# Friday: Using a ready-made `pipeline()`

I used `pipeline("text-classification")` with the DistilBERT SST-2 model. In just 3 lines of code, the pipeline downloaded the model, processed my text and returned a label (POSITIVE) with a score (0.97). The `summarization` task was not available in this version of the library, so I used classification instead.

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

print(classifier("Hugging Face makes AI easy for beginners."))
```

**Output:**

```
[{'label': 'POSITIVE', 'score': 0.9727}]
```

