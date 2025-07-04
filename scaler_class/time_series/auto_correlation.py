import numpy as np

def get_oneLag_AutoCor(data):
    """input: data-> a list of float elements.
       output: res-> return the float rounded upto 2 decimal places.
       """
    
    res=0
    #YOUR CODE GOES HERE
    
    n = len(data)
    mean = np.mean(data)
    numerator = sum((data[i] - mean) * (data[i - 1] - mean) for i in range(1, n))
    denominator = sum((data[i] - mean) ** 2 for i in range(n))
    res = numerator / denominator if denominator != 0 else 0

    return round(res, 2)

data = [23.32, 32.33, 32.88, 28.98, 33.16, 26.33, 29.88, 32.69, 18.98, 21.23, 26.66, 29.89]
corr = get_oneLag_AutoCor(data)
print("The autocorrelation of the data with one lag is: {}".format(corr))