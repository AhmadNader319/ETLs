ETL Projects Repository

This repository is a collection of ETL (Extract, Transform, Load) projects built during my data engineering journey. Each project is designed to extract data from various sources, transform it into meaningful formats, and load it into storage systems such as PostgreSQL.

* Project Structure

    etl-project/
    │
    ├── extract.py               # Loads raw data from the source specified 
    ├── transform.py             # Cleans and transforms data
    ├── load.py                  # Inserts data into PostgreSQL
    ├── config.py                # Database connection setup (locally for now)
    ├── main.py                  # ETL runner
    ├── README.md                # Project documentation
    └── requirements.txt         # Python dependencies

How It Works

1. Extract:
    * Reads the source_file.csv/various sources from the filesystem/APIs.

2. Transform:
    * Handles missing values and invalid entries
    * Unify datatypes and column renaming (including snake_case naming convention)
    * Drops duplicate rows
    * Renames columns to follow snake_case naming

3. Load:
    * Inserts the transformed data into a PostgreSQL table using efficient bulk loading (execute_values)/ (StringIO to be tried) 

* Requirements:

    Python 3.2.2+
    PostgreSQL

* Required Python packages (install with pip):

    pip install -r requirements.txt

* Contents of requirements.txt:
    
    pandas
    numpy
    psycopg2-binary

-- How to Run

    Update DB CredentialsEdit config.py with your PostgreSQL database name and user.

    Run the ETL Pipeline
        python main.py

Author

Ahmed NaderAspiring Data Engineer | Python & SQL EnthusiastFeel free to connect or contribute to the repository!
