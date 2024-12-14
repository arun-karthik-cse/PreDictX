import streamlit as st
from predict_page import show_predict_page 
from explore_page import show_explore_page

# Increase the timeout to 2 hour
# Custom CSS for styling
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

# Header
st.title("PreDictX")
# Sidebar and Page Routing
page = st.sidebar.selectbox("Menu", ("Predict", "Explore"))
if page == "Predict":
    show_predict_page()
elif page == "Explore":
    show_explore_page()
