import streamlit as st 
import matplotlib matplotlib.use('Agg')
st.markdown("""
    <style>
    /* General styles */
    body {
        background-color: #f4f6f9;
        font-family: 'Arial', sans-serif;
        color: #374151;
    }

    /* Header styles */
    .header {
        background-color: #2f3e46;
        padding: 60px;
        color: white;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        position: fixed;
        width: 100%;
        top: 0;
        z-index: 1000;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .header .logo {
        display: flex;
        align-items: center;
    }

    .header .logo img {
        height: 50px;
        margin-right: 15px;
    }

    .header a {
        color: #4CAF50;
        padding: 0 15px;
        text-decoration: none;
        font-size: 18px;
        transition: color 0.3s ease;
    }

    .header a:hover {
        color: #45a049;
    }

    /* Footer styles */
    .footer {
        background-color: #2f3e46;
        padding: 20px;
        color: white;
        text-align: center;
        font-size: 16px;
        position: fixed;
        width: 100%;
        bottom: 0;
        z-index: 1000;
        box-shadow: 0px -4px 10px rgba(0, 0, 0, 0.1);
    }

    .footer .footer-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
    }

    .footer .footer-logo img {
        height: 40px;
        margin-right: 15px;
    }

    .footer a {
        color: #4CAF50;
        text-decoration: none;
        transition: color 0.3s ease;
    }

    .footer a:hover {
        color: #45a049;
    }

    /* Body padding to accommodate fixed header and footer */
    body {
        padding-top: 100px;
        padding-bottom: 80px;
    }

    /* Sidebar styles */
    .sidebar .sidebar-content {
        background-color: #2f3e46;
        padding: 20px;
        border-radius: 10px;
    }

    .sidebar .sidebar-content h2 {
        color: #f4f6f9;
        font-size: 22px;
        margin-bottom: 20px;
    }

    .sidebar .sidebar-content img {
        margin-bottom: 20px;
        border-radius: 50%;
    }

    /* Button styles */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px;
        margin-top: 20px;
        border-radius: 10px;
        width: 100%;
    }

    /* Input box styles */
    .stTextInput>div>div>input {
        background-color: #f4f6f9;
        color: #2f3e46;
        border: 1px solid #2f3e46;
        border-radius: 5px;
    }

    /* Card-like container for pages */
    .card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        margin-top: 20px;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.15);
    }

    /* Plot styles */
    .element-container>div>div>div>div>div>div>div {
        background-color: #f4f6f9;
        padding: 10px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .title {
        color: #66CCCC; /* Unique color for title text */
        font-size: 36px; /* Increase font size for title */
        font-weight: bold; /* Make title bold */
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)
import pandas as pd 
import matplotlib.pyplot as plt 
st.markdown("""
    <style>
    .explore-container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
    }
    .explore-container h1 {
        font-size: 32px;
    }
    </style>
""", unsafe_allow_html=True)

models = {
    "Rice": "Rice_autoarima.pkl",
    "Wheat": "Wheat_arima_wfv.pkl",
    "Sugar": "Sugar_autoarima.pkl",
    "Potato": "Potato_arima_wfv.pkl",
    "Onion": "Onion_autoarima.pkl",
    "Tomato": "Tomato_autoarima.pkl"
}
"""def show_explore_page():
    st.markdown("<div class='explore-container'>", unsafe_allow_html=True)
    st.title("🔍 Explore Product Prices")
    st.write("Analyze historical wholesale prices for different products in the Indian market.")

    items = list(models.keys())
    item = st.selectbox("🛒 Product", items, help="Select the product you want to explore.")
    explore_button = st.button("📊 Explore for 10 days")

    if explore_button:
        df = pd.read_csv("final_time_without_null_full.csv", index_col="timestamp")
        if item in df.columns:
            df[item] = pd.to_numeric(df[item], errors='coerce')
            
            # Filter the DataFrame to include only the last 30 days
            last_30_days = df.tail(10)
            
            st.subheader(f"🛒 {item} Price Trends (Last 10 Days)")
            fig, ax1 = plt.subplots()
            ax1.plot(last_30_days[item], color='#FF4B4B', marker='o', mfc='#FFC0CB')
            plt.title(f'{item} Price Trends (Last 30 Days)', color='#374151')
            plt.xlabel('Date', color='#374151')
            plt.ylabel("Price", color='#374151')
            plt.grid(True, linestyle='--', alpha=0.7)
            st.pyplot(fig)
        else:
            st.error(f"Error: Column '{item}' not found in the dataset.")

    st.markdown("</div>", unsafe_allow_html=True)"""

def show_explore_page():
    st.markdown("<div class='explore-container'>", unsafe_allow_html=True)
    st.title("🔍 Explore Product Prices")
    st.write("Analyze historical wholesale prices for different products in the Indian market.")

    items = list(models.keys())
    item = st.selectbox("🛒 Product", items, help="Select the product you want to explore.")
    explore_button = st.button("📊 Explore for 10 days")

    if explore_button:
        try:
            df = pd.read_csv("wholesale.csv", index_col="timestamp")
            if item in df.columns:
                df[item] = pd.to_numeric(df[item], errors='coerce')
                
                # Filter the DataFrame to include only the last 30 days
                last_30_days = df.tail(10)
                
                st.subheader(f"🛒 {item} Price Trends (Last 10 Days)")
                fig, ax1 = plt.subplots()
                ax1.plot(last_30_days[item], color='#FF4B4B', marker='o', mfc='#FFC0CB')
                plt.title(f'{item} Price Trends (Last 30 Days)', color='#374151')
                plt.xlabel('Date', color='#374151')
                plt.ylabel("Price", color='#374151')
                plt.grid(True, linestyle='--', alpha=0.7)
                st.pyplot(fig)
            else:
                st.error(f"Error: Column '{item}' not found in the dataset.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    st.markdown("</div>", unsafe_allow_html=True)
