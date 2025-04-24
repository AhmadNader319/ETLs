# main script
from extract import load_csv
from transform import clean_data
from load import bulk_insert_df_execute_values
from config import get_connection

def run_etl():
    """Runs the ETL process."""
    try:
        file_path = "filepath to the csv file" # CSV file location
        df = load_csv(file_path) # Load data

        df = clean_data(df) # Clean data
        print(df.describe()) # Show cleaned data info

        conn = get_connection() # Connect to database
        bulk_insert_df_execute_values(df, "selected_dataset", conn) # Load to database
        conn.close() # Close connection
        print("PostgreSQL closed.")

    except Exception as e:
        print(f"ETL failed: {e}")

if __name__ == "__main__":
    run_etl()
