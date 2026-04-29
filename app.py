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

# Path to your data - Matches your GitHub folder: data/raw/customer_data.csv
data_path = "data/raw/customer_data.csv"

# 3. Logic to show different sections
if options == "Project Overview":
    st.header("Welcome!")
    st.write("This dashboard analyzes customer behavior and segments.")
    st.write("By using the data stored in your GitHub repository, we can visualize customer trends and retention.")
    st.info("Currently viewing the Project Overview. Use the sidebar to explore data.")

elif options == "Data Preview":
    st.header("Raw Data Sample")
    
    if os.path.exists(data_path):
        # Loading the data
        df = pd.read_csv(data_path)
        st.success(f"Loaded: {data_path}")
        st.write("### First 50 Rows")
        st.dataframe(df.head(50))
        
        # Show data statistics
        if st.checkbox("Show Summary Statistics"):
            st.write(df.describe())
    else:
        st.error(f"File not found! I am looking for: `{data_path}`. Please verify the folder structure in GitHub.")

elif options == "RFM Analysis":
    st.header("RFM Metrics Visualization")
    
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        
        # Automatically detect columns for the chart
        cols = df.columns.tolist()
        st.write(f"Detected columns: {', '.join(cols)}")
        
        st.markdown("### Interactive Distribution")
        x_axis = st.selectbox("Select X-axis for chart:", cols, index=0)
        y_axis = st.selectbox("Select Y-axis for chart:", cols, index=min(1, len(cols)-1))
        
        fig = px.scatter(df, x=x_axis, y=y_axis, 
                         color_discrete_sequence=['#ff4b4b'],
                         title=f"{x_axis} vs {y_axis}")
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Data file missing. Cannot generate analysis.")
