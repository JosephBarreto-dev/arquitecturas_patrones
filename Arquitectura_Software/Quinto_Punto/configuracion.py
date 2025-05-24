import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="notasdb",
        user="postgres",
        password="secretoGustambo123",
        host="localhost",
        port="5432"
    )
