import pandas as pd
import numpy as np

def standardize_column_names(data):
    print("Standardizing Column Names...")
    data.columns = [i.replace(' ', '_').lower() for i in data.columns]
    return data

def drop_features(data, columns_to_drop):
    print("Dropping Columns...")
    data = data.drop(columns_to_drop, axis=1, errors='ignore')
    return data

def convert_features_dtype_to_datetime(data, datetime_columns):
    print("Converting dtypes to datetime...")
    data[datetime_columns] = data[datetime_columns].apply(pd.to_datetime, infer_datetime_format=True, errors='ignore')
    return data

def convert_features_dtype_to_category(data, category_columns):
    print("Converting dtypes to category...")
    data[category_columns] = data[category_columns].apply(pd.Categorical)
    return data

def convert_features_dtype_to_numeric(data, numeric_columns):
    print("Converting dtypes to numeric...")
    data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='ignore')
    return data

def drop_duplicate_rows(data):
    print("Removing Duplicates...")
    data = data.drop_duplicates()
    return data

def replace_value(data, columns, value_to_replace, new_value):
    print("Replacing all instances of "+str(value_to_replace)+"...")
    if columns==[]:
        data = data.replace(value_to_replace, new_value)
    else:
        for column in columns:
            data[column] = data[column].replace(value_to_replace, new_value)
    return data

def fill_na_rows(data):
    print("Filling Missing Values...")
    na_columns = data.columns[data.isna().any()].tolist()
    for column in na_columns:
        data[column] = data[column].interpolate(method='pad', limit_direction='forward')
    return data

def drop_na_rows(data):
    print("Dropping Missing Values...")
    data = data.dropna() 
    return data

def remove_outliers_in_numerical_feature(data, num_columns):
    print("Removing outliers...")
    if num_columns==[]:
        num_columns = data.select_dtypes(include=np.number).columns
    for column in num_columns:
        q1 = data[column].quantile(0.25)
        q3 = data[column].quantile(0.75)
        iqr = q3-q1
        fence_low  = q1-1.5*iqr
        fence_high = q3+1.5*iqr
        data = data.loc[(data[column] > fence_low) & (data[column] < fence_high)]
    return data

#=================================================================================================

def clean(data, method="default", columns=[], dtype="numeric", to_replace="", value=np.nan):
    
    try:
        
        if method=="default":
            data = standardize_column_names(data)
            data = drop_duplicate_rows(data)
            data = drop_na_rows(data)  
            return data
    
        if method=="standardize":
            data = standardize_column_names(data)
            return data

        if method=="dropcols":
            data = drop_features(data, columns)
            return data

        if method=="dtypes":
            if dtype=="datetime":
                data = convert_features_dtype_to_datetime(data, columns)
            if dtype=="category":
                data = convert_features_dtype_to_category(data, columns)
            if dtype=="numeric":
                data = convert_features_dtype_to_numeric(data, columns)
            return data

        if method=="duplicates":
            data = drop_duplicate_rows(data)
            return data

        if method=="replaceval":
            data = replace_value(data, columns, to_replace, value)
            return data

        if method=="fillmissing": 
            data = fill_na_rows(data)
            return data
        
        if method=="dropmissing":
            data = drop_na_rows(data)
            return data
        
        if method=="outliers":
            data = remove_outliers_in_numerical_feature(data, columns)
            return data
        
    except Exception as e:
        print(e)
        return data