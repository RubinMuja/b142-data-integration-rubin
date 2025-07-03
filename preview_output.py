import pandas as pd

df = pd.read_parquet("output/avg_daily_cases.parquet")
print(df.head())

