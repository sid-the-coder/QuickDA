from quickda.config import *

def barchart_of_categorical_features(data, cat_column, cat_column_2):
    
    # Show barchart plot of a categorical feature sorted in descending order
    plot_order = data[cat_column].value_counts(dropna=False).index
    if cat_column_2==None:
        print("Bar Plot of "+cat_column)
        sns.catplot(y=cat_column, kind="count", data=data, hue=cat_column_2, order=plot_order, aspect=3)
    else:
        print("Bar Plot of "+cat_column+" with respect to "+cat_column_2)
        pivot_data = pd.crosstab(index=data[cat_column], columns=data[cat_column_2])
        pivot_data['sum'] = pivot_data.sum(axis=1)
        pivot_data = pivot_data.sort_values(by='sum')
        pivot_data = pivot_data.drop(columns='sum')
        pivot_data.plot.barh(stacked=True, figsize=(20,10))
    plt.show()

def get_summary_of_categorical_features(data, cat_column, cat_column_2):
    
    # If only one column is provided, generate frequency table otherwise generate cross tabulations
    if cat_column_2==None:
        print("Summary of "+cat_column)
        dic = {}
        dic['count'] = data[cat_column].value_counts(dropna=False)
        dic['relative_pct'] = data[cat_column].value_counts(dropna=False, normalize=True).round(2)
        data_out = pd.DataFrame(dic)
    else:
        print("Crosstabulation of "+cat_column+" across "+cat_column_2)
        data_out = pd.crosstab(index=data[cat_column], columns=data[cat_column_2], 
                               normalize="index").round(2)
        temp_crosstab = pd.crosstab(index=data[cat_column], columns=data[cat_column_2])
        data_out['sum'] = temp_crosstab.sum(axis=1)
        data_out = data_out.sort_values(by='sum', ascending=False)
        data_out = data_out.drop(columns='sum')
        
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