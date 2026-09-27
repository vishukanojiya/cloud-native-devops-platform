from fastapi import FastAPI
import os
import psycopg2

app = FastAPI(title="Cloud Native DevOps Platform")


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        database=os.getenv("DB_NAME", "devopsdb"),
        user=os.getenv("DB_USER", "devopsuser"),
        password=os.getenv("DB_PASSWORD", "devopspassword"),
    )


@app.get("/health")
def health():
    return {
        "status": "UP",
        "service": "backend"
    }


@app.get("/api/db-health")
def db_health():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        return {
            "status": "UP",
            "database": "PostgreSQL",
            "result": result[0]
        }

    except Exception as e:
        return {
            "status": "DOWN",
            "database": "PostgreSQL",
            "error": str(e)
        }


@app.get("/api/products")
def products():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, price FROM products ORDER BY id")
    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return [
        {
            "id": row[0],
            "name": row[1],
            "price": float(row[2])
        }
        for row in rows
    ]


@app.get("/api/orders")
def orders():
    return [
        {
            "id": 101,
            "product": "Laptop",
            "status": "CONFIRMED"
        }
    ]
