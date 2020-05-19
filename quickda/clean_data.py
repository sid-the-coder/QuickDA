import pandas as pd
import numpy as np
import missingno
import matplotlib.pyplot as plt

def drop_features(data, columns_to_drop):
    data.drop(columns_to_drop, inplace=True, axis=1, errors='ignore')
    return data

def convert_features_dtype_to_datetime(data, datetime_columns):
    for column in datetime_columns:
        data[column] = data[column].apply(pd.to_datetime, infer_datetime_format=True, errors='coerce')
    return data

def convert_features_dtype_to_category(data, dic):
    for column_name, is_ordinal in dic.items():
        data[column_name] = pd.Categorical(data[column_name], ordered=is_ordinal)
    return data

def convert_features_dtype_to_numeric(data, numeric_columns):
    for column in numeric_columns:
        data[column] = data[column].apply(pd.to_numeric, errors='coerce')
    return data

def drop_duplicate_rows(data):
    data.drop_duplicates(inplace=True)
    return data

def replace_value_with_na(data, value_to_replace):
    data.replace(value_to_replace, np.NaN, inplace=True)
    return data

def visualize_missing_data(data):
    missingno.matrix(data)
    plt.show()

def fill_na_rows(data, na_columns):
    for column in na_columns:
        data[column].interpolate(method='pad', limit_direction='forward', inplace=True)
    return data

def drop_na_rows(data):
    data.dropna(inplace=True)
    return data