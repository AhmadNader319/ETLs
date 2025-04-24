## S3 to S3 ETL Project
* This project performs an ETL (Extract, Transform, Load) process entirely within AWS S3. It extracts CSV files from a raw data location in S3, applies transformations, and loads the transformed data to a processed data location in the same S3 bucket.

## Project Description
* The goal of this project is to process data stored in CSV files within an S3 bucket.  It reads the data, performs cleaning and transformation steps, and then writes the processed data back to S3, organizing it into a separate location.  This is useful for data processing pipelines where you need to clean, transform, and prepare data for analysis or further use.

## Project Structure
```
S3_to_S3_ETL/
├── config.py
├── extract.py
├── load.py
├── main.py
├── transform.py
├── README.md
└── utils/ 
```

## How It Works
* Extraction:
    - 
        The extract.py module uses boto3 to connect to S3.

        The load_all_csvs_from_s3_prefix function retrieves all CSV files from the specified raw data location (prefix) within the S3 bucket.

        The CSV data is read into Pandas DataFrames.

* Transformation:
    -
        The transform.py module uses pandas to perform data transformations.

        The clean_missing_values function handles missing values in specified columns (in your example, 'Age' and 'BMI'). You can configure this to drop rows or fill missing values.

        Additional transformation functions (like merge_dataframes, standardize_units, and standardize_dates) are available in transform.py and can be incorporated into the main.py script.

* Loading:
    -
        The load.py module uses boto3 to write the transformed Pandas DataFrames back to S3.

        The upload_dataframe_to_s3 function converts each DataFrame to a CSV file in memory and uploads it to the specified processed data location (prefix) in the S3 bucket.

* Orchestration:
    - 
        The main.py script orchestrates the entire ETL process.

        It reads the configuration from config.py.

        It calls the functions in extract.py to get the data.

        It calls the functions in transform.py to transform the data.

        It calls the functions in load.py to save the processed data to S3.

## How to Run
* Clone the repository:

* git clone <your_repository_url>

        cd S3_to_S3_ETL
* Ensure you have AWS credentials configured.
* Install the dependencies:
* pip install -r requirements.txt
* Run the main script:

        python main.py


