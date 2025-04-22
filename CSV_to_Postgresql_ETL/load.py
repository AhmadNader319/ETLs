import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

def bulk_insert_df_execute_values(df: pd.DataFrame, table_name: str, conn: psycopg2.extensions.connection):
    cur = conn.cursor()
    try:
        values = [tuple(x) for x in df.to_numpy()]
        columns = ', '.join(df.columns)
        sql = f"INSERT INTO {table_name} ({columns}) VALUES %s"
        execute_values(cur, sql, values)
        conn.commit()
        print(f"Inserted {len(df)} rows into '{table_name}'")
    except psycopg2.Error as e:
        print(f"PostgreSQL Error: {e.pgerror}")
        conn.rollback()
        raise
    except Exception as e:
        print(f"Unexpected error during loading: {e}")
        conn.rollback()
        raise
    finally:
        cur.close()
