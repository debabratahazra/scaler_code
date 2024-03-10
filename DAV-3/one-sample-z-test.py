import numpy as np
from scipy.stats import norm

population_mean = 1800
population_stddev = 100

sample_mean = 1850
sample_size = 50

# z_score = (x - mu) / (sigma / root(n))
z_score = (sample_mean - population_mean) / (population_stddev/np.sqrt(sample_size))
print(z_score)

# as sample_mean is > population_mean, It is right tailed test
p_value = 1 - norm.cdf(z_score)
print(p_value)

# consider alpha / significance level => 1% = 0.01 
# i.e. confidence level is (1-alpha) => 99%
alpha = 0.01
if p_value < alpha:
    print('reject the null hypothesis')
    print('It is good job as Alternate hypothesis is more than population mean value')
else:
    print('failed to reject the null hypothesis')
print()
    
########################
########################

'''A company claims that the average time it takes to deliver a product to customers 
is 3 days.

The company's delivery process is under scrutiny, and a sample of 25 delivery times is 
collected. The sample mean delivery time is 3.5 days, and the population standard deviation 
is known to be 0.8 days.


At a 5% significance level, can we conclude that the average delivery time is greater than 
3 days?

Conduct a one-sample Z-test to determine the same. Also, evaluate the z-score for observed 
average time.'''


#Based on the given problem, we define our hypothesis as:

# H0: The average delivery time is 3 days
# Ha: The average delivery time is greater than 3 days

from scipy.stats import norm


# Population parameters
population_mean = 3  # Population average (Claimed) delivery time
population_stddev = 0.8  # Population standard deviation


# Sample statistics
sample_mean = 3.5 # Sample delivery time observed
sample_size = 25


# Calculate the standard error of the sample mean
standard_error = population_stddev / (sample_size ** 0.5)


# Calculate the Z-score
z_score = (sample_mean - population_mean) / standard_error


# Calculate the p-value: Right Tailed test
p_value = 1 - norm.cdf(z_score)


# Significance level
alpha = 0.05


# Compare p-value with the significance level
if p_value < alpha:
   print(f"Reject the null hypothesis. The average delivery time is greater than 3 days")
else:
   print(f"Fail to reject the null hypothesis. The average delivery time is 3 days")


print(f"Z-score: {z_score}")
print(f"P-value: {p_value}")
print()

#####################################
###################################

