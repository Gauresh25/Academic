# =============================================================================
# PRACTICAL 02 — LOCATION ANALYSIS
# Dataset : Tweets with Locations (multiple options work)
#   Option A → "Twitter US Airline Sentiment" — has 'tweet_coord', 'tweet_location'
#              search: "Twitter US Airline Sentiment" on Kaggle
#              file: Tweets.csv
#   Option B → "COVID-19 Twitter Dataset" — has user_location
#              search: "covid19 tweets" on Kaggle
# Key columns used: tweet_location  (or user_location / location)
# =============================================================================

import re
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ---------------------------------------------------------------------------
# STEP 1 — LOAD  (handles both common encoding issues)
# ---------------------------------------------------------------------------
try:
    df = pd.read_csv("Tweets.csv", encoding="utf-8", on_bad_lines="skip")
except Exception:
    df = pd.read_csv("Tweets.csv", encoding="latin-1", on_bad_lines="skip")

print("Shape   :", df.shape)
print("Columns :", df.columns.tolist())
print(df.head(3))
print("\nNull counts:\n", df.isnull().sum())

# ---------------------------------------------------------------------------
# STEP 2 — FIND LOCATION COLUMN
# ---------------------------------------------------------------------------
# Datasets name it differently — scan for common names
LOC_COL = None
for candidate in ["tweet_location", "user_location", "location", "place", "geo", "country"]:
    if candidate in df.columns:
        LOC_COL = candidate
        break
if LOC_COL is None:
    print("No location column found — available columns:", df.columns.tolist())
    raise SystemExit("Please set LOC_COL manually above.")
print(f"\nUsing location column: '{LOC_COL}'")

# ---------------------------------------------------------------------------
# STEP 3 — CLEAN LOCATION COLUMN
# ---------------------------------------------------------------------------
# Normalise case, strip whitespace, drop blanks and literal 'nan' strings
df["location_clean"] = (
    df[LOC_COL]
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace(r"\s+", " ", regex=True)   # collapse multiple spaces
)

# Remove clearly useless entries
df = df[~df["location_clean"].isin(["nan", "none", "", "null", "n/a", "na"])]
print(f"\nRows with valid location: {len(df)}")

# ---------------------------------------------------------------------------
# STEP 4 — COUNT LOCATIONS
# ---------------------------------------------------------------------------
top_locations = df["location_clean"].value_counts()
print(f"\nUnique locations: {len(top_locations)}")
print("\nTop 20 locations:\n", top_locations.head(20))

# ---------------------------------------------------------------------------
# STEP 5 — VISUALISE: horizontal bar chart (top 15)
# ---------------------------------------------------------------------------
top15 = top_locations.head(15)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(top15.index[::-1], top15.values[::-1], color="cornflowerblue", edgecolor="white")

# Annotate each bar with its count value

ax.set_xlabel("Number of Tweets", fontsize=11)
ax.set_title("Top 15 Locations by Tweet Count", fontsize=13)
ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
plt.tight_layout()
plt.savefig("p02_top_locations_bar.png", dpi=120)
plt.show()

# ---------------------------------------------------------------------------
# STEP 6 — VISUALISE: pie chart (top 8 + others bucket)
# ---------------------------------------------------------------------------
top8  = top_locations.head(8)
other = top_locations.iloc[8:].sum()
pie_data   = list(top8.values) + [other]
pie_labels = list(top8.index)  + ["other"]

plt.figure(figsize=(7, 7))
plt.pie(
    pie_data,
    labels=pie_labels,

)
plt.title("Location Distribution (top 8 + other)", fontsize=12)
plt.tight_layout()
plt.savefig("p02_location_pie.png", dpi=120)
plt.show()

# ---------------------------------------------------------------------------
# STEP 7 — OPTIONAL: tweet volume per country-level keyword
# ---------------------------------------------------------------------------
# Many user locations contain a country name buried in free text.
# This extracts simple country mentions for a cleaner macro view.
COUNTRIES = ["usa", "united states", "uk", "united kingdom", "india", "canada",
             "australia", "germany", "france", "brazil", "nigeria", "pakistan"]

def extract_country(loc):
    for c in COUNTRIES:
        if c in loc:
            return c
    return "other"

df["country"] = df["location_clean"].apply(extract_country)
country_counts = df["country"].value_counts()

plt.figure(figsize=(8, 4))
country_counts.plot(kind="bar", color="teal", edgecolor="white")
plt.title("Tweets by Country (keyword match)", fontsize=12)
plt.xlabel("Country")
plt.ylabel("Tweet Count")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("p02_country_bar.png", dpi=120)
plt.show()

# ---------------------------------------------------------------------------
# STEP 8 — INTERPRET
# ---------------------------------------------------------------------------
print("\n===== INTERPRETATION =====")
print(f"• Total tweets with valid location data : {len(df)}")
print(f"• Most active location  : {top_locations.index[0]} ({top_locations.iloc[0]} tweets)")
print(f"• Unique location strings: {len(top_locations)}")
print("• Location data is user-entered (free text) so many variations exist.")
print("• The country-level grouping reduces noise and shows macro-geographic trends.")
print("• US dominates Twitter location data in most English-language datasets.")
