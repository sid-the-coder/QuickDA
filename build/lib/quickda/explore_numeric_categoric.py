from quickda.config import *

def find_predictive_power_score(data, x):
    
    print("Feature Importance in the prediction of "+x)
    
    # Predictive Power Score - PPS Matrix
    predictors_df = pps.predictors(data, y=x)
    sns.set(rc={'figure.figsize':(20,10)})
    sns.barplot(data=predictors_df, x="ppscore", y="x")
    plt.show()

def scatterplot_between_numerical_features(data, x_num_column, y_num_column, cat_column):
    
    print("Scatterplot of "+x_num_column+" versus "+y_num_column)
    
    # Show Scatterplot between two features
    sns.set(rc={'figure.figsize':(20,10)})
    sns.scatterplot(x=x_num_column, y=y_num_column, hue=cat_column, data=data)
    plt.show()

def violinplot_of_categorical_with_numerical_feature(data, cat_column, num_column):
    
    print("Violinplot of numerical feature "+num_column+" across categorical feature "+num_column)
    
    # Show vilionplots to compare a categorical feature with Numerical feature
    fig = sns.catplot(x=cat_column, y=num_column, kind='violin', data=data, aspect=3)
    fig.set_xticklabels(rotation=90)
    plt.show()

def pivot_data(data, cat_index, cat_columns, num_values, agg_method):
    
    print("Pivot View")
    
    # Generate Pivot Tables
    data_out = data.pivot_table(index=cat_index, columns=cat_columns, 
                                values=num_values, aggfunc=agg_method).round(2)
    
    return data_out

#=================================================================================================

def eda_numcat(data, x, y=None, method="pps", hue=None, values=None, aggfunc="mean"):
    
    try:
        
        # Default method
        if method=="pps":
            return find_predictive_power_score(data, x)
        
        if method=="relationship":
            scatterplot_between_numerical_features(data, x, y, hue)
        
        if method=="comparison":
            violinplot_of_categorical_with_numerical_feature(data, x, y)
        
        if method=="pivot":
            return pivot_data(data, x, y, values, aggfunc)
    
    except Exception as e:
        print(e)