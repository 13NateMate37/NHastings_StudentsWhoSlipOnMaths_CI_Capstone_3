# Required libraires, cacher inside HelperFuncs.py
import streamlit as st
from HelperFuncs import loadDataframe

# Load cacehed dataframe
df = loadDataframe()


st.title("Project Overview")

st.write(
    """
    This project investigates which academic factors are associated with students'
    final Mathematics performance.

    The aim is to support Student Support Groups in identifying factors that may help
    indicate which students could benefit from additional academic support.
    """
)

st.markdown("### Business Requirement")

st.write(
    """
    The Student Support Team wants to better understand which factors are associated
    with students' final Mathematics performance so that students who may require
    additional academic support can be identified more effectively.
    """
)

st.markdown("### Dataset Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total Students",
        value=len(df)
    )

with col2:
    st.metric(
        label="Mean Final Grade",
        value=f"{df['G3'].mean():.2f}"
    )

with col3:
    st.metric(
        label="Median Final Grade",
        value=f"{df['G3'].median():.0f}"
    )

st.markdown("### Hypotheses")

st.write(
    """
    **H1:** Students who spend more time studying per week tend to achieve
    higher final Mathematics grades.

    **H2:** Students with a greater number of previous class failures tend to
    achieve lower final Mathematics grades.

    **H3:** Students with higher numbers of school absences tend to achieve
    lower final Mathematics grades.
    """
)

st.markdown("### Ethical Considerations")

st.write(
    """
    The analysis follows a data-minimisation approach by focusing only on variables
    required for the stated business requirement and hypotheses.

    The results are interpreted as associations rather than causes, and no single
    variable should be used in isolation to make decisions about individual students.
    """
)