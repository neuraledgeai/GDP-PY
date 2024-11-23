from business import Model
import streamlit as st
import plotly.express as px
import pandas as pd

class PresentationComponents:
  def __init__(
    self,
    model = Model()
  ):
    self.model = model

  def forecast_primary_chart(self, years):
    predicted_gdps =  self.model.makeForecast(years = range(1, years))
    actual_gdps = self.model.get_fitted_values()
    
    # Reset the index to make 'Year' a column
    actual_gdps = actual_gdps.reset_index()
    
    # Add a column to indicate whether the data is actual or predicted
    actual_gdps["Type"] = "Actual GDP"
    predicted_gdps["Type"] = "Predicted GDP"
    
    # Combine the DataFrames
    combined_df = pd.concat([actual_gdps, predicted_gdps])
    
    # Plot the chart
    fig = px.line(
      combined_df, 
      x="Year", 
      y="GDP", 
      color="Type", 
      title="Charting India's Economic Rise",
    )
    fig.update_traces(
        line=dict(width=3),  # Thicker line
        selector=dict(name="Actual GDP")  # Ensure Actual GDP is distinguished
    )
    fig.update_traces(
        line=dict(width=2, dash="dash"),  # Thinner, dashed line for prediction
        selector=dict(name="Predicted GDP")
    )
    fig.update_traces(
        line_color="blue",
        selector=dict(name="Actual GDP")
    )
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="GDP (in Trillions)",
        dragmode=False,
        showlegend=False
    )
    fig.update_traces(
        line_color="red",
        selector=dict(name="Predicted GDP")
    )
    
    if(years > 17):
      st.warning("Forecasting too far into the future may reduce accuracy.", icon="⚠️")
      
    st.plotly_chart(fig)
    st.write("The line chart depicts India's GDP growth. The blue line represents the actual GDP, while the red line shows the predicted GDP.")
  
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
    
    st.plotly_chart(fig)
    st.write(f"The bar chart provides a visual representation of India’s projected GDP growth over the next {years-1} years. Each bar represents the forecasted GDP value for a given year, displayed in trillions of US dollars.")
    
    #st.write("**Key Highlights**")
    with st.expander("Key Highlights", expanded = True):
      st.markdown(''':blue-background[Highlight-1] : India is expected to touch **$5 trillion in GDP at current prices by 2029-2030**.''')
      st.markdown(''':blue-background[Highlight-2] : The predicted GDP line indicates a continued upward trend.''')
      st.markdown(''':blue-background[Highlight-3] : The more rapid rise from 2000 to 2023 suggests significant economic expansion and development in the last two decades.''')

    st.markdown("""
    <div style="text-align: center; font-size: 0.8em; color: grey;">
    The model is trained on data only up to 2023, so predictions may vary due to future uncertainties. Please verify important information independently.
    </div>
    """, unsafe_allow_html=True)

  def empericalResults(self):
    
    # Get intercept and coefficient 
    intercept = self.model.intercept()
    coefficient = self.model.coef()
    
    # Get dataframe
    df = self.model.predict()

    # Get model fitted figure
    fig_fit = self.model.get_fitted_figure()

    # Reset the index to make 'Year' a column
    df = df.reset_index()
    
    # Subheader
    st.subheader("Emperical Results - Why GDP-PY is reliable?")
    st.write("The goal of this empirical analysis is to forecast India’s GDP growth trajectory and estimate the specific year in which India is likely to reach a GDP of $5 trillion. To do so, we estimate a linear regression function of the form")
    st.latex(r"{\text{GDP}_{\text{next year}}} = {\beta}_0 + {\beta}_1 \cdot \text{GDP}_{\text{previous year}}")
    st.write(f"The independent variable is the GDP value from the previous year, which we use to forecast future values. For example, if you provide the 2023 GDP value as the independent variable, the model will estimate the 2024 GDP based on the estimated intercept *{intercept}* and estimated slope *{coefficient}*.")
    st.plotly_chart(fig_fit)
    st.write("Each point represents the GDP of a given year plotted against the GDP of the previous year on the x-axis. The blue line represents the linear regression model fitted to this data.")
    # Plot figure
    fig = px.line(df, x="Year", y=["GDP", "Predicted GDP"], title="Actual vs Predicted GDP Over Time")
    fig.update_layout(xaxis_title="Year", yaxis_title="GDP (in Trillions)")
    st.plotly_chart(fig)
    st.write("This graph compares the actual GDP with the GDP predicted by the model. The closer the lines, the more accurate the model's predictions.")
    with st.expander("More Details"):
      url = "https://github.com/neuraledgeai/GDP-PY/blob/main/Forecasting_India_GDP.ipynb"
      st.markdown("Explore the full methodology and detailed steps in the [India_GDP_Forecast.ipynb notebook](%s). \nDiscover, learn, and innovate!" % url)
  
  def downloadData(self, years):
    # Get dataframes
    predicted_gdps =  self.model.makeForecast(years = range(1, years))
    actual_gdps = self.model.get_fitted_values()

    # Reset the index to make 'Year' a column
    actual_gdps = actual_gdps.reset_index()

    # Add a column to indicate whether the data is actual or predicted
    actual_gdps["Type"] = "Actual GDP"
    predicted_gdps["Type"] = "Forecasted GDP"

    # Combine the DataFrames
    combined_df = pd.concat([actual_gdps, predicted_gdps])
    
    # Subheader
    st.subheader("Download Actual and Predicted GDP Data")
    
    # Information
    st.write("Download the GDP data as a csv file. Hover mouse over the dataframe or touch on it to access download option.")
    
    # Dataframe
    st.dataframe(combined_df)
    
    st.markdown("""
    <div style="text-align: center; font-size: 0.8em; color: grey;">
    The model is trained on data only up to 2023, so predictions may vary due to future uncertainties. Please verify important information independently.
    </div>
    """, unsafe_allow_html=True)

  def resilientEconomy(self):
    # Subheader
    st.subheader("The Indian Economy has Demonstrated Remarkable Resilience")
    fig, fig1 = self.model.gdpGrowth()
    st.plotly_chart(fig)
    st.plotly_chart(fig1)
    st.markdown(''':blue-background[Highlight-1] : Indian economy is set in its transitional growth.''')
    st.markdown(''':blue-background[Highlight-2] : The pre-pandemic and post-pandemic transitional growth trends ensure no permanent loss in demand and output.''')
