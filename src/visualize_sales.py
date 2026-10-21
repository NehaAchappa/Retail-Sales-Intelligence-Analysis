
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Project folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "raw" / "superstore.csv"
OUTPUT_DIR = PROJECT_DIR / "reports" / "charts"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load dataset
df = pd.read_csv(DATA_FILE, encoding="cp1252")

# 1. Sales by category
category_sales = df.groupby("Category")["Sales"].sum().sort_values()

plt.figure(figsize=(9, 5))
category_sales.plot(kind="barh")
plt.title("Total Sales by Product Category")
plt.xlabel("Sales ($)")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sales_by_category.png", dpi=300)
plt.close()

# 2. Profit by region
region_profit = df.groupby("Region")["Profit"].sum().sort_values()

plt.figure(figsize=(9, 5))
region_profit.plot(kind="barh")
plt.title("Total Profit by Region")
plt.xlabel("Profit ($)")
plt.ylabel("Region")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "profit_by_region.png", dpi=300)
plt.close()

# 3. Profit by sub-category
subcategory_profit = (
    df.groupby("Sub-Category")["Profit"].sum().sort_values()
)

plt.figure(figsize=(10, 8))
subcategory_profit.plot(kind="barh")
plt.title("Profitability by Product Sub-Category")
plt.xlabel("Profit ($)")
plt.ylabel("Sub-Category")
plt.axvline(0, linewidth=1)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "profit_by_subcategory.png", dpi=300)
plt.close()

# 4. Monthly sales trend
df["Order Date"] = pd.to_datetime(
    df["Order Date"], format="%m/%d/%Y"
)
monthly_sales = (
    df.set_index("Order Date")["Sales"]
    .resample("MS")
    .sum()
)

plt.figure(figsize=(11, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_sales_trend.png", dpi=300)
plt.close()

print("All four charts were created successfully!")
print("Chart folder:", OUTPUT_DIR)
print("1. sales_by_category.png")
print("2. profit_by_region.png")
print("3. profit_by_subcategory.png")
print("4. monthly_sales_trend.png")
