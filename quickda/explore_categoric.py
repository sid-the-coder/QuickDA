import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set(style="darkgrid")

def barchart_of_categorical_features(data, cat_column, cat_column_2):
    
    print("Frequency Plot - Barchart")
    
    # Show barchart plot of a categorical feature sorted in descending order
    plot_order = data[cat_column].value_counts(dropna=False).index
    sns.catplot(y=cat_column, kind="count", data=data, hue=cat_column_2, order=plot_order, aspect=3)
    plt.show()

def get_summary_of_categorical_features(data, cat_column, cat_column_2):
    
    print("Summarize Categorical Features")
    
    # If only one column is provided, generate frequency table otherwise generate cross tabulations
    if cat_column_2==None:
        dic = {}
        dic['count'] = data[cat_column].value_counts(dropna=False)
        dic['relative_pct'] = data[cat_column].value_counts(dropna=False, normalize=True).round(2)
        data_out = pd.DataFrame(dic)
    else:
        data_out = pd.crosstab(index=data[cat_column], columns=data[cat_column_2], 
                               normalize="index").round(2)
        
    return data_out

#=================================================================================================================================

def eda_cat(data, x, y=None, method="default"):
    
    try:
        
        # Default method
        if method=="default":
            barchart_of_categorical_features(data, x, y)
            return get_summary_of_categorical_features(data, x, y)
    
    except Exception as e:
        print(e)