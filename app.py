import streamlit as st
import pandas as pd
import plotly.express as px

# Page setup
st.set_page_config(
    page_title="NFHS India Dashboard",
    layout="wide"
)

st.title("📊 National Family Health Survey (NFHS) Dashboard")
st.caption("India & State-level Analysis | Evidence-based Governance")

# Load data
@st.cache_data
def load_data():
    file_path = "/mnt/data/All India National Family Health Survey1.xlsx"
    df = pd.read_excel(file_path)
    return df

df = load_data()

st.success("NFHS data loaded successfully")

# Show raw data (optional)
with st.expander("🔍 View Raw Data"):
    st.dataframe(df, use_container_width=True)

# Identify columns dynamically
columns = df.columns.tolist()

# Sidebar filters
st.sidebar.header("🔎 Filters")

state_col = st.sidebar.selectbox(
    "Select State Column",
    options=columns
)

indicator_col = st.sidebar.selectbox(
    "Select Indicator Column",
    options=columns
