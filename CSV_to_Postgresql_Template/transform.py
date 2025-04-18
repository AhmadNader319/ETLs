import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Performs cleaning and preprocessing on the required dataset."""
    try:
        required_columns = ["cols as objects/holds strings"]
        for col in required_columns:
            if col not in df.columns:
                raise KeyError(f"Missing required column: {col}")

        df["col1"].fillna(value=df["col1"].mode()[0], inplace=True)
        df["col2"] = df["col3"].astype('int64')
        df.drop_duplicates(inplace=True)

        df.rename(columns={
            "ID": "id"
        }, inplace=True)

        print("Data transformation successful.")
        return df
    except Exception as e:
        print(f"Error during transformation: {e}")
        raise
