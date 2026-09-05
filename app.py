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

Use the navigation menu on the left to explore the dashboard and learn more about 
the findings of this investigation.
"""
)

# Skeleton'd via chatgpt

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Overview",
        "Study Time",
        "Previous Failures",
        "Absences",
        "Conclusion"
    ]
)

# -----------------------------
# Overview Page
# -----------------------------
if page == "Overview":

    st.title("Students Who Slip On Maths")
    st.subheader(
        "A dive into factors associated with students' performance in mathematics"
    )

    st.write(
        """
        This dashboard presents the results of an investigation into which academic
        factors are associated with students' final performance in mathematics.

        The analysis focuses on three factors:

        - Weekly study time
        - Previous class failures
        - School absences

        Use the navigation menu on the left to explore the findings.
        """
    )

# -----------------------------
# Study Time Page
# -----------------------------
elif page == "Study Time":

    st.title("Study Time and Final Grade")

    st.write(
        """
        This section investigates whether students who spend more time studying
        tend to achieve higher final Mathematics grades.
        """
    )

# -----------------------------
# Previous Failures Page
# -----------------------------
elif page == "Previous Failures":

    st.title("Previous Failures and Final Grade")

    st.write(
        """
        This section investigates whether students with a greater number of
        previous class failures tend to achieve lower final Mathematics grades.
        """
    )

# -----------------------------
# Absences Page
# -----------------------------
elif page == "Absences":

    st.title("School Absences and Final Grade")

    st.write(
        """
        This section investigates whether students with higher numbers of school
        absences tend to achieve lower final Mathematics grades.
        """
    )

# -----------------------------
# Conclusion Page
# -----------------------------
elif page == "Conclusion":

    st.title("Conclusion")

    st.write(
        """
        This section summarises the main findings from the analysis and considers
        how they could be used by a Student Support Team.
        """
    )