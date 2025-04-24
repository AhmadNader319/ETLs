# config.py
import psycopg2

def get_connection():
    """Connects to PostgreSQL."""
    try:
        conn = psycopg2.connect("dbname=#database_name# user=#username#") # Database details
        print("Connected to PostgreSQL.")
        return conn
    except psycopg2.OperationalError as e:
        print(f"Connection failed: {e}")
        raise
