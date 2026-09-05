# Required libraires, cacher inside HelperFuncs.py
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from HelperFuncs import loadDataframe

# Load the cached dataframe
df = loadDataframe()

st.title("Previous Failures and Final Grade")

st.markdown("### Hypothesis 2")

st.write(
    """
    Students with prior fails tend to be achieving lower final Mathematics grades thans students who are not failing.
    """
)

st.markdown("### Visual Analysis")

fig, ax = plt.subplots(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="failures",
    y="G3",
    ax=ax
)

ax.set_title("Prior Failures and Final Grades")
ax.set_xlabel("Prior Failures (0, 1, 2, 3)")
ax.set_ylabel("Final Grade (G3)")

st.pyplot(fig)

st.markdown("### Statistical Test")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Spearman's Rho",
        value="-0.361"
    )

with col2:
    st.metric(
        label="P-value",
        value="< 0.0001"
    )

st.markdown("### Interpretation")

st.write(
    """
    Here was found a statistically significant, negative association, between previous fails in class
    and an individuals final Mathematics grade.

    As the number of previous failures increases, the final grade tends to decrease.
    The relationship is stronger than the relationship found for study time.

    As the p-value is below 0.05, Hypothesis 2 is supported.
    """
)

st.markdown("### Business Insight")

st.write(
    """
    Previous academic failures may be a useful indicator when identifying students
    who could benefit from additional academic support. However, this factor should
    not be used in isolation when making decisions about individual students.
    """
)