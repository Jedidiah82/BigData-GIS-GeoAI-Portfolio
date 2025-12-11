---
title: "Lassa Fever GeoAI Forecasting — Liberia (2016–2026)"
author: "Godwin Etim Akpan"
affiliation: "Public Health Informatics | GeoAI | Spatial Epidemiology"
version: "1.0"
last_updated: "2025-01-01"

description: |
  A fully reproducible spatio-temporal forecasting pipeline integrating 
  national time series models (ARIMA, Prophet, STL decomposition) with 
  GeoAI-based county-level forecasting using XGBoost. Includes hotspot 
  mapping, trend decomposition, forecasting to 2026, and manuscript-ready 
  outputs for scientific communication.

datasets:
  - name: "Lassa Fever line list (mocked for reproducibility)"
    type: "CSV"
    source: "MoH/NPHIL (not distributed — synthetic template only)"
  - name: "Liberia administrative boundaries"
    type: "Shapefiles"
    source: "HDX / Humanitarian Data Exchange"

models:
  - ARIMA (univariate forecasting)
  - Prophet (trend–seasonality decomposition)
  - STL (observed seasonal decomposition)
  - XGBoost regression (GeoAI spatio-temporal forecasting)

dependencies:
  python: ">=3.10"
  packages:
    - pandas
    - numpy
    - scikit-learn
    - xgboost
    - prophet
    - geopandas
    - matplotlib
    - seaborn

reproducibility:
  requires:
    - Jupyter Lab or VS Code Notebooks
    - Mock datasets provided in data_template/
    - Shapefiles stored in shapefiles/
  run:
    - "Open 05_Reproducibility_Notebook.ipynb and execute all cells"

license: "MIT License (repository only — not for clinical use)"
---

# 🦠 **Lassa Fever GeoAI Forecasting — Liberia (2016–2026)**

This folder contains a complete **spatio-temporal forecasting workflow** for Lassa fever in Liberia.  
The project integrates **classical epidemiological time-series analysis** with **modern GeoAI** to predict national and subnational transmission patterns through **December 2026**.

Designed for **public health decision-making**, **epidemiological research**, and **GeoAI demonstration**, the workflow produces:

- 📈 National-level case forecasts (ARIMA, Prophet)  
- 🔍 Trend, seasonality, and anomaly decomposition (STL)  
- 🤖 County-level GeoAI projections (XGBoost)  
- 🗺 Heatmaps and hotspot spatial predictions  
- 🎥 (Optional) Animations of forecast progression  
- 📝 Manuscript-ready figures  

---

## 🔬 **Objectives**

1. Build a **cleaned national and county-level dataset** (2016–2022).  
2. Model monthly national incidence using:  
   - ARIMA  
   - Prophet  
   - STL decomposition  
3. Engineer spatio-temporal features for GeoAI (lags, rolling means, climate proxies).  
4. Train an **XGBoost model** to forecast county-level risk.  
5. Generate predictions for **2023–2026**.  
6. Produce **maps, figures, and tables** suitable for surveillance reporting and research publication.


---

## 🧠 **Modeling Workflow**

### **1️⃣ Time-Series Forecasting (National Level)**  
- ARIMA for autoregressive temporal modeling  
- Prophet for trend + seasonal cycle extraction  
- STL for structural decomposition  
- Confidence intervals and peak annotations  
- Comparison plots through **2026**  

### **2️⃣ GeoAI (County-Level Forecasting)**  
- Lagged case features (t-1, t-2, t-3)  
- Rolling means and seasonal features  
- Optional covariates (rainfall, temperature, roads, population)  
- XGBoost regression to generate **spatial predictions**  

### **3️⃣ Spatial Analysis**  
- Choropleth hotspot maps  
- Cluster visualization (SaTScan-style but custom Python)  
- Multi-panel yearly incidence maps  
- Animated county-level risk evolution (optional)

---

## 🖼 Example Outputs (Figures)

Your plots will appear here automatically when uploaded:

- **ARIMA vs Prophet Forecast (2016–2026)**
- **Prophet Trend & Seasonality Components**
- **STL Decomposition**
- **Rolling Mean Trends**
- **GeoAI Hotspot Map (December 2026)**
- **County-Level Incidence Maps (2017–2022)**
- **Cluster Maps for Localized Hotspots**

*(Images rendered from your analysis — no raw case data included.)*

---

## 🔒 **📌 Data Disclaimer**

All visualizations and outputs in this folder are derived from **aggregated, non-identifiable surveillance data** used strictly for academic and public health research purposes.

- **No individual-level data** is stored or shared.  
- **No confidential MoH/NPHIL datasets** are included.  
- Synthetic or template datasets are provided **only for reproducibility**.  
- Results shown here are analytical outputs and **do not represent official government reports**.

---

## 📚 **Citation**

If referencing this work in research or professional documentation:

Akpan, G.E. (2025). Lassa Fever GeoAI Forecasting — Liberia (2016–2026).
Big Data • GeoAI • Public Health Analytics Portfolio.
https://github.com/Jedidiah82/