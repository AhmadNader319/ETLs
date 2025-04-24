# load.py
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

def bulk_insert_df_execute_values(df: pd.DataFrame, table_name: str, conn: psycopg2.extensions.connection):
    """Inserts DataFrame into PostgreSQL."""
    cur = conn.cursor()
    try:
        values = [tuple(x) for x in df.to_numpy()] # Data to insert
        columns = ', '.join(df.columns) # Column names
        sql = f"INSERT INTO {table_name} ({columns}) VALUES %s" # SQL insert
        execute_values(cur, sql, values) # Execute insert
        conn.commit() # Save changes
        print(f"Inserted {len(df)} rows into '{table_name}'")
    except psycopg2.Error as e:
        print(f"PostgreSQL Error: {e.pgerror}")
        conn.rollback() # Undo changes
        raise
    except Exception as e:
        print(f"Loading error: {e}")
        conn.rollback() # Undo changes
        raise
    finally:
        cur.close() # Close connection
