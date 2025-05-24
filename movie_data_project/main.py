import sqlite3
import pandas as pd
from webscraping_movies import extract_transform_load_films
import os

DB_NAME = "Movies.db"
TABLE_NAME = "Top50Movies"
CSV_FILE = "top_50_films.csv"
URL_TO_SCRAPE = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'

def query_films_by_year(db_name=DB_NAME, table_name=TABLE_NAME, year=2000):
    """
    Queries the SQLite database for films released after a specified year.

    Args:
        db_name (str): The name of the SQLite database file.
        table_name (str): The name of the table in the SQLite database.
        year (int): The year to filter films by (films released AFTER this year).

    Returns:
        pandas.DataFrame: A DataFrame containing the queried films, or an empty DataFrame if no films
                          match or an error occurs.
    """
    conn = None
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_name)
        
        # Construct the SQL query to select films where the 'Year' column is greater than the input year.
        query = f"SELECT * FROM {table_name} WHERE CAST(Year AS INTEGER) > {year}"
        
        # Read the SQL query result into a pandas DataFrame
        df = pd.read_sql_query(query, conn)
        
        if df.empty:
            print(f"\nNo films found released after the year {year}.")
        else:
            print(f"\n--- Films released after {year} ---")
            print(df.to_string(index=False)) # Print DataFrame without index
            print("-----------------------------------\n")
        
        return df

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return pd.DataFrame() # Return empty DataFrame on error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()
    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()

def main_orchestration_menu():
    """
    Displays the main menu for the film database application and handles user input.
    """
    while True:
        print("\n--- Film Database Application Menu ---")
        print("1. Run ETL (Extract, Transform, Load) process")
        print("2. Query films released after a specific year")
        print("3. Exit")
        print("--------------------------------------")

        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            print("\nRunning ETL process...")
            if extract_transform_load_films(URL_TO_SCRAPE, DB_NAME, TABLE_NAME, CSV_FILE):
                print("ETL process completed successfully. Database and CSV updated.")
            else:
                print("ETL process failed. Check the error messages above.")
            input("Press Enter to continue...")

        elif choice == '2':
            while True:
                year_input = input("Enter the year (e.g., 2000) or 'back' to return to main menu: ").strip()
                if year_input.lower() == 'back':
                    break
                try:
                    year = int(year_input)
                    # Check if the database file exists before querying
                    if not os.path.exists(DB_NAME):
                        print(f"Error: Database file '{DB_NAME}' not found. Please run ETL first (Option 1).")
                        input("Press Enter to continue...")
                        break # Go back to main menu
                    query_films_by_year(year=year)
                    input("Press Enter to continue...") # Pause for user to read
                    break # Break from inner loop to show main menu again
                except ValueError:
                    print("Invalid year. Please enter a number or 'back'.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_orchestration_menu()

