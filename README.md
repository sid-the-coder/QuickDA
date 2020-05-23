# Quick-EDA

Simple & Easy-to-use python modules to perform Quick Exploratory Data Analysis for any structured dataset!

![EDA with Python](https://miro.medium.com/max/1400/1*Ptv1_9wX9O2Rm2IBklyufw.png)

## Getting Started

### Pre-Requistes

You will need to have [Python 3](https://www.python.org) and [Jupyter Notebook](https://jupyter.org) installed in your local system. Once installed, Fork this repository and clone it on your local to get the project structure setup.
```
git clone https://github.com/sid-the-coder/Quick-EDA.git
```

You will also need to install few python package dependencies in your evironment to get started. You can do this by:
```
pip3 install -r requirements.txt
```

## Table of Contents

1. [Data Exploration - explore(data)](https://github.com/sid-the-coder/Quick-EDA#data-exploration)
    - **data: pd.DataFrame**
    - **method: string, default="summarize"**
        - "summarize" : Generates a summary statistics of the dataset
        - "profile" : Generates a HTML Report of the Dataset Profile
    - **report_name: string, default="Dataset Report"**
        - Parameter to customise the generated report name
    - **is_large_dataset: Boolean, default=False**
        - Parameter set to True explicitly to flag, in case of a large dataset 
    
2. [Data Cleaning - clean(data)](https://github.com/sid-the-coder/Quick-EDA#data-cleaning)
    - **data: pd.DataFrame**
    - **method: string, default="default"**
        - "default" : Standardizes column names, Removes duplicates rows and Drops missing values
        - "standardize" : Standardizes column names
        - "dropcols" : Drops columns specified by the user
        - "dtypes" : Explicitly converts the Data Types as specified by the user
        - "duplicates" : Removes duplicate rows
        - "replaceval" : Replaces a value in dataframe with new value specified by the user
        - "fillmissing" : Interpolates all columns with missing values using forward filling
        - "dropmissing" : Drops all rows with missing values
        - "outliers" : Removes all outliers in data using IQR method
    - **columns: list/string, default=[]**
        - Parameter to specify column names in the DataFrame
    - **dtype: string, default="numeric"**
        - "numeric" : Converts columns dtype to numeric
        - "category" : Converts columns dtype to category
        - "datetime" : Converts columns dtype to datetime
    - **to_replace: string/integer/regex, default=""**
        - Parameter to pass a value to replace in the DataFrane
    - **value: string/integer/regex, default=np.nan**
        - Paramter to pass a new value that replaces an old value in the Dataframe
    
3. [EDA Numerical Features - eda_num(data)](https://github.com/sid-the-coder/Quick-EDA#eda-numerical-features)
    - **data: pd.DataFrame**
    - **method: string, default="default"**
        - "default" : Shows all Outlier & Distribution Analysis via BoxPlots & Histograms
        - "correlation" : Gets the correlation matrix between all numerical features
    - **bins: integer, default=10**
        - Parameter to set the number of bins while displaying histograms
    
4. [EDA Categorical Features - eda_cat(data, x)](https://github.com/sid-the-coder/Quick-EDA#eda-categorical-features)
    - **data: pd.DataFrame**
    - **x: string, First Categorical Type Column Name**
    - **y: string, default=None**
        - Parameter to pass the Second Categorical Type Column Name
    - **method: string, default="default"**
        - "default" : Shows category count plot & summarizes it in a frequency table
    
5. [EDA Numerical with Categorical Features - eda_numcat(data, x, y)](https://github.com/sid-the-coder/Quick-EDA#eda-numerical-with-categorical-features)
    - **data: pd.DataFrame**
    - **x: string/list, Numeric/Categorical Type Column Name(s)**
    - **y: string/list, Numeric/Categorical Type Column Name(s)**
    - **method: string, default="pps"**
        - "pps" : Calculates Predictive Power Score Matrix
        - "relationship" : Shows Scatterplot of given features
        - "comparison" : Shows violin plots to compare categories across numerical features
        - "pivot" : Generates pivot table using column names, values and aggregation function
    - **hue: string, default=None**
        - Parameter to visualise a categorical Type feature within scatterplots
    - **values: string/list, default=None**
        - Parameter to set columns to aggregate on pivot views
    - **aggfunc: string, default="mean"**
        - Parameter to set aggregate functions on pivot tables 
        - Example: 'min', 'max', 'mean', 'median', 'sum', 'count'
    
6. [EDA Time Series Data - eda_timeseries(data, x, y)](https://github.com/sid-the-coder/Quick-EDA#explore-time-series-data)
    - **data: pd.DataFrame**
    - **x: string, Datetime Type Column Name**
    - **y: string, Numeric Type Column Name**
