from extract import load_csv
from transform import clean_data
from load import bulk_insert_df_execute_values
from config import get_connection

def run_etl():
    try:
        file_path = "filepath to the csv file"
        df = load_csv(file_path)

        df = clean_data(df)
        print(df.describe())

        conn = get_connection()
        bulk_insert_df_execute_values(df, "selected_dataset", conn)
        conn.close()
        print("PostgreSQL connection closed.")

    except Exception as e:
        print(f"ETL Pipeline failed: {e}")

if __name__ == "__main__":
    run_etl()
