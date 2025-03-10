import pandas as pd


df = pd.read_csv("missing_data.csv")
df.fillna({"Age": 0, "City": "Unknown"}, inplace=True)
print(df)
df.to_csv("cleaned_data.csv", index=False)
