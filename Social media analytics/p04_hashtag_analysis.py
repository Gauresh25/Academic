import re, pandas as pd, matplotlib.pyplot as plt
from collections import Counter
from itertools import combinations
from gensim.parsing.preprocessing import remove_stopwords

df = pd.read_csv("Tweets.csv", encoding="utf-8", on_bad_lines="skip")

df["clean"] = df["text"].apply(remove_stopwords)

def tagger(text):
    return re.findall(r"#\w+",str(text).lower())


df["tags"] = df["clean"].apply(tagger)
#print(df["tags"].head(40))

all = [tag for row in df["tags"] for tag in row]
count = Counter(all)

print(count.most_common(10))
count = count.most_common(10)
print(type(count))
print(count)

tags = [x[0] for x in count]
value =  [x[1] for x in count]
plt.bar(tags,value)
plt.show()