import re, numpy as np, pandas as pd, matplotlib.pyplot as plt
from collections import Counter
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.parsing.preprocessing import remove_stopwords
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


df["polarity"] = df["clean"].apply(lambda x: TextBlob(x).sentiment.polarity)
df["subjectivity"] = df["clean"].apply(lambda x: TextBlob(x).sentiment.subjectivity)

def classify(polarity):
    if polarity>0.05:
        return "pos"
    elif polarity<0.05:
        return "neg"
    else:
        return "neutral"

df["sentiment"] = df["polarity"].apply(classify)

print(df["sentiment"].value_counts())
df["sentiment"].value_counts().plot(kind="bar")
plt.show()

from wordcloud import WordCloud
import matplotlib.pyplot as plt


text = " ".join(df["text"].dropna()).lower()
text = remove_stopwords(text)
new = text.split()

count = Counter(new)
print(count.most_common(10))

wc = WordCloud().generate(text)
plt.imshow(wc)
plt.show(

)