# transform.py
# functions data transformation steps, such as merging:
# Cleaning missing values, standardizing units and dates,
# Creating new features like revenue, profit margin, and category.
import pandas as pd

def merge_dataframes(df1, df2, on, how='inner'):
    # Merges two pandas DataFrames based on specified columns and join type.
    merged_df = pd.merge(df1, df2, on=on, how=how)
    return merged_df

def clean_missing_values(df, columns, strategy='dropna', fill_value=None):
    # Handles missing values in specified columns using either dropna or fillna strategy.
    if isinstance(columns, str):
        columns = [columns]
    if strategy == 'dropna':
        cleaned_df = df.dropna(subset=columns)
    elif strategy == 'fillna':
        cleaned_df = df.fillna(value={col: fill_value for col in columns})
    return cleaned_df

def standardize_units(df, column, conversion_factor):
    # Standardizes units in a specified column by applying a conversion factor.
    df[column] = df[column] * conversion_factor
    return df

def standardize_dates(df, column, format):
    # Standardizes dates in a specified column to a consistent format.
    df[column] = pd.to_datetime(df[column]).dt.strftime(format)
    return df
