'''

Imagine you are a quality control manager at a chocolate factory. You're responsible for 
ensuring that the average weight of chocolate bars produced in your factory meets a certain 

standard.

The standard weight of a chocolate bar is 50 grams, and it rarely deviates, 
with a known population standard deviation of 2 grams.


To maintain the quality of your chocolate bars, you collect a sample of 30 bars every day 
and weigh them.

You want to know if your production process is still on track and that the average weight of 
the chocolate bars is 50 grams.

You set the significance level (α) to 0.05, and you want to calculate the power of your quality 
control test.
'''
import numpy as np
from scipy import stats
from statsmodels.stats import power

data = [55, 45, 52, 48, 55, 52, 52, 53, 48, 52, 53, 47, 54, 51, 52, 51, 48, 52, 53, 54, 51, 51, 52, 54, 47, 52, 53, 48, 51, 54]

# Given Data
alpha = 0.05
confidence_level = 1 - (alpha/2)
sample_size = 30

z_critical = np.abs(round(stats.norm.isf(q=alpha/2), 4))
print("z critical value: ", z_critical)

sample_mean = np.mean(data)
print("sample mean: ", sample_mean)
sample_std = np.std(data)
print("sample_std value: ", sample_std)

hypothesis_mean = 50

effect_size = (sample_mean - hypothesis_mean) / sample_std 
print("effect size: ", effect_size)

power_of_test = power.zt_ind_solve_power(
    effect_size=effect_size, 
    nobs1=sample_size, 
    alpha=alpha, 
    power=None,
    ratio=0, 
    alternative='two-sided')
print("Power of Test: " , power_of_test)


