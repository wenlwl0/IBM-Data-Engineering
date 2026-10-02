# ETL project: World's largest banks by market capitalization

from datetime import datetime
from pathlib import Path
from io import StringIO
import sqlite3

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup


# Known project values
PROJECT_DIR = Path(__file__).resolve().parent

URL = (
    "https://web.archive.org/web/20230908091635/"
    "https://en.wikipedia.org/wiki/List_of_largest_banks"
)

TABLE_ATTRIBS = ["Name", "MC_USD_Billion"]
CSV_PATH = PROJECT_DIR / "exchange_rate.csv"
OUTPUT_PATH = PROJECT_DIR / "Largest_banks_data.csv"
DB_PATH = PROJECT_DIR / "Banks.db"
TABLE_NAME = "Largest_banks"
LOG_PATH = PROJECT_DIR / "code_log.txt"


def log_progress(message):
    """Append a timestamped progress message to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_PATH, "a", encoding="utf-8") as log_file:
        log_file.write(f"{timestamp} : {message}\n")


def extract(url, table_attribs):
    """Extract the bank market-capitalization table into a DataFrame."""
    response = requests.get(url, timeout=60)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Locate the table beneath the required heading.
    heading = soup.find(id="By_market_capitalization")

    if heading is None:
        raise ValueError("Could not find the By market capitalization heading.")

    table = heading.find_next("table")

    if table is None:
        raise ValueError("Could not find the market-capitalization table.")

    source_df = pd.read_html(StringIO(str(table)))[0]

    # Handle multi-level headers if present.
    if isinstance(source_df.columns, pd.MultiIndex):
        source_df.columns = source_df.columns.get_level_values(-1)

    bank_column = next(
        (
            column
            for column in source_df.columns
            if str(column).strip().lower() in {"bank name", "bank", "name"}
        ),
        None,
    )

    market_cap_column = next(
        (
            column
            for column in source_df.columns
            if "market cap" in str(column).lower()
        ),
        None,
    )

    if bank_column is None or market_cap_column is None:
        raise ValueError(
            f"Required columns were not found: {source_df.columns.tolist()}"
        )

    df = source_df[[bank_column, market_cap_column]].copy()
    df.columns = table_attribs

    # Strip whitespace/newlines, citation markers, and thousands separators.
    market_caps = (
        df["MC_USD_Billion"]
        .astype(str)
        .str.strip()
        .str.replace(r"\[[^\]]*\]", "", regex=True)
        .str.replace(",", "", regex=False)
    )

    df["MC_USD_Billion"] = pd.to_numeric(market_caps, errors="coerce")
    df = df.dropna(subset=["Name", "MC_USD_Billion"]).copy()
    df["MC_USD_Billion"] = df["MC_USD_Billion"].astype(float)
    df["Name"] = df["Name"].astype(str).str.strip()

    return df.reset_index(drop=True)


def transform(df, csv_path):
    """Convert USD market capitalization into GBP, EUR, and INR."""
    exchange_rate_df = pd.read_csv(csv_path)

    # First column contains currencies; second contains exchange rates.
    exchange_rate = dict(
        zip(
            exchange_rate_df.iloc[:, 0].astype(str).str.strip(),
            exchange_rate_df.iloc[:, 1],
        )
    )

    gbp_rate = float(exchange_rate["GBP"])
    eur_rate = float(exchange_rate["EUR"])
    inr_rate = float(exchange_rate["INR"])

    df = df.copy()

    df["MC_GBP_Billion"] = [
        np.round(x * gbp_rate, 2) for x in df["MC_USD_Billion"]
    ]

    df["MC_EUR_Billion"] = [
        np.round(x * eur_rate, 2) for x in df["MC_USD_Billion"]
    ]

    df["MC_INR_Billion"] = [
        np.round(x * inr_rate, 2) for x in df["MC_USD_Billion"]
    ]

    return df


def load_to_csv(df, output_path):
    """Save the transformed DataFrame as a CSV file."""
    df.to_csv(output_path, index=False)


def load_to_db(df, sql_connection, table_name):
    """Save the transformed DataFrame as a database table."""
    df.to_sql(
        table_name,
        sql_connection,
        if_exists="replace",
        index=False,
    )


def run_query(query_statement, sql_connection):
    """Print a SQL query and its results."""
    print(f"\nQuery: {query_statement}")

    query_output = pd.read_sql_query(query_statement, sql_connection)
    print(query_output.to_string(index=False))


# Execute the ETL process.
log_progress("Preliminaries complete. Initiating ETL process")

df = extract(URL, TABLE_ATTRIBS)

# Uncomment for the Task 2 extraction screenshot.
# print(df.to_string(index=False))

log_progress("Data extraction complete. Initiating Transformation process")

df = transform(df, CSV_PATH)
print("Transformed bank data:")
print(df.to_string(index=False))

print("\nMarket capitalization of the fifth bank in billion EUR:")
print(df["MC_EUR_Billion"].iloc[4])

log_progress("Data transformation complete. Initiating Loading process")

load_to_csv(df, OUTPUT_PATH)
log_progress("Data saved to CSV file")

sql_connection = sqlite3.connect(DB_PATH)
log_progress("SQL Connection initiated")

try:
    load_to_db(df, sql_connection, TABLE_NAME)
    log_progress("Data loaded to Database as a table, Executing queries")

    run_query(
        "SELECT * FROM Largest_banks",
        sql_connection,
    )

    run_query(
        "SELECT AVG(MC_GBP_Billion) FROM Largest_banks",
        sql_connection,
    )

    run_query(
        "SELECT Name FROM Largest_banks "
        "ORDER BY MC_USD_Billion DESC LIMIT 5",
        sql_connection,
    )

    log_progress("Process Complete")

finally:
    sql_connection.close()
    log_progress("Server Connection closed")