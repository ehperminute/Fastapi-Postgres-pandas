from fastapi import FastAPI
from database import get_connection

app = FastAPI()

@app.get("/stats/revenue")
def get_revenue():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT SUM(p.price * s.quantity)                      
                      FROM products p 
                          JOIN sales s ON s.product_id = p.id;""")
    revenue = cursor.fetchone()[0]
    if revenue is None:
        revenue = 0
    cursor.close()
    conn.close()
    return {"total_revenue": revenue}

