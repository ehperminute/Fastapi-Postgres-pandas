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

@app.get("/stats/country_revenue")
def country_revenue():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT c.country, SUM(p.price * s.quantity)  AS revenue                    
                    FROM products p 
                        JOIN sales s ON s.product_id = p.id
                        JOIN customers c ON s.customer_id = c.id
                    GROUP BY c.country
                    ORDER BY revenue DESC;
                    """)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return {"country_revenue": [{"counry": country, "revenue": revenue} 
                                    for country, revenue in rows]}

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
    return {"revenue_customers": [{"id": customer_id, "name": customer_name, "revenue": revenue} 
                                    for customer_id, customer_name, revenue in rows]}

@app.get("/stats/avg_order")
def avg_order():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT AVG(p.price * s.quantity) AS avg_order_value
        FROM sales s
        JOIN products p ON s.product_id = p.id;
    """)

    avg_value = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    if avg_value is None:
        avg_value = 0

    return {"avg_order_value": avg_value}


@app.get("/stats/revenue_date")
def revenue_date():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.sale_date, SUM(p.price * s.quantity) AS revenue
        FROM sales s
            JOIN products p ON s.product_id = p.id
        GROUP BY s.sale_date
        ORDER BY s.sale_date;
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    

    return {"revenue_by_date": [{"date": date, "revenue": revenue}
                                for date, revenue in rows]}
