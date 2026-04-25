import re, numpy as np, pandas as pd, matplotlib.pyplot as plt
from collections import Counter
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer

# --- Load ---
df = pd.read_csv("Tweets.csv", encoding="utf-8", on_bad_lines="skip")
TEXT_COL = next((c for c in ["text","tweet","content","body","message"] if c in df.columns), df.columns[0])

# --- Clean ---
STOPWORDS = {"the","is","in","at","of","and","a","to","for","it","this","that","with",
             "on","are","was","be","as","by","an","or","but","not","from","have","has",
             "he","she","they","we","you","i","my","your","its","their","our","so","if",
             "do","did","get","got","been","will","can","just","about","all","amp","rt"}

def clean(text):
    text = re.sub(r"http\S+|@\w+|[^a-z\s]", "", str(text).lower())
    return " ".join(w for w in text.split() if w not in STOPWORDS and len(w) > 2)

df["clean"] = df[TEXT_COL].apply(clean)
df = df[df["clean"].str.strip() != ""]

# --- Sentiment via TextBlob ---
# polarity: -1 (negative) to +1 (positive), subjectivity: 0 (factual) to 1 (opinionated)
df["polarity"]     = df["clean"].apply(lambda x: TextBlob(x).sentiment.polarity)
df["subjectivity"] = df["clean"].apply(lambda x: TextBlob(x).sentiment.subjectivity)
df["sentiment"]    = df["polarity"].apply(lambda p: "positive" if p > 0.05 else ("negative" if p < -0.05 else "neutral"))

# --- Plot 1: 4-panel sentiment overview ---
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# sentiment counts
df["sentiment"].value_counts().plot(kind="bar", ax=axes[0,0])
axes[0,0].set_title("Sentiment Count")

# polarity histogram
axes[0,1].hist(df["polarity"], bins=40)
axes[0,1].set_title("Polarity Distribution")

# subjectivity histogram
axes[1,0].hist(df["subjectivity"], bins=40)
axes[1,0].set_title("Subjectivity Distribution")

# polarity vs subjectivity scatter, coloured by sentiment
for label, group in df.groupby("sentiment"):
    axes[1,1].scatter(group["polarity"], group["subjectivity"], alpha=0.3, s=8, label=label)
axes[1,1].legend()
axes[1,1].set_title("Polarity vs Subjectivity")

plt.tight_layout()
plt.savefig("p05_sentiment_overview.png"); plt.show()

# --- Plot 2: TF-IDF top keywords ---
# TF-IDF scores words that are frequent in a doc but rare across all docs (distinctive words)
# fit_transform builds a word-score table: rows=tweets, columns=words
tfidf = TfidfVectorizer(max_features=30, stop_words="english", ngram_range=(1,2))
matrix = tfidf.fit_transform(df["clean"])

# average each word's score across all tweets
mean_scores = matrix.mean(axis=0)

# matrix.mean returns a weird 2D numpy matrix, flatten it to a normal 1D array
mean_scores = np.asarray(mean_scores).flatten()

# pair each score with its word name, put in a Series
scores = pd.Series(mean_scores, index=tfidf.get_feature_names_out())

# sort and plot top 20
scores.sort_values().tail(20).plot(kind="barh")
plt.title("Top 20 Keywords by TF-IDF")
plt.savefig("p05_tfidf.png"); plt.show()

# --- Plot 3: top words per sentiment class ---
for label in ["positive", "negative", "neutral"]:
    words = " ".join(df[df["sentiment"] == label]["clean"]).split()
    top = pd.Series(Counter(words).most_common(10), dtype=object)
    words, counts = zip(*Counter(words).most_common(10))
    pd.Series(counts, index=words).plot(kind="barh")
    plt.title(f"Top words — {label}")
    plt.tight_layout()
    plt.savefig(f"p05_words_{label}.png"); plt.show()