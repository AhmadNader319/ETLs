import io
import zipfile as zf
import os
import pandas as pd
import json
def _extract(file_path = '/Users/ahmednader/Desktop/Code Repository/ETLs/flat_files_ingestion/cord19_mini.zip'):
    
    extracted_path = '/Users/ahmednader/Desktop/Code Repository/ETLs/flat_files_ingestion/extracted_files'
    output_path = '/Users/ahmednader/Desktop/Code Repository/ETLs/flat_files_ingestion/parsed.csv'
    os.makedirs(extracted_path, exist_ok=True)

#    print(help(zf.ZipFile))
    with zf.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extracted_path)
        json_file_list = zip_ref.namelist()
#        print(json_file_list)
    
    df = _get_dataframe(extracted_path, json_file_list)
    print(df.head())
    
    df.to_csv(output_path, index=False)
    
    
def _get_dataframe(directory_path, file_name_list):
    df = pd.DataFrame()
    data = []
#    help(df)
    for path in file_name_list:
        file_path = f"{directory_path}/{path}"
        with open(file_path, 'r') as file:
            curr = json.load(file)
            
            combined = {"paper_id": curr["paper_id"], "metadata": curr["metadata"]}
            print(combined)
            data.append(combined)
    df = pd.DataFrame(data)
    return df
            
            
            
    
    
