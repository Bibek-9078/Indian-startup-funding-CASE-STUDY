"""
This module contains a Streamlit application for analyzing startups.

The application provides functionality to display similar startups based on a given startup name.

Usage:
    1. Import the module.
    2. Create an instance of the Startup class.
    3. Call the `similar_startups` method with a startup name to display similar startups.

Example:
    startup = Startup()
    startup.similar_startups('Example Startup')

Dependencies:
    - Streamlit
    - analysis module


Author: Abhishek Gupta
Github: https://github.com/1abhi6
"""

import streamlit as st
from analysis import Startup as StartupAnalysis

class Startup:
    """
    Class representing a startup and its analysis in a Streamlit application.
    """

    def __init__(self) -> None:
        """
        Initializes a Startup object and its associated analysis.
        """
        self.startup_analysis = StartupAnalysis()

    def similar_startups(self, startup_name):
        """
        Displays similar startups in the Streamlit application for a given startup name.

        Args:
            startup_name (str): The name of the startup.

        Returns:
            None
        """
        similar_startups = self.startup_analysis.similar_startups(startup_name)

        # Display the header for similar startups section
        st.subheader(
            'Similar Startups',
            help=f"These startups belong to the same sector as {startup_name}."
        )
        st.write('')

        # Create columns for displaying similar startups
        col0, col1, col2, col3 = st.columns(4)

        # Display the first similar startup in column 0
        with col0:
            try:
                st.write(similar_startups[0])
            except IndexError:
                st.write('')

        # Display the second similar startup in column 1
        with col1:
            try:
                st.write(similar_startups[1])
            except IndexError:
                st.write('')

        # Display the third similar startup in column 2
        with col2:
            try:
                st.write(similar_startups[2])
            except IndexError:
                st.write('')

        # Display the fourth similar startup in column 3
        with col3:
            try:
                st.write(similar_startups[3])
            except IndexError:
                st.write('')
