# extract.py
# Contains functions to load CSV files from S3, either a single file or all files under a given prefix.
import boto3
import pandas as pd
from io import StringIO

def load_csv_from_s3(bucket_name, key):
    # Loads a single CSV file from the specified S3 bucket and key into a pandas DataFrame.
    s3_client = boto3.client('s3')
    response = s3_client.get_object(
        Bucket = bucket_name,
        Key = key
    )
    return pd.read_csv(StringIO(response['Body'].read().decode('utf-8')))

def load_all_csvs_from_s3_prefix(bucket_name, prefix):
    # Loads all CSV files with the given prefix from the specified S3 bucket into a list of pandas DataFrames.
    s3_client = boto3.client('s3')
    response = s3_client.list_objects_v2(
        Bucket = bucket_name,
        Prefix = prefix
    )
    dfarr = []
    if 'Contents' in response:
        for obj_data in response['Contents']:
            if obj_data['Key'].endswith('.csv'):
                df = load_csv_from_s3(bucket_name, obj_data['Key'])
                if df is not None:
                    dfarr.append(df)
    return dfarr
