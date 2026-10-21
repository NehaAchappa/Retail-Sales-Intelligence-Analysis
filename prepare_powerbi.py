
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "raw" / "superstore.csv"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load the dataset
df = pd.read_csv(DATA_FILE, encoding="cp1252")

# Convert dates
df["Order Date"] = pd.to_datetime(
    df["Order Date"], format="%m/%d/%Y"
)
df["Ship Date"] = pd.to_datetime(
    df["Ship Date"], format="%m/%d/%Y"
)

# Add useful analysis columns
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
df["Order Month Name"] = df["Order Date"].dt.strftime("%b")
df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

# Export Power BI dataset
output_file = OUTPUT_DIR / "superstore_powerbi.csv"
df.to_csv(output_file, index=False)

print("Power BI dataset prepared successfully!")
print("Rows:", len(df))
print("Saved to:", output_file)
