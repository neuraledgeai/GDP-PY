import streamlit as st
from database import LocalDatabase
from business import Model
from display import PresentationComponents

st.set_page_config(
    page_title="India GDP Forecasting Tool",
    layout="wide",
)

pc = PresentationComponents()

st.sidebar.header("Navigate the Dashboard")
navigation = st.sidebar.radio(
    "Dive into the Data!",
    ["GDP Forecast", "Resilient Economy", "Emperical Results", "Download Forecasted Data"],
    captions=[
        "Visual Representation",
        "Visual Representation",
        "Visual Representation",
        "CSV file"
        
    ],
)
st.sidebar.header("Neural Edge AI")

# Home section
if navigation == "GDP Forecast":
    st.subheader("India's $5 Trillion Economy: :blue[A Data-Driven Perspective]")
    years = st.slider("Forecast Horizon (number of years)", 0, 20, 7)
    st.write("You can adjust the forecast horizon to see the predicted GDPs over the next few years.")
    pc.forecast_primary_chart(years = years+1)
    pc.forecast_bar_chart(years = years+1)
elif navigation == "Emperical Results":
    pc.empericalResults()
elif navigation == "Download Forecasted Data":
    years = st.slider("Forecast Horizon", 0, 20, 7)
    pc.downloadData(years = years+1)
elif navigation == "Resilient Economy":
    pc.resilientEconomy()
