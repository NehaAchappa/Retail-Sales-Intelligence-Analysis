
from pathlib import Path
import sqlite3
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DB_FILE = PROJECT_DIR / "data" / "processed" / "retail_sales.db"
SQL_FILE = PROJECT_DIR / "sql" / "business_analysis.sql"
OUTPUT_DIR = PROJECT_DIR / "reports" / "sql_results"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Read the SQL file
sql_text = SQL_FILE.read_text(encoding="utf-8")

# Separate the individual queries
queries = [
    query.strip()
    for query in sql_text.split(";")
    if query.strip()
]

# Execute each query and save its results
with sqlite3.connect(DB_FILE) as connection:
    for number, query in enumerate(queries, start=1):
        result = pd.read_sql_query(query, connection)

        print(f"\n{'=' * 60}")
        print(f"QUERY {number}")
        print("=" * 60)
        print(result.to_string(index=False))

        output_file = OUTPUT_DIR / f"query_{number}.csv"
        result.to_csv(output_file, index=False)

print("\nAll SQL queries executed successfully!")
print("Results saved in:", OUTPUT_DIR)
