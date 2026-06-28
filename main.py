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
    res = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return {"total revenue": res}

