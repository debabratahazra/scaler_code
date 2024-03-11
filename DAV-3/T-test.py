'''An experiment was performed to compare the effectiveness of Ammonium Chloride and urea 
on the grain yield (in quintal per hectare) and the results are given in the arrays below:

Ammonium_chloride = [13.4, 10.9, 11.2, 11.8, 14, 15.3, 14.2, 12.6, 17, 16.2, 16.5, 15.7]
Urea = [12, 11.7, 10.7, 11.2, 14.8, 14.4, 13.9, 13.7, 16.9, 16, 15.6, 16]
Conduct an appropriate test to compare the same with a 95% confidence level and choose 
the appropriate option below.'''

# We define our hypothesis as:

# H0 = the effect of ammonium chloride and urea on grain yield is equal.
# H1 = the effect of ammonium chloride and urea on grain yield is not equal.
# Since we need to compare two different samples, whose sample size is small (<30), 
# we will use Two Sample T-test

# Further, in order to test for the proposed alternate hypothesis, we will have to perform 
# a Two Tailed Test.     

from scipy.stats import ttest_ind

# Given samples of farm yields with following chemicals
ammonium_chloride = [13.4, 10.9, 11.2, 11.8, 14, 15.3, 14.2, 12.6, 17, 16.2, 16.5, 15.7]
urea = [12, 11.7, 10.7, 11.2, 14.8, 14.4, 13.9, 13.7, 16.9, 16, 15.6, 16]
alpha = 0.05 # Significance level

# Performing 2 Sample Two-Tailed T-test
t_stats, pvalue = ttest_ind(ammonium_chloride, urea, alternative ='two-sided')
print("P_value:",pvalue)

if pvalue < alpha:
  print('Reject H0 ; The effect of ammonium chloride and urea on grain yield is not equal')
else:
  print('Fail to reject H0 ; The effect of ammonium chloride and urea on grain yield is equal')
print()

################################################################
###############################################################
'''
Ques:::

A certain company decided to roll out a new training regime for its employees.

To test which regime (old or new) would be preferred by the employees, they made 5 
employees (who had earlier cleared the old regime) take part in the new training regime, 
and then score them both, out of 100.

Which of the following statistical procedures would be most appropriate to test the 
claim that employee overall scores are the same in both training regimes?

Employee:   1    2   3   4   5
Old Regim:  70   90  87  83  97
New Regim:  73   88  90  85  98

'''

'''
Ans::


Null and alternative hypotheses:

Null hypothesis (H₀): The mean score for the new training regime is equal to the mean 
score for the old training regime. µ_new = µ_old.

Alternative hypothesis (H₁): The mean score for the new training regime is different 
from the mean score for the old training regime. µ_new ≠ µ_old.

We know that two sample test is done when we are comparing the mean of two groups with 
each other. Here the condition for this satisfies.

Similarly, two sided tailed test is used when we evaluate on both sides, and here again, 
the condition satisfies to evaluate both the regimes.

And finally, since the same sample group takes part in both the before and after regimes, 
we can conclude that we need a Two-tailed two-sample dependent/paired t-test of means.
'''
##########################################################
#########################################################

'''
There are 8 females and 12 males in a coaching class.

After a practice test, the coach wants to know whether the average score of females is 
greater than the average score of males.

Given data describes the scores of females and males in his class.

female_scores=[25,30,45,49,47,35,32,42]

male_scores=[45,47,25,22,29,32,27,28,40,49,50,33]
Use an appropriate test to check whether the assumption of the coach is significant or 
not, at a 2% significance level?
'''

# Based on the given problem, we define our hypothesis as:

# H0: μ1 ≤ μ2, i.e., the average score of females is not greater than the average score 
# of males.
# H1: μ1 > μ2 i.e. the average score of females is greater than the average score of males.

# Based on these proposed hypothesis, we will need to perform Right-tailed test in order 
# to test for the alternate hypothesis.

import pandas as pd
from scipy.stats import ttest_ind

female_scores=pd.Series([25,30,45,49,47,35,32,42])
male_scores=pd.Series([45,47,25,22,29,32,27,28,40,49,50,33])

t_stat, p_value = ttest_ind(female_scores, male_scores, alternative="greater")
print("Test statistic = ", round(t_stat,3))
print("P_value =",p_value )

alpha=0.02
if p_value < alpha:
    print("Reject the null hypothesis. There is significant evidence that the average score of females is greater than the average score of males.")
else:
    print("Fail to reject the null hypothesis. There is no significant evidence that the average score of females is greater than the average score of males.")
print()

################################################################
###############################################################

'''
The Zumba trainer claims to the customers, that their new dance routine helps to reduce 
more weight.

Weight of 8 people were recorded before and after following the new Zumba training for 
a month:

wt_before = [85, 74, 63.5, 69.4, 71.6, 65,90,78]

wt_after = [82, 71, 64, 65.2, 67.8, 64.7,95,77]
Test the trainer's claim with 90% confidence. Further, what would be the pvalue?
'''

# Based on the given problem, we define our hypothesis as:

# H0: Customers did not reduce their weight after 1 month of new Zumba routine 
# μ-Before = μ-After 
# H1: Customers have reduced their weight after 1 month of new Zumba routine 
# μ-Before > μ-After​
 
# The nature of data here is in the form of “Before” and “After” the new Zumba dance routine. 
# Hence we will use Paired T-test using ttest_rel()

# Further, in order to test our proposed alternate hypothesis, we would have to perform 
# Right Tail test

from scipy.stats import ttest_rel

# Given samples of weight before and after 1 month of following new Zumba routine
wt_before = [85, 74, 63.5, 69.4, 71.6, 65,90,78]
wt_after = [82, 71, 64, 65.2, 67.8, 64.7,95,77]

alpha = 0.10 # Significance level

# Performing Paired Right-Tailed T-test
t_stat, pvalue = ttest_rel(wt_before, wt_after, alternative="greater" )
print('Test Statistic:', t_stat)
print('P value:', pvalue)

if pvalue < alpha:
  print('Reject H0 ; Customers have reduced their weight after 1 month of new Zumba routine')
else:
  print('Fail to reject H0 ; Customers did not reduce their weight after 1 month of new Zumba routine')
print()

########################################################################
#######################################################################

'''
The quality assurance department claims that on average the non-fat milk contains more 
than 190 mg of Calcium per 500 ml packet.

To check this claim 45 packets of milk are collected and the content of calcium is
recorded.

Perform an appropriate test to check the claim with a 90% confidence level.

data = [193, 321, 222, 158, 176, 149, 154, 223, 233, 177, 280, 244, 138, 210, 167, 129, 
254, 167, 194, 191, 128, 191, 144, 184, 330, 216, 212, 142, 216, 197, 231, 133, 205, 192, 
195, 243, 224, 137, 234, 171, 176, 249, 222, 234, 191]


Note: Round off the answer to four decimal places.
'''

# Since we need to test the claim made by company, we define our hypothesis as:

# H0: µ <= 190
# H1: µ > 190 (Right-tailed test)
# We perform one sample t-test.

from scipy.stats import ttest_1samp

data = pd.Series([193, 321, 222, 158, 176, 149, 154, 223, 233, 177, 280, 244, 138, 210, 167, 129, 254, 167, 194, 191, 128, 191, 144, 184, 330, 216, 212, 142, 216, 197, 231, 133, 205, 192, 195, 243, 224, 137, 234, 171, 176, 249, 222, 234, 191])

print("Observed sample mean = ", round(data.mean(), 2))
t_stat, p_value = ttest_1samp(data, popmean=190, alternative="greater")

print("Test statistic = ", round(t_stat,4))
print("P-value = ", round(p_value,4))

if p_value < 0.10:
 print("Reject H0")
else: 
 print("Fail to reject H0")
print()

################################################################
###############################################################

'''
You are appointed as a Data Analyst for a training program deployed by the Government of India.

The participants’ skills were tested before and after the training using some metrics on a 
scale of 10.

before = [2.45, 0.69, 1.80, 2.80, 0.07, 1.67, 2.93, 0.47, 1.45, 1.34]   

after = [7.71, 2.17, 5.65, 8.79, 0.23, 5.23, 9.19, 1.49, 4.56, 4.20] 
Conduct an appropriate test to assess a statistically significant increase in the average 
skill score after the training program, and then answer the below questions accordingly.

Note: Perform the test at alpha = 5%.
'''
# We propose the Hypothesis as follows:

# H0: No improvement in skills after training, i.e. μ1 = μ2​ 
# Ha: Positive effect / improvement in skills after training, i.e. μ1 < μ2​
 
# We can test this using Paired T-test

import scipy.stats as stats
import numpy as np

# Sample of participants’ skills tested before and after the training
before= [2.45, 0.69, 1.80, 2.80, 0.07, 1.67, 2.93, 0.47, 1.45, 1.34]
after = [7.71, 2.17, 5.65, 8.79, 0.23, 5.23, 9.19, 1.49, 4.56, 4.20]

before_mean = np.mean(np.array(before))
after_mean = np.mean(np.array(after))

print("before mean:",before_mean)
print("after mean:",after_mean)

# Performing the paired t-test
t_obs, p = stats.ttest_rel(before, after, alternative="less")

print(" T statistic = ", round(t_obs,2))
print(" p-value = ", round(p,4))

if(p < 0.05):
  print("Since, p-value < alpha, we reject the null hypothesis. Positive effect / improvement in skills after training")
else:
  print("Since, p-value > alpha, we fail to reject the null hypothesis. No effect / improvement in skills after training")
print()

################################################################
#################################################################

'''
Traditionally it is known that a green gram cultivation yields 12.0 quintals per hectare on 
an average.

In order to increase crop yields, scientists have developed a new variety of green grams, 
that can supposedly produce more than the expected average yield of 12 quintals per hectare.

To test the same, this variety of green grams was tested on 10 randomly selected farmer's 
fields.

The yield (quintals/hectare) was recorded as: 
[14.3,12.6,13.7,10.9,13.7,12.0,11.4,12.0,12.6,13.1]

With a 5% significance level, can we conclude that the average yield of this variety of 
green grams is more than the expected yield (12 quintals/hectare)?
'''

# Based on the question, we define our hypothesis as:

# H0 : This variety of green gram will Yield 12 quintals per hectare (Yield = 12)
# Ha : This variety of green gram will Yield more than 12 quintals per hectare (Yield > 12)
# We can solve this using One sample T-test

# Since we will be performing Right Tail Test, we will set alternative = "greater"

from scipy.stats import ttest_1samp

yield_data = [14.3,12.6,13.7,10.9,13.7,12.0,11.4,12.0,12.6,13.1]
alpha = 0.05  #5% significance level

tstat, pvalue = ttest_1samp(yield_data, 12.0, alternative = "greater")
print(pvalue)

if pvalue < alpha:
  print('Reject H0 ; Yield will be more than 12 quintals per hectare')
else:
  print('Fail to reject H0 ; Yield will be 12 quintals per hectare')
print()

###############################################################
###############################################################

'''
Samples of Body fat percentages of few gym going men and women are recorded.

men = [13.3, 6.0, 20.0, 8.0, 14.0, 19.0, 18.0, 25.0, 16.0, 24.0, 15.0, 1.0, 15.0]
women = [22.0, 16.0, 21.7, 21.0, 30.0, 26.0, 12.0, 23.2, 28.0, 23.0]
Perform an appropriate test to check if the mean body fat percentage of men and women is 
statistically different.

Assume the significance level to be 5%
'''

# Based on the given problem, we define our hypothesis as:

# H0 : Body fat percentage of men and women are same μ1 = μ2 
# Ha : Body fat percentage of men and women are different μ1 != μ2
# Since we need to compare two different samples, whose sample size is small (<30), 
# we will use Two Sample T-test

# Further, in order to test for the proposed alternate hypothesis, we will have to 
# perform a Two Tailed Test.

from scipy.stats import ttest_ind

# Given samples of gym-going men and women body fat percentages
men = [13.3, 6.0, 20.0, 8.0, 14.0, 19.0, 18.0, 25.0, 16.0, 24.0, 15.0, 1.0, 15.0]
women = [22.0, 16.0, 21.7, 21.0, 30.0, 26.0, 12.0, 23.2, 28.0, 23.0]
alpha = 0.05 # Significance level

# Performing 2 Sample Two-Tailed T-test
t_stats, pvalue = ttest_ind(men, women, alternative ='two-sided')
print(pvalue)

if pvalue < alpha:
  print('Reject H0 ; Body fat percentage of men and women are different')
else:
  print('Fail to reject H0 ; Body fat percentage of men and women are the same')
print()

####################
##############################################

'''
The average British man is 175.3 cm tall. A survey recorded the heights of 10 UK men 
and we want to know whether the mean of the sample is different from the population mean.

survey_height = [177.3, 182.7, 169.6, 176.3, 180.3, 179.4, 178.5, 177.2, 181.8, 176.5]

Perform an appropriate test and choose the correct option below, that we can conclude with 
a 5% significance.
'''

import numpy as np
from scipy import stats

'''
Null Hypothesis (H0): The sample mean height is equal to the population mean (μ = 175.3 cm).
Alternate Hypothesis (H1): The sample mean height is different from the population mean (μ ≠ 175.3 cm).
'''

# Population mean
population_mean = 175.3

# Heights of 10 UK men
survey_height = [177.3, 182.7, 169.6, 176.3, 180.3, 179.4, 178.5, 177.2, 181.8, 176.5]

# Perform one-sample t-test
t_statistic, p_value = stats.ttest_1samp(survey_height, population_mean,alternative = "two-sided")

# Set the significance level
alpha = 0.05

# Print the results
print("t-statistic:", t_statistic)
print("p-value:", p_value)

# Determine the conclusion
if p_value < alpha:
    print("Reject the null hypothesis")
    print("There is enough evidence to conclude that the sample mean height is different from the population mean.")
else:
    print("Fail to reject the null hypothesis")
    print("There is no enough evidence to conclude that the sample mean height is different from the population mean.")
print()

##########################################################
########################################################

'''
Samples of IQ scores are collected from two competing schools, as follows:

school_1 = [115, 111, 112, 101, 95, 98, 100, 90, 89, 108]
school_2 = [107, 103, 91, 99, 104, 98, 117, 113, 92, 96, 108, 115, 116, 88]
Perform an appropriate test with a 5% significance level to check if there is any 
statistically significant difference in the mean IQ's of these schools.
'''

# Based on the given problem, we define our hypothesis as:

# H0 : IQ scores of the two schools are same μ1 = μ2 
# Ha : IQ scores of the two schools are different μ1 != μ2 
# Since we need to compare two different samples, whose sample size is small (<30), 
# we will use Two Sample T-test

# Further, in order to test for the proposed alternate hypothesis, we will have to 
# perform a Two Tailed Test.

from scipy.stats import ttest_ind

# Sample IQ scores
school_1 = [115, 111, 112, 101, 95, 98, 100, 90, 89, 108]
school_2 = [107, 103, 91, 99, 104, 98, 117, 113, 92, 96, 108, 115, 116, 88]
alpha = 0.05 # Significance level

# Performing Two sample Twp Tiled T-test
t_stat, pvalue = ttest_ind(school_1, school_2, alternative ='two-sided')
print("p value : ", pvalue)

if pvalue < alpha:
  print('Reject H0 ; IQ scores of the two schools are different')
else:
  print('Fail to reject H0 ; IQ scores of the two schools are same')
print()

################################################################
################################################################

