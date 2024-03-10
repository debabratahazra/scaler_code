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

