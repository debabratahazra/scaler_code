import numpy as np
import pandas as pd

x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 4, np.nan, 8, 10, 12, 14]

i = 0
def lin_interpolate(y):
    #YOUR CODE GOES HERE

    global i
    # print(i)
    """Perform linear interpolation for x between (x1,y1) and (x2,y2) """
    if ((i)==0 or not (np.isnan(y)) or (i == df.shape[0]-1)):
      i = i+1
      return df.loc[i-1][1]

    y2 = df.iloc[i+1][1]
    x2 = i + 1
    y1 = df.iloc[i-1][1]
    x1 = i - 1
    x = i

    i = i + 1
    return round(((((y2 - y1) / (x2 - x1))* (x - x1)) + y1),2)

    #YOUR CODE ENDS HERE


df = pd.DataFrame({'x': x, 'y': y})
df['y'] = df.apply(lambda x: lin_interpolate(x['y']), axis = 1)

print(df)