import pandas as pd
import requests

df = pd.read_csv("fill2-copy.csv")

# print(df.head())

# print(df['tip'])

# tips = df['tip']

# print(tips.mean())

# print(tips[tips == 0.0].count())


df2 = pd.read_csv("dropped copy.csv")

# print(df2.head())

# print(df2['tip'])

# tips2 = df2['tip']

# print(tips2.mean())

# print(tips2[tips2 == 0.0].count())

cost = df['trip_total']
print(cost.mean())