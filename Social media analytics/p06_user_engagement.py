# =============================================================================
# PRACTICAL 06 — USER ENGAGEMENT ANALYSIS
# Dataset : Instagram Reach / Engagement Dataset (Kaggle)
#   → search "Instagram Influencer dataset" OR "Social Media Influencers" on Kaggle
#   → file: instagram_data.csv  OR  social_media_influencers_2022.csv
#   → key columns: likes, comments, shares (or saves), followers, post_type / content_type
# Goal: find what types of content drive the most engagement
# =============================================================================

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------------------------
# STEP 1 — LOAD
# ---------------------------------------------------------------------------
try:
    df = pd.read_csv("instagram_data.csv", encoding="utf-8", on_bad_lines="skip")
except Exception:
    df = pd.read_csv("instagram_data.csv", encoding="latin-1", on_bad_lines="skip")

print("Shape   :", df.shape)
print("Columns :", df.columns.tolist())
print(df.head(3))
print("\nNull counts:\n", df.isnull().sum())
print("\nData types:\n", df.dtypes)

# ---------------------------------------------------------------------------
# STEP 2 — IDENTIFY ENGAGEMENT COLUMNS
# ---------------------------------------------------------------------------
# These are the columns we will sum to get total engagement
POSSIBLE_ENG = ["likes", "comments", "shares", "saves", "retweets",
                "reactions", "impressions", "reach", "plays", "views"]

eng_cols = [c for c in POSSIBLE_ENG if c in df.columns]
print(f"\nEngagement columns found: {eng_cols}")

if not eng_cols:
    print("No standard engagement columns found. Columns:", df.columns.tolist())
    raise SystemExit("Map your column names to the POSSIBLE_ENG list above.")

# ---------------------------------------------------------------------------
# STEP 3 — CLEAN NUMERIC COLUMNS
# ---------------------------------------------------------------------------
# Social media data often stores numbers as strings: "1.2K", "3,400"
def parse_numeric(val):
    """Converts '1.2K', '3,400', or plain numbers to float."""
    s = str(val).strip().replace(",", "").lower()
    if s in ["nan", "none", ""]:
        return np.nan
    if s.endswith("k"):
        return float(s[:-1]) * 1_000
    if s.endswith("m"):
        return float(s[:-1]) * 1_000_000
    try:
        return float(s)
    except ValueError:
        return np.nan

for col in eng_cols:
    df[col] = df[col].apply(parse_numeric)

# Fill NaN engagement values with 0 before summing
df[eng_cols] = df[eng_cols].fillna(0)

# ---------------------------------------------------------------------------
# STEP 4 — COMPUTE TOTAL ENGAGEMENT
# ---------------------------------------------------------------------------
df["total_engagement"] = df[eng_cols].sum(axis=1)

# Engagement Rate = total engagement / followers (if followers column exists)
if "followers" in df.columns:
    df["followers"] = df["followers"].apply(parse_numeric)
    df["engagement_rate"] = df.apply(
        lambda r: r["total_engagement"] / r["followers"] * 100 if r["followers"] > 0 else 0,
        axis=1
    )
    print("\nEngagement rate stats:\n", df["engagement_rate"].describe())

print("\nTotal engagement stats:\n", df["total_engagement"].describe())

# ---------------------------------------------------------------------------
# STEP 5 — TOP ENGAGING CONTENT / USERS
# ---------------------------------------------------------------------------
# Check what grouping column exists
GROUP_COL = None
for candidate in ["content_type", "post_type", "category", "type",
                  "username", "influencer_name", "account"]:
    if candidate in df.columns:
        GROUP_COL = candidate
        break

if GROUP_COL:
    print(f"\nGrouping by: '{GROUP_COL}'")
    grouped = df.groupby(GROUP_COL)["total_engagement"].agg(["mean", "sum", "count"])
    grouped.columns = ["avg_engagement", "total_engagement", "post_count"]
    grouped = grouped.sort_values("avg_engagement", ascending=False)
    print(grouped)
else:
    print("\nNo content type column found — grouping by index buckets instead.")

# ---------------------------------------------------------------------------
# STEP 6 — VISUALISE: 4-panel engagement dashboard
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("User Engagement Analysis — Instagram/Social Media", fontsize=14)

# Panel A — Distribution of total engagement (log scale handles outliers)
axes[0, 0].hist(df["total_engagement"].clip(upper=df["total_engagement"].quantile(0.99)),
                bins=40, color="steelblue", edgecolor="white")
axes[0, 0].set_title("Engagement Distribution (clipped at 99th pct)")
axes[0, 0].set_xlabel("Total Engagement")
axes[0, 0].set_ylabel("Frequency")

# Panel B — Box plot per group (if GROUP_COL exists)
if GROUP_COL and df[GROUP_COL].nunique() <= 15:
    df_plot = df[df["total_engagement"] < df["total_engagement"].quantile(0.99)]
    sns.boxplot(data=df_plot, x=GROUP_COL, y="total_engagement", ax=axes[0, 1], palette="Set2")
    axes[0, 1].set_title(f"Engagement by {GROUP_COL}")
    axes[0, 1].tick_params(axis="x", rotation=30)
else:
    # Fallback: box plot of likes vs comments
    if "likes" in df.columns and "comments" in df.columns:
        axes[0, 1].boxplot([df["likes"].dropna(), df["comments"].dropna()],
                           labels=["likes", "comments"], patch_artist=True)
        axes[0, 1].set_title("Likes vs Comments Distribution")
    axes[0, 1].set_ylabel("Count")

# Panel C — Bar chart: average engagement per group
if GROUP_COL:
    avg_eng = df.groupby(GROUP_COL)["total_engagement"].mean().sort_values(ascending=False).head(10)
    avg_eng[::-1].plot(kind="barh", ax=axes[1, 0], color="mediumseagreen", edgecolor="white")
    axes[1, 0].set_title(f"Avg Engagement by {GROUP_COL}")
    axes[1, 0].set_xlabel("Average Total Engagement")
else:
    df["total_engagement"].sort_values(ascending=False).head(10).plot(
        kind="bar", ax=axes[1, 0], color="mediumseagreen")
    axes[1, 0].set_title("Top 10 Posts by Engagement")

# Panel D — Scatter: followers vs engagement (if available)
if "followers" in df.columns:
    sample = df.sample(min(500, len(df)), random_state=42)
    axes[1, 1].scatter(sample["followers"], sample["total_engagement"],
                       alpha=0.4, s=15, color="coral")
    axes[1, 1].set_title("Followers vs Total Engagement")
    axes[1, 1].set_xlabel("Followers")
    axes[1, 1].set_ylabel("Total Engagement")
    # Add correlation note
    corr = df["followers"].corr(df["total_engagement"])
    axes[1, 1].text(0.05, 0.92, f"r = {corr:.2f}", transform=axes[1, 1].transAxes, fontsize=10)
else:
    # Fallback scatter: likes vs comments
    if "likes" in df.columns and "comments" in df.columns:
        sample = df.sample(min(500, len(df)), random_state=42)
        axes[1, 1].scatter(sample["likes"], sample["comments"], alpha=0.4, s=10, color="coral")
        axes[1, 1].set_title("Likes vs Comments (scatter)")
        axes[1, 1].set_xlabel("Likes")
        axes[1, 1].set_ylabel("Comments")

plt.tight_layout()
plt.savefig("p06_engagement_dashboard.png", dpi=120)
plt.show()

# ---------------------------------------------------------------------------
# STEP 7 — CORRELATION HEATMAP OF ENGAGEMENT METRICS
# ---------------------------------------------------------------------------
numeric_eng = df[eng_cols + ["total_engagement"]].select_dtypes(include="number")
if numeric_eng.shape[1] >= 2:
    plt.figure(figsize=(8, 6))
    sns.heatmap(numeric_eng.corr(), annot=True, fmt=".2f", cmap="Blues", linewidths=0.5)
    plt.title("Correlation Between Engagement Metrics", fontsize=12)
    plt.tight_layout()
    plt.savefig("p06_engagement_heatmap.png", dpi=120)
    plt.show()

# ---------------------------------------------------------------------------
# STEP 8 — PIE: share of total engagement by content type
# ---------------------------------------------------------------------------
if GROUP_COL:
    pie_data = df.groupby(GROUP_COL)["total_engagement"].sum().sort_values(ascending=False)
    if len(pie_data) <= 10:
        plt.figure(figsize=(7, 7))
        plt.pie(pie_data.values, labels=pie_data.index, autopct="%1.1f%%", startangle=90)
        plt.title(f"Share of Total Engagement by {GROUP_COL}", fontsize=12)
        plt.tight_layout()
        plt.savefig("p06_engagement_pie.png", dpi=120)
        plt.show()

# ---------------------------------------------------------------------------
# STEP 9 — INTERPRET
# ---------------------------------------------------------------------------
print("\n===== INTERPRETATION =====")
print(f"• Total posts analysed         : {len(df):,}")
print(f"• Mean total engagement / post : {df['total_engagement'].mean():.0f}")
print(f"• Median total engagement      : {df['total_engagement'].median():.0f}")
print(f"• Engagement skew              : {df['total_engagement'].skew():.2f} (positive = few viral posts dominate)")
if GROUP_COL:
    best_group = df.groupby(GROUP_COL)["total_engagement"].mean().idxmax()
    print(f"• Highest avg engagement type  : {best_group}")
print("• Scatter plot shows whether more followers always means more engagement.")
print("• High r (>0.7) = follower count drives engagement; low r = content quality matters more.")
