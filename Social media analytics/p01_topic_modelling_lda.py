# =============================================================================
# PRACTICAL 01 — CONTENT ANALYSIS: TOPIC MODELLING WITH LDA
# Dataset : Apple Twitter Sentiment (Kaggle)
#   → search "Apple Twitter Sentiment" on Kaggle
#   → file: apple-twitter-sentiment-texts.csv
#   → key columns: text, sentiment
# Libraries: pandas, gensim, matplotlib, re
# =============================================================================

import re
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from gensim import corpora, models

# ---------------------------------------------------------------------------
# STEP 1 — LOAD
# ---------------------------------------------------------------------------
# Try utf-8 first; if that fails (common with scraped data) fall back to latin-1
try:
    df = pd.read_csv("apple-twitter-sentiment-texts.csv", encoding="utf-8", on_bad_lines="skip")
except Exception:
    df = pd.read_csv("apple-twitter-sentiment-texts.csv", encoding="latin-1", on_bad_lines="skip")

print("Shape :", df.shape)
print("Columns:", df.columns.tolist())
print(df.head(3))
print("\nNulls:\n", df.isnull().sum())

# ---------------------------------------------------------------------------
# STEP 2 — IDENTIFY TEXT COLUMN
# ---------------------------------------------------------------------------
# Common names for the tweet/text column across datasets
TEXT_COL = None
for candidate in ["text", "tweet", "content", "body", "message"]:
    if candidate in df.columns:
        TEXT_COL = candidate
        break
if TEXT_COL is None:
    TEXT_COL = df.columns[0]          # fallback: first column
print(f"\nUsing column: '{TEXT_COL}'")

# ---------------------------------------------------------------------------
# STEP 3 — CLEAN TEXT  (regex only — no NLTK download needed)
# ---------------------------------------------------------------------------
# Hardcoded stopwords: safe to use offline, covers most noise words
STOPWORDS = {
    "the","is","in","at","of","and","a","to","for","it","this","that","with",
    "on","are","was","be","as","by","an","or","but","not","from","have","has",
    "he","she","they","we","you","i","my","your","its","their","our","so","if",
    "do","did","get","got","been","will","can","just","about","all","more","also",
    "than","then","now","up","out","when","what","how","which","who","would","could",
    "should","said","no","yes","re","ve","ll","amp","rt","via","https","http"
}

def clean_text(text):
    """
    Cleans a single tweet:
      1. Lowercase everything
      2. Remove URLs (http / www)
      3. Remove @mentions
      4. Remove hashtag symbol (keep the word)
      5. Remove all non-alphabetic characters
      6. Tokenise by whitespace
      7. Drop stopwords and very short tokens (len <= 2)
    Returns a list of clean tokens (not a string) — gensim needs a list.
    """
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)          # remove URLs
    text = re.sub(r"@\w+", "", text)                     # remove mentions
    text = re.sub(r"#", "", text)                        # strip # symbol
    text = re.sub(r"[^a-z\s]", "", text)                 # keep only letters
    tokens = [w for w in text.split() if w not in STOPWORDS and len(w) > 2]
    return tokens

df["tokens"] = df[TEXT_COL].apply(clean_text)

# Remove rows where cleaning left nothing
df = df[df["tokens"].map(len) > 0]
print(f"\nRows after cleaning: {len(df)}")

# ---------------------------------------------------------------------------
# STEP 4 — BUILD GENSIM CORPUS
# ---------------------------------------------------------------------------
# Dictionary maps every unique word to an integer ID
dictionary = corpora.Dictionary(df["tokens"].tolist())

# filter_extremes:
#   no_below=3  → drop words appearing in fewer than 3 docs (typos / rare noise)
#   no_above=0.85 → drop words in >85% of docs (too common to distinguish topics)
dictionary.filter_extremes(no_below=3, no_above=0.85)
print(f"Dictionary size after filtering: {len(dictionary)} unique words")

# doc2bow converts each token list into a bag-of-words: [(word_id, count), ...]
corpus = [dictionary.doc2bow(tokens) for tokens in df["tokens"].tolist()]

# ---------------------------------------------------------------------------
# STEP 5 — TRAIN LDA MODEL
# ---------------------------------------------------------------------------
# num_topics: 5 is a good default; adjust based on how diverse the data is
# passes: 10 means 10 full passes through corpus (more = better but slower)
# random_state: fixes randomness so results are reproducible
NUM_TOPICS = 4
lda_model = models.LdaModel(
    corpus=corpus,
    id2word=dictionary,
    num_topics=NUM_TOPICS,
    passes=10,
    random_state=42,
    alpha="auto"       # auto learns the best topic distribution per document
)

# ---------------------------------------------------------------------------
# STEP 6 — PRINT TOPICS
# ---------------------------------------------------------------------------
print("\n===== DISCOVERED TOPICS =====")
for idx, topic in lda_model.print_topics(num_topics=NUM_TOPICS, num_words=8):
    print(f"Topic {idx}: {topic}")

# ---------------------------------------------------------------------------
# STEP 7 — VISUALISE: one bar chart per topic
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(1, NUM_TOPICS, figsize=(18, 4), sharey=False)
fig.suptitle("LDA Topic Word Weights — Apple Tweets", fontsize=13)

for i in range(NUM_TOPICS):
    # show_topic returns [(word, weight), ...] sorted by weight descending
    topic_words = dict(lda_model.show_topic(i, topn=8))
    words  = list(topic_words.keys())
    weights = list(topic_words.values())

    axes[i].barh(words, weights, color="steelblue")
    axes[i].set_title(f"Topic {i}", fontsize=11)
    axes[i].invert_yaxis()          # highest weight word at top
    axes[i].set_xlabel("Weight")

plt.tight_layout()
plt.savefig("p01_lda_topics.png", dpi=120)
plt.show()

# ---------------------------------------------------------------------------
# STEP 8 — ASSIGN DOMINANT TOPIC TO EACH DOCUMENT
# ---------------------------------------------------------------------------
def get_dominant_topic(bow):
    """Returns the topic index with the highest probability for a document."""
    topics = lda_model.get_document_topics(bow)
    if not topics:
        return -1
    return max(topics, key=lambda x: x[1])[0]

df["dominant_topic"] = [get_dominant_topic(corpus[i]) for i in range(len(df))]

# Distribution of dominant topics across the dataset
topic_dist = df["dominant_topic"].value_counts().sort_index()
print("\nDocuments per topic:\n", topic_dist)

# Pie chart of topic distribution
plt.figure(figsize=(6, 6))
plt.pie(
    topic_dist.values,
    labels=[f"Topic {i}" for i in topic_dist.index],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Share of Documents per LDA Topic")
plt.tight_layout()
plt.savefig("p01_topic_distribution.png", dpi=120)
plt.show()

# ---------------------------------------------------------------------------
# STEP 9 — INTERPRET
# ---------------------------------------------------------------------------
print("\n===== INTERPRETATION =====")
print("• Each bar chart shows the 8 most influential words for that topic.")
print("• Higher weight = word is more characteristic of that topic.")
print("• The pie chart shows how evenly tweets spread across topics.")
print("• Apple-related tweets typically split into: product features, customer")
print("  service, comparisons (vs Android), stock/news, and general praise/complaints.")
