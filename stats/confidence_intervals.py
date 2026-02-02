#!/usr/bin/env python3


"""
stats/confidence_intervals.py

This module contains the confidence_intervals function which computes
confidence intervals for various metrics in a provided dataframe.
"""


# Importing Neccessary Packages #
import pandas as pd
from scipy.stats import norm, t


def confidence_intervals(dataframe):
    """
    Computes confidence intervals for various metrics from a provided dataframe.
    
    Parameters:
        dataframe (pd.DataFrame): The dataset to be analyzed.
        
    Returns:
        dict: A dictionary containing the computed confidence intervals for each metric.
    """
    pass