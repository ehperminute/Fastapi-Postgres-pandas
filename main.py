from fastapi import FastAPI
from database import get_connection

app = FastAPI()

@app.get("/customers")
def get_customers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, country FROM customers ORDER BY id")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    customers = [
        {"id": row[0], "name": row[1], "country": row[2]}
        for row in rows
    ]

    return {"customers": customers}
