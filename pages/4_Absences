# Required libraires, cacher inside HelperFuncs.py
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from HelperFuncs import loadDataframe

# Load the cached dataframe
df = loadDataframe()

st.title("School Absences and Final Grade")

st.markdown("### Hypothesis 3")

st.write(
    """
    Students with more absences tend to acheive a lower grade.
    """
)

st.markdown("### Visual Analysis")

fig, ax = plt.subplots(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="absences",
    y="G3",
    ax=ax
)

ax.set_title("School Absences and Final Grade")
ax.set_xlabel("Number of School Absences")
ax.set_ylabel("Final Grade (G3)")

st.pyplot(fig)

st.markdown("### Statistical Test")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Spearman's Rho",
        value="0.018"
    )

with col2:
    st.metric(
        label="P-value",
        value="0.7254"
    )

st.markdown("### Interpretation")

st.write(
    """
    A statistically significant association was not found between school absences
    and final Mathematics grade.

    The Spearman correlation was very close to zero, indicating little to no
    monotonic relationship between the two variables.

    As the p-value is greater than 0.05, Hypothesis 3 is not supported.
    """
)

st.markdown("### Business Insight")

st.write(
    """
    The scope of the dataset does not support a notion of absences being a 
    useful indicator of final Mathematics performance.

    While it could be a contributing facotr in an individuals perforance,
    it should not be relied upon by itself when trying to identify students
    who may require additional academic support.
    """
)