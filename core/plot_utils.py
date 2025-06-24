import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats
from io import BytesIO

def plot_distribution(rv, x, y, label, view):
    fig, ax = plt.subplots()
    if hasattr(rv, "pmf"):
        ax.bar(x, y, color='skyblue', edgecolor='black')
    else:
        ax.plot(x, y, color='crimson')
    ax.set_title(f"{view} of {label}")
    ax.set_xlabel("x")
    ax.set_ylabel(view)
    st.pyplot(fig)
    download_plot(fig)

def plot_overlay(x1, y1, label1, x2, y2, label2, view):
    fig, ax = plt.subplots()
    ax.plot(x1, y1, label=label1, color='blue')
    ax.plot(x2, y2, label=label2, color='red')
    ax.set_title(f"Overlay: {label1} vs. {label2}")
    ax.set_xlabel("x")
    ax.set_ylabel(view)
    ax.legend()
    st.pyplot(fig)
    download_plot(fig)

def plot_csv_fit(view):
    file = st.file_uploader("Choose a file", type=["csv"])
    if file:
        df = pd.read_csv(file)
        col = st.selectbox("Select column:", df.columns)
        data = df[col].dropna().values

        x = np.linspace(min(data), max(data), 1000)
        dist_name = st.selectbox("Choose distribution to fit:", ["Normal", "Exponential", "LogNormal"])

        if dist_name == "Normal":
            mu, sigma = stats.norm.fit(data)
            fitted_rv = stats.norm(mu, sigma)
        elif dist_name == "Exponential":
            loc, scale = stats.expon.fit(data)
            fitted_rv = stats.expon(loc=loc, scale=scale)
        else:
            shape, loc, scale = stats.lognorm.fit(data, floc=0)
            fitted_rv = stats.lognorm(shape, loc=loc, scale=scale)

        y = fitted_rv.pdf(x)

        fig, ax = plt.subplots()
        ax.hist(data, bins=30, density=True, alpha=0.5, label="Data Histogram")
        ax.plot(x, y, color='green', label=f"Fitted {dist_name}")
        ax.set_title(f"Fitted {dist_name} Distribution")
        ax.set_xlabel(col)
        ax.set_ylabel("Density")
        ax.legend()
        st.pyplot(fig)
        download_plot(fig)

def download_plot(fig):
    buf = BytesIO()
    fig.savefig(buf, format="png")
    st.download_button("📥 Download Plot as PNG", data=buf.getvalue(), file_name="distinsight_plot.png", mime="image/png")
