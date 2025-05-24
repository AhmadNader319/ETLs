# ETLs & ELTs Repository

This repository contains data engineering projects focusing on **ETL (Extract, Transform, Load)** and **ELT (Extract, Load, Transform)** processes. These projects demonstrate end-to-end data pipeline implementations using Python and tools like PostgreSQL and Amazon S3.

---

## Projects

### CSV to PostgreSQL ETL
- **Description**: Extracts data from local CSV files, transforms it with pandas, and loads it into a PostgreSQL database.
- **Pipeline Type**: Traditional ETL
- **Technologies**: Python, Pandas, PostgreSQL, psycopg2

### S3 to S3 ELT
- **Description**: Extracts raw CSV files from an S3 bucket, loads them into a different S3 location, and applies transformations afterward.
- **Pipeline Type**: ELT using S3 as staging
- **Technologies**: Python, Boto3, Amazon S3

### Weather API ETL 
- **Description**: Extracts forecast and current weather, load all in 2 separated collections in MongoDB.
- **Pipeline Type**: ETL using MongoDB and real-time weather api 
- **Technologies**: Python, MongoDB, etc...

### Data_Mining_Tasks
- **Description** Data mining tasks for helwan university course of data mining applying classification and regression
---

## Repository Structure
```
ETLs&ELTs/  
│   ├── CSV_to_Postgresql_ETL/     
│   └──├── config.py   
│      ├── extract.py  
│      ├── load.py     
│      ├── main.py     
│      ├── transform.py    
│      └──  utils.py      
│   └── S3_to_S3_P1/  
│       ├── config.py   
│       ├── extract.py  
│       ├── load.py     
│       ├── main.py     
│       ├── transform.py
│   └── Weather_API_ETL
│       ├── config.py   
│       ├── extract.py  
│       ├── db_utils.py     
│       ├── main.py     
│       ├── weather_app.log
│   └── Weather_API_ETL
│       ├── config.py   
│       ├── vehicle_accidents_dataset.csv  
│       ├── vehicle_accident_analysis.py     
│       ├── car_price_dataset.csv     
│       ├── car_data_processing_regression.py         
│   ├── utils/        
│   ├── README.md   
│   └── requirements.txt    
└── shared_utils/ 
```

## Technologies Used:
- Python
- Pandas
- PostgreSQL
- Amazon S3
- Boto3


## Installation

```
git clone <repository_url>
cd ETLs&ELTs
pip install -r requirements.txt
```

## Usage
Each project has its own set of instructions. Please refer to the project-specific directories for details.

CSV to PostgreSQL ETL: See the CSV_to_Postgresql_ETL directory.  You will need a running PostgreSQL instance and to configure the database connection in config.py.

S3 to S3 ELT: See the S3_to_S3_P1 directory.  You will need an AWS account with S3 access and to configure your S3 buckets and credentials in config.py.

Data Mining Tasks (regression&classification): See the Data_Mining_Tasks directory. Easy run just install the dependencies in ../requirements.txt

Weather forecasting ETL: See the Weather_API_ETL directory. you will need to activate your new Weather api and MongoDB credentials in config.py.

## Authors

- [@AhmadNader319](https://github.com/AhmadNader319)
Ahmed Nader

---
Aspiring Data Engineer | Python & SQL & AWS EnthusiastFeel free to connect or contribute to the repository!
