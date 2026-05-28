import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM customers")
print("Total customers:", cursor.fetchone()[0])

conn.close()