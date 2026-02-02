#!/usr/bin/env python3


"""
pipeline/compute_metrics.py

This module contains the compute_all_metrics class which computes
various metrics from the provided dataframe.
"""

# Import necessary packages #
from stats.confidence_intervals import *
from stats.hypothesis import *
from stats.multiple_testing import *
from stats.power import *
from stats.sequential import *
from metrics.aggregations import *
from metrics.base import *
from metrics.cuped import *
from causal.regression import *
from causal.diff_in_diff import *


class compute_all_metrics:
    """
    Computes various metrics from a provided dataframe.
    Attributes:
        dataframe (pd.DataFrame): The dataset to be analyzed.
    """
    def __init__(self, dataframe):
        self.dataframe = dataframe
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n") # Remove all this
    
    # Function to get all Metric values from dataset #
    def get_metrics(self):
        metrics = 0
        return metrics

# Creating Dataframe #
# dataframe = get_products()
# print(dataframe.info())
# print(dataframe.describe())
# print(dataframe.isnull().sum())

# print(dataframe['product_id'])
# print(dataframe['category'])
# print(dataframe['discounted_price'])
# print(dataframe['actual_price'])
# print(dataframe['discount_percentage'])
# print(dataframe['rating'])
# print(dataframe['rating_count'])
# print(dataframe['user_id'])
# print(dataframe['user_name'])
# print(dataframe['review_id'])