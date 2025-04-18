import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    """Reads CSV from the provided path."""
    try:
        df = pd.read_csv(path)
        print(f"Successfully loaded CSV from: {path}")
        return df
    except FileNotFoundError:
        print(f"File not found: {path}")
        raise
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV: {e}")
        raise
