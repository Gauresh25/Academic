# =============================================================================
# DATASET DOWNLOAD REFERENCE — SMA PRACTICAL EXAM 2026
# Download ALL of these before the exam and keep them on a USB drive.
# Each file name below is what the Python scripts expect — rename after downloading.
# =============================================================================

DATASETS = {

    # -------------------------------------------------------------------------
    # PRIMARY: covers practicals 01, 04, 05, 08, 09
    # "Twitter US Airline Sentiment" — Kaggle
    # URL: https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment
    # File to download: Tweets.csv
    # Columns: text, airline, airline_sentiment, retweet_count, tweet_location
    # Why useful: has text + brand (airline) + location + sentiment labels + retweet counts
    #   → use for: sentiment, hashtag, brand, competitor, location
    "Tweets.csv": {
        "practicals": [4, 5, 8, 9, 2],
        "columns": ["text", "airline", "airline_sentiment", "tweet_location", "retweet_count"],
        "kaggle_search": "Twitter US Airline Sentiment",
    },

    # -------------------------------------------------------------------------
    # PRACTICAL 01 / 08 — Apple Twitter + Brand
    # "Apple Twitter Sentiment" — Kaggle
    # URL: https://www.kaggle.com/datasets/seriousran/appletwittersentimenttexts
    # File: apple-twitter-sentiment-texts.csv
    # Columns: text, sentiment
    "apple-twitter-sentiment-texts.csv": {
        "practicals": [1, 8],
        "columns": ["text", "sentiment"],
        "kaggle_search": "Apple Twitter Sentiment texts",
    },

    # -------------------------------------------------------------------------
    # PRACTICAL 03 — Trend Analysis (Ukraine War)
    # "Ukraine Conflict Twitter Dataset" — Kaggle
    # URL: https://www.kaggle.com/datasets/bwandowando/ukraine-russian-crisis-twitter-dataset-1-2-m-rows
    # File: UkraineTwitter.csv  (or similar)
    # Columns: date, text, hashtags, likes, retweet_count, user_location
    "UkraineTwitter.csv": {
        "practicals": [3],
        "columns": ["date", "text", "likes", "retweet_count"],
        "kaggle_search": "Ukraine Russia Twitter Crisis",
    },

    # -------------------------------------------------------------------------
    # PRACTICAL 06 — User Engagement (Instagram)
    # "Social Media Influencers" — Kaggle
    # URL: https://www.kaggle.com/datasets/ramjasmaurya/top-1000-social-media-channels
    # File: social media influencers - instagram sep 2022.csv
    # Columns: Followers, Avg. Likes, Posts, channel_info (category)
    "instagram_data.csv": {
        "practicals": [6],
        "columns": ["Followers", "Avg. Likes", "Posts", "channel_info"],
        "kaggle_search": "Top 1000 Social Media Influencers",
        "note": "Rename the downloaded file to instagram_data.csv"
    },

    # -------------------------------------------------------------------------
    # PRACTICAL 07 — EDA
    # "Spotify Tracks Dataset" — Kaggle
    # URL: https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset
    # File: dataset.csv  → rename to SpotifyFeatures.csv
    # Columns: track_genre, popularity, danceability, energy, valence, tempo, etc.
    "SpotifyFeatures.csv": {
        "practicals": [7],
        "columns": ["track_genre", "popularity", "danceability", "energy", "valence", "tempo"],
        "kaggle_search": "Spotify Tracks Dataset maharshipandya",
        "note": "Rename dataset.csv → SpotifyFeatures.csv"
    },

    # -------------------------------------------------------------------------
    # PRACTICAL 10 — Network Analysis
    # OPTION A: Same Tweets.csv from airline sentiment (use @mention graph)
    # OPTION B: SNAP Twitter Ego Network (edge list)
    # URL: https://snap.stanford.edu/data/ego-Twitter.html
    # File: twitter_combined.txt  (edge list: each line = "node1 node2")
    "twitter_combined.txt": {
        "practicals": [10],
        "columns": ["source_node", "target_node"],
        "source": "SNAP Stanford (snap.stanford.edu/data/ego-Twitter.html)",
        "note": "Optional — Tweets.csv also works for network practical"
    },
}

# =============================================================================
# COLUMN NAME CHEATSHEET — what to expect per dataset
# =============================================================================
COLUMN_MAP = {
    "Tweets.csv": {
        "text_col":    "text",
        "brand_col":   "airline",
        "location_col":"tweet_location",
        "sentiment_col":"airline_sentiment",
        "date_col":    "tweet_created",
        "likes_col":   "retweet_count",   # no direct 'likes', use retweets
    },
    "apple-twitter-sentiment-texts.csv": {
        "text_col":    "text",
        "sentiment_col": "sentiment",
    },
    "UkraineTwitter.csv": {
        "text_col":    "text",            # may vary — check df.columns
        "date_col":    "date",            # may be 'created_at'
        "location_col":"user_location",
        "likes_col":   "likes",
        "rt_col":      "retweet_count",
    },
    "SpotifyFeatures.csv": {
        "genre_col":   "track_genre",
        "numeric_cols":["popularity","danceability","energy","valence",
                        "tempo","acousticness","instrumentalness","loudness"],
    },
    "instagram_data.csv": {
        "followers_col": "Followers",
        "likes_col":     "Avg. Likes",
        "category_col":  "channel_info",
    },
}

# =============================================================================
# QUICK PRACTICAL → DATASET LOOKUP
# =============================================================================
PRACTICAL_DATASET = {
    1:  "apple-twitter-sentiment-texts.csv",
    2:  "Tweets.csv            (tweet_location column)",
    3:  "UkraineTwitter.csv    (date + text columns)",
    4:  "Tweets.csv            (text column — extract #hashtags with regex)",
    5:  "Tweets.csv            (text + airline_sentiment for comparison)",
    6:  "instagram_data.csv    (Followers + Avg. Likes + channel_info)",
    7:  "SpotifyFeatures.csv   (all numeric audio features + genre)",
    8:  "apple-twitter-sentiment-texts.csv + Tweets.csv for Samsung side",
    9:  "Tweets.csv            (4 airlines = 4 competitors)",
    10: "Tweets.csv            (build mention graph) OR twitter_combined.txt",
}

if __name__ == "__main__":
    print("=== DATASETS TO DOWNLOAD ===")
    for fname, info in DATASETS.items():
        print(f"\nFile    : {fname}")
        print(f"Use for : Practicals {info['practicals']}")
        print(f"Search  : {info.get('kaggle_search', info.get('source', ''))}")
        if "note" in info:
            print(f"Note    : {info['note']}")

    print("\n\n=== PRACTICAL → DATASET QUICK MAP ===")
    for p, d in PRACTICAL_DATASET.items():
        print(f"Practical {p:02d}:  {d}")
