import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

cursor = conn.cursor()

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance"
]

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table}: {count}")

cursor.execute("SELECT COUNT(*) FROM fact_sip_inflows")
print("fact_sip_inflows:", cursor.fetchone()[0])

conn.close()