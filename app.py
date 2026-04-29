import streamlit as st
import pandas as pd
import os
import plotly.express as px

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(page_title="Customer Analytics", page_icon="👥", layout="wide")

st.title("📊 Customer Segmentation & Retention")
st.markdown("---")

# 2. Sidebar Navigation
st.sidebar.title("Dashboard Menu")
options = st.sidebar.radio("Select a View", ["Project Overview", "Data Preview", "RFM Analysis"])

# Path to your data - Updated to match your exact filename in GitHub
data_path = "data/raw/online_retail_II.csv"

# 3. Logic to show different sections
if options == "Project Overview":
    st.header("Welcome!")
    st.write("This dashboard analyzes customer behavior using the Online Retail dataset.")
    st.write("We use **RFM (Recency, Frequency, Monetary)** modeling to group customers into segments.")
    st.info("The logic below is powered by the data in your GitHub repository.")

elif options == "Data Preview":
    st.header("Raw Data Sample")
    
    if os.path.exists(data_path):
        # Loading a sample for speed
        df = pd.read_csv(data_path, nrows=500)
        st.write(f"Showing first 500 rows of `{data_path}`")
        st.dataframe(df)
    else:
        st.error(f"File not found! I looked for: `{data_path}`. Please check if the filename is correct in your data/raw folder.")

elif options == "RFM Analysis":
    st.header("RFM Metrics Visualization")
    
    if os.path.exists(data_path):
        df = pd.read_csv(data_path, nrows=1000)
        
        # Creating a simple chart
        # Note: Your CSV uses 'Price' instead of 'UnitPrice' based on standard UCI datasets
        price_col = 'Price' if 'Price' in df.columns else 'UnitPrice'
        
        if price_col in df.columns and 'Quantity' in df.columns:
            df['TotalSales'] = df[price_col] * df['Quantity']
            fig = px.scatter(df, x="Quantity", y=price_col, 
                             size="TotalSales", color="Country" if "Country" in df.columns else None,
                             title="Sales Distribution")
            st.plotly_chart(fig, use_container_width=True)
            st.success("Analysis loaded successfully!")
        else:
            st.warning(f"Expected columns not found. Found: {list(df.columns)}")
    else:
        st.error("Data file missing.")
