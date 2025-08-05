import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

# Load dataset
df = pd.read_csv("dataset.csv", parse_dates=["Order Date", "Ship Date"], dayfirst=True)

# Create visuals directory
os.makedirs("visuals", exist_ok=True)

# Chart 1: Total Sales by Region
plt.figure(figsize=(8, 5))
region_sales = df.groupby("Region")["Sales"].sum().sort_values()
sns.barplot(x=region_sales.values, y=region_sales.index)
plt.title("Total Sales by Region")
plt.xlabel("Sales")
plt.ylabel("Region")
plt.tight_layout()
plt.savefig("visuals/chart1.png")
plt.close()

# Chart 2: Profit by Category
plt.figure(figsize=(8, 5))
category_profit = df.groupby("Category")["Profit"].sum().sort_values()
sns.barplot(x=category_profit.index, y=category_profit.values)
plt.title("Total Profit by Category")
plt.ylabel("Profit")
plt.xlabel("Category")
plt.tight_layout()
plt.savefig("visuals/chart2.png")
plt.close()

# Chart 3: Monthly Sales Trend
df['Month'] = df['Order Date'].dt.to_period("M").astype(str)
monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()
plt.figure(figsize=(10, 5))
sns.lineplot(x="Month", y="Sales", data=monthly_sales, marker="o")
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend")
plt.tight_layout()
plt.savefig("visuals/chart3.png")
plt.close()

# Chart 4: Sales vs. Profit Scatter Plot by Discount
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Sales", y="Profit", hue="Discount", palette="coolwarm", size="Quantity")
plt.title("Sales vs. Profit Colored by Discount")
plt.tight_layout()
plt.savefig("visuals/chart4.png")
plt.close()

print("Visuals saved in 'visuals/' folder.")
