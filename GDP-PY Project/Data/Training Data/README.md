# 🧾 Metadata: `training_data.csv`

**File Name:** `training_data.csv`  
**License:** [CC BY 4.0↗](https://creativecommons.org/licenses/by/4.0/)  
**Source:** World Bank Open Data (GDP, current US$)  
**Maintainer:** Anoop Kumar U | anoop_kumar_u@icloud.com  
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

## 📊 Sample Data

| Date | GDP (USD) | GDP_L1 (USD) |
|------|------------|--------------|
| 1961-01-01 | 39,232,435,784 | 37,029,883,876 |
| 1962-01-01 | 42,161,481,858 | 39,232,435,784 |
| 1963-01-01 | 48,421,923,459 | 42,161,481,858 |
| 1964-01-01 | 56,480,289,940 | 48,421,923,459 |
| 1965-01-01 | 59,556,105,229 | 56,480,289,940 |
| ... | ... | ... |
| 2024-01-01 | 3,912,686,168,582 | 3,638,489,096,033 |

*(Values rounded for readability)*

---

## ⚙️ Methodology Overview

- **Source Data:**  
  [World Bank GDP (current US$)](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=IN)

- **Processing Steps:**  
  1. Imported World Bank GDP data (CSV).  
  2. Converted `Date` column to datetime format.  
  3. Created a lagged feature `GDP_L1` by shifting the GDP series by one year.  
  4. Dropped missing records after lag creation.  

- **Usage:**  
  This dataset was used to train the **GDP-PY model**, which predicts future GDP based on historical growth patterns and lagged relationships.

---

## 🧭 Citation

If you use this dataset, please cite as:

> Kumar, A.U. (2025). *India GDP Historical Training Dataset (1961–2024)*. Derived from World Bank Open Data. Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

---

**Attribution:**  
World Bank Open Data — [GDP (current US$)](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=IN)  
© The World Bank | Licensed under [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
