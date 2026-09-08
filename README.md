<div align="center">

# Socioeconomic Analytics

### Data Intelligence & Visual Analytics Platform

**Interactive tools for exploring, comparing and visualizing socioeconomic indicators across cities, regions and countries.**

![Tier](https://img.shields.io/badge/Portfolio-Tier%20A-0A66C2?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

</div>

## The Problem

Socioeconomic datasets are multidimensional and difficult to interpret through static tables alone. This project turns those datasets into interactive analytical workflows that help users compare locations, inspect relationships between indicators and identify patterns visually.

## Solution

A modular Python/Streamlit application combines data processing, reusable analytical components and interactive visualization in a single interface. The project grew from econophysics research and evolved into a reusable visual-analytics toolkit.

## Key Capabilities

- Compare socioeconomic indicators between cities and regions
- Explore variable relationships with multiple scatter-plot approaches
- Analyze trends using binscatter techniques
- Navigate independent analytical modules from one interface
- Work with structured CSV datasets
- Maintain consistent country/region visual mappings

## Architecture

```text
User
  ↓
Streamlit Interface (main_code.py)
  ↓
Analysis Modules
  ├─ Binscatter
  ├─ Cities Compare
  ├─ Normal Scatter
  └─ Scatter Graph
  ↓
Shared Processing / Utilities
  ↓
CSV Data Layer
```

## Tech Stack

`Python` · `Streamlit` · `Jupyter` · `Data Visualization` · `Visual Analytics` · `CSV/Data Processing`

## Project Structure

```text
Streamlit_Dashboard/
├── main_code.py
├── functions.py
├── libraries.py
├── colors_countries_and_regions.py
├── Binscatter_code.py
├── Cities_Compare_code.py
├── NormalScatter_code.py
├── ScatterGraph_code.py
├── tabelas_csv/
└── requirements.txt
```

Additional directories preserve research, experiments and earlier analytical components, including `GraphGCA/`, `Master_Thesis_EconoPhysics/`, `NormalScatter/` and `ScatterGraph/`.

## Run Locally

```bash
git clone https://github.com/LeonardoCamargoRossato/Analysis_SocioEconomic_Indicator.git
cd Analysis_SocioEconomic_Indicator/Streamlit_Dashboard
pip install -r requirements.txt
streamlit run main_code.py
```

## Engineering Perspective

The current architecture separates interface, analysis, data and utility concerns, making the system a useful bridge between scientific research code and a product-oriented analytics application.

## Portfolio Classification

**Tier A — Featured Portfolio Project.** Selected to represent data engineering, visual analytics and the transformation of research methods into an interactive software solution.

---

**Leonardo Camargo Rossato** · Developer & Solution Architect · AI, Data & Deep Tech
