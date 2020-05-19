import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def boxplot_of_numerical_features(data):
    sns.set(style="darkgrid")
    columns = data.select_dtypes(include=np.number).columns
    for column in columns:
        sns.boxplot(x=data[column])
        plt.show()

def remove_outliers_in_numerical_feature(data, num_column):
    q1 = data[num_column].quantile(0.25)
    q3 = data[num_column].quantile(0.75)
    iqr = q3-q1
    fence_low  = q1-1.5*iqr
    fence_high = q3+1.5*iqr
    data_out = data.loc[(data[num_column] > fence_low) & (data[num_column] < fence_high)]
    return data_out

def histogram_of_numerical_features(data, num_of_bins):
    sns.set(style="darkgrid")
    columns = data.select_dtypes(include=np.number).columns
    for column in columns:
        sns.distplot(data[column], bins=num_of_bins)
        plt.show()

def get_correlation_between_numerical_features(data):
    corr = data.corr()
    return corr.style.background_gradient(cmap='coolwarm', axis=None).set_precision(2)