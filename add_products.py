import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

products = ["Cement", "Steel", "Nails", "Binding Wire", "Sand"]

for p in products:
    cursor.execute("INSERT INTO products (name) VALUES (?)", (p,))

conn.commit()
conn.close()

print("✅ Products added!")