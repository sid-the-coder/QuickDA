from pandas_profiling import ProfileReport
import pandas as pd
import os
import calendar
import time

def generate_data_profile_report(data, report_name, is_large_dataset):
    
    # If '/reports' path doesn't exist, create one
    if not os.path.exists("reports"):
        os.makedirs("reports")
        
    # Generate HTML Profile Report
    filename = os.path.join('reports', report_name.replace(' ', '_').lower() \
                            +"_"+str(calendar.timegm(time.gmtime()))+".html")
    profile = ProfileReport(data, title=report_name, minimal=is_large_dataset)
    profile.to_file(filename)
    
    return profile

def summarize_data(data):
    
    # Create a descriptive statistics dictionary
    dic = {}
    print('Calculating dtypes...')
    dic['dtypes'] = data.dtypes
    print('Calculating count...')
    dic['count'] = data.count()
    print('Calculating null_sum...')
    dic['null_sum'] = data.isnull().sum()
    print('Calculating null_pct...')
    dic['null_pct'] = data.isnull().mean()
    print('Calculating nunique...')
    dic['nunique'] = data.nunique()
    print('Calculating min...')
    dic['min'] = data.min()
    print('Calculating 25%...')
    dic['25%'] = data.quantile(0.25)
    print('Calculating 50%...')
    dic['50%'] = data.quantile(0.5)
    print('Calculating 75%...')
    dic['75%'] = data.quantile(0.75)
    print('Calculating max...')
    dic['max'] = data.max()
    print('Calculating mean...')
    dic['mean'] = data._get_numeric_data().mean()
    print('Calculating median...')
    dic['median'] = data._get_numeric_data().median()
    print('Calculating std...')
    dic['std'] = data._get_numeric_data().std()
    print('Calculating skew...')
    dic['skew'] = data._get_numeric_data().skew()
    
    # Convert dictionary to readable DataFrame
    eda = pd.DataFrame(dic)
    eda = eda.fillna('-').round(3)
    
    return eda

#================================================================================================================================

def explore(data, method="summarize", report_name="Dataset Report", is_large_dataset=False):
    
    try:
        
        # Default method
        if method=="summarize":
            eda = summarize_data(data)
            return eda

        if method=="profile":
            profile = generate_data_profile_report(data, report_name, is_large_dataset)
            return profile
            
    except Exception as e:
        print(e)