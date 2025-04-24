# transform.py
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the data."""
    try:
        required_columns = ["cols as objects/holds strings"] # Check these columns
        for col in required_columns:
            if col not in df.columns:
                raise KeyError(f"Missing column: {col}")

        df["col1"].fillna(value=df["col1"].mode()[0], inplace=True) # Fill missing 'col1'
        df["col2"] = df["col3"].astype('int64') # Convert 'col3' to int for 'col2'
        df.drop_duplicates(inplace=True) # Remove duplicates

        df.rename(columns={"ID": "id"}, inplace=True) # Rename 'ID' to 'id' or other columns 

        print("Data transformed.")
        return df
    except Exception as e:
        print(f"Transformation error: {e}")
        raise
