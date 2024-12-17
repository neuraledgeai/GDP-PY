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
    """
    Generates GDP forecasts for a specified number of future years using the trained linear regression model.

    Description
    -----------
    This method predicts future GDP values starting from the most recent known GDP value (2023). 
    It iteratively predicts the GDP for each year in the provided list using the fitted linear regression model, 
    where each year's GDP is based on the previous year's predicted value.

    Parameters
    ----------
    years : list of int
        A list of integers representing the years for which GDP forecasts are to be made. 
        Each value in the list represents an additional year (e.g., [1, 2, 3] corresponds to 2024, 2025, 2026).

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the following columns:
        - 'Year': The forecasted years as integers.
        - 'GDP': The predicted GDP values for each corresponding year as floats.

    Notes
    -----
    - The prediction starts from a GDP value of $3.353 trillion for the year 2023.
    - Each forecasted GDP value is used as input to predict the GDP of the subsequent year.
    - The method assumes a simple autoregressive structure where the previous year's GDP is the predictor.
    """
    # Initialize GDP value and corresponding year
    gdp = 3_353_470_000_000  # GDP for 2023
    corresponding_year = 2023

    # Lists to store predicted GDPs and corresponding years
    predicted_gdps = []
    corresponding_years = []

    # Generate predictions for each year in the input list
    for year in years:
        # Prepare the data for prediction
        X = np.array([[gdp]])

        # Make prediction using the trained model
        predicted_gdp = self.model.predict(X)

        # Update GDP and corresponding year for the next iteration
        corresponding_year += 1
        gdp = predicted_gdp[0]

        # Append the results to the respective lists
        predicted_gdps.append(predicted_gdp)
        corresponding_years.append(corresponding_year)

    # Create a DataFrame to store forecasted results
    data = {
        "Year": corresponding_years,
        "GDP": predicted_gdps
    }
    df = pd.DataFrame(data)

    # Ensure correct data types for output
    df["Year"] = df["Year"].astype(int)
    df["GDP"] = df["GDP"].astype(float)

    return df


  def predict(self):
    """
    Generates predictions for GDP using the trained linear regression model.

    Description
    -----------
    This method predicts GDP values based on the trained model using lagged GDP (`GDP_L1`) as the input feature.  
    It can be used to evaluate how well the model has learned the training data by comparing the actual GDP values with the predicted values.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing:
        - 'GDP': Actual GDP values from the dataset.
        - 'GDP_L1': The one-step lagged GDP values used as the input feature.
        - 'Predicted GDP': The GDP values predicted by the trained model.

    Notes
    -----
    - The input data for prediction is loaded using the `loadData` method with `lag=True`, ensuring that `GDP_L1` is available as the feature.
    - This method provides an assessment of the model's performance on the training data by comparing predicted values with actual values.
    """
    # Load the data with lagged GDP values
    df = self.db.loadData(lag=True)

    # Define the feature (GDP_L1) for prediction
    feature = ["GDP_L1"]
    X = df[feature]

    # Prepare a DataFrame to hold actual GDP, lagged GDP, and predicted GDP
    result = pd.DataFrame({
        "GDP": df["GDP"],                  # Actual GDP values
        "GDP_L1": df["GDP_L1"],            # Lagged GDP values (feature)
        "Predicted GDP": self.model.predict(X)  # Predicted GDP values
    })

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

  def get_fitted_values(self, lag=False):
    """
    Retrieves the cleaned GDP data from the database.

    Description
    -----------
    This method loads and returns the processed GDP data for further analysis or modeling. 
    By setting the `lag` parameter to `True`, the returned DataFrame will include a 
    one-step lagged feature (`GDP_L1`), in addition to the current GDP values.

    Parameters
    ----------
    lag : bool, optional, default=False
        If True, includes a one-step lagged GDP feature (`GDP_L1`) in the returned DataFrame.
        If False, only the current GDP values are included.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the processed GDP data with:
        - Index: Year (datetime index).
        - Columns:
            - 'GDP': The GDP values as floats.
            - 'GDP_L1' (optional): One-step lagged GDP values as floats (if `lag=True`).
    """
    df = self.db.loadData(lag=lag)
    return df

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
    """
    Generates a scatter plot to visualize the model's fitness on the training data.

    Description
    -----------
    This method creates a scatter plot to evaluate how well the linear regression model fits the training data.  
    It plots the actual GDP values (`GDP`) against the one-step lagged GDP values (`GDP_L1`) and overlays 
    the model's predicted GDP values as a linear trend line.

    The figure helps assess the model's performance visually by comparing the predicted values with the actual data.

    Returns
    -------
    plotly.graph_objs._figure.Figure
        An interactive Plotly scatter plot with:
        - Points representing the actual GDP values vs. the lagged GDP values.
        - A linear model line showing the predicted GDP values.

    Notes
    -----
    - The data for this visualization is retrieved using the `loadData` method with `lag=True` to include the `GDP_L1` feature.
    - The predicted GDP values are obtained using the fitted linear regression model (`self.model`).
    """
    # Load the data with lagged GDP values
    df = self.db.loadData(lag=True)

    # Define target and feature variables
    target = "GDP"
    feature = ["GDP_L1"]
    X_train = df[feature]
    y_train = df[target]

    # Prepare a DataFrame for plotting: actual GDP, lagged GDP, and predicted GDP
    data = pd.DataFrame({
        "GDP": y_train,
        "GDP_L1": X_train.squeeze(),  
        "Predicted_GDP": self.model.predict(X_train)
    })

    # Create a scatter plot to visualize actual vs predicted GDP values
    fig = px.scatter(
        data, 
        x="GDP_L1", 
        y="GDP", 
        title="Model Fitness",
        labels={
            "GDP_L1": "GDP_L1 (Previous Year, US$ Trillion)", 
            "GDP": "GDP (Current US$ Trillion)"
        }
    )

    # Add the model's predicted line to the plot
    fig.add_scatter(
        x=data["GDP_L1"], 
        y=data["Predicted_GDP"],  
        mode="lines", 
        name="Linear Model"
    )

    # Update figure layout for better interactivity and presentation
    fig.update_layout(dragmode=False)

    # Return the figure
    return fig
