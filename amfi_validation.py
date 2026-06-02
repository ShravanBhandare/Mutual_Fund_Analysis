import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Unique AMFI codes
fund_master_codes = set(fund_master["amfi_code"].unique())
nav_history_codes = set(nav_history["amfi_code"].unique())

# Missing codes
missing_codes = fund_master_codes - nav_history_codes

print("\nTotal AMFI Codes in Fund Master:")
print(len(fund_master_codes))

print("\nTotal AMFI Codes in NAV History:")
print(len(nav_history_codes))

print("\nMissing Codes:")
print(len(missing_codes))

if len(missing_codes) == 0:
    print("\n✅ All AMFI codes from Fund Master exist in NAV History.")
else:
    print("\n❌ Missing AMFI Codes:")
    print(sorted(missing_codes))