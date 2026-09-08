import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data_cleaned.csv")
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

plt.figure(figsize=(8,5))
df.groupby('Category')['Sales'].sum().plot(kind='bar', color='steelblue')
plt.title('Total Sales by Category')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('chart1_sales_by_category.png')
plt.show()

plt.figure(figsize=(8,5))
df.groupby(df['OrderDate'].dt.to_period('M'))['Sales'].sum().plot(kind='line', marker='o', color='green')
plt.title('Monthly Sales Trend')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('chart2_monthly_trend.png')
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(df['Quantity'], df['Sales'], color='orange')
plt.title('Quantity vs Sales')
plt.xlabel('Quantity')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('chart3_quantity_vs_sales.png')
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x='Category', y='Sales', data=df)
plt.title('Sales Distribution by Category')
plt.tight_layout()
plt.savefig('chart4_sales_boxplot.png')
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('chart5_correlation_heatmap.png')
plt.show()
