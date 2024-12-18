from business import Model
import streamlit as st
import plotly.express as px
import pandas as pd

class PresentationComponents:
  """
    A class to create and manage GDP visualization components.

    This class integrates with a forecasting model to provide insightful visualizations, 
    downloadable data, and empirical analysis that can be directly embedded into a Streamlit application. 
    It is designed to simplify the presentation of GDP trends, predictions, and key economic highlights.

    Methods
    -------
    __init__(model=Model())
        Initializes the class with a forecasting model.
    
    forecast_primary_chart(years)
        Creates a line chart to compare actual GDP values with future projections.
    
    forecast_bar_chart(years)
        Generates a bar chart to visualize GDP forecasts for the specified time horizon.
    
    empericalResults()
        Displays an empirical analysis of the forecasting model, including regression insights 
        and comparisons of actual vs. predicted GDP.
    
    downloadData(years)
        Provides an interface to download a combined dataset of actual and forecasted GDP values.
    
    resilientEconomy()
        Highlights India's economic resilience through visualizations of historical GDP trends 
        and transitional growth phases.

    Usage
    -----
    This class is designed for seamless integration into Streamlit apps, enabling interactive 
    exploration and presentation of GDP data. Use the methods to create and display 
    various types of visualizations and analysis with minimal effort.
    """
  def __init__(
    self,
    model = Model()
  ):
    """
    Initializes the class with the trained model.

    Parameters
    ----------
    model : Model, optional
        An instance of the `Model` class used to perform GDP forecasting 
        and analysis. By default, a new instance of `Model` is created.

    Attributes
    ----------
    model : Model
        Stores the provided `Model` instance, which contains the methods 
        and data necessary for GDP analysis and forecasting.

    Example
    -------
    >>> instance = MyClass()
    (Creates an instance with the default Model.)

    >>> custom_model = Model(parameters)
    >>> instance = MyClass(model=custom_model)
    (Creates an instance with a custom Model.)
    """
    self.model = model

  def forecast_primary_chart(self, years):
    """
    Generates an interactive line chart illustrating India's GDP growth trajectory and future projections.

    Description
    -----------
    This method visualizes India's GDP history and forecasts for future years using a trained model.  
    The chart combines historical GDP data and predicted GDP values to provide a comprehensive view of 
    the nation's economic progress and future potential.  

    The chart distinguishes between actual GDP (shown as a solid blue line) and predicted GDP 
    (shown as a red dashed line) to offer clear insights into past and projected trends.

    Parameters
    ----------
    years : int
        The number of years into the future for which GDP forecasts are to be made.  
        For example, if `years=5`, the method forecasts GDP for 5 future years starting from the latest year in the dataset.

    Returns
    -------
    None
        The method directly displays an interactive Plotly chart using Streamlit and writes descriptive 
        text to the Streamlit app interface.

    Notes
    -----
    - The method combines actual GDP data and forecasted GDP values into a single DataFrame for visualization.  
    - Actual GDP values are sourced from the `get_fitted_values` method, and forecasted values are 
      generated using the `makeForecast` method.
    - If the forecast horizon exceeds 17 years, a warning is displayed to indicate reduced forecasting accuracy.
    - Interactive features allow users to click on the chart to view detailed data points.

    Chart Features
    --------------
    - **Solid Blue Line**: Represents actual GDP values recorded from 1960 to the latest available year.
    - **Dashed Red Line**: Represents forecasted GDP values starting from 2024 onward.
    - Both lines are displayed with different thicknesses and colors for clarity.

    Streamlit Integration
    ----------------------
    - Displays an interactive line chart using `st.plotly_chart`.
    - Provides additional insights via `st.write` to describe the chart's purpose and features.
    - Offers context-specific messages:
        - **Warning**: Alerts users about reduced accuracy for long-term forecasts.
        - **Info**: Encourages users to experiment with forecast horizons.

    Example
    -------
    >>> model.forecast_primary_chart(years=10)
    (Displays a line chart showing actual GDP from 1960 to 2023 and forecasted GDP from 2024 to 2033.)

    """
    # Get data.
    predicted_gdps =  self.model.makeForecast(years = range(1, years))
    actual_gdps = self.model.get_fitted_values()
    
    # Reset the index to make 'Year' a column.
    actual_gdps = actual_gdps.reset_index()
    
    # Add a column to indicate whether the data is actual or predicted.
    actual_gdps["Type"] = "Actual GDP"
    predicted_gdps["Type"] = "Predicted GDP"
    
    # Combine the dataFrames.
    combined_df = pd.concat([actual_gdps, predicted_gdps])
    
    # Plot the figure.
    fig = px.line(
      combined_df, 
      x="Year", 
      y="GDP", 
      color="Type", 
      title="India's GDP : Past Growth and Future Projections",
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

    # Display a warning if user try to predict too far into the future.
    if(years > 17):
      st.warning("Forecasting too far into the future may reduce accuracy.", icon="⚠️")
    else:
      st.info("Adjust the *forecast horizon* to see the predicted GDPs over the next few years.", icon="💡")

    # Display the figure and its description.
    st.plotly_chart(fig)
    st.write("The line chart illustrates India's GDP trajectory at current prices from 1960 to 2023, showcasing the nation's impressive economic rise.")
    st.write("The **blue line** represents the actual GDP values recorded over time. The **red dashed line** represents the forecasted GDP from 2024 onward, offering insights into potential economic expansion in the coming years. (You can click or touch on the lines for detailed data points)")
    
  def forecast_bar_chart(self,years):
    """
    Generates an interactive bar chart for India's projected GDP growth over the forecast horizon.

    Description
    -----------
    This method visualizes India's GDP forecasts for the specified number of years into the future.  
    Each bar represents the forecasted GDP value for a particular year, providing a clear and concise view 
    of expected economic growth trends.  

    Additional highlights and insights are displayed alongside the chart to guide users in interpreting 
    the forecasts effectively.  

    Parameters
    ----------
    years : int
        The number of years into the future for which GDP forecasts are to be visualized.  
        For example, if `years=10`, the chart will show GDP forecasts from 2024 to 2033.

    Returns
    -------
    None
        The method directly displays:
        - An interactive bar chart using Streamlit.
        - Descriptive text and insights via Streamlit components.

    Notes
    -----
    - Forecasted GDP values are sourced from the `makeForecast` method.
    - The chart uses Plotly for interactive visualization, and the bars are styled for clarity.
    - A disclaimer is displayed to remind users that predictions are based on historical data up to 2023.

    Chart Features
    --------------
    - **Bars**: Represent forecasted GDP values for each year, displayed in trillions of US dollars.
    - **Text Labels**: Annotate each bar with its GDP value for easy readability.
    - **Axis Customization**: The x-axis includes years formatted for clarity and rotated labels for better visibility.

    Streamlit Integration
    ----------------------
    - Displays an interactive bar chart using `st.plotly_chart`.
    - Adds descriptive text using `st.write` to explain the chart's insights.
    - Highlights key takeaways with `st.markdown` inside an expandable section.
    - Displays a disclaimer about model limitations and uncertainties using HTML.

    Highlights Section
    -------------------
    - **Highlight-1**: Emphasizes the model's projection for India to reach $5 trillion in GDP by 2029-2030.
    - **Highlight-2**: Notes the predicted upward trend in GDP values over the forecast horizon.
    - **Highlight-3**: Draws attention to India's rapid economic expansion from 2000 to 2023.

    Example
    -------
    >>> model.forecast_bar_chart(years=10)
    (Displays a bar chart showing forecasted GDP from 2024 to 2033.)

    Disclaimer
    ----------
    The model is trained on data only up to 2023. Predictions are subject to uncertainties 
    and should be independently verified for critical decisions.
    """
    # Get dataframe.
    df =  self.model.makeForecast(years = range(1, years))

    # Plot figure.
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

    # Display the figure and its description.
    st.plotly_chart(fig)
    st.write(f"This bar chart provides a visual representation of India’s projected GDP growth over the next {years-1} years. Each bar represents the forecasted GDP value for a given year, displayed in trillions of US dollars.")

    # Display the key highlights.
    with st.expander("Key Highlights", expanded = True):
      st.markdown(''':blue-background[Highlight-1] : The model estimates that, on average, India is expected to touch **$5 trillion in GDP at current prices by 2029-2030**.''')
      st.markdown(''':blue-background[Highlight-2] : The predicted GDP line indicates a continued upward trend.''')
      st.markdown(''':blue-background[Highlight-3] : The more rapid rise from 2000 to 2023 suggests significant economic expansion and development in the last two decades.''')
    
    # Disclaimer. 
    st.markdown("""
    <div style="text-align: center; font-size: 0.8em; color: grey;">
    The model is trained on data only up to 2023, so predictions may vary due to future uncertainties. Please verify important information independently.
    </div>
    """, unsafe_allow_html=True)

  def empericalResults(self):
    """
    Displays the empirical results and justification for the reliability of the forecasting model.

    Description
    -----------
    This method performs an empirical analysis to illustrate the accuracy and reliability of the 
    linear regression model used for forecasting India’s GDP. It calculates the intercept and 
    coefficient of the model, compares predicted GDP values with actual values, and visualizes the results 
    using interactive charts.  

    The analysis seeks to demonstrate the tool's capability to predict India’s GDP growth trajectory and 
    identify the year when India is likely to achieve a GDP of $5 trillion.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The method directly displays:
        - Key regression statistics (intercept and coefficient) via Streamlit.
        - A scatter plot with a regression line to validate the model's fit.
        - A line chart comparing actual and predicted GDP values over time.
        - Additional insights and a link to the methodology notebook via Streamlit components.

    Workflow
    --------
    1. Retrieves the intercept and coefficient of the regression model.
    2. Predicts GDP values using the model's `predict` method.
    3. Plots:
        - A scatter plot with the fitted regression line to demonstrate the model's reliability.
        - A line chart comparing actual GDP values with predicted values.
    4. Provides a link to the full methodology in a GitHub-hosted notebook.

    Visualization Details
    ---------------------
    - **Scatter Plot**: Displays each year's GDP against the previous year's GDP.  
      The blue regression line illustrates the model fit.
    - **Line Chart**: Compares actual GDP values with predicted values over time, highlighting 
      the accuracy of the predictions.

    Mathematical Model
    ------------------
    The regression model is represented as:
    
    GDP_next year = beta_0 + beta_1 * GDP_previous year
    
    Where:
    - beta_0 is the intercept of the model.
    - beta_1 is the coefficient (slope) indicating the relationship between GDP of consecutive years.

    Streamlit Integration
    ----------------------
    - **Subheader**: Introduces the purpose of the empirical analysis.
    - **Equations and Descriptions**: Explains the regression equation with LaTeX rendering.
    - **Interactive Charts**: Displays scatter and line charts via `st.plotly_chart`.
    - **Expandable Section**: Provides a link to the full methodology hosted on GitHub.

    Example
    -------
    >>> model.empericalResults()
    (Displays regression results, visualizations, and additional insights via Streamlit.)

    Notes
    -----
    - This analysis assumes a linear relationship between the GDP of consecutive years.
    - The methodology and calculations are detailed in the linked GitHub notebook.

    Disclaimer
    ----------
    The model is based on historical GDP data up to 2023. Future predictions are subject to uncertainties 
    and should be interpreted accordingly.
    """
    # Get intercept and coefficient.
    intercept = self.model.intercept()
    coefficient = self.model.coef()
    
    # Get dataframe.
    df = self.model.predict()

    # Get model fitted figure.
    fig_fit = self.model.get_fitted_figure()

    # Reset the index to make 'Year' a column.
    df = df.reset_index()
    
    # Subheader.
    st.subheader("Emperical Results - Why this tool is reliable?")

    # Introduction.
    st.write("The goal of this empirical analysis is to forecast India’s GDP growth trajectory and estimate the specific year in which India is likely to reach a GDP of $5 trillion. To do so, we estimate a linear regression function of the form")
    st.latex(r"{\text{GDP}_{\text{next year}}} = {\beta}_0 + {\beta}_1 \cdot \text{GDP}_{\text{previous year}}")
    st.write(f"The independent variable is the GDP value from the previous year, which we use to forecast future values. For example, if you provide the 2023 GDP value as the independent variable, the model will estimate the 2024 GDP based on the estimated intercept *{intercept}* and estimated slope *{coefficient}*.")
    
    # Display 'fig_fit' and its description.
    st.plotly_chart(fig_fit)
    st.write("Each point represents the GDP of a given year plotted against the GDP of the previous year on the x-axis. The blue line represents the linear regression model fitted to this data.")
    
    # Plot the figure to visualize model performance.
    fig = px.line(df, x="Year", y=["GDP", "Predicted GDP"], title="Actual vs Predicted GDP Over Time")
    fig.update_layout(xaxis_title="Year", yaxis_title="GDP (in Trillions)")

    # Display 'fig' and its description.
    st.plotly_chart(fig)
    st.write("This graph compares the actual GDP with the GDP predicted by the model. The closer the lines, the more accurate the model's predictions.")

    # Display key highlights.
    with st.expander("More Details"):
      url = "https://github.com/neuraledgeai/GDP-PY/blob/main/Forecasting_India_GDP.ipynb"
      st.markdown("Explore the full methodology and detailed steps in the [India_GDP_Forecast.ipynb notebook](%s).  \nDiscover, learn, and innovate!" % url)

  
  def downloadData(self, years):
    """
    Provides an interface for downloading actual and forecasted GDP data.

    Description
    -----------
    This method combines actual GDP values with forecasted GDP values into a single 
    DataFrame and displays it using Streamlit. Users can download the data as a CSV file 
    for further analysis. The method also displays contextual information about the 
    model and its predictions.

    Parameters
    ----------
    years : int
        The forecast horizon, indicating the number of years into the future for which GDP 
        predictions are generated.

    Returns
    -------
    None
        The method directly displays:
        - A combined DataFrame of actual and forecasted GDP data.
        - An option to download the data as a CSV file via Streamlit.
        - Additional notes and contextual information about the model's predictions.

    Workflow
    --------
    1. Retrieves:
        - Actual GDP data using the `get_fitted_values` method.
        - Forecasted GDP data using the `makeForecast` method with a specified horizon.
    2. Resets the index of the actual GDP DataFrame to include the "Year" column.
    3. Adds a "Type" column to differentiate between actual and forecasted GDP data.
    4. Combines actual and forecasted data into a single DataFrame.
    5. Displays the combined data in an interactive table via `st.dataframe`.
    6. Provides an option to download the table as a CSV file.
    7. Displays a disclaimer about the accuracy and limitations of the predictions.

    Streamlit Integration
    ----------------------
    - **Subheader**: Introduces the purpose of the feature.
    - **Interactive DataFrame**: Displays the combined DataFrame of actual and forecasted GDP values.
    - **Download Option**: Users can download the DataFrame as a CSV file.
    - **Disclaimer**: Highlights the model's training data limitations and advises cautious interpretation 
      of predictions.

    Example
    -------
    >>> model.downloadData(10)
    (Displays actual and forecasted GDP values for the next 10 years and provides a download option.)

    Notes
    -----
    - Actual GDP data is retrieved for the years up to 2023.
    - Forecasted GDP data starts from the year following the latest actual GDP value.
    - Predictions are based on the model trained with historical data up to 2023 and may 
      vary due to future uncertainties.

    Disclaimer
    ----------
    The predictions generated by the model are based on historical data trends and may not account for 
    unforeseen economic, political, or environmental factors. Users are advised to verify important 
    information independently.
    """
    # Get dataframes.
    predicted_gdps =  self.model.makeForecast(years = range(1, years))
    actual_gdps = self.model.get_fitted_values()

    # Reset the index to make 'Year' a column.
    actual_gdps = actual_gdps.reset_index()

    # Add a column to indicate whether the data is actual or predicted.
    actual_gdps["Type"] = "Actual GDP"
    predicted_gdps["Type"] = "Forecasted GDP"

    # Combine the dataFrames.
    combined_df = pd.concat([actual_gdps, predicted_gdps])
    
    # Subheader.
    st.subheader("Download Actual and Predicted GDP Data")
    
    # Information.
    st.write("Download the GDP data as a csv file. Hover mouse over the dataframe or touch on it to access download option.")
    
    # Display the dataframe.
    st.dataframe(combined_df)

    # Disclaimer.
    st.markdown("""
    <div style="text-align: center; font-size: 0.8em; color: grey;">
    The model is trained on data only up to 2023, so predictions may vary due to future uncertainties. Please verify important information independently.
    </div>
    """, unsafe_allow_html=True)

  def resilientEconomy(self):
    """
    Visualizes India's economic resilience and transitional growth trends.

    Description
    -----------
    This method presents visual analyses of India's GDP trajectory over time, emphasizing its 
    remarkable resilience during periods of significant economic transformation and challenges. 
    Using visualizations generated by the `gdpGrowth` method, the analysis highlights key growth 
    phases, including the post-1991 economic reforms and the recovery post-pandemic.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The method directly displays:
        - Two visualizations illustrating India's GDP trajectory and transitional growth trends.
        - Insights about India's economic growth phases and resilience through explanatory text.
        - Key highlights summarized using an expandable section.

    Workflow
    --------
    1. Retrieves two Plotly visualizations from the `gdpGrowth` method:
        - The first chart shows India's overall GDP trajectory, emphasizing transformational growth.
        - The second chart compares actual GDP with a transitional growth trend (red dashed line).
    2. Displays the visualizations using `st.plotly_chart`.
    3. Provides a detailed explanation of each chart's insights:
        - Highlights the impact of post-1991 economic reforms on GDP acceleration.
        - Explains the transitional growth trend's significance, indicating structural strength.
    4. Summarizes key highlights of India's economic resilience in an expandable section.

    Streamlit Integration
    ----------------------
    - **Subheader**: Emphasizes India's economic resilience and growth.
    - **Charts**: Displays interactive visualizations of GDP trends.
    - **Explanatory Text**: Provides contextual insights about India's economic trajectory.
    - **Expandable Section**: Highlights key points of economic resilience and transitional growth.

    Example
    -------
    >>> model.resilientEconomy()
    (Displays visualizations and insights about India's economic resilience and growth.)

    Insights
    --------
    1. **Economic Reforms (Post-1991)**: 
        - The GDP curve shows a significant acceleration post-1991, driven by reforms, globalization, 
          and technological advancements.
    2. **Transitional Growth Trend**: 
        - The red dashed line in the visualizations represents India's steady upward growth trend, 
          signifying a strong economic foundation.
    3. **Resilience Post-Pandemic**: 
        - The alignment of pre-pandemic and post-pandemic growth trends highlights the Indian 
          economy's ability to recover without permanent loss in demand or output.

    Notes
    -----
    - The visualizations and insights are based on historical GDP data and trends.
    - Predictions and trends may not account for unforeseen economic, political, or global factors.

    Disclaimer
    ----------
    The projections and insights provided are based on historical data trends and model analyses. 
    Users are advised to interpret the findings in conjunction with other economic data and reports.
    """
    # Subheader.
    st.subheader("The Indian Economy has Demonstrated Remarkable Resilience")

    # Get figures.
    fig, fig1 = self.model.gdpGrowth()

    # Display first figure and its description.
    st.plotly_chart(fig)
    st.write("This plot visualizes India's GDP trajectory over the years, highlighting a pivotal phase of transformational economic growth. Post-1991, the GDP curve accelerates significantly, indicating India's transition into a high-growth phase driven by economic reforms, increased globalization, and technological advancements.")
    st.write("The red dashed line projects India's transitional growth trend, emphasizing the strong momentum. This trend reflects a robust economic foundation and the potential for continued expansion in the coming years.")
    
    # Display second figure and its description.
    st.plotly_chart(fig1)
    st.write("This plot highlights India's journey through the period of transitional growth. The blue line represents India's actual GDP, while the red dashed line illustrates the transitional growth trend, reflecting a steady upward trajectory.")
    st.write("Notably, the data underscores the Indian economy's ability to recover and maintain growth momentum, even in the face of significant challenges. The alignment of pre-pandemic and post-pandemic growth trends signifies that India experienced no permanent loss in demand or output, showcasing its structural strength.")

    # Display key highlights.
    with st.expander("Key Highlights", expanded = True):
      st.markdown(''':blue-background[Highlight-1] : Indian economy is set in its transitional growth.''')
      st.markdown(''':blue-background[Highlight-2] : The pre-pandemic and post-pandemic transitional growth trends ensure **no permanent loss in demand and output**.''')
