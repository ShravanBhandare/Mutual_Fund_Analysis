import sqlite3

# Connect database
conn = sqlite3.connect("bluestock_mf.db")

# Read schema file
with open("sql/schema.sql", "r") as f:
    schema = f.read()

# Execute schema
conn.executescript(schema)

print("Tables created successfully")

conn.commit()
conn.close()