# ETL and Data Pipelines with Apache Airflow

This repository contains the code for an ETL (Extract, Transform, Load) data pipeline built using Apache Airflow. The project was completed as part of the "ETL and Data Pipelines with Airflow" course.

The pipeline processes toll data from a compressed archive, performs extraction and consolidation of data from various file formats (CSV, TSV, and fixed-width), and finally transforms the data before loading it into a final file.

## Project Files

* `ETL_toll_data.py`: The main DAG file that defines the entire ETL pipeline.
* `tolldata.tgz`: The compressed data file used as the source for the pipeline.
* `airflow.cfg`, `airflow.db`, `logs/`: Standard Airflow configuration and working files.

## Visuals of the Pipeline

Here are some key screenshots from the project, demonstrating the DAG's structure and its successful execution.

### DAG Arguments and Definitions
A visualization of the DAG arguments and its definition.

![DAG Arguments](images_steps/dag_args.png)
![DAG Definition](images_steps/dag_definition.png)

### Task Definitions
Screenshots of the individual task configurations.

![Unzip Data Task](images_steps/unzip_data.png)
![Extract Data from CSV](images_steps/extract_data_from_csv.png)
![Extract Data from TSV](images_steps/extract_data_from_tsv.png)
![Transform Task](images_steps/transform.png)
![Consolidate Data Task](images_steps/consolidate_data.png)

### The Task Pipeline
The full pipeline, showing the dependencies between tasks.

![Task Pipeline](images_steps/task_pipeline.png)

### DAG in the Airflow UI
Proof of the DAG being submitted and successfully run in the Airflow UI.

![Submitted DAG](images_steps/submit_dag.png)
![Unpaused and Triggered DAG](images_steps/unpause_trigger_dag.png)
![DAG Task States](images_steps/dag_tasks.png)
![DAG Runs History](images_steps/dag_runs.png)

## Course Completion Certificate

[View Certificate](Certificate/ETL%20and%20Data%20Pipelines%20with%20Airflow.pdf)

