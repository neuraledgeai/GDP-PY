# 🧾 Metadata: `forecast_data.csv`

**File Name:** `forecast_data.csv`  
**License:** [CC BY 4.0↗](https://creativecommons.org/licenses/by/4.0/)  
**Source:** Derived from World Bank GDP (current USD) data — forecasted using GDP-PY model     
**Last Updated:** October 2025  

---

## 📘 Description

This dataset contains **forecasted GDP values for India (2025–2029)** at *current prices (USD)*, generated using the **GDP-PY forecasting model**. 
The model projects nominal GDP based on historical World Bank data, a linear regression model.
The projections indicate India’s steady economic momentum, crossing the **$5 trillion GDP mark by 2028**.

---

## 🧮 Data Dictionary

| Column Name | Type | Description |
|--------------|------|-------------|
| `Date` | `YYYY-MM-DD` | The reference date for the forecasted GDP value (as of January 1 each year). |
| `Forecast_GDP` | `float64` | Forecasted GDP in **current US dollars**. |

---

## 📊 Sample Data

| Date | Forecast_GDP (USD) |
|------|--------------------|
| 2025-01-01 | 4,184,125,110,813 |
| 2026-01-01 | 4,473,873,813,159 |
| 2027-01-01 | 4,783,167,350,117 |
| 2028-01-01 | 5,113,324,107,439 |
| 2029-01-01 | 5,465,751,401,836 |

*(Values rounded for readability)*

---

## ⚙️ Methodology Overview

- **Model:** GDP-PY (Polynomial Yield-based Model)  
- **Data Basis:** Historical GDP data (World Bank, 1960–2023)  
- **Currency:** USD (current prices, not adjusted for inflation)  
- **Computation:** Forecasts generated via regression on GDP growth rate trends with smoothing for post-pandemic volatility.  
- **Validation:** Cross-checked against IMF World Economic Outlook mid-2025 estimates.

---

**Attribution:**  
World Bank Open Data — [GDP (current US$)](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=IN)  
© The World Bank | Licensed under [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
