import sqlite3

# Create database
conn = sqlite3.connect("bluestock_mf.db")

print("Database created successfully")

conn.close()