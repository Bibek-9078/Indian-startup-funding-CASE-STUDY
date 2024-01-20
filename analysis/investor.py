"""
Module: Investor Analysis

This module provides functionality to analyze investor data in the startup dataset.


Dependencies:
- itertools
- random
- pandas (pd)
- dataset (startup)

Note: The `startup` dataset is imported from the `dataset` module.

Author: Abhishek Gupta
Github: https://github.com/1abhi6
"""

import itertools
import random
import pandas as pd

from dataset import startup

class Investor:
    """
    Investor class for analyzing investor data in the startup dataset.

    Attributes:
        startup (pandas.DataFrame): The startup dataset.

    Methods:
        __init__: Initializes the Investor class.
        investor_list: Returns the list of investors.
        recent_five_investments: Returns the five most recent investments of an investor.
        biggest_investment: Returns the highest investment made by an investor.
        invested_sector: Returns the sectors invested in by an investor.
        invested_subsector: Returns the sub-sectors invested in by an investor.
        invested_city: Returns the cities invested in by an investor.
        invested_type: Returns the types of investments made by an investor.
        yoy_investment: Returns the year-on-year investments made by an investor.
        get_similar_investors: Returns a list of similar investors based on the investor's vertical.
    """

    def __init__(self):
        """
        Initialize the Investor class.
        """
        self.startup = startup

    def investor_list(self):
        """
        Returns the list of investors.

        Returns:
            list: Sorted list of investors.
        """
        return sorted(set(self.startup['investors'].str.split(',').sum()))[2:]

    def recent_five_investments(self, investor_name):
        """
        Returns the five most recent investments of an investor.

        Args:
            investor_name (str): Name of the investor.

        Returns:
            pandas.DataFrame: DataFrame containing the recent investments.
        """
        recent_investment = self.startup[
        self.startup['investors'].str.contains(investor_name)
        ].head()[
            ['date', 'name', 'vertical', 'city', 'investors', 'type', 'amount']
        ].rename(columns={
            'date': 'Date of Investment',
            'name': 'Startup Name',
            'vertical': 'Vertical',
            'city': 'City',
            'investors': 'Investors',
            'type': 'Type',
            'amount': 'Amount (In crore ₹)'
        })

        return recent_investment

    def biggest_investment(self, investor_name):
        """
        Returns the highest investment made by an investor.

        Args:
            investor_name (str): Name of the investor.

        Returns:
            pandas.DataFrame: DataFrame containing the highest investment.
        """
        investments = self.startup[self.startup['investors'].str.contains(investor_name)]
        investments_grouped = investments.groupby('name')['amount'].sum()
        sorted_investments = investments_grouped.sort_values(ascending=False)
        top_investments = sorted_investments.head().reset_index()

        return top_investments


    def invested_sector(self, investor_name):
        """
        Returns the sectors invested in by an investor.

        Args:
            investor_name (str): Name of the investor.

        Returns:
            pandas.DataFrame: DataFrame containing the invested sectors.
        """
        investments = startup[startup['investors'].str.contains(investor_name)]
        investments_grouped = investments.groupby('vertical')['amount'].sum()
        investments_sum_by_vertical = investments_grouped.reset_index()

        return investments_sum_by_vertical


    def invested_subsector(self, investor_name):
        """
        Returns the sub-sectors invested in by an investor.

        Args:
            investor_name (str): Name of the investor.

        Returns:
            pandas.DataFrame: DataFrame containing the invested sub-sectors.
        """
        investments = startup[startup['investors'].str.contains(investor_name)]
        investments_grouped = investments.groupby('subvertical')['amount'].sum()
        investments_sum_by_subvertical = investments_grouped.reset_index()

        return investments_sum_by_subvertical


    def invested_city(self, investor_name):
        """
        Returns the cities invested in by an investor.

        Args:
            investor_name (str): Name of the investor.

        Returns:
            pandas.DataFrame: DataFrame containing the invested cities.
        """
        investments = startup[startup['investors'].str.contains(investor_name)]
        investments_grouped = investments.groupby('city')['amount'].sum()
        investments_sum_by_city = investments_grouped.reset_index()

        return investments_sum_by_city


    def invested_type(self, investor_name):
        """
        Returns the types of investments made by an investor.

        Args:
            investor_name (str): Name of the investor.

        Returns:
            pandas.DataFrame: DataFrame containing the invested types.
        """
        investments = startup[startup['investors'].str.contains(investor_name)]
        investments_grouped = investments.groupby('type')['amount'].sum()
        investments_sum_by_type = investments_grouped.reset_index()

        return investments_sum_by_type


    def yoy_investment(self, investor_name):
        """
        Returns the year-on-year investments made by an investor.

        Args:
            investor_name (str): Name of the investor.

        Returns:
            pandas.DataFrame: DataFrame containing the year-on-year investments.
        """
        investments = startup[startup['investors'].str.contains(investor_name)]
        investments_grouped = investments.groupby('year')['amount'].sum()
        investments_sum_by_year = investments_grouped.reset_index()

        return investments_sum_by_year


    def get_similar_investors(self, investor_name):
        """
        Returns a list of similar investors based on the investor's vertical.

        Args:
            investor_name (str): Name of the investor.

        Returns:
            list: List of similar investors.
        """
        investor_df = startup[startup['investors'].str.contains(investor_name)]

        if investor_df.empty:
            return pd.Series()

        investor_vertical = investor_df['vertical'].iloc[0]

        vertical_df = self.startup[
            (self.startup['vertical'] == investor_vertical) &
            (~self.startup['investors'].str.contains('Undisclosed Investors', case=False))
        ]

        vertical_df = vertical_df[vertical_df['investors'] != investor_name]

        nested_list = sorted(vertical_df['investors'].str.split(','))
        flattened_list = list(itertools.chain.from_iterable(nested_list))
        try:
            return random.sample(flattened_list, 4)
        except ValueError:
            return flattened_list
