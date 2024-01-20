"""
Module: Overall Analysis Component

This module provides classes for analyzing and visualizing data related to Indian startup funding.
It utilizes the Streamlit library for creating an interactive web-based dashboard.

Classes:
- PlotHorizontalBarChart: Class for plotting a horizontal bar chart.
- PlotLineChart: Class for plotting a line chart.
- SubHeader: Class for displaying a subheader with a tooltip.
- Overall: Class for handling overall analysis and plotting of startup data.

The module also imports the `Overall` class from the `analysis` module,
which contains the actual data analysis functions.

Author: Abhishek Gupta
Github: https://github.com/1abhi6
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from analysis import Overall as OverallAnalysis


class PlotHorizontalBarChart:
    """Class to plot a horizontal bar chart."""

    def __init__(
            self,
            x_axis: pd.Series,
            y_axis: pd.Series,
            layout_title,
            layout_x_axis: str,
            layout_yaxis: str) -> None:
        """
        Initialize the PlotHorizontalBarChart class.

        Args:
            x_axis (pd.Series): The x-axis data.
            y_axis (pd.Series): The y-axis data.
            layout_title: The title of the chart.
            layout_x_axis: The label for the x-axis.
            layout_yaxis: The label for the y-axis.
        """
        fig = go.Figure(data=go.Bar(
            x=x_axis,
            y=y_axis,
            orientation='h'
        ))

        fig.update_layout(
            title=layout_title,
            xaxis=dict(title=layout_x_axis),
            yaxis=dict(title=layout_yaxis)
        )

        st.plotly_chart(fig, use_container_width=True)


class PlotLineChart:
    """Class to plot a line chart."""

    def __init__(self, temp_df: str, x_axis: str, y_axis: str, layout_title: str) -> None:
        """
        Initialize the PlotLineChart class.

        Args:
            temp_df (str): The dataframe containing the chart data.
            x_axis (str): The column name for the x-axis.
            y_axis (str): The column name for the y-axis.
            layout_title (str): The title of the chart.
        """
        fig = px.line(
            temp_df,
            x=x_axis,
            y=y_axis,
            title=layout_title
        )

        st.plotly_chart(fig, use_container_width=True)


class SubHeader:
    """Class to display a subheader with a tooltip."""

    def __init__(self, title: str, tooltip: str) -> None:
        """
        Initialize the SubHeader class.

        Args:
            title (str): The title of the subheader.
            tooltip (str): The tooltip text.
        """
        st.subheader(title, help=tooltip)


class Overall:
    """Class to handle overall analysis and plotting of startup data."""

    def __init__(self) -> None:
        """Initialize the Overall class."""
        self.overall_analysis = OverallAnalysis()

    def plot_total_funding_mom(self):
        """Plot the total amount of funding in Indian startups month over month."""
        temp_df = self.overall_analysis.total_funding_mom()

        SubHeader(
            title='Total Amount of Funding in Indian Startups MoM',
            tooltip='Total Amount of Funding in Indian Startups on the basis of month and year'
        )

        PlotLineChart(
            temp_df=temp_df,
            x_axis='MM-YYYY',
            y_axis='Total Funding (In Crore Rs.)',
            layout_title='Total funding in Startups in MM-YYYY'
        )

    def plot_total_funded_startup_mom(self):
        """Plot the total number of funded Indian startups month over month."""
        temp_df = self.overall_analysis.total_funded_startup_mom()

        SubHeader(
            title='Total Funded Indian Startups MoM',
            tooltip='Total Funded Indian Startups on the basis of month and year'
        )

        PlotLineChart(
            temp_df=temp_df,
            x_axis='MM-YYYY',
            y_axis='Total Funded Startups',
            layout_title='Total Funded Startups in MM-YYYY'
        )

    def plot_most_funded_sector(self):
        """Plot the top 10 most funded sectors between 2015 to 2020."""
        most_funded_sectors = self.overall_analysis.most_funded_sector()

        SubHeader(
            title='Most Funded Sectors',
            tooltip='Top 10 Most Funded Sectors between 2015 to 2020'
        )

        PlotHorizontalBarChart(
            x_axis=most_funded_sectors['amount'],
            y_axis=most_funded_sectors['vertical'],
            layout_title='Top 10 Most Funded Sectors',
            layout_x_axis='Funding Amount (In Crore Rs)',
            layout_yaxis='Sector'
        )

    def plot_most_funded_type(self):
        """Plot the top 10 most funded types of rounds in startup funding."""
        most_funded_type = self.overall_analysis.most_funded_type()

        SubHeader(
            title='Most Funded Type',
            tooltip='Top 10 most funded type of round in startup funding'
        )

        PlotHorizontalBarChart(
            x_axis=most_funded_type['amount'],
            y_axis=most_funded_type['type'],
            layout_title='Top 10 Most Funded Types of Rounds',
            layout_x_axis='Funding Amount (In Crore Rs)',
            layout_yaxis='Type of Investment'
        )

    def plot_most_funded_cities(self):
        """Plot the top 10 most funded cities in startup funding."""
        most_funded_city = self.overall_analysis.most_funded_cities()

        SubHeader(
            title='Most Funded Cities',
            tooltip='Top 10 most funded cities in startup funding'
        )

        PlotHorizontalBarChart(
            x_axis=most_funded_city['amount'],
            y_axis=most_funded_city['city'],
            layout_title='Most Funded Cities',
            layout_x_axis='Funding Amount (In Crore Rs)',
            layout_yaxis='City'
        )

    def plot_most_funded_startups_yoy(self):
        """Plot the top 10 most funded startups year over year."""
        most_funded_startup_yoy = self.overall_analysis.most_funded_startups_yoy()

        SubHeader(
            title='Most Funded Startups YoY',
            tooltip='Top 10 most funded startups in startup funding YoY'
        )

        fig = px.bar(
            most_funded_startup_yoy,
            x='StartUp Name',
            y='Amount (In Crore Rs)',
            color='Year'
        )

        st.plotly_chart(fig, use_container_width=True)

    def plot_top_investors(self):
        """Plot the top investors based on their investment values."""
        top_investors = self.overall_analysis.top_investors()

        SubHeader(
            title='Top Investors',
            tooltip='Top most investors on the basis of their investment values.'
        )

        PlotHorizontalBarChart(
            x_axis=top_investors['amount'],
            y_axis=top_investors['investors'],
            layout_title='Top Most Investors',
            layout_x_axis='Funding Amount (In Crore Rs)',
            layout_yaxis='Investor'
        )

    def plot_funding_amount_year_month(self):
        """Plot the funding amount by year and month."""
        pivot_table = self.overall_analysis.funding_amount_year_month()

        SubHeader(
            title='Year and Month Funding',
            tooltip='Heatmap to show the funding amount by year and month.'
        )

        # Plotting the heatmap
        heatmap = go.Heatmap(
            x=pivot_table.columns,
            y=pivot_table.index,
            z=pivot_table.values,
            colorscale='Viridis'
        )

        layout = go.Layout(
            title='Funding Amount by Year and Month',
            xaxis={'title': 'Month'},
            yaxis={'title': 'Year'}
        )

        fig = go.Figure(data=[heatmap], layout=layout)
        st.plotly_chart(fig, use_container_width=True)
