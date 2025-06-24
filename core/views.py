import streamlit as st
from core.distribution_utils import get_params, get_y, use_case_map
from core.ai_suggestions import suggest_distribution
from core.plot_utils import plot_distribution, plot_overlay, plot_csv_fit

def single_distribution_view(view):
    col1, col2 = st.columns([2, 1])
    with col2:
        st.markdown("### Not sure what to pick?")
        query = st.text_input("Describe your problem", key="query_input")
        use_ai_suggestion = st.checkbox("Use Suggested Distribution", key="ai_checkbox")

        if query:
            guess = suggest_distribution(query)
            st.info(f"Suggested Distribution: **{guess}**")

        if use_ai_suggestion and query:
            dist_name = guess
        else:
            use_case = st.selectbox("🎯 Try a real-world example:", list(use_case_map.keys()))
            dist_name = use_case_map[use_case]

    with col1:
        rv, x, label = get_params(dist_name)
        y = get_y(rv, x, view)
        plot_distribution(rv, x, y, label, view)

def overlay_distribution_view(view):
    col1, col2 = st.columns(2)
    with col1:
        dist1 = st.selectbox("Distribution 1", list(use_case_map.values()), key="d1")
        rv1, x1, label1 = get_params(dist1, key_prefix="A")
    with col2:
        dist2 = st.selectbox("Distribution 2", list(use_case_map.values()), key="d2")
        rv2, x2, label2 = get_params(dist2, key_prefix="B")

    y1 = get_y(rv1, x1, view)
    y2 = get_y(rv2, x2, view)

    plot_overlay(x1, y1, label1, x2, y2, label2, view)

def csv_upload_view(view):
    plot_csv_fit(view)
