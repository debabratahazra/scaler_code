'''The average hourly wage of a sample of 150 workers in plant 'A' was Rs.2·87 with a 
standard deviation of Rs. 1·08.

The average wage of a sample of 200 workers in plant 'B' was Rs. 2·56 with a standard 
deviation of Rs. 1·28.

(i) Calculate the Z-score for this scenario.

(ii) Can an applicant safely assume that the hourly wages paid by plant 'A' are 
higher than those paid by plant 'B' at a 1% significance level?'''

# Based on the given problem, we define our hypotheses as:
# H0: μ1=μ2, i.e., the hourly wages paid by plant ‘A’ is equal to that paid by plant ‘B’.
# H1: μ1 > μ2, i.e., the hourly wages paid by plant ‘A’ are higher than that paid by plant ‘B’.
# Based on this, we need to perform a Right one-tailed test.

# Further, we can calculate the Z-score for 2 Sample Z Test using following formula:
# Z = x-bar1 - x-bar2 / sqrt(σ1^2/n1 + σ2^2/n2)

# Where:
# Z: The z-score, a standard normal variable used to determine the probability of the 
# observed difference between the two samples.
# x-bar1: The mean of the first sample.
# x-bar2: The mean of the second sample.
# σ1 : The standard deviation of the first population.
# σ2 : The standard deviation of the second population.
# n1 : The size of the first sample.
# n2 : The size of the second sample.

import numpy as np
from scipy import stats

# Define the function to calculate the two-sample z-test
def TwoSampZTest(samp_mean_1, samp_mean_2, samp_std_1, samp_std_2, n1, n2):
    denominator = np.sqrt((samp_std_1**2 / n1) + (samp_std_2**2 / n2))
    z_score = (samp_mean_1 - samp_mean_2) / denominator
    return z_score

# Given data for plant A
sample_mean_A = 2.87
sample_std_A = 1.08
sample_size_A = 150

# Given data for plant B
sample_mean_B = 2.56
sample_std_B = 1.28
sample_size_B = 200

# Set the significance level
significance_level = 0.01

# Calculate the z-score using the function
z_score = TwoSampZTest(sample_mean_A, sample_mean_B, sample_std_A, sample_std_B, sample_size_A, sample_size_B)

# Calculate the one-tailed p-value
p_value = 1-stats.norm.cdf(z_score)

# Compare the p-value to the significance level
if p_value < significance_level:
    conclusion = "Reject the null hypothesis. Hourly wages in plant 'A' are higher than those in plant 'B' at a 1% significance level."
else:
    conclusion = "Fail to reject the null hypothesis. No significant difference in hourly wages between plant 'A' and 'B' at a 1% significance level."

# Print the results
print(f'z-score: {z_score:.4f}')
print(f'p-value: {p_value:.4f}')
print('Conclusion:', conclusion)
print()

#########################################
#########################################

'''The Head of Data Analyst Department is conducting a comparative analysis of the 
complexity of SQL queries written by two analysts, namely Analyst X and Analyst Y.

He has gathered data on the number of lines of code for each SQL query.

Analyst X's SQL lines of code: [15, 18, 20, 17, 16, 19, 22, 16, 18, 21]
Analyst Y's SQL lines of code: [14, 17, 19, 16, 15, 18, 21, 15, 17, 20]

The analyst hypothesizes that Analyst Y writes less complex code compared to Analyst X. 
To investigate this hypothesis, conduct an appropriate test with a 90% confidence interval.
'''

# Based on the given question, we define our hypothesis as:

# Null Hypothesis: Analyst Y writes code with the same complexity as Analyst X (μY=μX)
# Alternative Hypothesis: Analyst Y writes less complex code compared to Analyst X (μY<μX)
# Hence, we would have to conduct a Left Tailed 2 Sample Z-Test.

from statsmodels.stats import weightstats as stests
import numpy as np

# Number of lines of code for SQL queries by Analyst X
sql_lines_X = [15, 18, 20, 17, 16, 19, 22, 16, 18, 21]

# Number of lines of code for SQL queries by Analyst Y
sql_lines_Y = [14, 17, 19, 16, 15, 18, 21, 15, 17, 20]

# Perform two-sample Z-test
z_score, p_value = stests.ztest(sql_lines_Y, sql_lines_X, alternative ='smaller')

# Confidence level
confidence_level = 0.90
alpha = 1 - confidence_level

# Print the results
print(f"Z-score: {z_score}")
print(f"P-value: {p_value}")

# Decision Rule
if p_value < alpha:
   print("Reject the null hypothesis. There is significant evidence that Analyst Y writes less complex code compared to Analyst X.")
else:
   print("Fail to reject the null hypothesis. There is no significant evidence that Analyst Y writes less complex code compared to Analyst X.")
print()

#############################
###############################   

'''
The Quidditch teams at Hogwarts conducted tryouts for two positions: Chasers and Seekers.

In Group Chasers, out of 90 students who tried out, 57 were selected. In Group Seekers, 
out of 120 students who tried out, 98 were selected.

Is there a significant difference in the proportion of students selected for Chasers and 
Seekers positions?

Conduct a test at 90% confidence level.
'''

# Null Hypothesis: There is no significant difference in the proportion of students selected
# for Chasers and Seekers positions at Hogwarts.

# Alternative Hypothesis: There is a significant difference in the proportion of students 
# selected for Chasers and Seekers positions at Hogwarts.

import statsmodels.api as sm

# Data for Chasers
selected_chasers = 57
total_chasers = 90

# Data for Seekers
selected_seekers = 98
total_seekers = 120

# Perform two-sample Z-proportion test
z_stat, p_value = sm.stats.proportions_ztest([selected_chasers, selected_seekers], [total_chasers, total_seekers], alternative = 'two-sided')

# Confidence level
confidence_level = 0.90
# Calculate the critical value for a two-tailed test
alpha = 1 - confidence_level

# Print the results
print(f"Z-statistic: {z_stat}")
print(f"P-value: {p_value}")

# Decision Rule
if p_value < alpha:
   print("Reject the null hypothesis. There is a significant difference in the proportion of students selected for Chasers and Seekers positions.")
else:
   print("Fail to reject the null hypothesis. There is no significant difference in the proportion of students selected for Chasers and Seekers positions.")
print()   

#########################################
########################################

# Ques:
""" A company is surveying to assess customer satisfaction with two different support 
approaches.

The company collects feedback from customers subjected to each approach and wants to 
compare the satisfied customers.

Which statistical test would be most appropriate for the company to compare the satisfied 
customers between the two support approaches, and what would be the relevant null hypothesis?
 """

# Ans:
""" In this scenario, the company is comparing the proportion of satisfied customers between 
two different groups (support approaches).
Therefore, we need a statistical test that compares the proportions between two independent 
samples.

One-sample z-test for mean: This is not suitable as it compares the mean of a single sample 
to a known mean.
Two-sample z-test for mean: This is not applicable as we are dealing with proportions, not 
means.
One-sample z-proportion test: This is only suitable for comparing the proportion of a single 
sample to a known proportion.
Two-sample z-proportion test: This is the best option as it specifically compares the 
proportions of two independent samples.
Null Hypothesis (H0): The proportion of satisfied customers is the same for both customer
support approaches.

Alternative Hypothesis (H1): The proportion of satisfied customers is different for the two 
customer support approaches.

By performing a two-sample z-proportion test, the company can statistically assess whether 
the observed difference in customer satisfaction between the two support approaches is 
simply due to chance or reflects a real difference in the effectiveness of the approaches.
"""

##################################################
#################################################

'''
As a product manager, you want to evaluate the user satisfaction for two different seasons 
of Naruto Shippuden (Season 1 and Season 2).

You collected feedback from 250 viewers who watched Season 1 of Naruto Shippuden, and 120 
expressed satisfaction. Similarly, for Season 2, you gathered data from 300 viewers, and 
150 of them expressed satisfaction.

Conduct an appropriate test at a 95% confidence interval to determine if there's a higher 
user satisfaction for Season 2 than for Season 1.
'''

# Based on the given problem, we define our hypothesis as:

# Null Hypothesis: The proportion of satisfied users for Season 2 is equal to or less than 
# the proportion for Season 1.
#Alternative Hypothesis: The proportion of satisfied users for Season 2 is higher than the 
# proportion for Season 1.
# We can solve this problem using the concept of Z Proportion Test

import numpy as np
from statsmodels.stats.proportion import proportions_ztest


# Given data
n_season1, x_season1 = 250, 120
n_season2, x_season2 = 300, 150


# Perform z-test for proportions
z_stat, p_value = proportions_ztest(count=[x_season2, x_season1], nobs=[n_season2, n_season1], alternative='larger')


# Display results
print(f"Z-statistic: {z_stat:.4f}")
print(f"P-value: {p_value:.4f}")


# Compare with critical value (e.g., for 95% confidence level)
alpha = 0.05
if p_value < alpha:
   print("Reject the null hypothesis. There is evidence of higher user satisfaction for Season 2 than Season 1.")
else:
   print("Fail to reject the null hypothesis. There is no significant evidence of higher user satisfaction for Season 2.")
print()

################################################################
################################################################

'''A state senator cannot decide how to vote on an environmental protection bill.

The senator decides to request a survey and if the proportion of registered voters 
supporting the bill exceeds 0.60, she will vote for it.

A random sample of 750 voters is selected and 495 are found to support the bill.

Conduct an appropriate test at a 90% confidence interval.
'''
# Based on the given problem, we define our hypothesis as:

# Null Hypothesis: The proportion of registered voters supporting the bill is less than or 
# equal to 0.60 (p≤0.60)
# Alternative Hypothesis: The proportion of registered voters supporting the bill is 
# greater than 0.60(p>0.60)
# Hence we would need to perform a Right Tailed Z Proportion Test.

import scipy.stats as stats
import math


# Given data
sample_size = 750
observed_support = 495
hypothesized_proportion = 0.60
confidence_level = 0.90


# Calculate the sample proportion
sample_proportion = observed_support / sample_size


# Calculate the standard error
standard_error = math.sqrt((hypothesized_proportion * (1 - hypothesized_proportion)) / sample_size)


# Calculate the Z-score
z_stat = (sample_proportion - hypothesized_proportion) / standard_error


# Calculate the p-value by conducting Right Tailed Test
p_value = 1 - stats.norm.cdf(z_stat)


print("Z-statistic:", z_stat)
print("P-value:", p_value)


alpha = 1 - confidence_level
if p_value < alpha:
 print("Reject the null hypothesis. There is evidence to suggest that the proportion of registered voters supporting the bill is greater than 0.60.")
else:
 print("Fail to reject the null hypothesis. There is no evidence to suggest that the proportion of registered voters supporting the bill is greater than 0.60.")
print()

#####################################################
####################################################

'''An IT team is comparing the response times of two different web servers, Server A and 
Server B, under a specific load. They have collected response time data for a sample of 
requests.

Server A: Mean response time of 120 milliseconds from 30 requests, with a standard 
deviation of 15 milliseconds.
Server B: Mean response time of 110 milliseconds from 35 requests, with a standard 
deviation of 12 milliseconds.
Conduct an appropriate test to determine if there is a significant difference in the 
mean response times between the two servers. Assume a 5% significance level.
'''

# Based on the given problem, we define our hypothesis as:

# Null Hypothesis: The mean response time of Server A is equal to the mean response time 
# of Server B.(μA = μB)
# Alternative Hypothesis: The mean response time of Server A is not equal to the mean 
# response time of Server B.(μA != μB)

# We can solve this problem using the concept of 2 Tailed 2 Sample Z-test


import numpy as np
from scipy import stats


# Define the function to calculate the two-sample Z-test
def TwoSampZTest(samp_mean_1, samp_mean_2, samp_std_1, samp_std_2, n1, n2):
   # Calculate the test statistic
   denominator = np.sqrt((samp_std_1**2 / n1) + (samp_std_2**2 / n2))
   z_score = (samp_mean_1 - samp_mean_2) / denominator
   return z_score


# Given data for Server A
mean_A = 120
std_dev_A = 15
sample_size_A = 30


# Given data for Server B
mean_B = 110
std_dev_B = 12
sample_size_B = 35


# Significance level
significance_level = 0.05


# Calculate the z-score using the function
z_score = TwoSampZTest(mean_A, mean_B, std_dev_A, std_dev_B, sample_size_A, sample_size_B)


# Calculate the two-tailed p-value
p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))


# Compare the p-value to the significance level
if p_value < significance_level:
   conclusion = "Reject the null hypothesis. There is a significant difference in the mean response times between Server A and Server B."
else:
   conclusion = "Fail to reject the null hypothesis. There is no significant difference in the mean response times between Server A and Server B."


# Print the results
print(f'z-score: {z_score:.4f}')
print(f'p-value: {p_value:.4f}')
print('Conclusion:', conclusion)
print()

###############################################################
##################################################################

'''A group of archers claims that they can hit the bullseye with a success rate of 70%. 
To test this claim, a random sample of 100 shots is taken, and 65 of them hit the bullseye.

Is there significant evidence to suggest that the archer’s actual success rate is greater
than 70% at a 95% confidence level?'''

# Based on the given question, we define our hypothesis as:

# Null Hypothesis: Success rate of this group of archers is 70%, i.e. p=0.7
# Alternative Hypothesis: Success rate of this group of archers is greater than 70%, 
# i.e. p>0.7

import numpy as np
import scipy.stats as stats

# Data
successes = 65  # Number of successful shots
total_shots = 100  # Total number of shots
claimed_success_rate = 0.70  # Claimed success rate by the archers

# Calculate the sample proportion
sample_proportion = successes / total_shots

# Calculate the standard error
standard_error = np.sqrt((claimed_success_rate * (1 - claimed_success_rate)) / total_shots)

# Calculate the Z-score
z_stat = (sample_proportion - claimed_success_rate) / standard_error

# Calculate the p-value for a right-tailed test
p_value = 1 - stats.norm.cdf(z_stat)

print("Z-statistic:", z_stat)
print(f"P-value: {p_value}")

# Confidence level
confidence_level = 0.95
alpha = 1 - confidence_level

if p_value < alpha:
   print("Reject the null hypothesis. There is significant evidence to suggest that the archers' actual success rate is greater than 70%.")
else:
   print("Fail to reject the null hypothesis. There is no significant evidence to suggest that the archers' actual success rate is greater than 70%.")
print()

################################################################
#################################################################

'''You are testing two drugs as a remedy. Drug A is effective in 41 out of a sample of 195. 
Drug B works on 351 out of 605 people.

Are the two drugs comparable in terms of effectiveness? Use a 5% significance level for 
testing.

Perform an appropriate test.'''

import numpy as np
import statsmodels.api as sm

# H0: The proportions are the same.
# H1: The proportions are different.

# Given data for Drug A
success_A = 41
sample_size_A = 195

# Given data for Drug B
success_B = 351
sample_size_B = 605

# Perform the two-proportion Z-test
z_stat, p_value = sm.stats.proportions_ztest([success_A, success_B], [sample_size_A, sample_size_B], alternative='two-sided')

# Significance level
alpha = 0.05

# Print the results
print(f"Z-statistic: {z_stat}")
print(f"P-value: {p_value}")

# Decision Rule
if p_value < alpha:
    print("Reject the null hypothesis. The proportions of Drug A and Drug B are significantly different.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in the proportions of Drug A and Drug B.")
print()

################################################################
################################################################

'''As a social media analyst, you want to compare the engagement rates of posts from two 
different accounts (Account X and Account Y).

You collected data on 180 posts from Account X, where 40 received high engagement. 
Similarly, you collect data on 200 posts from Account Y, where 60 received high engagement.

Conduct an appropriate test at a 95% confidence interval to determine if there's a 
significant difference in high engagement proportions between the two accounts.'''

# Based on the given problem, we define our hypothesis as:

# Null Hypothesis: The proportion of posts with high engagement is the same for 
# Account X and Account Y.
# Alternative Hypothesis: The proportion of posts with high engagement is different 
# for Account X and Account Y.
# We can solve this using the concepts of Z Proportion.

import numpy as np
from statsmodels.stats.proportion import proportions_ztest


# Given data
posts_X = 180
high_engagement_X = 40
posts_Y = 200
high_engagement_Y = 60


# Calculate sample proportions
p_X = high_engagement_X / posts_X
p_Y = high_engagement_Y / posts_Y


# Conduct a two-sample z-proportion test
count = np.array([high_engagement_X, high_engagement_Y])
nobs = np.array([posts_X, posts_Y])


z_stat, p_value = proportions_ztest(count, nobs, alternative='two-sided')


# Display results
print("Z-statistic:", z_stat)
print("P-value:", p_value)


# Check for significance
alpha = 0.05
if p_value < alpha:
   print("Reject the null hypothesis. There is a significant difference in high engagement proportions between Account X and Account Y.")
else:
   print("Fail to reject the null hypothesis. There is no significant difference in high engagement proportions between Account X and Account Y.")
print()

##################################################
###################################################