import pandas as pd
from textblob import TextBlob

# STEP 1: Load your Zara dataset
df = pd.read_csv("zara_large_reviews_500.csv")  # Make sure the file is in the same folder

# STEP 2: Define sentiment analysis function
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

# STEP 3: Apply sentiment analysis
df["polarity"] = df["review"].apply(lambda x: TextBlob(x).sentiment.polarity)
df["sentiment"] = df["review"].apply(analyze_sentiment)

# STEP 4: Save the updated dataset
df.to_csv("zara_reviews_with_sentiment.csv", index=False, encoding='utf-8')
print("Done! File saved as 'zara_reviews_with_sentiment.csv'")
