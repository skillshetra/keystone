#!/usr/bin/env python3


"""
pipeline/compute_metrics.py

This module contains the compute_all_metrics class which computes
various metrics from the provided dataframe.
"""


# Import necessary packages #
from stats.confidence_intervals import confidence_intervals
from stats.hypothesis import hypothesis_tests
from stats.multiple_testing import multiple_testing_correction
from stats.power import power_analysis
from stats.sequential import sequential_analysis
from metrics.aggregations import aggregations
from metrics.cuped import cuped_regression_analysis
from causal.regression import regression_causal_effects
from causal.diff_in_diff import diff_in_diff_causal_effects


class compute_all_metrics:
    """
    Computes various metrics from a provided dataframe.
    Attributes:
        dataframe (pd.DataFrame): The dataset to be analyzed.
    """
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.results = {}
    
    # Function to get all Metric values from dataset #
    def get_metrics(self):

        # Confidence Intervals #
        print("\033[34m[INFO] Computing Confidence Intervals.\033[0m")
        self.results['confidence_intervals'] = confidence_intervals(self.dataframe)

        # Hypothesis Testing #
        print("\033[34m[INFO] Computing Hypothesis Tests.\033[0m")
        self.results['hypothesis_tests'] = hypothesis_tests(self.dataframe)

        # Multiple Testing Correction #
        print("\033[34m[INFO] Applying Multiple Testing Correction.\033[0m")
        self.results['corrected_p_values'] = multiple_testing_correction(self.results['hypothesis_tests'])

        # Power Analysis #
        print("\033[34m[INFO] Computing Power Analysis.\033[0m")
        self.results['power_analysis'] = power_analysis(self.dataframe)

        # Sequential Analysis #
        print("\033[34m[INFO] Performing Sequential Analysis.\033[0m")
        self.results['sequential_results'] = sequential_analysis(self.dataframe)

        # Aggregations #
        print("\033[34m[INFO] Computing Aggregations.\033[0m")
        self.results['aggregations'] = aggregations(self.dataframe)

        # Cuped Regression #
        print("\033[34m[INFO] Performing Cuped Regression Analysis.\033[0m")
        self.results['cuped_results'] = cuped_regression_analysis(self.dataframe)

        # Causal Inference - Regression #
        print("\033[34m[INFO] Computing Causal Effects using Regression.\033[0m")
        self.results['regression_causal_effects'] = regression_causal_effects(self.dataframe)

        # Causal Inference - Difference in Differences #
        print("\033[34m[INFO] Computing Causal Effects using Difference in Differences.\033[0m")
        self.results['diff_in_diff_causal_effects'] = diff_in_diff_causal_effects(self.dataframe)

        # Returning Results #
        return self.results