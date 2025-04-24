ETLs & ELTs Repository
This repository contains data engineering projects focusing on ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) processes. These projects demonstrate data pipeline implementations for different data sources and destinations.

Projects
CSV to PostgreSQL ETL: This project extracts data from local CSV files, transforms it, and loads it into a local PostgreSQL database.  It showcases a traditional ETL approach.

S3 to S3 ELT: This project extracts multiple raw CSV files from an S3 bucket, loads them to another S3 location, and then transforms the data. This project demonstrates an ELT approach, leveraging S3 for the loading phase.

Repository Structure
ETLs&ELTs/
├── CSV_to_Postgresql_ETL/
│   ├── config.py
│   ├── extract.py
│   ├── load.py
│   ├── main.py
│   ├── transform.py
│   ├── utils.py
├── S3_to_S3_P1/
│   ├── config.py
│   ├── extract.py
│   ├── load.py
│   ├── main.py
│   ├── transform.py
│   ├── utils.py
├── README.md
├── requirements.txt
└── shared_utils/

Technologies Used:
Python

Pandas

PostgreSQL

Amazon S3

Boto3

Installation
Clone the repository:

git clone <repository_url>
cd ETLs&ELTs

Install the required Python packages:

pip install -r requirements.txt

Usage
Each project has its own set of instructions. Please refer to the project-specific directories for details.

CSV to PostgreSQL ETL: See the CSV_to_Postgresql_ETL directory.  You will need a running PostgreSQL instance and to configure the database connection in config.py.

S3 to S3 ELT: See the S3_to_S3_P1 directory.  You will need an AWS account with S3 access and to configure your S3 buckets and credentials in config.py.

Author

Ahmed Nader
Aspiring Data Engineer | Python & SQL & AWS EnthusiastFeel free to connect or contribute to the repository!
