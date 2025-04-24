## CSV to PostgreSQL ETL Project

* This project performs an ETL (Extract, Transform, Load) process for loading data from a CSV file into a PostgreSQL database.
---
## Project Structure
```
CSV_to_Postgresql_ETL/  
├── config.py           
├── extract.py          
├── load.py             
├── main.py             
├── transform.py        
└── README.md           
```
---
## How It Works

- Extract: load_csv() reads data from a CSV file.

- Transform: clean_data() cleans and preprocesses the extracted data.

- Load: bulk_insert_df_execute_values() inserts the cleaned data into a PostgreSQL table.

- Main: run_etl() orchestrates the entire ETL process.

## Requirements

* Python
* Pandas
* PostgreSQL
* psycopg2
* Install dependencies:
    * pip install pandas psycopg2

## Usage

* Set up a PostgreSQL database instance.
* Update config.py with your database connection credentials.
* Run the main ETL pipeline:
    * python main.py

📌 Notes

Ensure the CSV file path is correctly set in extract.py.

Table creation and schema management should be handled prior to running the ETL.
