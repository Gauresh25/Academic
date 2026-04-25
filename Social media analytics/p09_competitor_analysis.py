# =============================================================================
# PRACTICAL 09 — COMPETITOR ANALYSIS
# Dataset : Social Media Influencers / Brand Tweets (same as Brand Analysis)
#   → Use apple_samsung_tweets.csv  OR  Tweets.csv (airline: UA vs Delta vs Southwest)
#   → Or search "competitor analysis social media" on Kaggle
# Goal: compare multiple brands/competitors across:
#   post volume, sentiment, engagement, keyword strategy
# =============================================================================

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer

# ---------------------------------------------------------------------------
# STEP 1 — LOAD
# ---------------------------------------------------------------------------
try:
    df = pd.read_csv("Tweets.csv", encoding="utf-8", on_bad_lines="skip")
except Exception:
    df = pd.read_csv("Tweets.csv", encoding="latin-1", on_bad_lines="skip")

print("Shape   :", df.shape)
print("Columns :", df.columns.tolist())
print(df.head(2))

# ---------------------------------------------------------------------------
# STEP 2 — IDENTIFY BRAND + TEXT COLUMNS
# ---------------------------------------------------------------------------
TEXT_COL  = next((c for c in ["text","tweet","content","body","message"] if c in df.columns), df.columns[0])
BRAND_COL = next((c for c in ["airline","brand","company","product","label"] if c in df.columns), None)

print(f"\nText: '{TEXT_COL}' | Brand/Competitor: '{BRAND_COL}'")

# ---------------------------------------------------------------------------
# STEP 3 — SELECT COMPETITORS TO COMPARE (pick top 3–4)
# ---------------------------------------------------------------------------
if BRAND_COL:
    brand_counts = df[BRAND_COL].value_counts()
    COMPETITORS  = brand_counts.head(4).index.tolist()  # top 4 by volume
    df = df[df[BRAND_COL].isin(COMPETITORS)]
    print(f"\nCompetitors selected: {COMPETITORS}")
    print(df[BRAND_COL].value_counts())
else:
    # Detect from text using keyword approach
    BRAND_KEYWORDS = {
        "apple":   ["apple", "iphone", "ipad", "ios", "macbook"],
        "samsung": ["samsung", "galaxy", "oneui", "exynos"],
        "google":  ["google", "pixel", "android", "chromebook"],
        "microsoft":["microsoft", "windows", "xbox", "surface"]
    }
    def detect_brand(text):
        text_lower = str(text).lower()
        for brand, kws in BRAND_KEYWORDS.items():
            if any(k in text_lower for k in kws):
                return brand
        return None
    df["brand"]   = df[TEXT_COL].apply(detect_brand)
    BRAND_COL     = "brand"
    df            = df.dropna(subset=["brand"])
    COMPETITORS   = df["brand"].value_counts().head(4).index.tolist()
    df            = df[df["brand"].isin(COMPETITORS)]
    print(f"\nDetected competitors: {COMPETITORS}")

# Normalise brand names
df[BRAND_COL] = df[BRAND_COL].astype(str).str.strip().str.title()
COMPETITORS   = [c.title() for c in COMPETITORS]

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
    return " ".join(w for w in text.split() if w not in STOPWORDS and len(w) > 2)

df["clean_text"] = df[TEXT_COL].apply(clean_text)

# ---------------------------------------------------------------------------
# STEP 5 — SENTIMENT
# ---------------------------------------------------------------------------
df["polarity"] = df["clean_text"].apply(lambda x: TextBlob(x).sentiment.polarity)

def classify(p):
    return "positive" if p > 0.05 else ("negative" if p < -0.05 else "neutral")

df["sentiment"] = df["polarity"].apply(classify)

# ---------------------------------------------------------------------------
# STEP 6 — COMPUTE COMPETITOR METRICS TABLE
# ---------------------------------------------------------------------------
metrics = []
for comp in COMPETITORS:
    subset = df[df[BRAND_COL] == comp]
    metrics.append({
        "brand":        comp,
        "post_count":   len(subset),
        "avg_polarity": round(subset["polarity"].mean(), 3),
        "pct_positive": round((subset["sentiment"] == "positive").mean() * 100, 1),
        "pct_negative": round((subset["sentiment"] == "negative").mean() * 100, 1),
        "pct_neutral":  round((subset["sentiment"] == "neutral").mean()  * 100, 1),
    })

metrics_df = pd.DataFrame(metrics).set_index("brand")
print("\n===== COMPETITOR METRICS =====\n", metrics_df.to_string())

# ---------------------------------------------------------------------------
# STEP 7 — VISUALISE: 4-panel comparison figure
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 10))
fig.suptitle("Competitor Analysis — Social Media Comparison", fontsize=14)

# Panel A — Post Volume Bar (how much each brand is talked about)
axes[0, 0].bar(metrics_df.index, metrics_df["post_count"],
               color=plt.cm.Set2.colors[:len(COMPETITORS)], edgecolor="white")
axes[0, 0].set_title("Post Volume per Competitor")
axes[0, 0].set_ylabel("Number of Posts")
axes[0, 0].tick_params(axis="x", rotation=20)

# Panel B — Average Polarity comparison
colors_pol = ["mediumseagreen" if v >= 0 else "tomato" for v in metrics_df["avg_polarity"]]
axes[0, 1].bar(metrics_df.index, metrics_df["avg_polarity"],
               color=colors_pol, edgecolor="white")
axes[0, 1].axhline(0, color="black", linewidth=0.8, linestyle="--")
axes[0, 1].set_title("Average Sentiment Polarity")
axes[0, 1].set_ylabel("Polarity (-1 to +1)")
axes[0, 1].tick_params(axis="x", rotation=20)

# Panel C — Stacked bar: positive / neutral / negative %
x = np.arange(len(COMPETITORS))
width = 0.5
axes[1, 0].bar(x, metrics_df["pct_positive"], width, label="Positive",  color="mediumseagreen")
axes[1, 0].bar(x, metrics_df["pct_neutral"],  width, label="Neutral",   color="steelblue",
               bottom=metrics_df["pct_positive"])
axes[1, 0].bar(x, metrics_df["pct_negative"], width, label="Negative",  color="tomato",
               bottom=metrics_df["pct_positive"] + metrics_df["pct_neutral"])
axes[1, 0].set_xticks(x); axes[1, 0].set_xticklabels(COMPETITORS, rotation=20)
axes[1, 0].set_title("Sentiment Mix per Competitor (stacked %)")
axes[1, 0].set_ylabel("Percentage (%)")
axes[1, 0].legend(loc="upper right", fontsize=8)

# Panel D — Box plot of polarity distribution per competitor
comp_subsets = [df[df[BRAND_COL] == c]["polarity"].values for c in COMPETITORS]
bp = axes[1, 1].boxplot(comp_subsets, patch_artist=True, labels=COMPETITORS)
colors_box = plt.cm.Set2.colors[:len(COMPETITORS)]
for patch, color in zip(bp["boxes"], colors_box):
    patch.set_facecolor(color)
axes[1, 1].set_title("Polarity Distribution (box plot)")
axes[1, 1].set_ylabel("Polarity")
axes[1, 1].axhline(0, color="red", linestyle="--", linewidth=0.8)
axes[1, 1].tick_params(axis="x", rotation=20)

plt.tight_layout()
plt.savefig("p09_competitor_comparison.png", dpi=120)
plt.show()

# ---------------------------------------------------------------------------
# STEP 8 — TOP KEYWORDS PER COMPETITOR
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(1, len(COMPETITORS), figsize=(5 * len(COMPETITORS), 5))
if len(COMPETITORS) == 1:
    axes = [axes]
fig.suptitle("Top Keywords per Competitor", fontsize=13)

for ax, comp in zip(axes, COMPETITORS):
    docs = df[df[BRAND_COL] == comp]["clean_text"].dropna()
    if len(docs) < 5:
        ax.set_title(f"{comp} — not enough data"); continue
    tv = TfidfVectorizer(max_features=12, stop_words="english")
    mat = tv.fit_transform(docs)
    scores = pd.Series(np.asarray(mat.mean(axis=0)).flatten(),
                       index=tv.get_feature_names_out()).sort_values(ascending=True)
    scores.plot(kind="barh", ax=ax, color="mediumpurple", edgecolor="white")
    ax.set_title(comp)
    ax.set_xlabel("TF-IDF")

plt.tight_layout()
plt.savefig("p09_competitor_keywords.png", dpi=120)
plt.show()

# ---------------------------------------------------------------------------
# STEP 9 — INTERPRET
# ---------------------------------------------------------------------------
print("\n===== INTERPRETATION =====")
leader = metrics_df["post_count"].idxmax()
most_pos = metrics_df["pct_positive"].idxmax()
least_neg = metrics_df["pct_negative"].idxmin()
print(f"• Brand talked about most     : {leader} ({int(metrics_df.loc[leader,'post_count'])} posts)")
print(f"• Brand with most positive %  : {most_pos} ({metrics_df.loc[most_pos,'pct_positive']:.1f}%)")
print(f"• Brand with least negative % : {least_neg} ({metrics_df.loc[least_neg,'pct_negative']:.1f}%)")
print("• High post volume = high brand awareness; does not equal positive reception.")
print("• Stacked bar exposes which brand has the healthiest sentiment mix.")
print("• Keyword analysis shows whether competitors are known for features, issues, or events.")
