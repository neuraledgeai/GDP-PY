import pandas as pd

class LocalDatabase:
  
  def __init__(
    self,
    file_name = "gdp_india_1960-2023.csv"
  ):
    self.df = pd.read_csv(file_name)
    
  def loadData(self, lag=False):
    df = pd.melt(
        self.df,
        id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],  # Columns to keep as identifiers
        var_name='Year',      # The name of the new column for the years
        value_name='GDP'      # The name of the new column for the GDP values
    )
    df = df.set_index("Year").drop(columns=["Country Name", "Country Code", "Indicator Name", "Indicator Code"])
    if lag:
      # Adding a new feature for GDP_L1
      df["GDP_L1"] = df["GDP"].shift(1)
      df = df.dropna()  # Drop rows with NaN values resulting from the shift
      df["GDP_L1"] = df["GDP_L1"].astype(float)

    df["GDP"] = df["GDP"].astype(float)
    
    
    return df
  
