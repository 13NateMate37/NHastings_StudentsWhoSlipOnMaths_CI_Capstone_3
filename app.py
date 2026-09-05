import streamlit as st

st.set_page_config(
    page_title="Students Who Slip On Maths",
    page_icon="📊",
    layout="wide",
)

st.title("Students Who Slip On Maths")
st.subheader("A dive into factors affecting students' performance in mathematics")

st.write(
    """
This dashboard presents the results found in investigating which academmic factors
most associated with a student's final performance in mathematics. The data was recorded and collected 
from Portuguese secondary school students across two different schools.

The analysis focuses on:
- Weekly study time
- Previous failures in class
- Absences from class


Use the navigation menu on the left to explore the dashboard and learn more about 
the findings of this investigation.
"""
)

