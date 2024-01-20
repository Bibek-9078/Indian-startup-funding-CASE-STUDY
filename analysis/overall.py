"""
Module: Overall Analysis

This module provides classes and methods to analyze startup investment data.
It contains the `Overall` class which offers various methods to calculate and
analyze different aspects of the startup investments.

Dependencies:
- pandas (pd)
- dataset (startup)

Note: The `startup` dataset is imported from the `dataset` module.

Author: Abhishek Gupta
Github: https://github.com/1abhi6
"""

import pandas as pd

from dataset import startup

class Overall:
    """
    This class provides various methods to analyze the startup investment data.
    """

    def __init__(self):
        self.startup = startup

    def total_invested_amount(self):
        """
        Calculates the total invested amount across all startups.

        Returns:
            float: Total invested amount.
        """
        return round(self.startup['amount'].sum())

    def max_amount_infused(self):
        """
        Finds the maximum amount infused by a single investor in a startup.

        Returns:
            float: Maximum amount infused.
        """
        result = self.startup.groupby('name')['amount'].max()
        sorted_result = result.sort_values(ascending=False)
        max_value = sorted_result.head(1).values[0]

        return max_value


    def avg_ticket_size(self):
        """
        Calculates the average ticket size (investment amount) per startup.

        Returns:
            float: Average ticket size.
        """
        return self.startup.groupby('name')['amount'].sum().mean()

    def total_funded_startup(self):
        """
        Counts the total number of funded startups.

        Returns:
            int: Total number of funded startups.
        """
        return self.startup['name'].nunique()

    def total_funding_mom(self):
        """
        Calculates the total funding amount on a month-by-month basis.

        Returns:
            pandas.DataFrame: DataFrame containing the total funding amount for each month.
        """
        temp_df = startup.groupby(['year', 'month'])['amount'].sum().reset_index()
        temp_df['MM-YYYY'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
        temp_df.rename(columns={
            'amount': 'Total Funding (In Crore Rs.)'
        }, inplace=True)

        return temp_df

    def total_funded_startup_mom(self):
        """
        Calculates the total number of funded startups on a month-by-month basis.

        Returns:
            pandas.DataFrame: DataFrame containing the total number of funded startups for each
            month.
        """
        temp_df = startup.groupby(['year', 'month'])['amount'].count().reset_index()
        temp_df['MM-YYYY'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

        temp_df.rename(columns={
            'amount': 'Total Funded Startups'
        }, inplace=True)

        return temp_df

    def most_funded_sector(self):
        """
        Finds the sectors with the highest total funding amounts.

        Returns:
            pandas.DataFrame: DataFrame containing the most funded sectors and
            their corresponding amounts.
        """
        temp_df = startup.groupby('vertical')['amount'].sum().reset_index()
        most_funded_sectors = temp_df[temp_df['amount'] != 0.0].sort_values(
            by='amount',
            ascending=False
        ).head(10)

        most_funded_sectors['amount'] = round(most_funded_sectors['amount'], 2)

        return most_funded_sectors

    def most_funded_type(self):
        """
        Finds the startup types with the highest total funding amounts.

        Returns:
            pandas.DataFrame: DataFrame containing the most funded startup types and
            their corresponding amounts.
        """
        temp_df = startup.groupby('type')['amount'].sum().reset_index()
        most_funded_type = temp_df[temp_df['amount'] != 0.0].sort_values(
            by='amount',
            ascending=False
        ).head(10)

        return most_funded_type

    def most_funded_cities(self):
        """
        Finds the cities with the highest total funding amounts.

        Returns:
            pandas.DataFrame: DataFrame containing the most funded cities and
            their corresponding amounts.
        """
        temp_df = startup.groupby('city')['amount'].sum().reset_index()
        most_funded_city = temp_df[temp_df['amount'] != 0]

        # Add the amount of Bengaluru to Bangalore
        most_funded_city.loc[most_funded_city['city'] == 'Bangalore', 'amount'] += \
            most_funded_city.loc[most_funded_city['city'] == 'Bengaluru', 'amount'].values[0]

        # Drop the Bengaluru row
        most_funded_city = most_funded_city[most_funded_city['city'] != 'Bengaluru']

        most_funded_city = most_funded_city.sort_values(by='amount', ascending=False).head(10)
        most_funded_city['amount'] = round(most_funded_city['amount'], 2)

        return most_funded_city

    def most_funded_startups_yoy(self):
        """
        Finds the startups with the highest funding amounts on a year-over-year basis.

        Returns:
            pandas.DataFrame: DataFrame containing the most funded startups for
            each year and their corresponding amounts.
        """
        most_funded_startup_yoy = startup.groupby(['year', 'name'])['amount'].sum() \
            .sort_values(ascending=False).reset_index().drop_duplicates(
            'year',
            keep='first'
        ).sort_values(by='year')

        most_funded_startup_yoy.rename(columns={
            'year': 'Year',
            'name': 'StartUp Name',
            'amount': 'Amount (In Crore Rs)'
        }, inplace=True)

        return most_funded_startup_yoy

    def top_investors(self):
        """
        Finds the top investors based on their total investment amounts.

        Returns:
            pandas.DataFrame: DataFrame containing the top investors and
            their corresponding amounts.
        """
        # New dataframe with separate rows for each investor
        investor_list = []
        for _, row in startup.iterrows():
            investors = row['investors'].split(', ')
            for investor in investors:
                investor_list.append({
                    'date': row['date'],
                    'name': row['name'],
                    'vertical': row['vertical'],
                    'subvertical': row['subvertical'],
                    'city': row['city'],
                    'investors': investor,
                    'type': row['type'],
                    'amount': row['amount'],
                    'year': row['year'],
                    'month': row['month']
                })

        new_df = pd.DataFrame(investor_list)

        top_investors = new_df.groupby('investors')['amount'].sum().reset_index()

        # Add the amounts of SoftBank Group and Softbank and store the result in SoftBank Group
        softbank_group_amount = top_investors.loc[
            top_investors['investors'] == 'SoftBank Group', 'amount'
        ].values[0]

        softbank_amount = top_investors.loc[
            top_investors['investors'] == 'Softbank', 'amount'
        ].values[0]

        updated_amount = softbank_group_amount + softbank_amount
        top_investors.loc[top_investors['investors'] == 'SoftBank Group', 'amount'] = updated_amount

        # Drop the Softbank row
        top_investors = top_investors[top_investors['investors'] != 'Softbank']

        top_investors = top_investors.sort_values(by='amount', ascending=False).head(10)
        return top_investors

    def funding_amount_year_month(self):
        """
        Calculates the funding amount on a year-by-month basis.

        Returns:
            pandas.DataFrame: Pivot table containing the funding amounts for each year and month.
        """
        # Aggregate funding amount by year and month
        df_agg = startup.groupby(['year', 'month'])['amount'].sum().reset_index()

        # Create pivot table
        pivot_table = df_agg.pivot(index='year', columns='month', values='amount')

        return pivot_table
