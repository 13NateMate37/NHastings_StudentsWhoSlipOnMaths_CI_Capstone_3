import streamlit as st

st.title("Conclusion")

st.markdown("### Hypothesis Results")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="H1: Study Time",
        value="Supported",
        delta="ρ = 0.105"
    )

with col2:
    st.metric(
        label="H2: Previous Failures",
        value="Supported",
        delta="ρ = -0.361"
    )

with col3:
    st.metric(
        label="H3: Absences",
        value="Not Supported",
        delta="ρ = 0.018"
    )

st.markdown("### Overall Findings")

st.write(
    """
    The analysis found that the three investigated factors were not equally
    associated with final Mathematics performance.

    Weekly study time showed a statistically significant though very weak, positive
    association with final grade.

    Previous class failures displayed the strongest relationship, with students who
    had a greater number of previous failures tending to achieve lower final grades.

    School absences prove to have no statistically significant association with final
    Mathematics performance in this dataset.
    """
)

st.markdown("### Business Recommendation")

st.write(
    """
    Of the three factors investigated, previous academic failures appear to provide
    the most useful information, with more than failure indicating a greater likelyhood
    of needing additional academic support.

    Study time may provide some additional context, but its relationship with
    final performance is weak. Efforts could be taken to accomadate students getting 
    closer to 5 hours of study time, which demonstrated the most return in imporoving 
    ones final grade.  
    
    Absence count alone should not be treated as areliable indicator of Mathematics 
    performance based on this analysis.

    Further research into other outside factors, such as family support and social activity, 
    may provide additional insight into factors which indicate a students' likelihood of success.
    """
)

st.markdown("### Ethical Considerations")

st.write(
    """
    These findings should be used to support, rather than replace, professional
    judgement.

    The relationships identified in this analysis are associations and do not
    demonstrate causation. No single variable should be used to automatically
    label a student as being at risk.

    Decisions about student support should consider wider context and avoid using
    unnecessary personal or family information where it is not required for the
    stated analytical purpose.
    """
)