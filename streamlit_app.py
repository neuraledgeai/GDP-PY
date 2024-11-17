import streamlit as st
from display import PresentationComponents

# Set page title and layout
st.set_page_config(
    page_title="India GDP Forecasting Tool",
    layout="wide",
)

# Instantiate presentation layer
pc = PresentationComponents()

# Sidebar
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

# Dashboard
if navigation == "GDP Forecast":
    st.subheader(":blue[When will India touch $5 trillion economy milestone?]")
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
