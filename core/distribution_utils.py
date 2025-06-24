import streamlit as st
import numpy as np
import scipy.stats as stats

use_case_map = {
    "Call arrivals (Poisson)": "Poisson",
    "A/B test results (Binomial)": "Binomial",
    "Height of people (Normal)": "Normal",
    "Time until failure (Exponential)": "Exponential",
    "Proportion of votes (Beta)": "Beta"
}

def get_params(dist_name, key_prefix=""):
    if dist_name == "Bernoulli":
        p = st.slider("p", 0.0, 1.0, 0.5, key=key_prefix+"p")
        return stats.bernoulli(p), np.array([0, 1]), f"Bernoulli(p={p})"
    elif dist_name == "Binomial":
        n = st.slider("n", 1, 100, 10, key=key_prefix+"n")
        p = st.slider("p", 0.0, 1.0, 0.5, key=key_prefix+"p")
        return stats.binom(n, p), np.arange(0, n+1), f"Binomial(n={n}, p={p})"
    elif dist_name == "Poisson":
        lam = st.slider("λ (rate)", 0.1, 20.0, 5.0, key=key_prefix+"lam")
        return stats.poisson(lam), np.arange(0, 30), f"Poisson(λ={lam})"
    elif dist_name == "Normal":
        mu = st.slider("μ (mean)", -10.0, 10.0, 0.0, key=key_prefix+"mu")
        sigma = st.slider("σ (std dev)", 0.1, 10.0, 1.0, key=key_prefix+"sigma")
        x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
        return stats.norm(mu, sigma), x, f"Normal(μ={mu}, σ={sigma})"
    elif dist_name == "Exponential":
        lam = st.slider("λ (rate)", 0.1, 10.0, 1.0, key=key_prefix+"lam")
        x = np.linspace(0, 10, 1000)
        return stats.expon(scale=1/lam), x, f"Exponential(λ={lam})"
    elif dist_name == "Beta":
        a = st.slider("α", 0.1, 10.0, 2.0, key=key_prefix+"a")
        b = st.slider("β", 0.1, 10.0, 2.0, key=key_prefix+"b")
        x = np.linspace(0, 1, 1000)
        return stats.beta(a, b), x, f"Beta(α={a}, β={b})"
    elif dist_name == "LogNormal":
        mu = st.slider("μ (log-mean)", -1.0, 3.0, 0.5, key=key_prefix+"mu")
        sigma = st.slider("σ (log-std dev)", 0.1, 2.0, 0.5, key=key_prefix+"sigma")
        x = np.linspace(0, 10, 1000)
        return stats.lognorm(s=sigma, scale=np.exp(mu)), x, f"LogNormal(μ={mu}, σ={sigma})"

def get_y(rv, x, view):
    return rv.cdf(x) if view == "CDF" else (rv.pmf(x) if hasattr(rv, "pmf") else rv.pdf(x))
