# =============================================================================
# PRACTICAL 07 — EXPLORATORY DATA ANALYSIS (EDA)
# Dataset : Spotify Tracks Dataset (Kaggle) — rich numeric + categorical columns
#   → search "Spotify Tracks Dataset" OR "Spotify 1 million tracks" on Kaggle
#   → file: tracks.csv  OR  SpotifyFeatures.csv
#   → key columns: popularity, danceability, energy, genre, duration_ms, etc.
# Required charts: BAR, BOX, SCATTER, PIE  (min 4 distinct types)
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------------------------
# STEP 1 — LOAD
# ---------------------------------------------------------------------------
try:
    df = pd.read_csv("SpotifyFeatures.csv", encoding="utf-8", on_bad_lines="skip")
except Exception:
    df = pd.read_csv("SpotifyFeatures.csv", encoding="latin-1", on_bad_lines="skip")

print("Shape   :", df.shape)
print("Columns :", df.columns.tolist())
print("\n--- df.head() ---")
print(df.head(3))

# ---------------------------------------------------------------------------
# STEP 2 — BASIC INFO (always show this to examiner first)
# ---------------------------------------------------------------------------
print("\n--- df.info() ---")
df.info()

print("\n--- Null counts ---")
print(df.isnull().sum())

print("\n--- df.describe() ---")
print(df.select_dtypes(include="number").describe().round(2))

# ---------------------------------------------------------------------------
# STEP 3 — CLEAN
# ---------------------------------------------------------------------------
# Drop full duplicates
before = len(df)
df = df.drop_duplicates()
print(f"\nDuplicates removed: {before - len(df)}")

# Drop rows missing key columns (adjust to what's in your dataset)
KEY_COLS = [c for c in ["popularity", "genre", "danceability", "energy"] if c in df.columns]
df = df.dropna(subset=KEY_COLS)
print(f"Rows after dropping nulls in key columns: {len(df)}")

# ---------------------------------------------------------------------------
# CHART 1 — BAR CHART: top genres or top categories
# ---------------------------------------------------------------------------
# Find a sensible categorical column
CAT_COL = None
for candidate in ["genre", "track_genre", "playlist_genre", "artist_name", "category"]:
    if candidate in df.columns and df[candidate].nunique() <= 50:
        CAT_COL = candidate
        break

plt.figure(figsize=(11, 5))
if CAT_COL:
    genre_counts = df[CAT_COL].value_counts().head(15)
    bars = plt.bar(genre_counts.index, genre_counts.values,
                   color=plt.cm.tab20.colors[:len(genre_counts)], edgecolor="white")
    for bar, val in zip(bars, genre_counts.values):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max(genre_counts) * 0.01,
                 str(val), ha="center", fontsize=8)
    plt.title(f"Top 15 {CAT_COL.replace('_',' ').title()} by Track Count", fontsize=13)
    plt.xlabel(CAT_COL)
else:
    # Fallback: histogram as bar for a numeric column
    num_col = df.select_dtypes(include="number").columns[0]
    df[num_col].value_counts().head(15).plot(kind="bar")
    plt.title(f"Top values in '{num_col}'", fontsize=12)

plt.ylabel("Count")
plt.xticks(rotation=40, ha="right")
plt.tight_layout()
plt.savefig("p07_eda_bar.png", dpi=120)
plt.show()
print("\n[BAR CHART] Shows distribution of tracks across genres/categories.")

# ---------------------------------------------------------------------------
# CHART 2 — BOX PLOT: popularity spread across top genres
# ---------------------------------------------------------------------------
NUM_COL = None
for candidate in ["popularity", "danceability", "energy", "valence", "tempo"]:
    if candidate in df.columns:
        NUM_COL = candidate
        break
if NUM_COL is None:
    NUM_COL = df.select_dtypes(include="number").columns[0]

plt.figure(figsize=(12, 5))
if CAT_COL:
    # Only top N genres (too many groups make the plot unreadable)
    top_cats = df[CAT_COL].value_counts().head(10).index
    df_box   = df[df[CAT_COL].isin(top_cats)]
    sns.boxplot(data=df_box, x=CAT_COL, y=NUM_COL, palette="Set3")
    plt.title(f"{NUM_COL.title()} Distribution by {CAT_COL.replace('_',' ').title()}", fontsize=13)
    plt.xticks(rotation=30, ha="right")
else:
    sns.boxplot(y=df[NUM_COL], color="steelblue")
    plt.title(f"Box Plot of {NUM_COL.title()}", fontsize=13)

plt.tight_layout()
plt.savefig("p07_eda_boxplot.png", dpi=120)
plt.show()
print(f"[BOX CHART] Shows median, IQR and outliers in '{NUM_COL}' across groups.")

# ---------------------------------------------------------------------------
# CHART 3 — SCATTER PLOT: two numeric columns
# ---------------------------------------------------------------------------
# Find two numeric columns that are likely correlated
NUM_COLS = df.select_dtypes(include="number").columns.tolist()
x_col = "danceability" if "danceability" in NUM_COLS else NUM_COLS[0]
y_col = "energy"       if "energy"       in NUM_COLS else (NUM_COLS[1] if len(NUM_COLS) > 1 else NUM_COLS[0])

# Sample to avoid over-plotting
sample = df.sample(min(2000, len(df)), random_state=42)

plt.figure(figsize=(8, 5))
scatter = plt.scatter(sample[x_col], sample[y_col],
                      alpha=0.3, s=10, c=sample[NUM_COL] if NUM_COL in NUM_COLS else "steelblue",
                      cmap="viridis")
if NUM_COL in NUM_COLS:
    plt.colorbar(scatter, label=NUM_COL)

corr_val = df[x_col].corr(df[y_col])
plt.title(f"{x_col.title()} vs {y_col.title()}  (r = {corr_val:.2f})", fontsize=12)
plt.xlabel(x_col.title())
plt.ylabel(y_col.title())
plt.tight_layout()
plt.savefig("p07_eda_scatter.png", dpi=120)
plt.show()
print(f"[SCATTER] Correlation between '{x_col}' and '{y_col}': r = {corr_val:.2f}")

# ---------------------------------------------------------------------------
# CHART 4 — PIE CHART: share of tracks per top genre (or category)
# ---------------------------------------------------------------------------
plt.figure(figsize=(7, 7))
if CAT_COL:
    top8      = df[CAT_COL].value_counts().head(8)
    other_sum = df[CAT_COL].value_counts().iloc[8:].sum()
    pie_vals  = list(top8.values) + [other_sum]
    pie_lbls  = list(top8.index)  + ["Other"]
else:
    # Fallback: split numeric column into quartiles
    bins_col  = pd.cut(df[NUM_COL], bins=4, labels=["Low", "Medium-Low", "Medium-High", "High"])
    pie_vals  = bins_col.value_counts().values
    pie_lbls  = bins_col.value_counts().index.tolist()
    other_sum = 0

plt.pie(pie_vals, labels=pie_lbls, autopct="%1.1f%%", startangle=140)
plt.title(f"Share of Tracks by {CAT_COL if CAT_COL else NUM_COL}", fontsize=12)
plt.tight_layout()
plt.savefig("p07_eda_pie.png", dpi=120)
plt.show()
print("[PIE CHART] Shows proportional dominance of each genre/category.")

# ---------------------------------------------------------------------------
# BONUS CHART 5 — HEATMAP: numeric feature correlations
# ---------------------------------------------------------------------------
corr_cols = [c for c in ["popularity","danceability","energy","valence","tempo",
                          "acousticness","instrumentalness","speechiness","loudness"]
             if c in df.columns]
if len(corr_cols) >= 3:
    plt.figure(figsize=(9, 7))
    sns.heatmap(df[corr_cols].corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Heatmap of Audio Features", fontsize=12)
    plt.tight_layout()
    plt.savefig("p07_eda_heatmap.png", dpi=120)
    plt.show()
    print("[HEATMAP] Red = strong positive correlation, Blue = negative correlation.")

# ---------------------------------------------------------------------------
# STEP 4 — SUMMARY STATISTICS TABLE
# ---------------------------------------------------------------------------
print("\n===== EDA SUMMARY =====")
print(f"Dataset shape          : {df.shape}")
print(f"Numeric columns        : {df.select_dtypes(include='number').columns.tolist()}")
print(f"Categorical columns    : {df.select_dtypes(include='object').columns.tolist()}")
if CAT_COL:
    print(f"Most common {CAT_COL}  : {df[CAT_COL].value_counts().idxmax()}")
if NUM_COL:
    print(f"'{NUM_COL}' mean     : {df[NUM_COL].mean():.2f}")
    print(f"'{NUM_COL}' median   : {df[NUM_COL].median():.2f}")
    print(f"'{NUM_COL}' std      : {df[NUM_COL].std():.2f}")

print("\n===== INTERPRETATION =====")
print("• Bar chart reveals which genre/category has the most representation in the dataset.")
print("• Box plot shows median and outliers — genres with wide boxes have high variability.")
print("• Scatter reveals whether two features move together (e.g. danceable = more energetic).")
print("• Pie shows proportional dominance — one or two genres often dominate streaming datasets.")
print("• Heatmap lets you quickly see multi-feature correlations; useful for feature selection.")
