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
    
url = "https://github.com/neuraledgeai/GDP-PY/blob/main/README.md"
st.sidebar.markdown(
    f"""<div style="text-align: center"><i><a href="{url}" target="_blank" style="text-decoration: none; color: inherit;">About this research work</a></i></div>""",
    unsafe_allow_html=True
)

# Dashboard
if selected == "Forecast GDP":
    st.subheader("Future GDP Outlook For India")
    #st.write("You can start by adjusting the *forecast horizon* to see the predicted GDPs over the next few years.")
    years = st.slider("Forecast Horizon (number of years)", 0, 20, 7)
    pc.forecast_primary_chart(years = years+1)
    pc.forecast_bar_chart(years = years+1)
    st.balloons()
elif selected == "Emperical Results":
    pc.empericalResults()
elif selected == "Download Data":
    years = st.slider("Forecast Horizon", 0, 20, 7)
    pc.downloadData(years = years+1)
elif selected == "Resilient Economy":
    pc.resilientEconomy()
