# README: ETL Pipeline in Python

** Overview

This is a simple ETL (Extract, Transform, Load) pipeline implemented in Python. The script processes data from .csv, .json, and .xml files in the current directory. It transforms height from inches to meters and weight from pounds to kilograms, then stores the result in a .csv file.

Features

Extract data from multiple file formats: CSV, JSON, XML

Transform data units to standard metric (meters, kilograms)

Load the processed data into a single CSV file

Log each phase of the ETL process

File Structure

```
.
├── script.py                # ETL script
├── *.csv                   # Raw CSV data files
├── *.json                  # Raw JSON data files
├── *.xml                   # Raw XML data files
├── transformed_data.csv    # Output file
└── logfile.txt             # Log of ETL process
```
# How to Run

### Download and extract the source data:

wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip
- **unzip source.zip** 

** Make sure the extracted CSV, JSON, and XML files are in the same directory as the script.

1. Run the script:
```
python script.py
```
Check the transformed_data.csv for the consolidated and transformed data.

## Data Schema

Each record in any input file format should have the following fields:

name: Person's name

height: Height in inches

weight: Weight in pounds

## Output:

- transformed_data.csv: Contains all extracted and converted records

- logfile.txt: Contains logs with timestamps for all ETL steps


