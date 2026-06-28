import time
from database import get_connection

while True:
    try:
        conn = get_connection()
        break
    except Exception:
        print("Waiting for PostgreSQL...")
        time.sleep(1)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price NUMERIC NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    product_id INTEGER NOT NULL REFERENCES products(id),
    quantity INTEGER NOT NULL,
    sale_date DATE NOT NULL
);
""")

conn.commit()
cursor.close()
conn.close()

print("Database initialized")
