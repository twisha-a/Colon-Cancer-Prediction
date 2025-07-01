# preprocessing.py
from sklearn.preprocessing import StandardScaler
import pandas as pd

def preprocess_data(df):
    """
    Cleans and preprocesses the data.
    """
    # Handle missing values (example: fill numeric columns with median)
    df.fillna(df.median(numeric_only=True), inplace=True)
    
    # Convert categorical columns to numeric if necessary (one-hot encoding example)
    categorical_cols = df.select_dtypes(include=['object']).columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    # Normalize/Standardize numeric features
    scaler = StandardScaler()
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    print("Data preprocessing completed.")
    return df

import pandas as pd

def filter_dataframe(df, site_prefix="C18.", year_column="Year of diagnosis", site_column="Primary Site - labeled"):
    """
    Filters a DataFrame based on the following conditions:
    1. The site_column starts with a specified prefix.
    2. The year_column contains numeric years > 2014 or matches specific strings ("1975-2021").

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        site_prefix (str): The prefix for filtering the site_column (default: "C18.").
        year_column (str): The column name containing year-related data (default: "Year of diagnosis").
        site_column (str): The column name for site filtering (default: "Primary Site - labeled").

    Returns:
        pd.DataFrame: A filtered DataFrame based on the conditions.
    """
    # Ensure the required columns exist
    if site_column not in df.columns or year_column not in df.columns:
        raise ValueError(f"Columns '{site_column}' and/or '{year_column}' are missing in the DataFrame.")

    # Filter rows where the site_column starts with the specified prefix
    filtered_df = df[df[site_column].str.startswith(site_prefix, na=False)]

    # Filter rows where the year_column meets the specified conditions
    filtered_df = filtered_df[
        (filtered_df[year_column].apply(lambda x: x.isdigit() and int(x) > 2014)) |
        (filtered_df[year_column] == "1975-2021")
    ]

    return filtered_df
