# config.py
# Defines configuration variables for S3 bucket names and prefixes for raw and processed data.
import boto3 as boto

BUCKET_NAME = "bucket_name"
RAW_PREFIX = "raw/dataset/path"
PROCESSED_PREFIX = "processed/dataset/path"

def get_s3_bucket():
    # Returns the configured S3 bucket name.
    return BUCKET_NAME

def get_raw_s3_prefix():
    # Returns the configured prefix for raw data in S3.
    return RAW_PREFIX

def get_processed_s3_prefix():
    # Returns the configured prefix for processed data in S3.
    return PROCESSED_PREFIX
