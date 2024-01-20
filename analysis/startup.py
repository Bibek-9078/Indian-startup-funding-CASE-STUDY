"""
Module: Startup Analysis

This module provides classes and methods for analyzing startup data.

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


class Startup:
    """
    Startup class for retrieving information and performing operations related to startups.

    Attributes:
        startup (pandas.DataFrame): DataFrame containing startup data.

    Methods:
        __init__: Initializes the Startup class with the startup data.
        list_of_startups: Returns a list of startup names.
        sector: Returns the sector of a given startup.
        subsector: Returns the subsector of a given startup.
        location: Returns the location (city) of a given startup.
        stage: Returns the stage of a given startup.
        investors: Returns the investors of a given startup.
        investment_date: Returns the investment date of a given startup.
        funding: Returns the total funding amount of a given startup.
        similar_startups: Returns a list of similar startups based on the vertical
        of a given startup.
    """

    def __init__(self):
        """
        Initialize the Startup class with the startup data.
        """
        self.startup = startup

    def list_of_startups(self):
        """
        Returns a list of startup names.

        Returns:
            list: A list of startup names.
        """
        return list(startup['name'].sort_values().unique())[1:]

    def sector(self, startup_name):
        """
        Returns the sector of a given startup.

        Args:
            startup_name (str): Name of the startup.

        Returns:
            str: The sector of the startup.
        """
        return self.startup[self.startup['name'] == startup_name]['vertical'].values[0]

    def subsector(self, startup_name):
        """
        Returns the subsector of a given startup.

        Args:
            startup_name (str): Name of the startup.

        Returns:
            str: The subsector of the startup.
        """
        return self.startup[self.startup['name'] == startup_name]['subvertical'].values[0]

    def location(self, startup_name):
        """
        Returns the location (city) of a given startup.

        Args:
            startup_name (str): Name of the startup.

        Returns:
            str: The location (city) of the startup.
        """
        return self.startup[self.startup['name'] == startup_name]['city'].values[0]

    def stage(self, startup_name):
        """
        Returns the stage of a given startup.

        Args:
            startup_name (str): Name of the startup.

        Returns:
            str: The stage of the startup.
        """
        return self.startup[self.startup['name'] == startup_name]['type'].values[0]

    def investors(self, startup_name):
        """
        Returns the investors of a given startup.

        Args:
            startup_name (str): Name of the startup.

        Returns:
            str: The investors of the startup.
        """
        return self.startup[self.startup['name'] == startup_name]['investors'].values[0]

    def investment_date(self, startup_name):
        """
        Returns the investment date of a given startup.

        Args:
            startup_name (str): Name of the startup.

        Returns:
            str: The investment date of the startup.
        """
        return self.startup[self.startup['name'] == startup_name]['date'].values[0]

    def funding(self, startup_name):
        """
        Returns the total funding amount of a given startup.

        Args:
            startup_name (str): Name of the startup.

        Returns:
            float: The total funding amount of the startup.
        """
        company = self.startup[self.startup['name'] == startup_name]
        return company.groupby('name')['amount'].sum().values[0]

    def similar_startups(self, startup_name):
        """
        Returns a list of similar startups based on the vertical of a given startup.

        Args:
            startup_name (str): Name of the startup.

        Returns:
            list: A list of similar startup names.
        """
        vertical = startup.loc[startup['name'] == startup_name, 'vertical'].values[0]

        temp_startups = startup.loc[startup['vertical'] == vertical, 'name'].unique()

        similar_startups = []
        for company in temp_startups:
            if company != startup_name:
                similar_startups.append(company)

        return similar_startups
