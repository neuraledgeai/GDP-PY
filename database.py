import pandas as pd

class LocalDatabase:
  """
    A class to manage and process local GDP data for India.

    This class provides methods to load, clean, and transform GDP data stored in a CSV file.
    The data is structured to enable time-series analysis and includes options for adding
    lagged features to aid in modeling and forecasting.

    Attributes
    ----------
    df : pd.DataFrame
        The raw data loaded from the specified CSV file. This is initialized when the class is instantiated
        and used as a base for further transformations.

    Methods
    -------
    __init__(file_name="gdp_india_1960-2023.csv")
        Initializes the class by loading a CSV file containing India's GDP data.

    loadData(lag=False)
        Loads and processes a cleaned DataFrame containing time-series data of India's GDP.
        Optionally includes a one-step lagged feature for analysis.
    """
  
  def __init__(
    self,
    file_name = "gdp_india_1960-2023.csv"
  ):
    """
    Initializes the class by loading a CSV file containing India's GDP data.

    Parameters
    ----------
    file_name : str, optional, default="gdp_india_1960-2023.csv"
        The name or path of the CSV file containing the GDP data. 
        The file is expected to have columns such as 'Country Name', 'Country Code', 
        'Indicator Name', 'Indicator Code', and GDP values for different years.

    Attributes
    ----------
    df : pd.DataFrame
        A DataFrame that holds the raw data loaded from the CSV file.
        The DataFrame will be further processed in other methods for analysis.
    """
    
    # Load the GDP data from the specified CSV file into a DataFrame.
    # This DataFrame will be stored as an instance attribute for use in other methods.
    self.df = pd.read_csv(file_name)
    
  def loadData(self, lag=False):
    """
    Loads and processes a cleaned DataFrame containing time-series data of India's GDP.

    Parameters
    ----------
    lag : bool, optional, default=False
        If True, includes a one-step lagged GDP feature (`GDP_L1`) in the returned DataFrame.
        Otherwise, only the current year's GDP data is included.

    Returns
    -------
    pd.DataFrame
        A processed DataFrame with the following structure:
        - Index: Year (set as the index column).
        - Columns: 
            - 'GDP': The GDP values as floats.
            - 'GDP_L1' (if `lag=True`): The one-step lagged GDP values as floats.
    """
    
    # Reshape the DataFrame using melt to organize the data.
    df = pd.melt(
        self.df,
        id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],  # Columns to keep as identifiers
        var_name='Year',      # The name of the new column for the years
        value_name='GDP'      # The name of the new column for the GDP values
    )
    
    # Convert "Year" to a pandas datetime object and set it as the index for time-series analysis. Also drop unnecessary identifier columns.
    df["Year"] = pd.to_datetime(df["Year"], format="%Y")
    df = df.set_index("Year").drop(columns=["Country Name", "Country Code", "Indicator Name", "Indicator Code"]) 
    
    # Add a one-step lagged GDP feature if the "lag" parameter is "True".
    if lag:
      df["GDP_L1"] = df["GDP"].shift(1) # Adding a new feature for GDP_L1
      df = df.dropna()  # Drop rows with NaN values resulting from the shift
      df["GDP_L1"] = df["GDP_L1"].astype(float) # Ensure the "lagged-GDP" column is of type "float".
      
    # Ensure the "GDP" column is of type "float" for consistency in numerical operations.
    df["GDP"] = df["GDP"].astype(float) #Make sure that the GDP column is of type float.
    
    # Return the cleaned and processed DataFrame.
    return df
  
