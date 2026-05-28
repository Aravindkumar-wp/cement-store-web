import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("ALTER TABLE customers ADD COLUMN opening_balance INTEGER DEFAULT 0")

conn.commit()
conn.close()

print("Column added successfully!")