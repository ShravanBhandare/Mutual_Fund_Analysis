import sqlite3
import pandas as pd

# Connect database
conn = sqlite3.connect("bluestock_mf.db")

# Load datasets
fund = pd.read_csv("Data/Raw/01_fund_master.csv")
nav = pd.read_csv("Data/processed/clean_nav.csv")
tx = pd.read_csv("Data/processed/clean_transactions.csv")
perf = pd.read_csv("Data/processed/clean_performance.csv")
perf = perf[
    [
        "amfi_code",
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct",
        "benchmark_3yr_pct",
        "alpha",
        "beta",
        "sharpe_ratio",
        "sortino_ratio",
        "std_dev_ann_pct",
        "max_drawdown_pct",
        "aum_crore",
        "expense_ratio_pct",
        "morningstar_rating",
        "risk_grade"
    ]
]

# Load into tables
fund.to_sql(
    "dim_fund",
    conn,
    if_exists="append",
    index=False
)

nav.to_sql(
    "fact_nav",
    conn,
    if_exists="append",
    index=False
)

tx.to_sql(
    "fact_transactions",
    conn,
    if_exists="append",
    index=False
)

perf.to_sql(
    "fact_performance",
    conn,
    if_exists="append",
    index=False
)


sip = pd.read_csv("Data/Raw/04_monthly_sip_inflows.csv")

sip.to_sql(
    "fact_sip_inflows",
    conn,
    if_exists="replace",
    index=False
)

print("All data loaded successfully")

conn.commit()
conn.close()

