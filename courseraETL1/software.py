import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

# File definitions
tmpfile    = "temp.tmp"             # Temporary file (not used in this version)
logfile    = "logfile.txt"          # File to record ETL process logs
targetfile = "transformed_data.csv" # Final output CSV file

# ----------------------------
# Extraction Functions
# ----------------------------

def extract_from_csv(file_to_process):
    """Reads a CSV file and returns a DataFrame."""
    return pd.read_csv(file_to_process)

def extract_from_json(file_to_process):
    """Reads a JSON file and returns a DataFrame."""
    return pd.read_json(file_to_process, lines=True)

def extract_from_xml(file_to_process):
    """Parses an XML file and extracts data into a DataFrame."""
    rows = []
    tree = ET.parse(file_to_process)
    root = tree.getroot()

    # Iterate over each person element
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        rows.append({"name": name, "height": height, "weight": weight})
    
    return pd.DataFrame(rows)

def extract():
    """Scans the current directory for supported files and extracts their data."""
    dataframes = []

    # Extract data from all CSV files
    for csvfile in glob.glob("*.csv"):
        dataframes.append(extract_from_csv(csvfile))

    # Extract data from all JSON files
    for jsonfile in glob.glob("*.json"):
        dataframes.append(extract_from_json(jsonfile))

    # Extract data from all XML files
    for xmlfile in glob.glob("*.xml"):
        dataframes.append(extract_from_xml(xmlfile))

    # Combine all data into a single DataFrame
    return pd.concat(dataframes, ignore_index=True) if dataframes else pd.DataFrame()

# ----------------------------
# Transformation Function
# ----------------------------

def transform(data):
    """
    Converts height from inches to meters and weight from pounds to kilograms.
    Rounds values to 2 decimal places.
    """
    data['height'] = round(data['height'] * 0.0254, 2)       # 1 inch = 0.0254 meters
    data['weight'] = round(data['weight'] * 0.45359237, 2)   # 1 pound = 0.45359237 kilograms
    return data

# ---------------
