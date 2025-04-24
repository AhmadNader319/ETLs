ETL Project# 1
This project performs an ETL (Extract, Transform, Load) process for loading data from a CSV file into a PostgreSQL database.

Project Structure
CSV_to_Postgresql_ETL/
├── config.py
├── extract.py
├── load.py
├── main.py
├── transform.py
└── README.md

How It Works
Extract: load_csv reads data from a CSV file.

Transform: clean_data cleans and preprocesses the data.

Load: bulk_insert_df_execute_values inserts the data into a PostgreSQL table.

Main: run_etl orchestrates the process.

Requirements
Python

Pandas

PostgreSQL

psycopg2

Usage
Set up a PostgreSQL database.

Update config.py with your database credentials.

Run main.py.

