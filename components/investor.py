"""
Investor Analysis App

This module defines a Streamlit application for analyzing investor data.
It provides interactive visualizations and insights about an investor's investments
and related information.

The application utilizes the `streamlit` and `plotly` libraries for creating
the user interface and visualizations.

Usage:
    1. Instantiate the `Investor` class.
    2. Call the desired methods to display specific analysis results.

Author: Abhishek Gupta
Github: https://github.com/1abhi6
"""


import streamlit as st
import plotly.express as px

from analysis import Investor as InvestorAnalysis


class Investor:
    """A class representing an investor and providing analysis functions."""

    def __init__(self):
        """Initialize the Investor class."""
        self.investor_analysis = InvestorAnalysis()

    def recent_five_investments(self, investor_name):
        """Display the five most recent investments of the investor.

        Args:
            investor_name (str): The name of the investor.

        Returns:
            None
        """
        st.subheader(
            'Most Recent Investments',
            help=f"{investor_name}'s five most recent investments."
        )
        st.dataframe(self.investor_analysis.recent_five_investments(investor_name))

    def plot_biggest_investment(self, investor_name):
        """Plot a bar chart of the investor's biggest investments in terms of amount.

        Args:
            investor_name (str): The name of the investor.

        Returns:
            None
        """
        st.subheader(
            'Biggest Investments',
            help=f"{investor_name}'s biggest investments in terms of amount."
        )
        biggest_investment_df = self.investor_analysis.biggest_investment(investor_name)
        fig = px.bar(biggest_investment_df, x='name', y='amount')
        st.plotly_chart(fig, use_container_width=True)

    def plot_invested_sector(self, investor_name):
        """Plot a pie chart of the investor's most invested sector.

        Args:
            investor_name (str): The name of the investor.

        Returns:
            None
        """
        st.subheader(
            'Sector Invested in',
            help=f"{investor_name}'s most invested sector."
        )
        sector_df = self.investor_analysis.invested_sector(investor_name)
        fig = px.pie(sector_df, values='amount', names='vertical')
        st.plotly_chart(fig, use_container_width=True)

    def plot_invested_subsector(self, investor_name):
        """Plot a pie chart of the investor's most invested subsector.

        Args:
            investor_name (str): The name of the investor.

        Returns:
            None
        """
        st.subheader(
            'Subsector Invested in',
            help=f"{investor_name}'s most invested subsector."
        )
        subsector_df = self.investor_analysis.invested_subsector(investor_name)
        fig = px.pie(subsector_df, values='amount', names='subvertical')
        st.plotly_chart(fig, use_container_width=True)

    def plot_invested_city(self, investor_name):
        """Plot a pie chart of the investor's most invested city.

        Args:
            investor_name (str): The name of the investor.

        Returns:
            None
        """
        st.subheader(
            'City Invested in',
            help=f"{investor_name}'s most invested city."
        )
        city_df = self.investor_analysis.invested_city(investor_name)
        fig = px.pie(city_df, values='amount', names='city')
        st.plotly_chart(fig, use_container_width=True)

    def plot_invested_type(self, investor_name):
        """Plot a pie chart of the investor's investment types.

        Args:
            investor_name (str): The name of the investor.

        Returns:
            None
        """
        st.subheader(
            'Investment Type',
            help=f"{investor_name}'s stage of investments."
        )
        investment_type_df = self.investor_analysis.invested_type(investor_name)
        fig = px.pie(investment_type_df, values='amount', names='type')
        st.plotly_chart(fig, use_container_width=True)

    def plot_yoy_investment(self, investor_name):
        """Plot a line chart of the investor's year-on-year investments.

        Args:
            investor_name (str): The name of the investor.

        Returns:
            None
        """
        st.subheader(
            'YOY investment',
            help=f"{investor_name}'s year-on-year investments."
        )
        yoy_investment_df = self.investor_analysis.yoy_investment(investor_name)
        fig = px.line(yoy_investment_df, x="year", y="amount")
        st.plotly_chart(fig, use_container_width=True)

    def similar_investors(self,investor_name):
        """Displays the name of four random investors.

        Args:
            investor_name (str): The name of the investor.

        Returns:
            None
        """
        similar_investors = self.investor_analysis.get_similar_investors(investor_name)

        st.subheader(
            'Similar Investors',
            help=f"These investors have invested in the same sectors as {investor_name}."
        )
        st.write('')
        col0, col1, col2, col3 = st.columns(4)
        with col0:
            try:
                st.write(similar_investors[0])
            except IndexError:
                st.write('')
        with col1:
            try:
                st.write(similar_investors[1])
            except IndexError:
                st.write('')
        with col2:
            try:
                st.write(similar_investors[2])
            except IndexError:
                st.write('')
        with col3:
            try:
                st.write(similar_investors[3])
            except IndexError:
                st.write('')
