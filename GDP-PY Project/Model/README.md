# 🤖 GDP-PY Forecasting Model 

This file documents the **GDP Forecasting Model** built as part of the **GDP-PY Project**.  
The model uses a **Linear Regression** approach to predict India’s future GDP based on historical data from the **World Bank**.

---

## 🧠 Model Overview

- **Model Type:** Linear Regression  
- **Purpose:** Predict India's GDP (in current USD) for upcoming years using past GDP trends.  
- **Input Feature:** Lagged GDP (`GDP_L1`) — previous year's GDP value.  
- **Target Variable:** `GDP` — current year's GDP value.  
- **Training Data Size:** 64 yearly observations.  
- **Training Source:** [World Bank GDP Data (India)](https://github.com/neuraledgeai/GDP-PY/blob/main/GDP-PY%20Project/Data/GDP%20Data%20(World%20Bank)/gdp_current_usd_india.csv)

---

## ⚙️ Methodology

- Imported India’s GDP data from the World Bank dataset.  
- Converted the `Date` column into datetime format.  
- Created a lagged feature `GDP_L1` (previous year’s GDP).  
- Dropped missing records created by lagging.  
- Defined:
  - **Feature (X):** `GDP_L1`
  - **Target (y):** `GDP`
- Split the available 64 yearly records for model fitting.  
- Trained a **Linear Regression model** using `GDP_L1` as the only predictor.

---

## 📊 Model Performance

| Metric | Value (USD) | Description |
|:--------|:------------:|:------------|
| **Baseline MAE** | 848,610,406,234.99 | Mean Absolute Error using mean-based prediction |
| **Model MAE** | 45,792,623,222.29 | Mean Absolute Error after Linear Regression training |

🔹 The model reduces the MAE by over **94%**, demonstrating strong accuracy in capturing GDP trends.  
🔹 Given GDP’s strong autocorrelation, a **simple lag-based linear model** performs remarkably well.

---

## 🧩 Forecasting Logic

The trained model is used recursively to generate multi-year GDP forecasts:

```python
def make_prediction(gdp):
    X = pd.DataFrame([[gdp]], columns=["GDP_L1"])
    forecast = model.predict(X)
    return forecast[0]

def forecast_gdp(last_gdp, last_year, n_years=5):
    forecasts = []
    gdp_value = last_gdp
    
    for _ in range(n_years):
        gdp_value = make_prediction(gdp_value)
        forecasts.append(gdp_value)
    
    future_years = pd.date_range(
        start=f"{last_year+1}-01-01", 
        periods=n_years, 
        freq="YS"
    )
    
    return pd.DataFrame({"Forecast_GDP": forecasts}, index=future_years)
