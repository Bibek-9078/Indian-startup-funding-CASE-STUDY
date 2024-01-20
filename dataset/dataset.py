"""
Module: Startup Data Processing

This module reads a cleaned startup dataset from a CSV file and performs
data processing operations on it.

Dependencies:
- pandas (pd)

Author: Abhishek Gupta
Github: https://github.com/1abhi6
"""

import pandas as pd

startup = pd.read_csv('dataset/startup_cleaned.csv')
startup['date'] = pd.to_datetime(startup['date'])
startup['year'] = startup['date'].dt.year
startup['month'] = startup['date'].dt.month
