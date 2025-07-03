import pandas as pd
import numpy as np

def impute(df, window_size):
    """ df is the dataframe consisting of two columns date and units_sold
        and window_size represents the size of window for moving average"""
    
    #YOUR CODE GOES HERE
    df['units_sold'] = df.units_sold.fillna(value = df.units_sold.rolling(window_size).mean().shift(1)).round(1)
    #YOUR CODE ENDS HERE
    
    return df


df = pd.DataFrame({'date':['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04', '2018-01-05', '2018-01-06'], 'units_sold':[6519.0, 6654.0, 7332.0, np.nan, 7211.0, 6882.0]})
window_size = 3 
print(df)
print("Imputing missing values using moving average with window size of {}".format(window_size)) 
ans = impute(df, window_size)
print(ans)