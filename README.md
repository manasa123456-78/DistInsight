# DistInsightDistInsight: Interactive Probability Distribution Visualizer
DistInsight is an interactive Streamlit-based tool that helps visualize and explore various probability distributions.
It supports multiple modes including single distribution plots, dual distribution overlays, and CSV-based real-world data fitting.

## Features
  Multi-Mode Explorer: Visualize single distributions, overlay two distributions, or fit distributions to uploaded CSV data.
  Dynamic Parameter Sliders: Supports 7+ discrete and continuous distributions with real-time PDF/PMF/CDF view switching.
  NLP-Enabled Suggestions: Rule-based AI that suggests appropriate distributions based on problem descriptions.
  CSV Integration: Upload datasets and automatically fit Normal, Exponential, or LogNormal models with histogram overlays.
  Plot Download: Download generated distribution plots as PNG files for reports and presentations.

## Folder Structure
```text
distinsight/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── core/                   # Core logic
│   ├── __init__.py
│   ├── views.py            # UI rendering for each mode
│   ├── distribution_utils.py  # Distribution parameter logic
│   ├── ai_suggestions.py      # NLP-based distribution recommendation
│   └── plot_utils.py          # Plotting and download logic
│
├── assets/                 # Optional images or custom CSS
└── data/                   # Sample CSV files for demo/testing
    └── example.csv
```

## Technologies Used
Python
Streamlit
NumPy
SciPy
Matplotlib
Pandas

## Setup Instructions
Clone the repository:
```bash
git clone https://github.com/your-username/distinsight.git
cd distinsight
```
Install the dependencies:
```bash
pip install -r requirements.txt
```
Run the app:
```bash
streamlit run app.py
```
