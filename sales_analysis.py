
from pathlib import Path
import pandas as pd

# Find the project folder and dataset
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "raw" / "superstore.csv"

# Load the dataset
df = pd.read_csv(DATA_FILE, encoding="cp1252")

# Convert dates into proper date format
df["Order Date"] = pd.to_datetime(
    df["Order Date"], format="%m/%d/%Y"
)
df["Ship Date"] = pd.to_datetime(
    df["Ship Date"], format="%m/%d/%Y"
)

# Calculate overall business performance
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
total_quantity = df["Quantity"].sum()
profit_margin = (total_profit / total_sales) * 100

print("\n========== BUSINESS PERFORMANCE ==========")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Unique Orders: {total_orders:,}")
print(f"Unique Customers: {total_customers:,}")
print(f"Total Items Sold: {total_quantity:,}")
print(f"Overall Profit Margin: {profit_margin:.2f}%")

# Sales and profit by product category
category_analysis = (
    df.groupby("Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Units_Sold=("Quantity", "sum")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\n========== CATEGORY PERFORMANCE ==========")
print(category_analysis.round(2).to_string())

# Sales and profit by region
region_analysis = (
    df.groupby("Region")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\n========== REGIONAL PERFORMANCE ==========")
print(region_analysis.round(2).to_string())

# Identify loss-making sub-categories
subcategory_analysis = (
    df.groupby("Sub-Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    )
    .sort_values("Total_Profit")
)

print("\n========== LOWEST-PROFIT SUB-CATEGORIES ==========")
print(subcategory_analysis.head(10).round(2).to_string())

# Analyze discounts and profit
df["Discount Band"] = pd.cut(
    df["Discount"],
    bins=[-0.001, 0, 0.2, 0.4, 1],
    labels=["No Discount", "Low (0-20%)",
            "Medium (20-40%)", "High (40%+)"],
    include_lowest=True
)

discount_analysis = (
    df.groupby("Discount Band", observed=False)
    .agg(
        Transactions=("Order ID", "count"),
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Average_Profit=("Profit", "mean")
    )
)

print("\n========== DISCOUNT ANALYSIS ==========")
print(discount_analysis.round(2).to_string())

# Save analysis results for future reporting
output_folder = PROJECT_DIR / "data" / "processed"
output_folder.mkdir(parents=True, exist_ok=True)

category_analysis.to_csv(output_folder / "category_analysis.csv")
region_analysis.to_csv(output_folder / "region_analysis.csv")
subcategory_analysis.to_csv(output_folder / "subcategory_analysis.csv")
discount_analysis.to_csv(output_folder / "discount_analysis.csv")

print("\nAnalysis completed successfully!")
print("Results saved in the data/processed folder.")
