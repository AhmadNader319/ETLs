# Imports
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Define DAG arguments
default_args = {
    'owner': 'Data Engineer',
    'start_date': datetime(2025, 8, 1),
    'email': ['data.engineer@example.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1),
)

# Define the base path for your files
# This path is based on your Airflow HOME directory
base_path = '/Users/ahmednader/airflow/dags/finalassignment'

# Task 1: Unzip the data
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command=f'tar -zxvf {base_path}/tolldata.tgz -C {base_path}/',
    dag=dag,
)

# Task 2: Extract data from CSV
# Fields to extract: Rowid, Timestamp, Anonymized Vehicle number, Vehicle type
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command=f'cut -d"," -f1,2,3,4 {base_path}/vehicle-data.csv > {base_path}/staging/csv_data.csv',
    dag=dag,
)

# Task 3: Extract data from TSV
# Fields to extract: Number of axles, Tollplaza id, Tollplaza code
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command=f'cut -f5,6,7 {base_path}/tollplaza-data.tsv > {base_path}/staging/tsv_data.csv',
    dag=dag,
)

# Task 4: Extract data from fixed-width file
# Fields to extract: Type of Payment code, Vehicle Code
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command=f'cut -c 59-62,63-67 {base_path}/payment-data.txt > {base_path}/staging/fixed_width_data.csv',
    dag=dag,
)

# Task 5: Consolidate data
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command=f'paste -d"," {base_path}/staging/csv_data.csv {base_path}/staging/tsv_data.csv {base_path}/staging/fixed_width_data.csv > {base_path}/staging/extracted_data.csv',
    dag=dag,
)

# Task 6: Transform data
# Transform 'Vehicle type' field to capital letters. This is the 4th column.
transform_data = BashOperator(
    task_id='transform_data',
    bash_command=f"""awk 'BEGIN{{FS=OFS=","}}{{$4=toupper($4)}}1' {base_path}/staging/extracted_data.csv > {base_path}/staging/transformed_data.csv""",
    dag=dag,
)

# Define the task pipeline
unzip_data >> [extract_data_from_csv, extract_data_from_tsv, extract_data_from_fixed_width] >> consolidate_data >> transform_data
