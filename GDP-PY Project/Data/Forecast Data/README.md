# 🧾 Metadata: `forecast_data.csv`

**File Name:** [`forecast_data.csv`](https://github.com/neuraledgeai/GDP-PY/blob/main/GDP-PY%20Project/Data/Forecast%20Data/forecast_data.csv)  
**License:** [CC BY 4.0↗](https://creativecommons.org/licenses/by/4.0/)  
**Source:** Derived from World Bank GDP (current USD) data — forecasted using [GDP-PY model](https://github.com/neuraledgeai/GDP-PY/tree/main/GDP-PY%20Project/Model)     
**Last Updated:** October 2025  

---

## 📘 Description

This dataset contains **forecasted GDP values for India (2025–2029)** at *current prices (USD)*, generated using the [GDP-PY forecasting model](https://github.com/neuraledgeai/GDP-PY/tree/main/GDP-PY%20Project/Model). 
The model projects nominal GDP based on historical World Bank data, a linear regression model.
The projections indicate India’s steady economic momentum, crossing the **$5 trillion GDP mark by 2028**.

---

## 🧮 Data Dictionary

| Column Name | Type | Description |
|--------------|------|-------------|
| `Date` | `YYYY-MM-DD` | The reference date for the forecasted GDP value (as of January 1 each year). |
| `Forecast_GDP` | `float64` | Forecasted GDP in **current US dollars**. |

---

## ⚙️ Methodology Overview

- **How the data was produced?:**  
  1. Imported the [World Bank GDP data (CSV)](https://github.com/neuraledgeai/GDP-PY/blob/main/GDP-PY%20Project/Data/GDP%20Data%20(World%20Bank)/gdp_current_usd_india.csv).
  2. Prepared the [training data](https://github.com/neuraledgeai/GDP-PY/tree/main/GDP-PY%20Project/Data/Training%20Data)
  3. The [GDP-PY forcasting model](https://github.com/neuraledgeai/GDP-PY/tree/main/GDP-PY%20Project/Model) was trained.
  4. Used the last known GDP value for 2024 as the starting point (`3.91 trillion USD`).
  5. Predicted GDP recursively for the next 5 years (2025–2029)
  6. Compiled results into a DataFrame and exported as [`forecast_data.csv`](https://github.com/neuraledgeai/GDP-PY/blob/main/GDP-PY%20Project/Data/Forecast%20Data/forecast_data.csv).

- **Usage:**  

  The [`forecast_data.csv`](https://github.com/neuraledgeai/GDP-PY/blob/main/GDP-PY%20Project/Data/Forecast%20Data/forecast_data.csv) file can be used for visualizing India’s GDP growth trends (2025–2029), building dashboards or economic models, and analysing GDP trend.

---

**Attribution:**  
World Bank Open Data — [GDP (current US$)](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=IN)  
© The World Bank | Licensed under [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
