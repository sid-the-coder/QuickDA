import pandas as pd
import numpy as np

def standardize_column_names(data):
    
    print("Standardizing Column Names...")
    
    # Replace space and '_' in column names and convert them to lowercase 
    data.columns = [i.replace(' ', '_').lower() for i in data.columns]
    
    return data

def drop_features(data, columns_to_drop):
    
    print("Dropping Columns...")
    
    # Drop all the list of columns specified by the user
    data = data.drop(columns_to_drop, axis=1, errors='ignore')
    
    return data

def drop_duplicate_rows(data):
    
    print("Removing Duplicates...")
    
    # Drop all the duplicate rows
    data = data.drop_duplicates()
    
    return data

def replace_value(data, columns, value_to_replace, new_value):
    
    print("Replacing values...")
    
    # If columns not specified by the user, replace value in all columns 
    if columns==[]:
        data = data.replace(value_to_replace, new_value)
    else:
        for column in columns:
            data[column] = data[column].replace(value_to_replace, new_value)
            
    return data

def fill_na_rows(data):
    
    print("Filling Missing Values...")
    
    # Retrieve the list of columns having nulls and interpolate for each column
    na_columns = data.columns[data.isna().any()].tolist()
    for column in na_columns:
        data[column] = data[column].interpolate(method='pad', limit_direction='forward')
        
    return data

def drop_na_rows(data):
    
    print("Dropping Missing Values...")
    
    # Drop all nulls
    data = data.dropna() 
    
    return data

def reduce_feature_cardinality(data, category_column, new_value, threshold):
    
    print("Reducing Column Cardinality...")
    
    # If user doesn't input new value to replace with
    if pd.isnull(new_value):
        new_value = "other"
        
    # Find relative frequency of column to compare with threshold
    relative_pct = data[category_column].value_counts(dropna=False, normalize=True).round(2)
    
    values_to_retain = []
    # If threshold not provided by user, retain only top 5 values else extract values to retain
    if threshold == 0:
        values_to_retain = relative_pct[:5].index.to_list()
    else:
        cum_relative_pct = 0
        for idx in relative_pct.index:
            cum_relative_pct += relative_pct[idx]
            if cum_relative_pct < threshold:
                values_to_retain.append(idx)
            if cum_relative_pct == threshold:
                values_to_retain.append(idx)
                break
                
    # Replace all values in DataFrame other than values marked to be retained
    data_out = data.copy()
    data_out.loc[~data[category_column].isin(values_to_retain), category_column] = new_value
    
    return data_out

def convert_features_dtype_to_datetime(data, datetime_columns):
    
    print("Converting dtypes to datetime...")
    
    # Convert columns to datetime
    data_out = data.copy()
    data_out.loc[:, datetime_columns] = data[datetime_columns].apply(pd.to_datetime, infer_datetime_format=True, errors='ignore')
    
    return data_out

def convert_features_dtype_to_category(data, category_columns):
    
    print("Converting dtypes to category...")
    
    # Convert columns to category type
    data_out = data.copy()
    data_out.loc[:, category_columns] = data[category_columns].apply(pd.Categorical)
    
    return data_out

def convert_features_dtype_to_numeric(data, numeric_columns):
    
    print("Converting dtypes to numeric...")
    
    # Convert columns to numeric
    data_out = data.copy()
    data_out.loc[:, numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='ignore')
    
    return data_out

def remove_outliers_in_numerical_feature(data, num_columns):
    
    print("Removing outliers...")
    
    # If user doesn't provide the column name(s), then infer the type
    if num_columns==[]:
        num_columns = data.select_dtypes(include=np.number).columns
        
    # Remove outliers for specified columns
    for column in num_columns:
        q1 = data[column].quantile(0.25)
        q3 = data[column].quantile(0.75)
        iqr = q3-q1
        fence_low  = q1-1.5*iqr
        fence_high = q3+1.5*iqr
        data = data.loc[(data[column] > fence_low) & (data[column] < fence_high)]
        
    return data

#================================================================================================================================

def clean(data, method="default", columns=[], dtype="numeric", to_replace="", value=np.nan, threshold=0):
    
    try:
        
        # Default method
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
        
        if method=="cardinality":
            data = reduce_feature_cardinality(data, columns, value, threshold)
            return data

        if method=="dtypes":
            if dtype=="datetime":
                data = convert_features_dtype_to_datetime(data, columns)
            if dtype=="category":
                data = convert_features_dtype_to_category(data, columns)
            if dtype=="numeric":
                data = convert_features_dtype_to_numeric(data, columns)
            return data
        
        if method=="outliers":
            data = remove_outliers_in_numerical_feature(data, columns)
            return data
        
    except Exception as e:
        print(e)
        return data