import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def barchart_of_categorical_features(data, cat_column, cat_column_2):
    print("Frequency Plot - Barchart")
    sns.set(style="darkgrid")
    plot_order = data[cat_column].value_counts(dropna=False).index
    sns.catplot(y=cat_column, kind="count", data=data, hue=cat_column_2, order=plot_order, aspect=3)
    plt.show()

def get_summary_of_categorical_features(data, cat_column, cat_column_2):
    print("Summarize Categorical Features")
    if cat_column_2==None:
        dic = {}
        dic['count'] = data[cat_column].value_counts(dropna=False)
        dic['relative_pct'] = data[cat_column].value_counts(dropna=False, normalize=True).round(2)
        data_out = pd.DataFrame(dic)
    else:
        data_out = pd.crosstab(index=data[cat_column], columns=data[cat_column_2], 
                               normalize="index").round(2)
    return data_out

#=================================================================================================

def eda_cat(data, x, y=None, method="default"):
    
    try:
        
        if method=="default":
            barchart_of_categorical_features(data, x, y)
            return get_summary_of_categorical_features(data, x, y)
    
    except Exception as e:
        return e