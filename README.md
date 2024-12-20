# Forecasting India's Path to a $5 Trillion Economy

This research paper explores India's economic growth trajectory with a focus on forecasting the timeline for achieving the $5 trillion GDP milestone. It develops a predictive model and an interactive web application (GDP-PY) to visualize and analyze India’s GDP growth trends.

The project leverages historical GDP data, machine learning models, and interactive visualizations to make economic trends accessible and actionable.

# 📜 Abstract

India's economy has demonstrated remarkable resilience and steady growth, particularly in the wake of transformative events like the 1991 economic reforms and the COVID-19 pandemic. This research employs a linear regression model trained on historical GDP data to estimate when India will achieve a GDP of $5 trillion. The findings highlight that, on average, this milestone is expected to be reached by 2029–2030, with robust economic trends underpinning this projection.

The interactive web tool, GDP-PY, complements this research by providing visual insights, downloadable data, and customizable forecasting horizons for researchers, policymakers, and enthusiasts.

# 🎯 Objectives

1. Develop a predictive model to forecast India's GDP for future years.
2. Estimate when India will achieve a GDP of $5 trillion at current prices.
3. Analyze pre- and post-pandemic growth patterns to highlight the economy's resilience.
4. Provide an open-source, user-friendly web application (GDP-PY) to explore GDP trends.
5. Share the methodology transparently to foster collaboration and innovation.

# 🚀 Features

- **Customizable Forecast Horizons**: Explore GDP projections for your desired timeline.
- **Visual Insights**: Line and bar charts highlight past growth, predictions, and transitional trends.
- **Empirical Validation**: See model performance with actual vs. predicted GDP comparisons.
- **Downloadable Data**: Access historical and forecasted GDP data for further analysis.
- **Open-Source Methodology**: Transparent implementation to foster collaboration.

# 📊 Components

1. **GDP Forecasting**
   - Predict GDP values for future years using a trained regression model.
   - Identify key milestones, such as reaching $5 trillion GDP.
2. **Resilient Economic Trends**
   - Visualize India’s recovery post-pandemic.
   - Analyze transitional growth trends showcasing economic resilience.
3. **Interactive Web Application: GDP-PY**
   - Visit [GDP-PY](https://gdp-py.streamlit.app) for interactive visualizations, tools, and insights.

# 🛠 Methodology

1. **Data Collection**
   - Historical GDP data (1960–2023) sourced from the [World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=IN).
2. **Model Development**
   - Linear regression model, trained on lagged GDP values for simplicity and interpretability, is employed to predict future growth.
3.  **Forecasting**
    - The trained model was used to forecast GDP values for a customizable range of future years. 
5. **Model Evaluation**
   - Empirical evaluation through actual vs. predicted comparisons and visualization of model fit.
6. **Visualization and User Interaction**
   - A web application ([GDP-PY](https://gdp-py.streamlit.app)) was developed to present the findings interactively.

# 🌟 Explore

**🦋 Web Application**

Visit [GDP-PY](https://gdp-py.streamlit.app) to explore visualizations and predictions interactively.

**📦 Data & Resources**

- Dataset: Historical GDP data (1960–2023) from [World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=IN).
- Notebook: [Full Methodology](https://github.com/neuraledgeai/GDP-PY/blob/main/Forecasting_India_GDP.ipynb).

**🔬 Emperical Results**

- Forecast Accuracy: The model predicts GDP growth trends with high reliability.
- Key Insight: India will likely achieve $5 trillion GDP by 2029-2030 at current prices.

>[!TIP]
>For a deeper dive into the data description, emperical results and methods used in this project, please check out the [`Forecasting_India_GDP.ipynb`](https://github.com/neuraledgeai/GDP-PY/blob/main/Forecasting_India_GDP.ipynb) notebook. Whether you're interested in the technical details or the insights derived from the analysis, the notebook provides a comprehensive overview of the entire project.

# License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](https://github.com/neuraledgeai/GDP-PY/blob/main/LICENSE) for more details.

# Author

Anoop Kumar U, MA Economics, S.N. College, Varkala.

Email: anoop_kumar_u@icloud.com

# Acknowledgement

I, Anoop Kumar U, thank all instructors and colleagues who reviewed this research draft before publication. Their valuable insights and constructive feedback greatly enhanced its quality and clarity.

I also thank the creators and contributors of the open-source libraries that were instrumental in this research, especially

- Scikit-learn - [Copyright (c) 2007-2024 The scikit-learn developers. All rights reserved](https://github.com/scikit-learn/scikit-learn?tab=BSD-3-Clause-1-ov-file).
- Pandas - [Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team All rights reserved](https://github.com/pandas-dev/pandas?tab=BSD-3-Clause-1-ov-file).
- Joblib - [Copyright (c) 2008-2021, The joblib developers. All rights reserved](https://github.com/joblib/joblib?tab=BSD-3-Clause-1-ov-file).
- [Matplotlib](https://ieeexplore.ieee.org/document/4160265).
- [Streamlit](https://github.com/streamlit/streamlit?tab=Apache-2.0-1-ov-file).

Finally, I would like to thank the open-source and research community for their continuous inspiration and support, which drives innovation and collaboration in pursuit of knowledge.

# Disclaimer

The model is trained on data only up to 2023, so predictions may vary due to future uncertainties. As new GDP data becomes available, the model will be retrained,*potentially revising the current conclusion of India achieving a $5 trillion GDP by 2029-2030*, ensuring accuracy with the latest trends. For updated forecasts visit [GDP-PY](https://gdp-py.streamlit.app).
