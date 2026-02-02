#!/usr/bin/env python3
"""
db.py

Handles connection to Supabase and fetching product data.
"""

# Import necessary packages #
from os import environ as env
from pandas import DataFrame
from supabase import create_client, Client

# Get Supabase URL and Key from environment variables (or use defaults) #
url: str = env.get("SUPABASE_URL")
key: str = env.get("SUPABASE_KEY")

# Create a Supabase database client #
database: Client = create_client(url, key)


def get_products() -> DataFrame:
    """
    Fetch all product records from the Supabase 'products' table
    and return as a pandas DataFrame.

    Returns:
        pd.DataFrame: Dataframe containing all product records.
    """
    print("\033[34m[INFO] Fetching products from the database...\033[0m")
    
    try:
        response = database.table("products").select("*").execute()
        df = DataFrame(response.data)
        print(f"\033[32m[✔] Dataframe is ready with {len(df)} rows!\033[0m")
        return df
    except Exception as e:
        print(f"\033[31m[ERROR] Failed to fetch products: {e}\033[0m")
        return DataFrame()  # return empty dataframe if fetch fails #