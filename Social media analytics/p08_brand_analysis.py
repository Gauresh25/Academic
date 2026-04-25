# =============================================================================
# PRACTICAL 08 — BRAND ANALYSIS
# Dataset : Apple vs Samsung Twitter Sentiment (Kaggle)
#   → search "Apple Samsung Twitter" OR "Brand Sentiment Twitter" on Kaggle
#   → file: apple_samsung_tweets.csv  OR  brand_tweets.csv
#   → Fallback: use "Twitter US Airline Sentiment" Tweets.csv — filter by airline name
# key columns: text/tweet, brand/company (or filter from text itself)
# Goal: compare sentiment, keywords, and engagement between two brands
# =============================================================================

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer

# ---------------------------------------------------------------------------
# STEP 1 — LOAD
# ---------------------------------------------------------------------------
try:
    df = pd.read_csv("apple_samsung_tweets.csv", encoding="utf-8", on_bad_lines="skip")
except Exception:
    try:
        df = pd.read_csv("apple_samsung_tweets.csv", encoding="latin-1", on_bad_lines="skip")
    except Exception:
        # Fallback: use airline dataset, treat "United" and "Delta" as two brands
        df = pd.read_csv("Tweets.csv", encoding="latin-1", on_bad_lines="skip")
        df = df.rename(columns={"airline": "brand", "text": "text"})
        df = df[df["brand"].isin(["United", "Delta"])]
        df["brand"] = df["brand"].str.lower()
        print("Using airline dataset as fallback — brands: United vs Delta")

print("Shape   :", df.shape)
print("Columns :", df.columns.tolist())
print(df.head(3))

# ---------------------------------------------------------------------------
# STEP 2 — IDENTIFY TEXT + BRAND COLUMNS
# ---------------------------------------------------------------------------
TEXT_COL = None
for c in ["text", "tweet", "content", "body", "message"]:
    if c in df.columns:
        TEXT_COL = c; break
if TEXT_COL is None:
    TEXT_COL = df.columns[0]

BRAND_COL = None
for c in ["brand", "company", "airline", "product", "label", "category"]:
    if c in df.columns:
        BRAND_COL = c; break

print(f"\nText column : '{TEXT_COL}' | Brand column : '{BRAND_COL}'")

# ---------------------------------------------------------------------------
# STEP 3 — IF NO BRAND COLUMN: DETECT BRAND FROM TEXT
# ---------------------------------------------------------------------------
# Your friend's tip: if brand column is missing, use keyword detection in text
if BRAND_COL is None:
    print("\nNo brand column found — detecting brand from tweet text using keywords.")
    BRAND_KEYWORDS = {
        "apple":   ["apple", "iphone", "macbook", "ipad", "ios", "appstore", "siri", "imac"],
        "samsung": ["samsung", "galaxy", "android", "exynos", "oneui", "knox", "bixby"]
    }
    def detect_brand(text):
        text_lower = str(text).lower()
        for brand, keywords in BRAND_KEYWORDS.items():
            if any(kw in text_lower for kw in keywords):
                return brand
        return "other"

    df["brand"] = df[TEXT_COL].apply(detect_brand)
    BRAND_COL   = "brand"
    print("Brand distribution:\n", df["brand"].value_counts())
    # Keep only the two main brands
    df = df[df[BRAND_COL].isin(["apple", "samsung"])]
    print(f"Rows after filtering to apple/samsung: {len(df)}")

df[BRAND_COL] = df[BRAND_COL].astype(str).str.lower().str.strip()

# ---------------------------------------------------------------------------
# STEP 4 — CLEAN TEXT
# ---------------------------------------------------------------------------
STOPWORDS = {
    "the","is","in","at","of","and","a","to","for","it","this","that","with",
    "on","are","was","be","as","by","an","or","but","not","from","have","has",
    "he","she","they","we","you","i","my","your","its","their","our","so","if",
    "do","did","get","got","been","will","can","just","about","all","more","also",
    "than","then","now","up","out","when","what","how","amp","rt","via"
}

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#(\w+)", r"\1", text)
    text = re.sub(r"[^a-z\s]", "", text)
    tokens = [w for w in text.split() if w not in STOPWORDS and len(w) > 2]
    return " ".join(tokens)

df["clean_text"] = df[TEXT_COL].apply(clean_text)

# ---------------------------------------------------------------------------
# STEP 5 — SENTIMENT WITH TEXTBLOB
# ---------------------------------------------------------------------------
df["polarity"]  = df["clean_text"].apply(lambda x: TextBlob(x).sentiment.polarity)

def classify(p):
    if p > 0.05:    return "positive"
    elif p < -0.05: return "negative"
    else:           return "neutral"

df["sentiment"] = df["polarity"].apply(classify)

# ---------------------------------------------------------------------------
# STEP 6 — SPLIT INTO BRAND DATAFRAMES
# ---------------------------------------------------------------------------
brands = sorted(df[BRAND_COL].unique())[:2]  # take first two brands alphabetically
b1, b2 = brands[0], brands[1]

df_b1 = df[df[BRAND_COL] == b1]
df_b2 = df[df[BRAND_COL] == b2]
print(f"\n'{b1}' rows: {len(df_b1)}  |  '{b2}' rows: {len(df_b2)}")

# ---------------------------------------------------------------------------
# STEP 7 — VISUALISE: 2 SENTIMENT BAR CHARTS (one per brand — requirement)
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=False)
fig.suptitle(f"Sentiment Comparison: {b1.title()} vs {b2.title()}", fontsize=14)

PALETTE = {"positive": "mediumseagreen", "neutral": "steelblue", "negative": "tomato"}

for ax, brand_df, brand_name in [(axes[0], df_b1, b1), (axes[1], df_b2, b2)]:
    s_counts = brand_df["sentiment"].value_counts()
    bar_colors = [PALETTE.get(s, "gray") for s in s_counts.index]
    bars = ax.bar(s_counts.index, s_counts.values, color=bar_colors, edgecolor="white", width=0.5)
    for bar, val in zip(bars, s_counts.values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max(s_counts) * 0.02,
                str(val), ha="center", fontsize=10)
    ax.set_title(f"{brand_name.title()} Sentiment", fontsize=12)
    ax.set_ylabel("Tweet Count")
    ax.set_ylim(0, s_counts.max() * 1.15)

plt.tight_layout()
plt.savefig("p08_brand_sentiment_bars.png", dpi=120)
plt.show()

# ---------------------------------------------------------------------------
# STEP 8 — COMPARISON: polarity averages + tweet counts
# ---------------------------------------------------------------------------
comparison = pd.DataFrame({
    "brand":         [b1.title(),        b2.title()],
    "tweet_count":   [len(df_b1),        len(df_b2)],
    "avg_polarity":  [df_b1["polarity"].mean(), df_b2["polarity"].mean()],
    "pct_positive":  [(df_b1["sentiment"] == "positive").mean() * 100,
                      (df_b2["sentiment"] == "positive").mean() * 100],
    "pct_negative":  [(df_b1["sentiment"] == "negative").mean() * 100,
                      (df_b2["sentiment"] == "negative").mean() * 100],
})
print("\n===== BRAND COMPARISON TABLE =====\n", comparison.to_string(index=False))

# Side-by-side bar: positive vs negative % per brand
metrics = ["pct_positive", "pct_negative"]
x = np.arange(len(metrics))
width = 0.3

plt.figure(figsize=(8, 5))
plt.bar(x - width/2, comparison.loc[comparison["brand"] == b1.title(), metrics].values.flatten(),
        width, label=b1.title(), color="steelblue", edgecolor="white")
plt.bar(x + width/2, comparison.loc[comparison["brand"] == b2.title(), metrics].values.flatten(),
        width, label=b2.title(), color="coral", edgecolor="white")
plt.xticks(x, ["%Positive", "%Negative"])
plt.title(f"Positive vs Negative % — {b1.title()} vs {b2.title()}", fontsize=12)
plt.ylabel("Percentage (%)")
plt.legend()
plt.tight_layout()
plt.savefig("p08_brand_comparison_bar.png", dpi=120)
plt.show()

# ---------------------------------------------------------------------------
# STEP 9 — TOP KEYWORDS PER BRAND (TF-IDF)
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("Top Keywords by Brand (TF-IDF)", fontsize=13)

for ax, brand_df, brand_name in [(axes[0], df_b1, b1), (axes[1], df_b2, b2)]:
    docs = brand_df["clean_text"].dropna()
    if len(docs) < 5:
        ax.set_title(f"{brand_name.title()} — not enough data")
        continue
    tfidf = TfidfVectorizer(max_features=15, stop_words="english")
    mat   = tfidf.fit_transform(docs)
    scores = pd.Series(
        np.asarray(mat.mean(axis=0)).flatten(),
        index=tfidf.get_feature_names_out()
    ).sort_values(ascending=True).tail(12)
    scores.plot(kind="barh", ax=ax, color="mediumpurple", edgecolor="white")
    ax.set_title(f"{brand_name.title()} — Top Keywords")
    ax.set_xlabel("Mean TF-IDF")

plt.tight_layout()
plt.savefig("p08_brand_keywords.png", dpi=120)
plt.show()

# ---------------------------------------------------------------------------
# STEP 10 — POLARITY OVER TIME (if date column exists)
# ---------------------------------------------------------------------------
DATE_COL = next((c for c in df.columns if c in ["date","created_at","timestamp","datetime"]), None)
if DATE_COL:
    df["parsed_date"] = pd.to_datetime(df[DATE_COL], errors="coerce")
    df_time = df.dropna(subset=["parsed_date"])
    df_time["month"] = df_time["parsed_date"].dt.to_period("M")
    polarity_time = df_time.groupby(["month", BRAND_COL])["polarity"].mean().reset_index()
    pivot = polarity_time.pivot(index="month", columns=BRAND_COL, values="polarity")

    plt.figure(figsize=(11, 4))
    for col in pivot.columns:
        plt.plot([str(m) for m in pivot.index], pivot[col], marker="o", label=col.title())
    plt.title("Average Polarity Over Time by Brand", fontsize=12)
    plt.xlabel("Month"); plt.ylabel("Avg Polarity")
    plt.xticks(rotation=45, ha="right")
    plt.legend(); plt.tight_layout()
    plt.savefig("p08_brand_polarity_over_time.png", dpi=120)
    plt.show()

# ---------------------------------------------------------------------------
# STEP 11 — INTERPRET
# ---------------------------------------------------------------------------
print("\n===== INTERPRETATION =====")
for _, row in comparison.iterrows():
    print(f"\n{row['brand']}:")
    print(f"  Tweets: {row['tweet_count']}  |  Avg polarity: {row['avg_polarity']:.3f}")
    print(f"  Positive: {row['pct_positive']:.1f}%  |  Negative: {row['pct_negative']:.1f}%")
print("\n• Brand with more positive tweets has stronger social media reception.")
print("• Keyword differences reveal what users talk about per brand (features vs. issues).")
print("• If one brand has significantly higher negative %, it may indicate PR/product issues.")
