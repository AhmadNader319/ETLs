import requests as rq
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
import os

def extract_transform_load_films(url, db_name="Movies.db", table_name="Top50Movies", csv_file="top_50_films.csv"):
    """
    Extracts film data from a URL, transforms it, and loads it into a CSV and SQLite database.

    Args:
        url (str): The URL to scrape film data from.
        db_name (str): The name of the SQLite database file.
        table_name (str): The name of the table in the SQLite database.
        csv_file (str): The name of the CSV file to save the data.

    Returns:
        bool: True if the ETL process was successful, False otherwise.
    """
    print(f"Starting ETL process from URL: {url}")
    try:
        # --- Extraction ---
        response = rq.get(url)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find_all('tbody')
        if not table:
            print("Error: No <tbody> element found on the page.")
            return False
        
        rows = table[0].find_all('tr')

        # --- Transformation ---
        df = pd.DataFrame(columns=["Average Rank", "Film", "Year"])
        count = 0

        for row in rows:
            cols = row.find_all('td')
            if count < 50 and len(cols) >= 3:
                try:
                    avg_rank = cols[0].text.strip()
                    film = cols[1].text.strip()
                    year = cols[2].text.strip()

                    table_dict = {
                        "Average Rank": avg_rank,
                        "Film": film,
                        "Year": year
                    }
                    df1 = pd.DataFrame([table_dict]) # Create DataFrame from dictionary
                    df = pd.concat([df, df1], ignore_index=True)
                    count += 1
                except IndexError:
                    print(f"Skipping malformed row: {row.text.strip()}")
                    continue
            elif count >= 50:
                break

        if df.empty:
            print("No data extracted. The table might be empty or structured differently than expected.")
            return False

        # --- Loading to CSV ---
        df.to_csv(csv_file, index=False)
        print(f"Data successfully saved to {csv_file}")

        # --- Loading to SQLite ---
        conn = sqlite3.connect(db_name)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
        print(f"Data successfully loaded into {db_name} in table '{table_name}'.")
        
        return True

    except rq.exceptions.RequestException as e:
        print(f"Network or request error during ETL: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred during ETL: {e}")
        return False

if __name__ == "__main__":
    url_to_scrape = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
    print("Running webscraping_movies.py directly for demonstration...")
    if extract_transform_load_films(url_to_scrape):
        print("ETL process completed successfully.")
    else:
        print("ETL process failed.")
