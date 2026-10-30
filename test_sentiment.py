from transformers import pipeline

def test_positive_sentence():
    classifier = pipeline(
        "text-classification",
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    )
    result = classifier("I love this product, it works perfectly!")[0]
    assert result["label"] == "POSITIVE"
