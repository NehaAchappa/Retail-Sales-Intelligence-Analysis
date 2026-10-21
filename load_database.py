
from pathlib import Path
import sqlite3
import pandas as pd

# Locate project files
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "raw" / "superstore.csv"
DB_FOLDER = PROJECT_DIR / "data" / "processed"
DB_FOLDER.mkdir(parents=True, exist_ok=True)

DB_FILE = DB_FOLDER / "retail_sales.db"

# Load the CSV dataset
df = pd.read_csv(DATA_FILE, encoding="cp1252")

# Create the SQLite database and table
with sqlite3.connect(DB_FILE) as connection:
    df.to_sql(
        "superstore",
        connection,
        if_exists="replace",
        index=False
    )

    # Verify the number of rows imported
    result = pd.read_sql_query(
        "SELECT COUNT(*) AS total_rows FROM superstore",
        connection
    )

    print("Database created successfully!")
    print("Database location:", DB_FILE)
    print("Rows imported:", result.loc[0, "total_rows"])

print("Table name: superstore")
