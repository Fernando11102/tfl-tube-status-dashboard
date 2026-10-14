import pandas as pd

df = pd.read_csv("tube_status.csv")

print("First 5 rows:")
print(df.head())

print("\nTotal records:", len(df))

print("\nService status summary:")
print(df["status"].value_counts())

disruptions = df[
    (df["status"] != "Good Service") &
(df["status"] != "Unknown")
]

print("\nPotential disruptions:")
print(disruptions[["line", "status"]])