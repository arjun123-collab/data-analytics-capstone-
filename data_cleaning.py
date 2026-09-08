import pandas as pd

df = pd.read_csv("sales_data.csv")

print(df.shape)
print(df.dtypes)
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()
df['CustomerAge'] = df['CustomerAge'].fillna(df['CustomerAge'].median())
df['SatisfactionRating'] = df['SatisfactionRating'].fillna(df['SatisfactionRating'].median())
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

df.to_csv("sales_data_cleaned.csv", index=False)
print("Cleaned dataset saved.")
