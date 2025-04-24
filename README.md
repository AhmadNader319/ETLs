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

## Authors

- [@AhmadNader319](https://github.com/AhmadNader319)
Ahmed Nader

---
Aspiring Data Engineer | Python & SQL & AWS EnthusiastFeel free to connect or contribute to the repository!
