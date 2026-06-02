import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())