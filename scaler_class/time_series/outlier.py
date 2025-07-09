import numpy as np

def replace_outliers(arraySeries):
    """arraySeries is a numpy array,
       return the required numpy array"""
    
    # Calculate the absolute difference of each timepoint from the series mean
    mean = np.mean(arraySeries)
    std = np.std(arraySeries)
    abs_diff = np.abs(arraySeries - mean)
    
    # Calculate the threshold for outliers (2 standard deviations from the mean)
    threshold = 2 * std
    
    # Create a mask for values that are greater than the threshold
    mask = abs_diff > threshold
    
    # Replace outliers with the median of the array
    median = np.median(arraySeries)
    arraySeries[mask] = median
    return arraySeries


arraySeries = np.array([ 330, 11500, 16500, 914, 796, 353, 6470, 219, 389, 805, 256, 919, 398, 900, 496, -6240, 948, 711, 306, 777, 719, 545, 248])
print("The original array is: \n{}".format(arraySeries))
print()
retuned_array = replace_outliers(arraySeries)
print("The array after replacing outliers is: \n{}".format(retuned_array))