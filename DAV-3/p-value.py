'''The verbal reasoning in the GRE has an average score of 150 and a standard deviation 
of 8.5.

A coaching centre claims that their students are better. An average of 10 people showed 
that students from this coaching centre have an average score of 155.

At a 5% significance level (or 95% confidence level), can we conclude that students 
from the coaching centre are better? Use the Z-test, and compute the p-value.'''


# Null Hypothesis (H0): The average verbal reasoning score of students from the coaching centre is the same as the national average verbal reasoning score.(μ = 150)
# Alternative Hypothesis (Ha): The average verbal reasoning score of students from the coaching centr2 is better than the national average verbal reasoning score. (μ > 150)

import scipy.stats as stats

# Given data
mu = 150  # Population average (national)
sigma = 8.5  # Population standard deviation
n = 10  # Sample size
sample_mean = 155  # Sample mean

# Calculate the standard error of the mean (SEM)
sem = sigma / (n**0.5)

# Calculate the Z-score
Z = (sample_mean - mu) / sem

# Calculate the p-value for the right-tailed test
p_value = 1 - stats.norm.cdf(Z)

# Set the significance level (alpha)
alpha = 0.05

# Compare the p-value to the significance level
if p_value < alpha:
    print(f"p-value: {p_value}, Reject the null hypothesis. \
          Hence students from the coaching center are better")
else:
    print(f"p-value: {p_value}, Fail to reject the null hypothesis. \
          Hence students from the coaching center are not better")
print()
    
###########################
###########################

'''Out of a sample of 1,000 people residing in Maharashtra, 540 are rice eaters,
while the rest consume wheat primarily.

Can we assume that rice and wheat are equally popular in this state at a 5% 
significance level?'''

import statsmodels.api as sm

# H0: Both rice and wheat are equally popular in the State (P = 0.5)
# Ha: Both rice and wheat are not equally popular in the State( P ≠ 0.5)(two-tailed test).

# Given data
total_population = 1000
rice_eaters = 540
wheat_eaters = total_population - rice_eaters
assumed_proportion = 0.5  # Assuming equal popularity of rice and wheat

# Hypothesis test
z_stat, p_value = sm.stats.proportions_ztest(rice_eaters, total_population, assumed_proportion, alternative='two-sided')
print("Z-statistic:", z_stat)
print("P-value:", p_value)

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. Rice and wheat are not equally popular in \
        Maharashtra at a 5% significance level.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference \
        in the popularity of rice and wheat in Maharashtra at a 5% significance level.")
print()

################################################################
#################################################################
