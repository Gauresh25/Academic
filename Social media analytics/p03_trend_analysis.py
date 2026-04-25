import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load
try:
    df = pd.read_csv("UkraineTwitter.csv", encoding="utf-8", on_bad_lines="skip")
except Exception:
    df = pd.read_csv("UkraineTwitter.csv", encoding="latin-1", on_bad_lines="skip")
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df["parsed_date"] = pd.to_datetime(df["tweetcreatedts"], errors="coerce")
df = df.dropna(subset=["parsed_date"])

# Choose your resolution: "h", "15min", "min"
df["bucket"] = df["parsed_date"].dt.floor("h")
trend = df.groupby("bucket").size()
trend.plot()
plt.show()