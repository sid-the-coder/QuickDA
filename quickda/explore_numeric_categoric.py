import ppscore as pps
import seaborn as sns
import matplotlib.pyplot as plt

def find_predictive_power_score(data):
    pscore = pps.matrix(data)
    return pscore.style.background_gradient(cmap='coolwarm', axis=None).set_precision(2)

def scatterplot_between_categorical_features(data, x_num_column, y_num_column, cat_column=None):
    sns.set(style="darkgrid")
    sns.set(rc={'figure.figsize':(20,10)})
    sns.scatterplot(x=x_num_column, y=y_num_column, hue=cat_column, data=data)
    plt.show()

def violinplot_of_categorical_with_numerical_feature(data, cat_column, num_column):
    fig = sns.catplot(x=cat_column, y=num_column, kind='violin', data=data, aspect=3)
    fig.set_xticklabels(rotation=90)
    plt.show()

def pivot_data(data, cat_columns_1, agg_num_columns, cat_columns_2=None, agg_method='median'):
    data_out = data.pivot_table(index=cat_columns_1, 
                                columns=cat_columns_2, 
                                values=agg_num_columns, 
                                aggfunc=agg_method).round(2)
    return data_out