import streamlit as st
from display import PresentationComponents
from streamlit_option_menu import option_menu

# Set page title and layout
st.set_page_config(
    page_title="GDP-PY",
    layout="wide",
)

# Instantiate presentation layer
pc = PresentationComponents()

# Sidebar
with st.sidebar:
    selected = option_menu(
        "GDP-PY", ["Forecast GDP", "Resilient Economy",  "Emperical Results", "Download Data"], 
        icons=["bar-chart-fill", "ubuntu", "card-text", "download"],
        menu_icon="window-stack",
        #default_index=2
    )
st.sidebar.write("A project of *Neural Edge AI*")

# Dashboard
if selected == "Forecast GDP":
    st.subheader("Future GDP Outlook For India")
    st.write("You can start by adjusting the *forecast horizon* to see the predicted GDPs over the next few years.")
    years = st.slider("Forecast Horizon (number of years)", 0, 20, 7)
    st.write(":blue[**When will India Touch $5 Trillion Economy Milestone?**]")
    pc.forecast_primary_chart(years = years+1)
    pc.forecast_bar_chart(years = years+1)
elif selected == "Emperical Results":
    pc.empericalResults()
elif selected == "Download Data":
    years = st.slider("Forecast Horizon", 0, 20, 7)
    pc.downloadData(years = years+1)
elif selected == "Resilient Economy":
    pc.resilientEconomy()
