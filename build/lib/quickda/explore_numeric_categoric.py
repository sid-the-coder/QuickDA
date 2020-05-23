import ppscore as pps
import seaborn as sns
import matplotlib.pyplot as plt

def find_predictive_power_score(data):
    print("Predictive Power Score - Heatmap")
    pscore = pps.matrix(data)
    return pscore.style.background_gradient(cmap='coolwarm', axis=None).set_precision(2)

def scatterplot_between_numerical_features(data, x_num_column, y_num_column, cat_column):
    print("Analyse Relationships - Scatterplot")
    sns.set(style="darkgrid")
    sns.set(rc={'figure.figsize':(20,10)})
    sns.scatterplot(x=x_num_column, y=y_num_column, hue=cat_column, data=data)
    plt.show()

def violinplot_of_categorical_with_numerical_feature(data, cat_column, num_column):
    print("Compare Category - Violinplot")
    fig = sns.catplot(x=cat_column, y=num_column, kind='violin', data=data, aspect=3)
    fig.set_xticklabels(rotation=90)
    plt.show()

def pivot_data(data, cat_index, cat_columns, num_values, agg_method):
    print("Pivot View")
    data_out = data.pivot_table(index=cat_index, columns=cat_columns, 
                                values=num_values, aggfunc=agg_method).round(2)
    return data_out

#=================================================================================================

def eda_numcat(data, x, y, method="pps", hue=None, values=None, aggfunc="mean"):
    
    try:
        
        if method=="pps":
            return find_predictive_power_score(data)
        
        if method=="relationship":
            scatterplot_between_numerical_features(data, x, y, hue)
        
        if method=="comparison":
            violinplot_of_categorical_with_numerical_feature(data, x, y)
        
        if method=="pivot":
            return pivot_data(data, x, y, values, aggfunc)
    
    except Exception as e:
        return e