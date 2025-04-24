# load.py
# Contains functions to upload pandas DataFrames and local files to S3.
import boto3
import pandas as pd
from io import StringIO
from config import get_s3_bucket

def upload_dataframe_to_s3(dataframe, key):
    # Uploads a pandas DataFrame to an S3 bucket as a CSV file.
    bucket_name = get_s3_bucket()
    csv_buffer = StringIO()
    dataframe.to_csv(csv_buffer, index=False, encoding='utf-8')
    csv_buffer.seek(0)
    s3_client = boto3.client('s3')
    s3_client.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=csv_buffer.getvalue().encode('utf-8'),
        ContentType='text/csv'
    )
    print(f"DataFrame successfully uploaded to s3://{bucket_name}/{key}")

def upload_file_to_s3(local_file_path, key):
    # Uploads a local file to an S3 bucket.
    bucket_name = get_s3_bucket()
    s3_client = boto3.client('s3')
    with open(local_file_path, 'rb') as f:
        s3_client.upload_fileobj(f, bucket_name, key)
    print(f"File '{local_file_path}' successfully uploaded to s3://{bucket_name}/{key}")
