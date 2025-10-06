# 🧾 Metadata: `training_data.csv`

**File Name:** [`training_data.csv`](https://github.com/neuraledgeai/GDP-PY/blob/main/GDP-PY%20Project/Data/Training%20Data/training_data.csv)  
**License:** [CC BY 4.0↗](https://creativecommons.org/licenses/by/4.0/)  
**Source:** World Bank Open Data (GDP, current US$)  
**Last Updated:** October 2025  

---

## 📘 Description

This dataset contains **historical GDP data for India (1961–2024)**, used for training the **GDP-PY forecasting model**.  
Each record represents India's GDP at *current prices (USD)*, along with a **lagged feature (`GDP_L1`)** that stores the GDP value from the previous year.  

This dataset forms the foundation for model training, enabling the projection of GDP growth up to 2029.

---

## 🧮 Data Dictionary

| Column Name | Type | Description |
|--------------|------|-------------|
| `Date` | `YYYY-MM-DD` | The reference year for the GDP value (as of January 1). |
| `GDP` | `float64` | Nominal GDP of India in **current US dollars** for that year. |
| `GDP_L1` | `float64` | Previous year’s nominal GDP (lagged by one year), used as a predictor variable. |

---

## ⚙️ Methodology Overview

- **How the data was produced?:**  
  1. Imported [World Bank GDP data (CSV](https://github.com/neuraledgeai/GDP-PY/blob/main/GDP-PY%20Project/Data/GDP%20Data%20(World%20Bank)/gdp_current_usd_india.csv).  
  2. Converted `Date` column to datetime format.  
  3. Created a lagged feature `GDP_L1` by shifting the GDP series by one year.  
  4. Dropped missing records after lag creation.  

- **Usage:**  
  This dataset was used to train the **GDP-PY model**, which predicts future GDP based on historical growth patterns and lagged relationships.

---

**Attribution:**  
World Bank Open Data — [GDP (current US$)](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=IN)  
© The World Bank | Licensed under [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
