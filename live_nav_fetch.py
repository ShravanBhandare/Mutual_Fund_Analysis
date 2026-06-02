import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

funds = {
    "hdfc_top100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for fund_name, amfi_code in funds.items():

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    print(f"Fetching {fund_name}...")

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = f"data/raw/{fund_name}_nav.csv"

        nav_df.to_csv(file_name, index=False)

        print(f"Saved: {file_name}")

    else:
        print(f"Failed: {fund_name}")