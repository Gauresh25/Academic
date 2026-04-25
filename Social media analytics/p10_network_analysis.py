import re

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import seaborn as sns

df = pd.read_csv("instagram_data.csv")

print(df.head())


def cleaner(value):
    value = str(value).strip()
    if 'M' in value:
        return float(value.replace('M', '')) * 1_000_000
    elif 'K' in value:
        return float(value.replace('K', '')) * 1_000
    else:
        return float(value)  # ✅ handles plain numbers too

df["likes"] = df["likes"].apply(cleaner)
df["comments"] = df["comments"].apply(cleaner)
df["shares"] = df["shares"].apply(cleaner)

scaler = StandardScaler()

X = df[["likes","comments","shares"]].dropna()
Xs = scaler.fit_transform(X)

km = KMeans(n_clusters=3,random_state=0)
df["cluster"] = km.fit_predict(Xs)
plt.scatter(x=df["comments"],y=df["likes"],c=df["cluster"],alpha=0.3)
plt.show()

subd = df[["likes","comments","shares"]]

sns.heatmap(subd.corr())
plt.show()