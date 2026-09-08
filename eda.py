import pandas as pd

df = pd.read_csv("sales_data_cleaned.csv")

print(df.describe())
print(df.corr(numeric_only=True))

Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Sales'] < Q1 - 1.5*IQR) | (df['Sales'] > Q3 + 1.5*IQR)]
print("Outliers in Sales:\n", outliers[['OrderID','Sales']])
