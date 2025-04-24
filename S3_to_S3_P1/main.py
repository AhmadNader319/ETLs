# main.py
# Orchestrates the ETL process: extracts data from raw S3, applies transformations, and loads the results to processed S3.
from config import get_s3_bucket, get_raw_s3_prefix, get_processed_s3_prefix
from extract import load_all_csvs_from_s3_prefix
from transform import clean_missing_values, create_revenue_column  # Import your desired transformations
from load import upload_dataframe_to_s3

if __name__ == "__main__":
    raw_bucket = get_s3_bucket()
    raw_prefix = get_raw_s3_prefix()
    processed_prefix = get_processed_s3_prefix() # Assuming this is in config

    print(f"Starting ETL process from s3://{raw_bucket}/{raw_prefix}")

    # --- Extraction ---
    raw_dataframes = load_all_csvs_from_s3_prefix(raw_bucket, raw_prefix)

    if raw_dataframes:
        print(f"Successfully extracted {len(raw_dataframes)} DataFrames.")
        print("Heads of the loaded raw DataFrames:")
        for i, df in enumerate(raw_dataframes):
            print(f"--- DataFrame {i+1} ---")
            print(df.head())
            if i >= 2:  # Print head of the first 3 for brevity
                print("(Showing heads of the first 3 DataFrames)")
                break

        # --- Transformation ---
        transformed_dataframes = []
        for df in raw_dataframes:
            print("Applying transformations...")
            df_cleaned = clean_missing_values(df, columns=['Age', 'BMI']) 
            transformed_dataframes.append(df_cleaned)
        print("Transformations complete.")

        # --- Loading ---
        print(f"Loading transformed data to s3://{raw_bucket}/{processed_prefix}")
        uploaded_files = []
        for i, df_to_upload in enumerate(transformed_dataframes):
            output_key = f"{processed_prefix}transformed_data_{i+1}.csv"
            upload_dataframe_to_s3(df_to_upload, output_key)
            uploaded_files.append(f"s3://{raw_bucket}/{output_key}")
        print("Loading complete.")

        # --- Print Loaded Files ---
        if uploaded_files:
            print("\nSuccessfully loaded the following files:")
            for file_path in uploaded_files:
                print(file_path)
        else:
            print("\nNo files were loaded to S3.")

        print("ETL process finished.")

    else:
        print("No dataframes found to process.")
