#!/usr/bin/env python3


"""
stats/hypothesis.py

This module contains the hypothesis_tests function which performs various
statistical hypothesis tests on a provided dataframe.
"""


# Importing Neccessary Packages #
import pandas as pd
from scipy.stats import ttest_ind, normaltest, f_oneway


def hypothesis_tests(dataframe):
    """
    Performs various statistical hypothesis tests on a provided dataframe.
    
    Parameters:
        dataframe (pd.DataFrame): The dataset to be analyzed.
        
    Returns:
        dict: A dictionary containing the results of the hypothesis tests.
    """
    pass