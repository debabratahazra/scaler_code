'''
A national survey was conducted to obtain information on the alcohol consumption patterns 
of U.S. adults by marital status.
A random sample of 1772 residents, aged 18 and older, yielded the data displayed in Table 
below:

image: DAV-3/Screenshot_2023-04-27_at_1.36.46_PM.png

Test whether Marital status and alcohol consumption are associated with a 5% 
significance level.

'''

# To test if there is an association between two features, we can use the 
# Chi Squared Test for Independence.

from scipy.stats import chi2_contingency

'''
H0: Marital status and alcohol consumption are not associated.
Ha: Marital status and alcohol consumption are associated. '''

observed = [[67,213,74], [411,633,129], [85,51,7], [27,60,15]]
test_statistic, p_value, dof, expected_values = chi2_contingency(observed)

print("Test statistic:", test_statistic)
print("p-value:", p_value)

alpha = 0.05

if(p_value < alpha):
  print("Reject H0 (Null Hypothesis),i.e. Marital status and alcohol consumption are associated.")
else:
  print("Fail to Reject H0 (Null Hypothesis),i.e. Marital status and alcohol consumption are not associated.")
print()

################################################################
################################################################

'''
According to a survey conducted on car owners, it was determined that

60% of owners have only one car,
28% have two cars, and
12% have three or more cars.
Suppose Ram conducted his own survey within his residential society, and found that

73 owners have only one car,
38 owners have two cars, and
18 owners have three or more cars.
Determine whether Ram's survey supports the original one, with a significance level 
of 0.05.
'''
# Based on the given problem, we define our hypotheses as:
# Null Hypothesis (H0): The distribution of the number of cars owned by car owners in 
# your survey is the same as the distribution in the original survey.

# Alternative Hypothesis (H1): The distribution of the number of cars owned by car 
# owners in your survey is different from the distribution in the original survey.

# We can find out if our observations are consistent with the original survey using 
# Chi-Square Goodness of Fit Test

import numpy as np
from scipy import stats
from scipy.stats import chisquare

# Original survey distribution
expected_distribution = np.array([0.60, 0.28, 0.12])

# Your survey results
observed_distribution = np.array([73, 38, 18])

# Calculate the expected counts based on your sample size
total_sample_size = observed_distribution.sum()
expected_counts = expected_distribution * total_sample_size

# Perform the Chi-Square Goodness of Fit test
chi_squared_stat, p_value = chisquare(f_obs=observed_distribution, f_exp=expected_counts)

# Define the significance level (alpha)
alpha = 0.05
print(f"Chi-Square Statistic: {chi_squared_stat}")
print(f"P-value: {p_value}")
# Check if the p-value is less than alpha to determine significance
if p_value < alpha:
    print("Reject the null hypothesis. Your survey results are significantly different.")
else:
    print("Fail to reject the null hypothesis. Your survey results are consistent with the original survey.")
print()

################################################################
################################################################

# Ques:
'''
A telecom company had taken a survey of smartphone owners in a certain town 5 years 
back and found 73% of the population own a smartphone, and have been since using this 
data to make their business decisions.

Now a new marketing manager has joined, and he believes this value is not valid anymore. 
Thus he conducts a survey of 500 people and finds that 420 of them responded with 
affirmation as to owning a smartphone.

Which statistical test would you use to compare these two survey data?
'''

# Ans:
'''
We will be using a test of proportions here since we want to test whether our 
assumptions/beliefs about the change in smartphone owners are even True or not.

The single proportion (or one-sample) z test is used to compare a proportion of 
responses or values in a sample of data to a (hypothesized) proportion in the
population from which our sample data are drawn.
'''
#################################################################
################################################################

'''
A random sample of adults yielded the following data on age and Internet usage.

image: DAV-3\Screenshot_2023-04-27_at_2.34.39_PM.png

At 1% significance level, does the data provide sufficient evidence to conclude 
that an association exists between age and Internet usage?
'''
#  For this problem statement, we need to perform the chi-squared test for independence. 
# We can use the code given below:

from scipy.stats import chi2_contingency

# H0: Age and Internet usage are not associated
# Ha: Age and Internet usage are associated'''

observed = [[6, 38, 31], 
 [14, 31, 4],
 [50, 50, 5]]

test_statistic, p_value, dof, expected = chi2_contingency(observed)

print("Test statistic:", test_statistic)
print("p-value:", p_value)

alpha = 0.01

if(p_value < alpha):
  print("Reject H0 (Null Hypothesis),i.e. Age and Internet usage are associated")
else:
  print("Fail to Reject H0 (Null Hypothesis),i.e. Age and Internet usage are not associated")
print()

######################################################
########################################################

'''
The U.S. Census Bureau compiles information on the money income of people by type 
of residence and publishes its finding in Current Population Reports.

Independent simple random samples of people consists of following types of residences

Inside Principal Cities (IPC),
Outside Principal Cities but within Metropolitan Areas (OPC), and
Outside Metropolitan Areas (OMA),
The Census gave the following data on income levels:

Image: DAV-3\Screenshot_2023-04-27_at_2.43.31_PM.png

At the 5% significance level, can you conclude that the type of residence is related 
to income level?
'''
# To find if there is a relation between given features, we will use the Chi-Squared 
# Test for Independence.
# H0: type of residence is not related to income level
# Ha: type of residence is related to income level

from scipy.stats import chi2_contingency
observed = [[75, 106, 46],
[106, 161, 61],
[98, 183, 52],
[48, 102, 14]]

test_statistic, p_value, dof, expected = chi2_contingency(observed)

print("Test statistic:", test_statistic)
print("p-value:", p_value)

alpha = 0.05

if(p_value < alpha):
  print("Reject H0 (Null Hypothesis),i.e. type of residence is related to income level")
else:
  print("Fail to Reject H0 (Null Hypothesis),i.e. type of residence is not related to income level")
print()
###################################################
###################################################

'''
A Mobile Retail store owner is interested in the distribution of popular smartphone 
brands among a group of 200 people.

They expect that 30% of people would prefer Brand A, 40% would prefer Brand B and 30% 
would prefer Brand C.

However, upon surveying the group, the results are as follows: 70 prefer Brand A, 
80 prefer Brand B, and 50 prefer Brand C.

Conduct an appropriate test to see if the distribution of preferences matches the 
store owner's expectations at a 5% significance level.
'''

# Based on the problem, we define our hypothesis as:

# Null Hypothesis (H0): The distribution of smartphone brand preferences matches the 
# expected distribution.
# Alternative Hypothesis (H1): The distribution of smartphone brand preferences does 
# not match the expected distribution.

# In order to check whether the observed distribution matches the expectations, we can 
# use Chi Squared Goodness of Fit test

import numpy as np
from scipy import stats

observed_counts = np.array([70, 80, 50])
expected_counts = np.array([0.30 * 200, 0.40 * 200, 0.30 * 200])

chi_squared_stat, p_value = stats.chisquare(f_obs=observed_counts, f_exp=expected_counts)

alpha = 0.05

print(f"Chi-Square Statistic: {chi_squared_stat}")
print(f"P-value: {p_value}")
if p_value < alpha:
    print("Reject the null hypothesis. The distribution of smartphone brand preferences does not match the expected distribution.")
else:
    print("Fail to reject the null hypothesis. The distribution of smartphone brand preferences matches the expected distribution.")
print()

########################################################
#######################################################

'''
Suppose you are interested in the distribution of time spent on a website, by it's users. 
You expect that:

20% of users spend less than 5 minutes,
50% spend between 5 and 10 minutes, and
30% spend more than 10 minutes.
After collecting data from 200 users, you find that

30 users spent less than 5 minutes,
85 users spent between 5 and 10 minutes, and
85 users spent more than 10 minutes.
Conduct an appropriate test to see if the distribution of browsing times matches your 
expectations at a 5% significance level.
'''

# Based on the problem, we define the hypothesis as:

# Null Hypothesis (H0): The distribution of browsing times matches the expected distribution.
# Alternative Hypothesis (H1): The distribution of browsing times does not match the expected 
# distribution.

# In order to check whether the observed distribution matches the expectations, we can use Chi Squared Goodness 
# of Fit test

import numpy as np
from scipy import stats

observed_counts = np.array([30, 85, 85])
expected_counts = np.array([0.20 * 200, 0.50 * 200, 0.30 * 200])

chi_squared_stat, p_value = stats.chisquare(f_obs=observed_counts, f_exp=expected_counts)

alpha = 0.05

print(f"Chi-Square Statistic: {chi_squared_stat}")
print(f"P-value: {p_value}")

if p_value < alpha:
    print("Reject the null hypothesis: The distribution of browsing times does not match expectations.")
else:
    print("Fail to reject the null hypothesis: The distribution of browsing times matches expectations.")
print()
####################################################
###################################################

'''
Preventable chronic diseases are increasing rapidly in Native American populations, particularly diabetes.

Below is a contingency table showing the cross-classification of educational attainment and diabetic state.

Image: DAV-3\Screenshot_2023-04-27_at_1.53.31_PM.png

At 1% significance level, does the data provide sufficient evidence to conclude that an association exists 
between educational level and 
diabetic state for Native Americans?
'''

#  In order to check if there is an association between two features, we can use the Chi-Squared Test for 
# Independence.

# H0: educational level and diabetic state are not associated
# Ha: educational level and diabetic state are associated

from scipy.stats import chi2_contingency

observed = [[33, 218],
[25, 389],
[20, 393],
[17, 178]]

test_statistic, p_value, dof, expected_values = chi2_contingency(observed)

print("Test statistic:", test_statistic)
print("p-value:", p_value)

alpha = 0.01

if(p_value < alpha):
  print("Reject H0 (Null Hypothesis),i.e. educational level and diabetic state are associated")
else:
  print("Fail to Reject H0 (Null Hypothesis),i.e. educational level and diabetic state are not associated")
print()

#####################################################
#######################################################

'''
A Nationwide survey was conducted where an independent and random sample of adults residing in urban, suburban, 
and rural regions, were asked a question: "Do you support or oppose the motion of requiring a background check, 
for all gun buyers?"

The survey results are in the table below:

Image: DAV-3\Screenshot_2023-04-27_at_2.24.27_PM.png

At 1% significance level, does the data provide sufficient evidence to conclude that there is an association
between the region that an adult resides in, and the response received from them?
'''

# In order to check whether there is an association between two features, we can use Chi-Squared Test for 
# Independence.
# H0 : response and regions are not associated
# Ha : response and regions are associated

from scipy.stats import chi2_contingency

observed  = [[335, 348, 318], [35, 23, 50]]

test_statistic, p_value, dof, expected = chi2_contingency(observed)
print('p-value:',round(p_value,5))

if p_value > 0.01:
  print('Since p_value > 0.01 we fail to reject the null hypothesis(i.e.response and regions are not associated)')

else:
  print('Since p_value < 0.01 we reject the null hypothesis (i.e. response and regions are associated)')
print()

#####################################################################
#####################################################################

'''
Suppose you have a coin. You toss the coin 100 times and get 48 heads and 52 tails.

Perform a test to check whether the coin is fair or biased.

You want to determine if the coin is fair at a 5% significance level.
'''

# Based on our problem, we define our hypothesis as:

# Null Hypothesis (H0): The coin is fair (P(heads) = 0.5).
# Alternative Hypothesis (H1): The coin is not fair (P(heads) ≠ 0.5).
# Under the assumption of null hypothesis, we would expect to get 50 heads and 50 tails.

# We need to use the Chi Square Goodness of Fit Test to check if H0 is true.

import numpy as np
from scipy import stats

observed_counts = np.array([48, 52])
expected_counts = np.array([50, 50])

chi_squared_stat, p_value = stats.chisquare(f_obs=observed_counts, f_exp=expected_counts)

alpha = 0.05

print(f"Chi-Square Statistic: {chi_squared_stat}")
print(f"P-value: {p_value}")

if p_value < alpha:
    print("Reject the null hypothesis. The coin is not fair.")
else:
    print("Fail to reject the null hypothesis. The coin is fair.")
print()

##########################################################
##########################################################

'''
Suppose you have data on 150 students' exam scores, and you want to test if the distribution 
of scores falls within predefined categories.

The expected distribution is

30% in the "Excellent" category,
40% in the "Good" category, and
30% in the "Average" category.
Upon observation, you notice that there are:

45 students fall into the "Excellent" category,
50 students into the "Good" category, and
55 students into the "Average" category.
Conduct an appropriate test to see if the distribution matches expectations at a 
5% significance level
'''

# Based on the problem, we define our hypothesis as:

# Null Hypothesis (H0): The distribution of exam scores matches the expected distribution.
# Alternative Hypothesis (H1): The distribution of exam scores does not match the expected distribution.

# In order to check whether the observed distribution matches the expectations, we can use 
# Chi Squared Goodness of Fit test

import numpy as np
from scipy import stats

observed_counts = np.array([45, 50, 55])
expected_counts = np.array([0.30 * 150, 0.40 * 150, 0.30 * 150])

chi_squared_stat, p_value = stats.chisquare(f_obs=observed_counts, f_exp=expected_counts)

print(f"Chi-Square Statistic: {chi_squared_stat}")
print(f"P-value: {p_value}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. The distribution of exam scores does not match the expected distribution.")
else:
    print("Fail to reject the null hypothesis. The distribution of exam scores matches the expected distribution.")
print()

#############################################################
#############################################################

