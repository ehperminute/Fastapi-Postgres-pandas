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


@app.get("/stats/products_revenue")
def get_products_revenue():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT p.id, p.name, SUM(p.price * s.quantity)  AS revenue                    
                    FROM products p 
                        JOIN sales s ON s.product_id = p.id
                    GROUP BY p.id, p.name
                    ORDER BY revenue DESC;
                    """)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return {"revenue_products": [{"id": product_id, "name": product_name, "revenue": revenue} 
                                    for product_id, product_name, revenue in rows]}

@app.get("/stats/customers_revenue")
def customers_revenue():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT c.id, c.name, SUM(p.price * s.quantity)  AS revenue                    
                    FROM products p 
                        JOIN sales s ON s.product_id = p.id
                        JOIN customers c ON s.customer_id = c.id
                    GROUP BY c.id, c.name
                    ORDER BY revenue DESC;
                    """)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return {"revenue_customers": [{"id": product_id, "name": product_name, "revenue": revenue} 
                                    for product_id, product_name, revenue in rows]}



