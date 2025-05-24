import pandas as pd
import json
import ast

def _transform(file_path = '/Users/ahmednader/Desktop/Code Repository/ETLs/flat_files_ingestion/parsed.csv'):
    df = pd.read_csv(file_path)
    print(type(df["metadata"].iloc[6]))
    metadata = ast.literal_eval(df["metadata"].iloc[6])
    print(metadata.keys())

