import streamlit as st
import pandas as pd
import os

# 1. Page Configuration
st.set_page_config(page_title="Customer Analytics", page_icon="👥")

st.title("📊 Customer Segmentation & Retention")
st.markdown("---")

# 2. Sidebar Navigation
st.sidebar.title("Dashboard Menu")
options = st.sidebar.radio("Select a View", ["Project Overview", "RFM Analysis", "Data Preview"])

# 3. Logic to show different sections
if options == "Project Overview":
    st.header("Welcome!")
    st.write("This app analyzes customer behavior and segments.")
    st.info("Next step: We will link your ML clustering models here!")

elif options == "Data Preview":
    st.header("Raw Data Sample")
    # This looks for the data in your data/raw folder
    data_path = "data/raw/customer_data.csv" # <--- UPDATE THIS with your actual filename!
    
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        st.dataframe(df.head(10))
    else:
        st.warning(f"Could not find the data file at {data_path}. Please check the file name in your 'data/raw' folder.")

elif options == "RFM Analysis":
    st.header("RFM Metrics")
    st.write("Recency, Frequency, and Monetary charts will appear here.")
