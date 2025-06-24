import streamlit as st
from core.views import single_distribution_view, overlay_distribution_view, csv_upload_view

st.set_page_config(page_title="DistInsight - Distribution Explorer", layout="wide")
st.title("DistInsight: Interactive Distribution Explorer")

mode = st.sidebar.radio("Choose Mode:", ["Single Distribution", "Overlay Two Distributions", "Upload CSV & Fit"])
view = st.sidebar.radio("View Type:", ["PDF/PMF", "CDF"])

if mode == "Single Distribution":
    single_distribution_view(view)

elif mode == "Overlay Two Distributions":
    overlay_distribution_view(view)

elif mode == "Upload CSV & Fit":
    csv_upload_view(view)
