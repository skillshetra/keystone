#!/usr/bin/env python3


"""
run_analysis.py

This module defines the Key_Stone_Analysis class which orchestrates
the full data analysis pipeline:
- Load data
- Compute metrics
- Persist results
"""

# Import necessary packages #
from db import get_products
from pipeline.compute_metrics import compute_all_metrics
from pipeline.persist_results import save_results


class Key_Stone_Analysis:
    # Main class to run the Keystone data analysis pipeline #

    def __init__(self):
        """
        Initialize the analysis class.
        You can set up logging or other configs here if needed.
        """
        print("\033[34m[INFO] Initializing Keystone Analysis...\033[0m")
        self.dataframe = None
        self.metrics = None

    def get_dataframe(self):
        """
        Fetch the product data from the database.
        Returns:
            pd.DataFrame: Loaded product data
        """
        print("\033[34m[INFO] Fetching data from the database...\033[0m")
        self.dataframe = get_products()
        print(f"\033[32m[INFO] Dataframe loaded with {len(self.dataframe)} rows.\033[0m")
        return self.dataframe

    def compute_metrics(self):
        """
        Compute all metrics on the loaded dataframe.
        Returns:
            dict: Computed metrics
        """
        if self.dataframe is None:
            raise ValueError("Dataframe not loaded. Call get_dataframe() first.")

        print("\033[34m[INFO] Computing metrics...\033[0m")
        self.metrics = compute_all_metrics(self.dataframe).get_metrics()
        print("\033[32m[INFO] Metrics computation completed.\033[0m")
        return self.metrics

    def persist_results(self):
        """
        Save computed metrics to the database or file.
        """
        if self.metrics is None:
            raise ValueError("Metrics not computed. Call compute_metrics() first.")

        print("\033[34m[INFO] Persisting results...\033[0m")
        save_results(self.metrics)
        print("\033[32m[INFO] Results persisted successfully.\033[0m")

    def run(self):
        """
        Execute the full analysis pipeline: load data, compute metrics, persist results.
        """
        self.get_dataframe()
        self.compute_metrics()
        self.persist_results()
        print("\n" + "="*60)
        print("*" * 5 + " ✅  Keystone Analysis Completed Successfully! ✅ " + "*" * 5)
        print("="*60 + "\n")