Analysis SocioEconomic Indicator

This repository contains an interactive data analysis application built with Python and Streamlit, focused on the exploration, comparison, and visualization of socio-economic indicators across cities, regions, and countries.

The project was developed as a visual analytics tool to support the understanding of complex datasets through modular analysis components and interactive visualizations.

Overview

The application allows the user to:

Compare socio-economic indicators between cities and regions
Explore relationships between variables using different types of scatter plots
Analyze trends through binscatter techniques
Navigate between multiple analytical modules
Work with structured datasets stored in CSV format

The system follows a modular architecture, where each type of analysis is implemented as an independent component.

Project Structure
Analysis_SocioEconomic_Indicator/

├── Streamlit_Dashboard/
│   ├── main_code.py
│   ├── functions.py
│   ├── libraries.py
│   ├── colors_countries_and_regions.py
│   ├── Binscatter_code.py
│   ├── Cities_Compare_code.py
│   ├── NormalScatter_code.py
│   ├── ScatterGraph_code.py
│   ├── tabelas_csv/
│   ├── images/
│   ├── __pycache__/
│   └── requirements.txt
│
├── GraphGCA/
├── Master_Thesis_EconoPhysics/
├── NormalScatter/
├── ScatterGraph/
Description of Components
Streamlit_Dashboard/

This is the main application layer, responsible for the user interface and orchestration of all analysis modules.

main_code.py
Entry point of the application. Controls navigation, layout, and interaction between modules.
functions.py
Contains reusable functions for data processing, filtering, and manipulation.
libraries.py
Centralizes imports and dependencies used across the project.
colors_countries_and_regions.py
Defines visual standards (color mappings) for countries and regions to ensure consistency across plots.
Analysis Modules

Each module encapsulates a specific analytical approach:

Binscatter_code.py
Implements binscatter plots for identifying average trends in noisy data.
Cities_Compare_code.py
Provides direct comparison between cities based on selected indicators.
NormalScatter_code.py
Standard scatter plot analysis for visualizing relationships between variables.
ScatterGraph_code.py
Extended/custom scatter plot implementation with additional visual or analytical features.
Data and Assets
tabelas_csv/
Contains all datasets used in the application. These are structured socio-economic indicators in CSV format.
images/
Stores images used in the interface (logos, backgrounds, etc.).
pycache/
Automatically generated Python cache files.
requirements.txt
Lists all Python dependencies required to run the project.
Additional Directories
GraphGCA/
Master_Thesis_EconoPhysics/
NormalScatter/
ScatterGraph/

These directories appear to contain auxiliary scripts, experiments, or earlier versions of analytical components related to the project development and research context.

How to Run

Clone the repository:

git clone https://github.com/LeonardoCamargoRossato/Analysis_SocioEconomic_Indicator.git
cd Analysis_SocioEconomic_Indicator/Streamlit_Dashboard

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run main_code.py
Architecture

The project follows a layered structure:

Interface layer: Streamlit (main_code.py)
Analysis layer: modular scripts (*_code.py)
Data layer: CSV files
Utility layer: shared functions and configurations

This design allows the system to be extended or integrated into more robust architectures, such as APIs or full-stack applications.

Possible Extensions
Integration with databases (PostgreSQL, Supabase, etc.)
Backend API (FastAPI or Flask)
Frontend decoupling (React or similar frameworks)
User data upload and dynamic dataset handling
Automated report generation
Authentication and multi-user support
Author

Leonardo Rossato
PhD Student at ITA
Physicist and Data Scientist
President at ICTQ Foton
