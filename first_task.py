
from pathlib import Path
import pandas as pd

# Locate the project and dataset
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "raw" / "superstore.csv"

# Check whether the dataset exists
if not DATA_FILE.exists():
    raise FileNotFoundError(
        f"Dataset not found at: {DATA_FILE}\n"
        "Check that superstore.csv is inside data/raw."
    )

# Load the dataset
df = pd.read_csv(DATA_FILE, encoding="cp1252")

# Display basic information
print("\n--- DATASET LOADED SUCCESSFULLY ---")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- FIRST FIVE ROWS ---")
print(df.head())

print("\n--- DATA TYPES AND NON-NULL VALUES ---")
df.info()

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print("Duplicate rows:", df.duplicated().sum())

print("\n--- SALES AND PROFIT SUMMARY ---")
print(df[["Sales", "Profit"]].describe())
