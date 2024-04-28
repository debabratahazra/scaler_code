import numpy as np
from scipy import stats

# Given IQ scores before and after the drug
IQ_before = np.array([101,124,89,57,135,98,69,105,114,106,97,121,93,116,102,71,88,108,144,99])
IQ_after = np.array([113,127,89,70,127,104,69,127,115,99,104,120,95,129,106,71,94,112,154,96])

# Calculate the differences
differences = IQ_after - IQ_before

# Perform the paired t-test
t_stat, p_value = stats.ttest_rel(differences, np.zeros(len(differences)))

print(f"t-statistic: {t_stat}, p-value: {p_value}")
print()
##################################################'

import numpy as np
from scipy import stats

# IQ scores before and after using Donepezil
IQ_before = np.array([101,124,89,57,135,98,69,105,114,106,97,121,93,116,102,71,88,108,144,99])
IQ_after = np.array([113,127,89,70,127,104,69,127,115,99,104,120,95,129,106,71,94,112,154,96])

# Calculate the differences
IQ_difference = IQ_after - IQ_before

# Calculate the mean and standard deviation of the differences
mean_difference = np.mean(IQ_difference)
std_dev_difference = np.std(IQ_difference, ddof=1)  # Set ddof=1 for sample standard deviation

# Number of pairs of measurements
n = len(IQ_before)

# Calculate the test statistic
t_statistic = mean_difference / (std_dev_difference / np.sqrt(n))

# Degrees of freedom
df = n - 1

# Calculate the critical value for a one-tailed test at 90% confidence
critical_value = stats.t.ppf(0.90, df)

# Print the results
print("Mean of IQ differences:", mean_difference)
print("Standard deviation of IQ differences:", std_dev_difference)
print("Paired samples t-test statistic:", t_statistic)
print("Critical value for one-tailed test at 90% confidence:", critical_value)

# Calculate the p-value
p_value = 1 - stats.t.cdf(t_statistic, df)

# Print the p-value
print("P-value for the paired samples t-test:", p_value)

# Conclusion
alpha = 0.10  # Significance level (corresponding to 90% confidence)
if p_value < alpha:
    print("Reject the null hypothesis. There is sufficient evidence to conclude that the IQ scores after using Donepezil are significantly higher than the IQ scores before using Donepezil.")
else:
    print("Fail to reject the null hypothesis. There is not sufficient evidence to conclude that the IQ scores after using Donepezil are significantly higher than the IQ scores before using Donepezil.")
print()

######################

import scipy.stats as stats
import numpy as np

# Sample of participants’ skills tested before and after the training
before= [101,124,89,57,135,98,69,105,114,106,97,121,93,116,102,71,88,108,144,99]
after = [113,127,89,70,127,104,69,127,115,99,104,120,95,129,106,71,94,112,154,96]

before_mean = np.mean(np.array(before))
after_mean = np.mean(np.array(after))

print("before mean:",before_mean)
print("after mean:",after_mean)

# Performing the paired t-test
t_obs, p = stats.ttest_rel(before, after, alternative="less")

print(" T statistic = ", round(t_obs,2))
print(" p-value = ", round(p,4))

if(p < 0.1):
  print("Since, p-value < alpha, we reject the null hypothesis. Positive effect / improvement in skills after training")
else:
  print("Since, p-value > alpha, we fail to reject the null hypothesis. No effect / improvement in skills after training")
print()

#############################


from scipy.stats import ttest_rel

# Given samples of weight before and after 1 month of following new Zumba routine
wt_before = [101,124,89,57,135,98,69,105,114,106,97,121,93,116,102,71,88,108,144,99]
wt_after = [113,127,89,70,127,104,69,127,115,99,104,120,95,129,106,71,94,112,154,96]

alpha = 0.10 # Significance level

# Performing Paired Right-Tailed T-test
t_stat, pvalue = ttest_rel(wt_before, wt_after, alternative="less" )
print('Test Statistic:', t_stat)
print('P value:', pvalue)

if pvalue < alpha:
  print('Reject H0 ; Customers have reduced their weight after 1 month of new Zumba routine')
else:
  print('Fail to reject H0 ; Customers did not reduce their weight after 1 month of new Zumba routine')
print()
############################

import numpy as np
from scipy import stats

# Flaws data for each machine
m1 = np.array([8, 9, 11, 12])
m2 = np.array([6, 8, 10, 4])
m3 = np.array([14, 12, 18, 9])
m4 = np.array([20, 22, 25, 23])

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(m1, m2, m3, m4)

# Print the p-value and conclusion
print("P-value for the ANOVA test:", p_value)
alpha = 0.05  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis. There is significant evidence to suggest that there is a difference in the performance of the four machines.")
else:
    print("Fail to reject the null hypothesis. There is not enough evidence to suggest that there is a difference in the performance of the four machines.")
print()
#################################
import numpy as np
from scipy.stats import f_oneway

# Data for each machine
m1 = np.array([8, 9, 11, 12])
m2 = np.array([6, 8, 10, 4])
m3 = np.array([14, 12, 18, 9])
m4 = np.array([20, 22, 25, 23])

# Perform one-way ANOVA
f_statistic, p_value = f_oneway(m1, m2, m3, m4)

print("F-statistic:", f_statistic)
print("P-value:", p_value)
print()

########################
#########################

import numpy as np
from scipy import stats

# Given data
claimed_mean = 21.50  # Claimed average highway mileage in Km/L
sample_mean = 20.42  # Sample average highway mileage in Km/L
sample_std_dev = 2.7  # Standard deviation of the sample in Km/L
n = 45  # Sample size

# Perform one-sample t-test
t_statistic = (sample_mean - claimed_mean) / (sample_std_dev / np.sqrt(n - 1))
p_value = stats.t.cdf(t_statistic, df=n-1)

# Calculate the critical t-value for a one-tailed test at 99% confidence
alpha = 0.01  # Significance level for a one-tailed test
t_critical = stats.t.ppf(alpha, df=n-1)

# Print the p-value, t-statistic, and critical t-value
print("P-value for the one-sample t-test:", p_value)
print("One-sample t-test statistic:", t_statistic)
print("Critical t-value for a one-tailed test at 99% confidence:", t_critical)

# Conclusion
if t_statistic < -t_critical:
    print("Reject the null hypothesis. With 99% confidence, there is sufficient evidence to conclude that the average highway mileage is statistically lower than the claimed fuel economy.")
else:
    print("Fail to reject the null hypothesis. With 99% confidence, there is not sufficient evidence to conclude that the average highway mileage is statistically lower than the claimed fuel economy.")
print()

#####################
import numpy as np
from scipy import stats

# Data from 45 cars
mileage_data = np.array([20.42]) # Assuming this is the sample mean

# Hypothesized population mean (claimed fuel economy)
mu = 21.50

# Perform one-sample t-test
t_statistic, p_value = stats.ttest_1samp(mileage_data, mu)

print("T statistic:", t_statistic)
print("P-value:", p_value)

# Setting significance level
alpha = 0.01

# Interpret the results
if p_value < alpha:
    print("Reject the null hypothesis; the average highway mileage is statistically lower than the claimed fuel economy.")
else:
    print("Fail to reject the null hypothesis; there is no statistically significant evidence that the average highway mileage is lower than the claimed fuel economy.")
print()

######################################

import numpy as np
from scipy import stats

# Given data
claimed_mean = 21.50  # Claimed average highway mileage in Km/L
sample_mean = 20.42  # Sample average highway mileage in Km/L
sample_std_dev = 2.7  # Standard deviation of the sample in Km/L
n = 45  # Sample size

# Perform one-sample t-test
t_statistic = (sample_mean - claimed_mean) / (sample_std_dev / np.sqrt(n - 1))
p_value = stats.t.cdf(t_statistic, df=n-1)

# Calculate the critical t-value for a one-tailed test at 99% confidence
alpha = 0.01  # Significance level for a one-tailed test
t_critical = stats.t.ppf(alpha, df=n-1)

# Print the p-value, t-statistic, and critical t-value
print("P-value for the one-sample t-test:", p_value)
print("One-sample t-test statistic:", t_statistic)
print("Critical t-value for a one-tailed test at 99% confidence:", t_critical)

# Conclusion
if t_statistic < -t_critical:
    print("Reject the null hypothesis. With 99% confidence, there is sufficient evidence to conclude that the average highway mileage is statistically lower than the claimed fuel economy.")
else:
    print("Fail to reject the null hypothesis. With 99% confidence, there is not sufficient evidence to conclude that the average highway mileage is statistically lower than the claimed fuel economy.")
print()

####################################

import numpy as np
from scipy import stats

# Given data
claimed_mean = 21.50  # Claimed average highway mileage in Km/L
sample_mean = 20.42  # Sample average highway mileage in Km/L
sample_std_dev = 2.7  # Standard deviation of the sample in Km/L
n = 45  # Sample size

# Perform one-sample t-test
t_statistic = (sample_mean - claimed_mean) / (sample_std_dev / np.sqrt(n - 1))
p_value = stats.t.cdf(t_statistic, df=n-1)

# Print the p-value
print("P-value for the one-sample t-test:", p_value)
print()

##################################

import numpy as np
from scipy import stats

# Given data
claimed_mean = 21.50  # Claimed average highway mileage in Km/L
sample_mean = 20.42  # Sample average highway mileage in Km/L
pop_std_dev = 2.7  # Population standard deviation of the highway mileage in Km/L
n = 45  # Sample size

# Calculate the standard error
standard_error = pop_std_dev / np.sqrt(n)

# Perform one-sample z-test
z_statistic = (sample_mean - claimed_mean) / standard_error
p_value = 2 * (1 - stats.norm.cdf(np.abs(z_statistic)))  # Two-tailed test

# Print the p-value
print("P-value for the one-sample z-test:", p_value)
print()

########################

import numpy as np
from scipy import stats

# Data from 45 cars
mileage_data = np.array([20.42]) # Assuming this is the sample mean

# Hypothesized population mean (claimed fuel economy)
mu = 21.50

# Perform one-sample t-test
t_statistic, p_value = stats.ttest_1samp(mileage_data, mu)

print("T statistic:", t_statistic)
print("P-value:", p_value)

# Setting significance level
alpha = 0.01

# Interpret the results
if p_value < alpha:
    print("Reject the null hypothesis; the average highway mileage is statistically lower than the claimed fuel economy.")
else:
    print("Fail to reject the null hypothesis; there is no statistically significant evidence that the average highway mileage is lower than the claimed fuel economy.")
print()

############################

from statsmodels.stats.weightstats import ztest

# Data from 45 cars
data = [20.42] * 45 # Assuming this is the sample mean repeated for each car

# Hypothesized population mean (claimed fuel economy)
value = 21.50

# Perform one-sample Z-test
z_statistic, p_value = ztest(data, value=value)

print("Z statistic:", z_statistic)
print("P-value:", p_value)

# Setting significance level
alpha = 0.01

# Interpret the results
if p_value < alpha:
    print("Reject the null hypothesis; the average highway mileage is statistically lower than the claimed fuel economy.")
else:
    print("Fail to reject the null hypothesis; there is no statistically significant evidence that the average highway mileage is lower than the claimed fuel economy.")
print()

########################

import pandas as pd

# Sample dataset
data = {'date': ['2022-01-15', '2022-04-22', '2022-07-08', '2022-10-30']}
df = pd.DataFrame(data)

df['quarter'] = pd.to_datetime(df['date']).dt.month // 3 + 2
# print(df.head())
df['quarter'] = pd.to_datetime(df['date']).apply(lambda x: 'Q'+str((x.month-1)//3+1).zfill(2))
# print(df.head())
df['quarter'] = pd.to_datetime(df['date']).dt.quarter
# print(df.head())
df['quarter'] = pd.to_datetime(df['date']).apply(lambda x: 'Q'+str((x.month-1)//3+2))
print(df.head())
print()

######################

import numpy as np
from scipy import stats

# Given data
claimed_mean = 21.50  # Claimed average highway mileage in Km/L
sample_mean = 20.42  # Sample average highway mileage in Km/L
sample_std_dev = 2.7  # Standard deviation of the sample in Km/L
n = 45  # Sample size

# Perform one-sample t-test
t_statistic = (sample_mean - claimed_mean) / (sample_std_dev / np.sqrt(n))
p_value = stats.t.cdf(t_statistic, df=n-1)

# Print the p-value
print("P-value for the one-sample t-test:", p_value)
print()

####################

'''
Sun Pharmaceutical Industries claims that a person's IQ improves after they use the Donepezil drug.

To test this claim a trial was conducted considering 20 patients. An IQ test was conducted for these patients before giving the drug and an IQ test was conducted for the same set of patients after the drug the recorded results are shown below.

IQ_before=[101,124,89,57,135,98,69,105,114,106,97,121,93,116,102,71,88,108,144,99]

IQ_after=[113,127,89,70,127,104,69,127,115,99,104,120,95,129,106,71,94,112,154,96]
Perform an appropriate test to test the claim at 90% confidence.
'''

#####################

