import pickle
import streamlit as st
st.markdown("""
    <style>
    /* General styles */
    body {
        background-color: #f4f6f9;
        font-family: 'Arial', sans-serif;
        color: #374151;
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

    /* Header styles */
    h1, h2, h3, h4 {
        color: #2f3e46;
        font-weight: bold;
    }

    /* Input box styles */
    .stTextInput>div>div>input {
        background-color: #f4f6f9;
        color: #2f3e46;
        border: 1px solid #2f3e46;
        border-radius: 5px;
    }

    /* Date input styles */
    .stDateInput>div>div>input {
        background-color: #f4f6f9;
        color: #2f3e46;
        border: 1px solid #2f3e46;
        border-radius: 5px;
    }

    /* Dropdown styles */
    .stSelectbox>div>div>div>select {
        background-color: #f4f6f9;
        color: #2f3e46;
        border: 1px solid #2f3e46;
        border-radius: 5px;
    }

    /* Table styles */
    .dataframe {
        background-color: #f4f6f9;
        color: #374151;
        border-radius: 10px;
        margin-top: 20px;
    }

    /* Plot styles */
    .element-container>div>div>div>div>div>div>div {
        background-color: #f4f6f9;
        padding: 10px;
        border-radius: 10px;
        margin-top: 20px;
    }

    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

    body {
        font-family: 'Roboto', sans-serif;
        background-color: #f4f6f9;
        color: #333;
        transition: all 0.3s ease;
    }

    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }

    h1, h2, h3, h4 {
        color: #2f3e46;
        font-weight: 700;
        margin-bottom: 20px;
        text-align: center;
    }

    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 50px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #45a049;
        transform: translateY(-3px);
    }

    .stTextInput>div>div>input {
        background-color: #f4f6f9;
        color: #2f3e46;
        border: 1px solid #2f3e46;
        border-radius: 5px;
        padding: 10px;
        transition: all 0.3s ease;
    }

    .stTextInput>div>div>input:focus {
        border-color: #4CAF50;
        box-shadow: 0px 0px 10px rgba(76, 175, 80, 0.2);
    }

    .stDateInput>div>div>input {
        background-color: #f4f6f9;
        color: #2f3e46;
        border: 1px solid #2f3e46;
        border-radius: 5px;
        padding: 10px;
        transition: all 0.3s ease;
    }

    .stDateInput>div>div>input:focus {
        border-color: #4CAF50;
        box-shadow: 0px 0px 10px rgba(76, 175, 80, 0.2);
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

    /* Sidebar styles */
    .sidebar .sidebar-content {
        background-color: #2f3e46;
        padding: 20px;
        border-radius: 15px;
        transition: all 0.3s ease;
    }

    .sidebar .sidebar-content h2 {
        color: #f4f6f9;
        font-size: 22px;
        margin-bottom: 20px;
    }

    .sidebar .sidebar-content img {
        margin-bottom: 20px;
        border-radius: 50%;
        transition: all 0.3s ease;
    }

    .sidebar .sidebar-content img:hover {
        transform: scale(1.1);
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
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
st.markdown("""
    <style>
    .predict-container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
    }
    .predict-container h1 {
        font-size: 32px;
    }
    </style>
""", unsafe_allow_html=True)
def load_model(model_name):
    with open(model_name, "rb") as f:
        data = pickle.load(f)
    return data


models = {
    "Rice": "Rice_autoarima.pkl",
    "Wheat": "Wheat_arima_wfv.pkl",
    "Sugar": "Sugar_autoarima.pkl",
    "Potato": "Potato_arima_wfv.pkl",
    "Onion": "Onion_autoarima.pkl",
    "Tomato": "Tomato_autoarima.pkl"
}
"""def show_predict_page():
    st.markdown("<div class='predict-container'>", unsafe_allow_html=True)
    st.title("💡 Price Prediction")
    st.write("Predict future prices of products using our advanced models. Please provide the required inputs below.")

    # Date input with custom styles
    start_date = st.date_input("🗓️ Start Date", help="Select the start date for prediction.")
    end_date = st.date_input("🗓️ End Date", help="Select the end date for prediction.")

    if start_date > end_date:
        st.error("End date must be after start date")
    else:
        items = list(models.keys())
        item = st.selectbox("🛒 Product", items, help="Select the product to predict prices.")
        predict_button = st.button("🚀 Predict")

        if predict_button:
            model_name = models[item]
            model = load_model(model_name)
            data = model.predict(start=start_date, end=end_date)
            rounded_output = np.round(data, 2)
            st.subheader("📈 Product Price Prediction:")
            fig, ax1 = plt.subplots()
            ax1.plot(rounded_output, color='#FF4B4B', marker='o', mfc='#FFC0CB')
            plt.title(f'{item} Price Prediction', color='#374151')
            plt.xlabel('Date', color='#374151')
            plt.ylabel("Price", color='#374151')
            plt.grid(True, linestyle='--', alpha=0.7)
            st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)"""

def show_predict_page():
    st.markdown("<div class='predict-container'>", unsafe_allow_html=True)
    st.title("💡 Price Prediction")
    st.write("Predict future prices of products using our advanced models. Please provide the required inputs below.")

    # Date input with custom styles
    col1, col2 = st.columns(2)
    start_date = col1.date_input("🗓️ Start Date", help="Select the start date for prediction.")
    end_date = col2.date_input("🗓️ End Date", help="Select the end date for prediction.")

    if start_date > end_date:
        st.error("End date must be after start date")
    else:
        items = list(models.keys())
        item = st.selectbox("🛒 Product", items, help="Select the product to predict prices.")
        predict_button = st.button("🚀 Predict")

        if predict_button:
            model_name = models[item]
            model = load_model(model_name)
            data = model.predict(start=start_date, end=end_date)
            rounded_output = np.round(data, 2)
            st.subheader("📈 Product Price Prediction:")
            fig, ax1 = plt.subplots()
            ax1.plot(rounded_output, color='#FF4B4B', marker='o', mfc='#FFC0CB')
            plt.title(f'{item} Price Prediction', color='#374151')
            plt.xlabel('Date', color='#374151')
            plt.ylabel("Price", color='#374151')
            plt.grid(True, linestyle='--', alpha=0.7)
            st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)
