'''
The United States is divided into four regions: Northeast, Midwest, South and West regions.

Independent random samples of households in these regions yielded the data on last year’s energy consumptions.

a = [13, 8, 11, 12, 11]
b = [15, 10, 16, 11, 13, 10]
c = [5, 11, 9, 5]
d = [8, 10, 6, 5, 7]

Image: DAV-3/Screenshot_2023-04-27_at_4.57.01_PM.png


At a 5% significance level, does the data provide sufficient evidence to conclude that 
there is a difference in last year’s mean energy consumption
by households among the four regions?

'''

# Based on the given problem, we define our hypothesis as:

# H0 : Last year’s mean energy consumption is equal among households of the four 
# regions
# Ha : Not all regions’ households had the same mean energy consumption in last year
# Since we are required to conduct an experiment between MULTIPLE groups at the same time, 
# we will use ANOVA Test

from scipy.stats import f_oneway

a = [13, 8, 11, 12, 11]
b = [15, 10, 16, 11, 13, 10]
c = [5, 11, 9, 5]
d = [8, 10, 6, 5, 7]

test_statistic, p_value = f_oneway(a,b,c,d)

print("P Value:", p_value)

if p_value < 0.05:
    print("Reject H0; Not all regions' households had the same mean energy consumption in last year")
else:
    print("Fail to reject H0; Last year's mean energy consumption is equal among households of the four regions")
print()

############################################################
############################################################

# QQ plots:

# Ans:
'''
Let’s look at each option carefully:

If the points on a QQ plot closely follow a straight line, the plot indicates that the 
Normal model is an adequate representation for the data: True:
-If the points on a Normal quantile plot lie close to a straight line, it indicates that 
the Normal model is an adequate representation for the data. A departure from a straight 
line suggests a deviation from normality.


A histogram, showing the typical mound-like appearance of the Normal distribution, is 
more helpful than a QQ plot for assessing Normality: False:
-This statement is incorrect. The quantile plot is often considered more helpful than a 
histogram for assessing normality. While a histogram provides an overall shape, the 
quantile plot offers a direct comparison to the expected quantiles of a Normal distribution, 
making it more sensitive to departures from normality.


Outliers on a QQ plot will manifest as points significantly deviating from the overall 
pattern of the plot.: True:
-On a quantile plot, outliers will appear as points that are far away from the overall 
pattern of the plot. This makes it easier to identify outliers compared to a histogram.


The QQ plot is a very useful graphical tool for assessing the adequacy of the Normal model.
: True:
-The Normal quantile plot is indeed a very useful graphical tool for assessing the adequacy 
of the Normal model. It provides a visual check of normality by comparing the distribution of data points to the expected distribution under normality.
'''

###############################################################
##############################################################

# Ques: Mark the correct assumptions of ANOVA:

# Ans: (all 3)

# Populations from which samples are drawn should be normal
# The samples should be drawn randomly and independently
# The variability between the dependent variables within different groups is equal.

''' Explanation: 

- Populations from which samples are drawn should be normal because ANOVA is a 
parametric test based on the assumption that the data follow the normal distribution. 
Hence it is necessary to test the normality. If the data does not follow the normal d
istribution, ANOVA cannot be applied.

- The value of 1 observation must not influence the value of other observations. 
All experimental units must be independent, and each experimental unit must contribute 
only 1 response value and the samples should be drawn randomly from the larger normal 
population. The samples should be drawn randomly and independently.

- The variability between the dependent variables within different groups is equal as a 
significantly different variance could overshadow the differences between means and lead 
to incorrect conclusions
'''

####################################################################
####################################################################

'''
There is a website, "www.goodreads.com" where people can leave their reviews about a 
book and rate them on a scale of 1 to 5 stars.
The following table gives the number of pages of a random sample of books with different 
ratings, as listed on the site:


one_star = [382, 391, 335, 368, 400, 372]
two_star = [560, 343, 512, 329, 391, 367]
three_star = [384, 458, 409, 309, 374, 459]
four_star = [325, 390, 304, 240, 306, 169]
five_star = [360, 298, 272, 368, 320, 326]

At a 1% significance level, does the data provide sufficient evidence to conclude that 
there is a difference in the mean number of pages among books in these five rating groups?
'''

# Based on the given problem, we define our hypothesis as:

# H0: Number of pages in the books belonging to different rating groups is same
# Ha: Number of pages in the books belonging to different rating groups is different
# Since we are required to conduct an experiment between MULTIPLE groups at the same time, 
# we will use ANOVA Test

from scipy.stats import f_oneway

one_star = [382, 391, 335, 368, 400, 372]
two_star = [560, 343, 512, 329, 391, 367]
three_star = [384, 458, 409, 309, 374, 459]
four_star = [325, 390, 304, 240, 306, 169]
five_star = [360, 298, 272, 368, 320, 326]

test_statistic, p_value = f_oneway(one_star, two_star, three_star, four_star, five_star)

print("P Value:", p_value)

alpha = 0.01
if  p_value < alpha:
    print("Reject H0, Number of pages in the books belonging to different rating groups is different")
else:
    print("Fail to reject H0; Number of pages in the books belonging to different rating groups is same")
print()

####################################################################
####################################################################

'''
Consumer Reports publishes reviews and comparisons of products based on results from its 
laboratory.
Data from their website gave the following table for battery lives in hours, for samples 
of smartphones made by four different mobile companies.

Brand_A = [19.60, 18.82, 19.00, 18.45, 19.79, 19.03, 17.89, 19.42]
Brand_B = [21.10, 20.00, 20.43, 19.67, 18.99, 19.98, 20.14, 19.78]
Brand_C = [10.31, 10.02, 9.41, 9.89, 10.05, 10.52, 11.02, 10.42]
Brand_D = [17.02, 16.71, 17.78, 18.65, 15.98, 17.63, 17.00, 16.78, 16.92, 17.14]

At a 2% significance level, does the data provide sufficient evidence to conclude that 
there is a significant difference in the mean battery life, among the four brands?

And, if significant, then perform pairwise T-tests to identify which pairs of smartphone 
brands offer a different mean battery life.
'''

# Since we need to compare numerical values of 4 (>2) groups, let’s perform ANOVA test 
# to see if there is any significant difference between the mean battery life of these 
# smartphone brands.

# We define our hypothesis as:

# Null Hypothesis (H0): There are no significant differences in the mean battery life of 
# smartphones among these 4 brands
# Alternative Hypothesis (H1): There is at least one pair of smartphone brands that offer a 
# significant difference in their mean battery
# We can use the following code for the same. The significance level is set at 0.02

import scipy.stats as stats

# Sample data for battery life of different smartphone brands
brand_A = [19.60, 18.82, 19.00, 18.45, 19.79, 19.03, 17.89, 19.42]
brand_B = [21.10, 20.00, 20.43, 19.67, 18.99, 19.98, 20.14, 19.78]
brand_C = [10.31, 10.02, 9.41, 9.89, 10.05, 10.52, 11.02, 10.42]
brand_D = [17.02, 16.71, 17.78, 18.65, 15.98, 17.63, 17.00, 16.78, 16.92, 17.14]

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(brand_A, brand_B, brand_C, brand_D)

# Print the results
print("One-Way ANOVA results:")
print("F-statistic:", f_statistic)
print("P-value:", p_value)

alpha = 0.02

# Interpret the results of one-way ANOVA
if p_value < alpha:
   print("Reject the null hypothesis")
   print("There is at least one pair of smartphone brands that offer a significantly different mean battery life.")
else:
   print("Fail to reject the null hypothesis")
   print("There are no significant differences in the mean battery life of smartphones among these 4 brands.")
print()

###################################################
####################################################

'''
The pharmaceutical company collected data on the treatment effects (values in 
corresponding units) of two drug formulations (Group A and Group B) in a study

group_a_effects = [1.5, 1.8, 1.2, 1.6, 1.7]

group_b_effects = [1.4, 1.9, 1.3, 1.5, 1.8]
The researchers want to assess whether the variances of the treatment effects are 
significantly different among the two groups.

Perform the appropriate test with a 90% confidence level, calculate the p-value and 
interpret the conclusions.
'''

# By default, Levene Test utilizes the following hypothesis:

# H0: The variances between the groups are equal
# Ha: The variances between the groups are different
# Further it is mentioned that alpha = 0.1 (90% confidence level)
# So we need to compute the pvalue of Levene’s test, and compare it to alpha

import numpy as np
from scipy.stats import levene

# Treatment effects for Group A and Group B
group_a_effects = [1.5, 1.8, 1.2, 1.6, 1.7]
group_b_effects = [1.4, 1.9, 1.3, 1.5, 1.8]

# Perform Levene's test
statistic, p_value = levene(group_a_effects, group_b_effects)

print("Levene's Test Statistic:", statistic)
print("P-value:", p_value)

# 90% Confidence level
alpha = 0.1

if p_value < alpha:
 print('Reject H0; The variances between the groups are different')
else:
 print('Fail to reject H0; The variances between the groups are same')
print()

###############################################################
##################################################################

'''
Ques:
If a QQ plot displays points deviating both above and below the reference line,
what might you infer about the dataset?

Image: DAV-3/Screenshot_2023-12-12_at_5.41.28_PM.png

'''
# Ans: 
# The dataset has outliers.
# The dataset is not normally distributed

''' Explanation:
If a QQ plot displays points deviating both above and below the line, it suggests that 
the dataset has outliers.

Outliers are data points that significantly differ from the overall pattern of the dataset.
In a QQ plot, these outliers manifest as points that deviate from the expected line, 
indicating a departure from the normal distribution.

'''

####################################################################
#####################################################################

'''
A software development team is comparing the performance of three different algorithms 
for sorting large datasets.

The team collects the execution time (in milliseconds) for each algorithm on 20 different 
datasets:

algorithm_A = np.array([23, 25, 22, 27, 28, 24, 26, 29, 21, 30, 25, 43, 26, 28, 24, 22, 27, 
46, 25, 29]) 

algorithm_B = np.array([31, 28, 29, 32, 30, 33, 27, 28, 32, 30, 31, 29, 30, 48, 33, 31, 29, 
30, 32, 31]) 

algorithm_C = np.array([45, 43, 23, 49, 49, 8, 21, 20, 42, 40, 28, 46, 44, 37, 44, 38, 42, 
34, 42, 40])

Check for the assumptions of One-way ANOVA & decide the appropriate test to determine if 
there is a statistically significant difference in the execution times of the three 
algorithms at a 95% confidence level.
'''

# One way ANOVA has the following assumptions, that we need to perform the following:

# Normality Check: We will perform a Shapiro-Wilk test to test if data follows normal 
# distribution.
# Equal Variance Check: We will perform Levene test to test for equal variances across 
# groups.

import numpy as np
from scipy.stats import shapiro

algorithm_A = np.array([23, 25, 22, 27, 28, 24, 26, 29, 21, 30, 25, 43, 26, 28, 24, 22, 27, 46, 25, 29])
algorithm_B = np.array([31, 28, 29, 32, 30, 33, 27, 28, 32, 30, 31, 29, 30, 48, 33, 31, 29, 30, 32, 31])
algorithm_C = np.array([45, 43, 23, 49, 49, 8, 21, 20, 42, 40, 28, 46, 44, 37, 44, 38, 42, 34, 42, 40])

# H0: Data is Gaussian
# Ha: Data is not Gaussian

# Shapiro-Wilk test for Algorithm A
stat, pvalue_a = shapiro(algorithm_A)
# Shapiro-Wilk test for Algorithm B
stat, pvalue_b = shapiro(algorithm_B)
# Shapiro-Wilk test for Algorithm C
stat, pvalue_c = shapiro(algorithm_C)

alpha = 0.05

print("Shaprio results:")
print("algorithm_A:", pvalue_a,"; Not normally distributed" if pvalue_a <= alpha else " ; Normally distributed")
print("algorithm_B:", pvalue_b,"; Not Normally distributed" if pvalue_b <= alpha else " ; Normally distributed")
print("algorithm_C:", pvalue_c,"; Not Normally distributed" if pvalue_c <= alpha else " ; Normally distributed")
print()



from scipy.stats import levene

# H0: Variances are equal
# Ha: Variances are not equal

# Levene test
statistic, pvalue_levene = levene(algorithm_A, algorithm_B, algorithm_C)
print('Levene test p-value:',pvalue_levene)

if p_value < 0.05:
 print("Variances are not equal")
else:
 print("Variances are equal")
print()


# Since we can see that data does not follow assumptions of One Way ANOVA, we 
# will need to perform Kruskal-Wallis test in order to make conclusions.

from scipy.stats import kruskal
# Null Hypothesis (H0): The medians of the execution times are the same for all three algorithms.
# Alternative Hypothesis (H1): At least one of the medians of the execution times is different among the three algorithms.

stat, p_value = kruskal(algorithm_A, algorithm_B, algorithm_C)

print("test statistic:",stat)
print("p_value:",p_value)

if p_value < 0.05:
   print("Reject H0")
   print("At least one of the medians of the execution times is different among the three algorithms")
else:
   print("Fail to reject H0")
   print("The medians of the execution times are the same for all three algorithms.")
print()

###############################################
################################################

'''
A Company wishes to test whether three sales persons Saurav, Naveen, and Radha make the 
same sales or they differ in their selling ability by comparing the average number of 
sales made by them last week.

Out of 14 sales 'Saurav' made 5, 'Naveen' made 4 and 'Radha' made 5. The following arrays 
describes the records of the sales persons in rupees.

Saurav = [300, 400, 300, 500, 50]
Naveen = [600, 300, 300, 400]
Radha = [700, 300, 400, 600, 500]

Test whether the average sales of the Saurav, Naveen, and Radha differ in size at a 95% 
confidence level.
'''

import numpy as np
from scipy.stats import f_oneway

'''
Null Hypothesis (H0): The average sales of Saurav, Naveen, and Radha are equal.
Alternative Hypothesis (Ha): At least one of the salesperson's average sales is different from the others.'''

saurav = np.array([300, 400, 300, 500, 50])
naveen = np.array([600, 300, 300, 400])
radha = np.array([700, 300, 400, 600, 500])

# Perform one-way ANOVA
f_statistic, p_value = f_oneway(saurav, naveen, radha)

# Significance level (alpha)
alpha = 0.05

print("F-statistic:", f_statistic)
print("p-value:", p_value)

# Compare p-value with significance level
if p_value < alpha:
    print("Reject null hypothesis: There is a significant difference in average sales.")
else:
    print("Fail to reject null hypothesis: There is no significant difference in average sales.")
print()

#############################################
###############################################

'''
Note:

Kruskal Wallis test is used to determine if there are any statistically significant 
differences between the medians of three or more independent (unrelated) groups.

Shapiro Wilk test is used to check if a sample comes from a normally distributed population.

ANOVA is used to determine if there are any statistically significant differences between 
the means of three or more independent (unrelated) groups.

Levene’s Test assesses the homogeneity of variances for a set of independent samples. 
Commonly used before ANOVA to check the assumption of equal variances.

'''

##########################################################
###############################################################

'''
A pharmaceutical company conducted a clinical trial to test the effectiveness of three 
different drug treatments (Drug A, Drug B, and Drug C) on patients with a specific medical 
condition.

The trial measured the reduction in symptoms for each patient after treatment. 
The dataset consists of three groups, each representing one drug treatment, 
where each value represents the unit difference before and after taking the drugs.

drug_a = [8, 17, 16, 25, 17]
drug_b = [9, 8, 16, 7, 8]
drug_c = [7, 6, 5, 4, 6]

Conduct an appropriate test to assess overall differences with a 99% confidence level 
and, if significant, perform pairwise t-tests to identify which pairs of drug treatments 
exhibit significant differences in the reduction of symptoms.
'''

# Since we need to compare the numerical values between 3 (>2) groups/categories, 
# we need to perform ANOVA test to see if there is any significant difference between
# the reduction of symptoms among these drug treatments.

# We define our hypothesis as:

# Null Hypothesis (H0): There are no significant differences in symptom reduction 
# caused by the three drug treatments
# Alternative Hypothesis (H1): There is at least one pair of drug treatment that 
# results in significant different symptom reduction.

# Further, we need to be 99% confident in our conclusions.

import scipy.stats as stats

# Sample data for each drug treatment (reduction in symptoms)
drug_a = [8, 17, 16, 25, 17]
drug_b = [9, 8, 16, 7, 8]
drug_c = [7, 6, 5, 4, 6]

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(drug_a, drug_b, drug_c)

# Print the results
print("One-Way ANOVA results:")
print("F-statistic:", f_statistic)
print("P-value:", p_value)

alpha = 0.01

# Interpret the results of one-way ANOVA
if p_value < alpha:
   print("Reject the null hypothesis")
   print("There is at least one significant difference in symptom reduction among the three drug treatments.")
else:
   print("Fail to reject the null hypothesis")
   print("There are no significant differences in symptom reduction caused by the three drug treatments.")
print()


# Now that we know there is a significant difference among the drug treatments, 
# we need to Perform Pairwise T-Test for each pair of drug treatments 
# (A vs. B, B vs. C, A vs. C), and calculate the t-statistic and p-value for each pair.

# Therefore, we formulate our Hypotheses as:

# H0: There is no significant difference in the mean reduction in symptoms 
# between the two drug treatments.
# Ha: There is a significant difference in the mean reduction in symptoms 
# between the two drug treatments.

# The significance level is set at 0.01

import numpy as np
from scipy.stats import ttest_ind

# Sample data for each drug treatment (reduction in symptoms)
drug_a = [8, 17, 16, 25, 17]
drug_b = [9, 8, 16, 7, 8]
drug_c = [7, 6, 5, 4, 6]

# Perform pairwise t-tests
result_ab = ttest_ind(drug_a, drug_b)
result_bc = ttest_ind(drug_b, drug_c)
result_ac = ttest_ind(drug_a, drug_c)

# Significance level
alpha = 0.01

# Print results
print("Pairwise t-test results:")
print("A vs. B:", result_ab.pvalue," ; Significant" if result_ab.pvalue <= alpha else " ; Not Significant")
print("B vs. C:", result_bc.pvalue," ; Significant" if result_bc.pvalue <= alpha else " ; Not Significant")
print("A vs. C:", result_ac.pvalue," ; Significant" if result_ac.pvalue <= alpha else " ; Not Significant")
print()
###########################################################
###########################################################

'''
The Highway Administration conducts an annual survey on motor vehicles travelling on the 
highway. They publish their findings in Highway Statistics, based on different types of 
vehicles.
Independent simple random samples of cars, buses, and trucks yielded the data on a number 
of thousand miles driven last year.

cars = [19.9, 15.3, 2.2, 6.8, 34.2, 8.3, 12.0, 7.0, 9.5, 1.1]
buses = [1.8, 24.6, 7.2, 37.0, 7.2, 21.2, 6.5, 23.6]
trucks = [13.3, 23.0, 25.4, 15.3, 57.1, 14.5, 26.0]

We want to decide if there is a difference in last year’s mean number of miles driven 
among cars, buses, and trucks.

At a 93% confidence level, does the data provide sufficient evidence to conclude that 
there is a difference in last year’s mean number of miles driven by cars, buses, and trucks?
'''

# Based on the given problem, we define our hypothesis as:

# H0 : Mean no. of miles driven on the highway, by the different vehicle types was same in 
# the last year
# Ha : Mean no. of miles driven on the highway, by the different vehicle types was different 
# in the last year
# Since we are required to conduct an experiment between MULTIPLE groups at the same time,
# we will use ANOVA Test

from scipy.stats import f_oneway

cars = [19.9, 15.3, 2.2, 6.8, 34.2, 8.3, 12.0, 7.0, 9.5, 1.1]
buses = [1.8, 24.6, 7.2, 37.0, 7.2, 21.2, 6.5, 23.6]
trucks = [13.3, 23.0, 25.4, 15.3, 57.1, 14.5, 26.0]

test_statistic, p_value = f_oneway(cars, buses, trucks)
print("p_value:",p_value)

alpha = 0.07
if  p_value < alpha:
    print("Reject H0; Mean no. of miles driven on the highway, by the different vehicle types was different in the last year")
else:
    print("Fail to reject H0; Mean no. of miles driven on the highway, by the different vehicle types was same in the last year")
print()
