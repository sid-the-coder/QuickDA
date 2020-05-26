import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set(style="darkgrid")

def boxplot_of_numerical_features(data):
    
    print("Outlier Analysis - Boxplot")
    
    # Show Boxplots of all numeric columns
    columns = data.select_dtypes(include=np.number).columns
    for column in columns:
        sns.boxplot(x=data[column])
        plt.show()

def histogram_of_numerical_features(data, num_of_bins):
    
    print("Distribution Analysis - Histogram")
    
    # Show histogram of all numeric columns
    columns = data.select_dtypes(include=np.number).columns
    for column in columns:
        sns.distplot(data[column], bins=num_of_bins)
        plt.show()

def get_correlation_between_numerical_features(data):
    
    print("Correlation Analysis - Heatmap")
    
    # Retreive correlation matrix
    corr = data.corr()
    
    return corr.style.background_gradient(cmap='coolwarm', axis=None).set_precision(2)

#=================================================================================================================================

def eda_num(data, method="default", bins=10):
    
    try:
        
        # Default method
        if method=="default":
            boxplot_of_numerical_features(data)
            histogram_of_numerical_features(data, bins)
            
        if method=="correlation":
            return get_correlation_between_numerical_features(data)
    
    except Exception as e:
        print(e)