import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Dataset loaded successfully!")
print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print("\nFirst 5 rows:")
print(df.head())

print("\nColumn info:")
print(df.dtypes)

print(f"\nMissing values:\n{df.isnull().sum()}")
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
print("\nData cleaned. No missing values or duplicates.")

df["Date"] = pd.to_datetime(df["Date"])

total_revenue = df["Total_Sales"].sum()
avg_order_value = df["Total_Sales"].mean()
total_units_sold = df["Quantity"].sum()
highest_sale = df["Total_Sales"].max()
lowest_sale = df["Total_Sales"].min()

product_revenue = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
best_product = product_revenue.idxmax()

region_revenue = df.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)
best_region = region_revenue.idxmax()

df["Month"] = df["Date"].dt.strftime("%B")
monthly_revenue = df.groupby("Month")["Total_Sales"].sum()

print("\n" + "="*45)
print("         SALES ANALYSIS REPORT")
print("="*45)
print(f"Total Revenue       : Rs.{total_revenue:,.2f}")
print(f"Average Order Value : Rs.{avg_order_value:,.2f}")
print(f"Total Units Sold    : {total_units_sold}")
print(f"Highest Single Sale : Rs.{highest_sale:,.2f}")
print(f"Lowest Single Sale  : Rs.{lowest_sale:,.2f}")

print("\nRevenue by Product:")
for product, revenue in product_revenue.items():
    print(f"  {product:<15}: Rs.{revenue:,.2f}")

print(f"\nBest Selling Product: {best_product}")

print("\nRevenue by Region:")
for region, revenue in region_revenue.items():
    print(f"  {region:<10}: Rs.{revenue:,.2f}")

print(f"\nTop Performing Region: {best_region}")

print("\nMonthly Revenue Breakdown:")
for month, revenue in monthly_revenue.items():
    print(f"  {month:<12}: Rs.{revenue:,.2f}")

print("\n" + "="*45)
print("Analysis complete.")
