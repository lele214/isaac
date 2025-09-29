import sqlite3
import csv

conn = sqlite3.connect("items.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    item_id INTEGER,
    pickup TEXT,
    quality INTEGER,
    effect TEXT,
    type TEXT,
    item_pool TEXT
)
""")

with open("items.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
        INSERT INTO items (name, item_id, pickup, quality, effect, type, item_pool)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            row["name"],
            row["item_id"],
            row["pickup"],
            row["quality"],
            row["effect"],
            row["type"],
            row["item_pool"]
        ))
        
conn.commit()
conn.close()

print("Import CSV → DB terminé")
