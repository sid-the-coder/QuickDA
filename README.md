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

1. [Data Exploration](https://github.com/sid-the-coder/Quick-EDA#data-exploration)
    - standardize_column_names(data)
    - generate_data_profile_report(data, report_name, is_large_dataset)
    - summarize_data(data)
    
2. [Data Cleaning](https://github.com/sid-the-coder/Quick-EDA#data-cleaning)
    - drop_features(data, columns_to_drop)
    - convert_features_dtype_to_datetime(data, datetime_columns)
    - convert_features_dtype_to_category(data, dic)
    - convert_features_dtype_to_numeric(data, numeric_columns)
    - drop_duplicate_rows(data)
    - replace_value_with_na(data, value_to_replace)
    - visualize_missing_data(data)
    - fill_na_rows(data, na_columns)
    - drop_na_rows(data)
    
3. [EDA - Numerical Features](https://github.com/sid-the-coder/Quick-EDA#eda-numerical-features)
    - boxplot_of_numerical_features(data)
    - remove_outliers_in_numerical_feature(data, num_column)
    - histogram_of_numerical_features(data, num_of_bins)
    - get_correlation_between_numerical_features(data)
    
4. [EDA - Categorical Features](https://github.com/sid-the-coder/Quick-EDA#eda-categorical-features)
    - barchart_of_categorical_features(data, cat_column, cat_column_2=None)
    - get_summary_of_categorical_feature(data, cat_column, cat_column_2=None)
    
5. [EDA - Numerical with Categorical Features](https://github.com/sid-the-coder/Quick-EDA#eda-numerical-with-categorical-features)
    - find_predictive_power_score(data)
    - scatterplot_between_categorical_features(data, x_num_column, y_num_column, cat_column=None)
    - violinplot_of_categorical_with_numerical_feature(data, cat_column, num_column)
    - pivot_data(data, cat_columns_1, agg_num_columns, cat_columns_2=None, agg_method='median')
    
6. [EDA - Time Series Data](https://github.com/sid-the-coder/Quick-EDA#explore-time-series-data)
    - plot_time_series_distribution(data, datetime_column, target_column)
    