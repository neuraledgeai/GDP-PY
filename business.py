import joblib
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from database import LocalDatabase
import pandas as pd
import plotly.express as px

class Model:
  def __init__(
    self,
    model_name = "india_gdp_forecasting_model.pkl",
    db = LocalDatabase()
  ):
    self.model = joblib.load(model_name)
    self.db = db
    
  def makeForecast(self, years):
    # This is GDP for 2023, so that we can start predicting from 2024 to the given number of years
    gdp = 3_353_470_000_000
    corresponding_year = 2023
    
    # To keep predicted GDPs and their corresponding years
    predicted_gdps = []
    corresponding_years = []

    for year in years:
      # Prepare data
      X = np.array([[gdp]])

      # Make prediction and update the corresponding year and gdp
      predicted_gdp = self.model.predict(X)
      corresponding_year = corresponding_year + 1
      gdp = predicted_gdp[0]
      
      # Add predicted_gdp and corresponding_year to predicted_gdps and corresponding_years lists
      predicted_gdps.append(predicted_gdp)
      corresponding_years.append(corresponding_year)

    data = {
      "Year" : corresponding_years,
      "GDP" : predicted_gdps
    }
    df = pd.DataFrame(data)
    df["Year"] = df["Year"].astype(int)
    df["GDP"] = df["GDP"].astype(float)
    
    return df

  def predict(self):
    # Prepare data
    #db = LocalDatabase()
    df = self.db.loadData(lag=True)

    # Split
    feature = ["GDP_L1"]
    X = df[feature]
    
    # Result
    result = pd.DataFrame(
      {
        "GDP" : df["GDP"],
        "GDP_L1" : df["GDP_L1"],
        "Predicted GDP" : self.model.predict(X)
      }
    )
    return result

  def gdpGrowth(self):
    """
    Generates two interactive line plots to visualize India's GDP growth and its transitional economic growth.

    Description
    -----------
    This method produces two figures:
    1. **GDP Growth at Current Prices**: A line chart showing India's GDP trends over the years.
    2. **Transitional Growth**: A focused chart highlighting India's economic resilience and transitional growth 
       between 2003 and 2023 with a trend line.

    Returns
    -------
    tuple
        A tuple containing two Plotly figures:
        - fig : Plotly Figure
            GDP Growth at Current Prices.
        - fig1 : Plotly Figure
            Transitional Growth with a trend line for 2003–2023.

    Notes
    -----
    - The data is sourced from the `loadData` method of the database object (`self.db`).
    - A transitional trend line is manually added to both charts to represent economic growth 
      between the years 2003 and 2023.

    """
    # Load GDP data from the database and reset the index to make 'Year' a column.
    df = self.db.loadData()
    df = df.reset_index()

    # Define data points for the transitional trend line.
    start_year, end_year = 2003, 2023
    start_gdp, end_gdp = 607700687237.318, 3549918918777.53

    # 1. Plot GDP Growth at Current Prices
    fig = px.line(
        df, 
        x="Year", 
        y="GDP", 
        title="GDP Growth at Current Prices"
    )
    fig.add_scatter(
        x=[start_year, end_year], 
        y=[start_gdp, end_gdp], 
        mode='lines', 
        name="Transitional growth trend", 
        line=dict(dash='dash', color='red')
    )
    fig.update_layout(
        dragmode=False,
        xaxis_title="Year",
        yaxis_title="GDP (in Trillions)",
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )

    # 2. Plot Transitional Growth (2003–2023)
    df["Year"] = df["Year"].dt.strftime("%Y")  # Format 'Year' as a string for clean display
    fig1 = px.line(
        df, 
        x="Year", 
        y="GDP", 
        title="Transitional Growth",
        range_x=[start_year, end_year]
    )
    fig1.add_scatter(
        x=[start_year, end_year], 
        y=[start_gdp, end_gdp], 
        mode='lines', 
        name="Transitional growth trend", 
        line=dict(dash='dash', color='red')
    )
    fig1.update_layout(
        dragmode=False,
        xaxis_title="Year",
        yaxis_title="GDP (in Trillions)",
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )

    # Return the two generated figures.
    return fig, fig1

    
  #def get_fitted_values(self):
   # df = self.db.loadData()
    #return df 

  def get_fitted_values(self, lag=False):
    """
    Retrieves the cleaned GDP data from the database.

    Description
    -----------
    This method loads and returns the processed GDP data for further analysis or modeling.
    
    Returns
    -------
    pd.DataFrame
        A DataFrame containing the cleaned GDP data with:
        - Index: Year (datetime index).
        - Columns: 
            - 'GDP': The GDP values as floats.
    """
    df = self.db.loadData(lag=lag)
    return df

  #def intercept(self):
   # return self.model.intercept_   
  
  def intercept(self):
    """
    Retrieves the intercept term of the fitted model.

    Description
    -----------
    This method returns the intercept term (`beta_0`) of the linear regression model 
    associated with this class. The intercept represents the baseline value of the 
    dependent variable when all predictor variables are zero.

    Returns
    -------
    float
        The intercept value of the linear regression model.
    """
    return self.model.intercept_

  #def coef(self):
   # return self.model.coef_[0]
  def coef(self):
    """
    Retrieves the coefficient of the fitted model.

    Description
    -----------
    This method returns the coefficient (`beta_1`) of the linear regression model.
    The coefficient represents the relationship between the predictor variable (GDP_L1) 
    and the target variable (GDP). It indicates the change in the target variable for a unit 
    increase in the predictor variable.

    Returns
    -------
    float
        The coefficient value of the linear regression model.
    """
    return self.model.coef_[0]

  def get_fitted_figure(self):
    # Get data frame with lagged values 
    df = self.db.loadData(lag=True)

    # Split the data
    target = "GDP"
    feature = ["GDP_L1"]
    X_train = df[feature]
    y_train = df[target]

    # Prepare the data for plotting 
    data = pd.DataFrame({
      "GDP": y_train,
      "GDP_L1": X_train.squeeze(),  
      "Predicted_GDP": self.model.predict(X_train)
    })

    # Plot the figure
    fig = px.scatter(data, x="GDP_L1", y="GDP", title="Model Fitness",
                     labels={"GDP_L1": "GDP_L1 (Previous Year, US$ Trillion)", "GDP": "GDP (Current US$ Trillion)"}
                    )
    fig.add_scatter(x=data["GDP_L1"], y=data["Predicted_GDP"],  mode="lines", name="Linear Model")
    fig.update_layout(
        dragmode=False
    )
    return fig

  
    
  
