import streamlit as st
import pandas as pd
import os
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Customer Analytics", page_icon="👥", layout="wide")

st.title("📊 Customer Segmentation & Retention")
st.markdown("---")

# 2. Sidebar Navigation
st.sidebar.title("Dashboard Menu")
options = st.sidebar.radio("Select a View", ["Project Overview", "Data Preview", "RFM Analysis"])

# Path to your data - updated based on your repo structure
data_path = "data/raw/online_retail.csv"

# 3. Logic to show different sections
if options == "Project Overview":
    st.header("Welcome!")
    st.write("This dashboard analyzes customer behavior using the Online Retail dataset.")
    st.write("We use **RFM (Recency, Frequency, Monetary)** modeling to group customers into segments for better marketing retention.")
    st.info("The logic below is powered by the data in your GitHub repository.")

elif options == "Data Preview":
    st.header("Raw Data Sample")
    
    if os.path.exists(data_path):
        # We only load a small portion for the preview to keep it fast
        df = pd.read_csv(data_path, nrows=500)
        st.write(f"Showing first 500 rows of `{data_path}`")
        st.dataframe(df)
    else:
        st.error(f"File not found! Make sure `{data_path}` exists in your GitHub repo.")

elif options == "RFM Analysis":
    st.header("RFM Metrics Visualization")
    
    if os.path.exists(data_path):
        df = pd.read_csv(data_path, nrows=1000)
        
        # Creating a simple chart to show 'Monetary' value (Unit Price * Quantity)
        if 'UnitPrice' in df.columns and 'Quantity' in df.columns:
            df['TotalSales'] = df['UnitPrice'] * df['Quantity']
            fig = px.scatter(df, x="Quantity", y="UnitPrice", 
                             size="TotalSales", color="Country",
                             title="Sales Distribution (Quantity vs Price)")
            st.plotly_chart(fig, use_container_width=True)
            st.success("Analysis loaded successfully!")
        else:
            st.warning("Expected columns (UnitPrice/Quantity) not found in the CSV.")
    else:
        st.error("Data file missing. Please check your GitHub 'data/raw' folder.")
