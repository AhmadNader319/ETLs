# extract.py
import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    """Reads CSV file."""
    try:
        df = pd.read_csv(path)
        print(f"Loaded: {path}")
        return df
    except FileNotFoundError:
        print(f"File not found: {path}")
        raise
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV: {e}")
        raise
