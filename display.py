from business import Model
import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

class PresentationComponents:
  def __init__(
    self,
    model = Model()
  ):
    self.model = model

  def forecast_bar_chart(self,years):
    # Get dataframe
    df =  self.model.makeForecast(years = range(1, years))

    # Plot figure
    fig = px.bar(
        df, 
        x="Year", 
        y="GDP", 
        title=f"GDP Forecast Over the Next {years-1} Years",
        text="GDP"
    )
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="GDP (in Trillions)",
        template="plotly_white",
        xaxis=dict(
          tickmode="linear",
          tickangle=45,
        ),
        dragmode=False
    )
    fig.update_traces(
        marker_color="dodgerblue",  
        marker_line_color="black",  
        marker_line_width=1.5,
        texttemplate="%{text:.2s}",
        textposition="outside" 
    )
    if(years > 17):
      st.warning("Forecasting too far into the future may reduce accuracy.", icon="⚠️")
      
    st.plotly_chart(fig)
    st.write(f"The Bar Chart provides a visual representation of India’s projected GDP growth over the next {years-1} years. Each bar represents the forecasted GDP value for a given year, displayed in trillions of US dollars.")
    st.markdown(''':blue-background[Highlight] : India is expected to touch 5 trillion in GDP at current prices by 2030.''')
    st.markdown("""
    <div style="text-align: center; font-size: 0.8em; color: grey;">
    The model is trained on data only up to 2023, so predictions may vary due to future uncertainties. Please verify important information independently.
    </div>
    """, unsafe_allow_html=True)

  def forecast_line_chart(self, years):
    # Get dataframe
    df =  self.model.makeForecast(years = range(1, years))

    # Plot figure
    fig = px.line(
        df, 
        x="Year", 
        y="GDP", 
        title=f"GDP Forecast Over the Next {years-1} Years",
        markers=True
    )
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="GDP (in Trillions)",
        template="plotly_white",
        xaxis=dict(
            tickmode="linear",
            tickangle=45,
        ),
        dragmode=False
    )
    fig.update_traces(
        line=dict(color="royalblue", width=3),  
        marker=dict(size=8, color="darkblue")
    )
    if(years > 17):
      st.warning("Forecasting too far into the future may reduce accuracy.", icon="⚠️")
      
    st.plotly_chart(fig)
    st.write(f"The Line Chart provides a visual representation of India’s projected GDP growth over the next {years-1} years. Each point represents the forecasted GDP value for a given year, displayed in trillions of US dollars.")
    st.markdown(''':blue-background[Highlight] : India is expected to touch 5 trillion in GDP at current prices by 2030.''')
    st.markdown("""
    <div style="text-align: center; font-size: 0.8em; color: grey;">
    The model is trained on data only up to 2023, so predictions may vary due to future uncertainties. Please verify important information independently.
    </div>
    """, unsafe_allow_html=True)

  def modelPerformance(self):
    # Get dataframe
    df = self.model.predict()

    # Reset the index to make 'Year' a column
    df = df.reset_index()
    
    # Subheader
    st.subheader("Model Performance")
    
    # Plot figure
    fig = px.line(df, x="Year", y=["GDP", "Predicted GDP"], title="Actual vs Predicted GDP Over Time")
    fig.update_layout(xaxis_title="Year", yaxis_title="GDP (in Trillions)")
    st.plotly_chart(fig)
    st.write("This graph compares the actual GDP with the GDP predicted by the model. The closer the lines, the more accurate the model's predictions.")
    
  def downloadData(self, years):
    # Get dataframe
    df =  self.model.makeForecast(years = range(1, years))
    
    # Subheader
    st.subheader("Download Predicted GDP Data")
    
    # Information
    st.write("Download the predicted GDP data as a csv file. Hover mouse over the dataframe or touch on it to access download option.")
    
    # Dataframe
    st.dataframe(df)
    
    st.markdown("""
    <div style="text-align: center; font-size: 0.8em; color: grey;">
    The model is trained on data only up to 2023, so predictions may vary due to future uncertainties. Please verify important information independently.
    </div>
    """, unsafe_allow_html=True)

  def resilientEconomy(self):
    # Subheader
    st.subheader("Resilient Economy")
    fig, fig1 = self.model.gdpGrowth()
    st.plotly_chart(fig)
    st.plotly_chart(fig1)
    st.markdown(''':blue-background[Highlight-1] : Indian economy is set in its transitional growth.''')
    st.markdown(''':blue-background[Highlight-2] : The pre-pandemic and post-pandemic transitional growth trends ensure no permanent loss in demand and output.''')
