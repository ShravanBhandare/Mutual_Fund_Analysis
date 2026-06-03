import pandas as pd

# Load NAV History Dataset
nav = pd.read_csv("Data/Raw/02_nav_history.csv")

print("Original Shape:", nav.shape)

# Convert date column
nav["date"] = pd.to_datetime(nav["date"])

# Remove duplicates
nav = nav.drop_duplicates()

# Remove invalid NAV values
nav = nav[nav["nav"] > 0]

# Sort records
nav = nav.sort_values(
    by=["amfi_code", "date"]
)

print("Cleaned Shape:", nav.shape)

# Save cleaned file
nav.to_csv(
    "Data/processed/clean_nav.csv",
    index=False
)

print("clean_nav.csv created successfully")

# ==========================================
# TRANSACTION DATA CLEANING
# ==========================================
import pandas as pd
tx = pd.read_csv(
    "Data/Raw/08_investor_transactions.csv"
)

print("\nTransaction Data")
print("Original Shape:", tx.shape)

# Convert date
tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"]
)

# Remove duplicates
tx = tx.drop_duplicates()

# Keep only valid transaction amounts
tx = tx[tx["amount_inr"] > 0]

# Clean text columns
text_cols = [
    "transaction_type",
    "state",
    "city",
    "city_tier",
    "age_group",
    "gender",
    "payment_mode",
    "kyc_status"
]

for col in text_cols:
    tx[col] = tx[col].astype(str).str.strip()

print("Cleaned Shape:", tx.shape)

# Save cleaned file
tx.to_csv(
    "Data/processed/clean_transactions.csv",
    index=False
)

print("clean_transactions.csv created successfully")



# ==========================================
# PERFORMANCE DATA CLEANING
# ==========================================

perf = pd.read_csv(
    "Data/Raw/07_scheme_performance.csv"
)

print("\nPerformance Data")
print("Original Shape:", perf.shape)

# Remove duplicates
perf = perf.drop_duplicates()

# Basic validations

# Expense Ratio > 0
perf = perf[perf["expense_ratio_pct"] > 0]

# Beta should be positive
perf = perf[perf["beta"] > 0]

# Morningstar rating between 1 and 5
perf = perf[
    perf["morningstar_rating"].between(1, 5)
]

print("Cleaned Shape:", perf.shape)

perf.to_csv(
    "Data/processed/clean_performance.csv",
    index=False
)

print("clean_performance.csv created successfully")