from fastapi import FastAPI
from database import get_connection

app = FastAPI()

@app.get("/stats/revenue")
def get_revenue():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute()

