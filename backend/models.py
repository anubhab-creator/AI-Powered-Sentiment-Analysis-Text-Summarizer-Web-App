from transformers import pipeline

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment"
)

summarizer_pipeline = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)
