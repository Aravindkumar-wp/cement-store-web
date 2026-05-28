import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# ------------------ CUSTOMERS ------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    address TEXT
)
""")

# ------------------ SALES ------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    product TEXT,
    quantity INTEGER,
    price REAL,
    labour REAL,
    transport REAL,
    total REAL,
    paid REAL,
    pending REAL,
    date TEXT
)
""")

# ------------------ PAYMENTS ------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    amount REAL,
    date TEXT
)
""")

# ------------------ WORKERS ------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS workers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    salary_per_day REAL
)
""")

# ------------------ ATTENDANCE ------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    worker_id INTEGER,
    date TEXT,
    status TEXT
)
""")

# ------------------ SALARY ADVANCE ------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS salary_advances (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    worker_id INTEGER,
    amount REAL,
    date TEXT
)
""")

# ------------------ PRODUCTS (STOCK) ------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    stock INTEGER
)
""")

# ------------------ STOCK MOVEMENTS ------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS stock_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    type TEXT,   -- add / sale
    quantity INTEGER,
    date TEXT
)
""")

# ------------------ SUPPLIERS ------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT
)
""")

# ------------------ PURCHASES ------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_id INTEGER,
    product TEXT,
    quantity INTEGER,
    total REAL,
    paid REAL,
    pending REAL,
    date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS stock_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    opening INTEGER,
    added INTEGER,
    sold INTEGER,
    closing INTEGER,
    date DATE,
    FOREIGN KEY(product_id) REFERENCES products(id)
)
""")

conn.commit()
conn.close()

print("Database created successfully!")
