import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect("dbname=#database_name# user=#username#")
        print("Successfully connected to PostgreSQL.")
        return conn
    except psycopg2.OperationalError as e:
        print(f"Failed to connect to PostgreSQL: {e}")
        raise
