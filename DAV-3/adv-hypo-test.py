'''
A researcher is interested in determining the effects of different dosages of a 
dietary supplement on the performance of both males and females on a physical 
endurance test.

The three different dosages of the medicine are low, medium, and high, and the genders 
are male and female.

Sample data:

Dietary,Supplement_Dosage,Test_values
Female,Low,35.6
Female,Medium,49.4
Female,High,55.2
Male,Low,92.2
Male,Medium,45.4
Male,High,70.8
Female,Low,56.9
Female,Medium,87.0
Female,High,23.4
Male,Low,45.9
Male,Medium,34.2
Male,High,98.9


Conduct an appropriate hypothesis test to determine the interaction effects of the 
test at a 1% significance level.

'''

# Ans:
'''
Based on the given problem,
we need to analyzes the independent effects of two categorical variables 
(dosage & gender) on a continuous variable (performance test values) while considering 
their potential interaction. Hence, we perform Two-way ANOVA to test the effects of 
the test.

We define our hypothesis as:


Null Hypothesis (H0):

There is no significant difference in average performance scores among different 
dietary supplement dosages.
There is no significant difference in average performance scores between male and 
female participants.
There is no significant interaction effect between dietary supplement dosage and 
gender on average performance scores.


Alternative Hypothesis (H1):

There is a significant difference in average performance scores among different 
dietary supplement dosages.
There is a significant difference in average performance scores between male and 
female participants.
There is a significant interaction effect between dietary supplement dosage and 
gender on average performance scores.

We can do this using the following code:
'''

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

link = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/059/215/original/dosages.csv?1702370732"

df = pd.read_csv(link)

# fit an ols model on the data frame
# use 'fit()' to fit the linear model
# ols('dependent variable ~ C(independent variable1) * C(independent variable2)', data=df).fit()
test = ols('Test_values ~ C(Dietary) * C(Supplement_Dosage)', data=df).fit()

# create a table for a 2-way ANOVA test
# Pass the linear model 'test'
# 'typ = 2' performs two-way ANOVA
anova_table = sm.stats.anova_lm(test, typ = 2)

# Display the results
print(anova_table)
print()

'''
The results of the Two-way ANOVA test indicate the following:

Dietary (Gender):
The p-value is 0.339742, which is greater than the significance level of 0.01.
Therefore, we fail to reject the null hypothesis for the effect of gender on average 
performance, suggesting that there is no significant difference in average performance 
between males and females.

Supplement Dosage:
The p-value is 0.878657, exceeding the significance level.
Thus, we fail to reject the null hypothesis related to the effect of supplement 
dosage on average performance.
This implies that there is no significant difference in average performance among 
different dosages of the dietary supplement.

Interaction between Dietary and Supplement Dosage:
The p-value is 0.131502, which is greater than 0.01.
Consequently, we fail to reject the null hypothesis for the interaction effect 
between gender and supplement dosage.
This suggests that the combined effect of gender and supplement dosage does not 
significantly impact average performance.

Conclusion:
Based on these results, we do not have enough evidence to conclude that there is no 
significant difference in average performance on the physical endurance test based on 
gender, supplement dosage, or interaction.
'''

###################################################################
###################################################################

'''
A researcher wants to investigate the effects of two different fertilizers 
(‘A’ & ‘B’) and three watering frequencies (‘Low’, ‘Medium’, ‘High’) on the growth 
of tomato plants.

Is there a significant interaction between the fertilizer type and watering frequency 
on plant growth?

Dataset:

Fertilizer,Watering_Frequency,Plant_Height
A,Low,15.2
A,Medium,20.7
A,High,24.3
B,Low,18.4
B,Medium,23.1
B,High,26.5
A,Low,32.7
A,Medium,21.7
A,High,27.3
B,Low,38.4
B,Medium,33.1
B,High,36.5
A,Low,12.2
A,Medium,22.7
A,High,35.3
B,Low,28.4
B,Medium,22.1
B,High,24.5

Conduct an appropriate hypothesis test to determine only the interaction effects 
of this research at a 5% significance level.

'''


# Ans:
'''
Based on the given problem,
we need to analyse the independent effects of two categorical variables 
(fertilizer types & watering frequencies) on a continuous variable (plant height)
while considering their potential interaction. Hence, we perform Two-way ANOVA to 
test the effects of the test.

We define our hypothesis as:


Null Hypothesis (H0):

There is no significant difference in average plant height among different fertilizer types.
There is no significant difference in average plant height across different watering 
frequencies.
There is no significant interaction effect between fertilizer type and watering frequency 
on average plant height.


Alternative Hypothesis (H1):

There is a significant difference in average plant height among different fertilizer types.
There is a significant difference in average plant height across different watering 
frequencies.
There is a significant interaction effect between fertilizer type and watering frequency 
on average plant height.

We can solve this, using the following code.
'''

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

link = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/059/216/original/Fertilizer.csv?1702370971"
df= pd.read_csv(link)

# Fit the linear model
model = ols('Plant_Height ~ C(Fertilizer) * C(Watering_Frequency)', data=df).fit()

# Perform two-way ANOVA
anova_table = sm.stats.anova_lm(model, typ=2)

# Print the ANOVA table
print(anova_table)
print()

'''
Fertilizer Type (H0 vs. H1):

F-statistic = 1.509060
p-value = 0.242831
Since the p-value is greater than 0.05 (significance level), we fail to reject the null 
hypothesis (H0).
Therefore, there is no statistically significant difference in average plant height among 
different fertilizer types.


Watering Frequency (H0 vs. H1):

F-statistic = 0.903226
p-value = 0.431117
Similar to the fertilizer type analysis, the p-value is greater than 0.05, leading us 
to fail to reject the null hypothesis (H0).
This means there is no statistically significant difference in average plant height 
across different watering frequencies.


Interaction (H0 vs. H1):

F-statistic = 0.449075
p-value = 0.648519
Again, the p-value exceeding 0.05 allows us to fail to reject the null hypothesis (H0).
This implies that the effect of fertilizer type on plant growth does not differ 
significantly across different watering frequencies.


Conclusion:

There is no statistically significant evidence to suggest that fertilizer type, 
watering frequency, or their interaction have a significant impact on plant growth.
Or,
There is no significant difference in plant growth across different watering frequencies.
'''

##################################################################
##################################################################

'''
The Committee head of a national entrance exam wants to 
analyze if there are any differences in learning outcomes between students 
with different educational backgrounds (high school or college) and teaching 
methods (traditional or interactive) on test scores.

Dataset:

Education,Teaching_Method,Test_Score
High School,Traditional,72
High School,Interactive,85
College,Traditional,70
College,Interactive,92
High School,Traditional,74
High School,Interactive,97
College,Traditional,76
College,Interactive,94
High School,Traditional,86
High School,Interactive,90
College,Traditional,69
College,Interactive,78
High School,Traditional,82
High School,Interactive,93
College,Traditional,98
College,Interactive,92


Conduct an appropriate hypothesis test to determine the main effects & interaction 
effects of the test at a 5% significance level.

'''

# Ans:

'''
Based on the given problem,
we need to analyse the independent effects of two categorical variables 
(educational backgrounds & teaching methods) on a continuous variable (test scores) 
while considering their potential interaction. Hence, we perform Two-way ANOVA to 
test the effects of the test.

Based on the setup, we can define our hypotheses as:


Null Hypothesis (H0):

There is no significant difference in average test scores between students from 
different educational backgrounds.
There is no significant difference in average test scores across teaching methods.
There is no significant interaction effect between educational background and teaching 
method on average test scores.


Alternative Hypothesis (H1):

There is a significant difference in average test scores between students from 
different educational backgrounds.
There is a significant difference in average test scores across different teaching methods.
There is a significant interaction effect between educational background and teaching 
method on average test scores.

We can use the following code, to solve the problem.
'''
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

link = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/059/218/original/Teaching_Method.csv?1702373208"
df= pd.read_csv(link)

# Fit the linear model
model = ols('Test_Score ~ C(Education) * C(Teaching_Method)', data=df).fit()

# Perform two-way ANOVA
anova_table = sm.stats.anova_lm(model, typ=2)

# Print the ANOVA table
print(anova_table)
print()

'''
Based on the ANOVA table, we can analyze the effects of educational background, 
teaching method, and their interaction on student test scores:


Educational Background (H0 vs. H1):

F-statistic = 0.081477
p-value = 0.780172
Since the p-value is greater than 0.05 (significance level), we fail to reject the 
null hypothesis (H0).
Therefore, there is no statistically significant difference in average test scores
between students with different educational backgrounds.


Teaching Method (H0 vs. H1):

F-statistic = 7.199348
p-value = 0.019920
The p-value is less than 0.05, leading us to reject the null hypothesis (H0).
This suggests a statistically significant difference in average test scores across 
teaching methods.


Interaction (H0 vs. H1):

F-statistic = 0.052146
p-value = 0.823216
With a p-value above 0.05, we fail to reject the null hypothesis (H0).
This means the effect of educational background on test scores does not 
significantly differ across different teaching methods.


Conclusion:
The analysis indicates that the teaching method significantly impacts student test scores, 
while educational background does not significantly influence them.
However, no significant interaction exists between educational background and teaching 
method on student performance.
'''

###################################################################
####################################################################

'''
An online shopping platform is testing two different delivery methods to improve the 
delivery times for their customers.

The data below represents the delivery times (in hours) for a sample of orders using 
Method A and Method B.

delivery_method_A = [2.5, 3.2, 2.8, 3.5, 3.0, 2.7, 2.9, 3.1, 2.6, 3.3]

delivery_method_B = [3.8, 3.2, 3.5, 3.1, 3.9, 3.0, 3.3, 3.6, 3.4, 3.7]

Using an appropriate test, determine if there is a significant difference in the delivery 
time distributions between Method A and Method B. Use a significance level of 0.05.
'''

# Ans:
'''
Based on the given problem, we define our hypotheses as:

Null Hypothesis (H0): The samples are drawn from the same distribution.
Alternative Hypothesis (H1): The samples are not drawn from the same distribution.
In other words:

H0: The delivery time distributions for Method A and Method B are the same.
H1: The delivery time distributions for Method A and Method B are different.

To solve this problem, we will have to use KS Test, since we do not have any 
information about the underlying distribution of delivery time data.
'''
from scipy import stats

# Given data
delivery_method_A = [2.5, 3.2, 2.8, 3.5, 3.0, 2.7, 2.9, 3.1, 2.6, 3.3]
delivery_method_B = [3.8, 3.2, 3.5, 3.1, 3.9, 3.0, 3.3, 3.6, 3.4, 3.7]

# Perform the KS test
ks_statistic, p_value = stats.kstest(delivery_method_A, delivery_method_B)

# Significance level
alpha = 0.05

# Print the results
print("KS Statistic:", ks_statistic)
print("P-value:", p_value)

# Check if the p-value is less than alpha
if p_value < alpha:
   print("Reject the null hypothesis. There is a significant difference in the delivery time distributions between Method A and Method B.")
else:
   print("Fail to reject the null hypothesis. There is no significant difference in the delivery time distributions between Method A and Method B.")
print()

###############################################################
##############################################################

'''
A researcher is investigating the distribution of response times (in seconds) for two 
different versions of a mobile app, i.e. the time taken for a mobile app to respond to 
a user action, measured in seconds.


The goal is to determine if the response time distributions significantly differ between 
the two versions.

Data for 20 users for each app version is collected.

response_times_version_A = [1.2, 1.3, 1.1, 1.4, 1.2, 1.3, 1.0, 1.5, 1.2, 1.3, 1.2, 1.4, 
1.1, 1.3, 1.2, 1.5, 1.3, 1.4, 1.2, 1.3]

response_times_version_B = [1.6, 1.2, 1.3, 1.4, 1.1, 1.3, 1.2, 1.5, 1.3, 1.4, 1.2, 1.3, 
1.2, 1.4, 1.1, 1.3, 1.5, 1.2, 1.3, 1.4]

'''
# Ans: KS Test

'''
Explanation:

One-Way ANOVA:
This test is used for comparing the means of more than two groups.
In this scenario, we only have two groups (app versions A and B), making ANOVA 
inappropriate.


Two-Sample Z-test:
This test requires the assumption of normality in the population distributions.
Since we have no information about the underlying distribution of response times, this 
assumption cannot be verified, making the two-sample z-test a not appropriate choice.


Paired T-Test:
This test is designed for situations where the same subjects are measured under two 
different conditions.
Here, we have different users for each app version, violating the paired assumption.


Two-Sample Z-proportion:
This test is specifically designed for comparing proportions, not continuous variables 
like response times.


KS Test (Kolmogorov-Smirnov Test):
This test is ideal for comparing the cumulative distribution functions (CDFs) of two samples.

KS test is the most appropriate choice for this scenario because it doesn’t require any 
assumptions about the underlying distributions and can accurately detect potential 
differences in the locations and shapes of the response time distributions for the 
two mobile app versions.
'''

####################################################################
######################################################################

'''
A data analyst is comparing the sales amounts (in dollars) for two different 
marketing strategies (A and B). The sales data for 20 days under each strategy 
is collected.


sales_strategy_A = [156, 153, 157, 154, 156, 159, 152, 156, 157, 154, 153, 157, 157,152, 
155, 154, 151, 157, 155, 151]

sales_strategy_B = [135, 147, 126, 136, 158, 139, 163, 141, 156, 142, 130, 129, 161, 158, 
117, 151, 121, 135, 123, 153]

Perform an appropriate test to assess if there is a significant difference in the sales 
distributions between Strategy A and Strategy B. Use a significance level of 0.05.
'''

# Based on the given question, we define our hypothesis as:

# Null Hypothesis (H0): The distributions of sales amounts for Strategy A and Strategy B 
# are identical.
# Alternative Hypothesis (H1): The distributions of sales amounts for Strategy A and 
# Strategy B are not identical.
# We can solve this problem using KS Test as we do not have information about the 
# underlying distribution of sales data.

from scipy.stats import kstest


# Given data
sales_strategy_A = [156, 153, 157, 154, 156, 159, 152, 156, 157, 154, 153, 157, 157,152, 155, 154, 151, 157, 155, 151]
sales_strategy_B = [135, 147, 126, 136, 158, 139, 163, 141, 156, 142, 130, 129, 161, 158, 117, 151, 121, 135, 123, 153]

# Perform KS test
statistic, p_value = kstest(sales_strategy_A, sales_strategy_B)

# Significance level
alpha = 0.05

# Print the results
print("KS Statistic:", statistic)
print("P-value:", p_value)

# Check if the p-value is less than alpha
if p_value < alpha:
   print("Reject the null hypothesis. There is a significant difference in the sales distributions between Strategy A and Strategy B.")
else:
   print("Fail to reject the null hypothesis. There is no significant difference in the sales distributions between Strategy A and Strategy B.")
print()

#######################################################################
#######################################################################

'''
A bank is launching two different approaches (A and B) to encourage customers to adopt 
its new mobile banking app. The bank randomly assigns a group of customers to each 
approach and monitors their adoption rates over a month.

Data:

Group A (Approach A): [38, 40, 42, 37, 39, 41, 36, 35, 43, 38]  
Group B (Approach B): [48, 45, 46, 43, 50, 44, 49, 47, 42, 46] 
Objective:

Assess whether the new incentive program in Approach B leads to a statistically 
significant improvement in the adoption rates compared to Approach A.
'''

# The bank is conducting A/B testing to evaluate two different approaches (A and B) 
# aimed at encouraging customers to adopt its new mobile banking app.
# A/B Testing Process:

# The bank collects adoption rate data from a random group of customers for both 
# Approach A and Approach B.
# A two-sample t-test is performed to compare the means of the adoption rates 
# between the two groups.
# The t-statistic and p-value are calculated.

import scipy.stats as stats

# Null Hypothesis (H0): μA ≥ μB (There is no significant improvement in the adoption rates for Approach B compared to Approach A).
# Alternative Hypothesis (H1): μA < μB (There is a significant improvement in the adoption rates for Approach B compared to Approach A).

# Data
group_A = [38, 40, 42, 37, 39, 41, 36, 35, 43, 38]
group_B = [48, 45, 46, 43, 50, 44, 49, 47, 42, 46]

# Two-sample t-test
t_statistic, p_value = stats.ttest_ind(group_A, group_B, alternative = 'less')

# Print results
print("T-statistic:", t_statistic)
print("P-value:", p_value)

# Interpret results
alpha = 0.05

if p_value < alpha:
   print("Reject the null hypothesis. There is a significant improvement in the adoption rates for Approach B compared to Approach A")
else:
   print("Fail to reject the null hypothesis. There is no significant improvement in the adoption rates for Approach B compared to Approach A")
print()

###################################################################
###################################################################
# A/B Testing:

'''
A) A coffee shop considering two different promotional strategies 
(Strategy A and Strategy B) to boost sales during the morning hours is a scenario 
suitable for A/B testing. In A/B testing, the coffee shop can randomly assign 
customers to either Strategy A or Strategy B and measure the impact on sales. 
This helps in determining which strategy leads to a higher increase in sales.

B) A university conducting a survey to assess the effectiveness of two teaching 
methods (Method A and Method B) in improving student performance in mathematics 
is also suitable for A/B testing. The university can randomly assign students to 
either Method A or Method B, assess their performance, and determine if one 
teaching method is more successful than the other.

C) The scenario with the nutritionist comparing average weight loss among three 
different diet plans involves more than two groups (Low-Carb, Mediterranean, and Vegan). 
While it is a suitable scenario for ANOVA (Analysis of Variance), A/B testing is 
typically designed for comparing two variations.

D) The manufacturing company studying the effects of two factors (Temperature and Humidity)
on material strength involves more than two variations (different combinations of 
temperature and humidity). Similar to option C, this scenario is better suited for 
ANOVA or factorial experiments, as it involves more than two variations.


In A/B testing, the focus is on comparing two variations to determine which one 
performs better in achieving a specific goal or outcome.
'''

#################################################################
##################################################################

'''
Suppose you conducted an experiment to investigate the impact of two different 
advertising strategies (A and B) on the click-through rates of a website.

After running the experiment, you found that the click-through count for Strategy 
A was 150, and for Strategy B, it was 200.

Perform a hypothesis test to determine if the difference in click-through rates 
between Strategy A and Strategy B is statistically significant. Use a significance 
level of 0.05. Assume 1000 users were exposed to each strategy.
'''

# Ans:
''' Explanation:

You need to conduct an A/B test to evaluate two different advertising approaches (A and B) 
aimed at increasing click through rates for a website.

A/B Testing Process:

You have collected data about the click through rates, from a random group of customers 
for both Approach A and Approach B.

A Two-Sample Proportion Z-test is performed.
The resultant z-statistic and p-value are calculated.

Null Hypothesis (H0): There is no difference in the click-through rates between advertising 
strategies A and B.
- In other words, the population proportions of clicks for both strategies are equal.

Alternative Hypothesis (H1): There is a significant difference in the click-through rates 
between advertising strategies A and B.
- In other words, the population proportions of clicks for both strategies are not equal.
'''

import statsmodels.api as sm
import numpy as np

# Number of users exposed to each strategy
n_A = n_B = 1000

# Number of users who clicked through for each strategy
clicks_A = 150
clicks_B = 200

# Proportions for each strategy
prop_A = clicks_A / n_A
prop_B = clicks_B / n_B

# Perform two-sample proportion z-test
z_stat, p_value = sm.stats.proportions_ztest([clicks_A, clicks_B], [n_A, n_B], alternative='two-sided')

# Print the results
print(f"Z-statistic: {z_stat}")
print(f"P-value: {p_value}")

# Interpret the results
alpha = 0.05
if p_value < alpha:
   print("Reject the null hypothesis. There is a significant difference in click-through rates between Strategy A and Strategy B.")
else:
   print("Fail to reject the null hypothesis. There is no significant difference in click-through rates between Strategy A and Strategy B.")
print()

#########################################################################
########################################################################

'''
A coffee shop wants to understand the relationship between the age group 
('20-30','31-40', '41-50') and their preferred coffee type 
(Light Roast, Medium Roast, Dark Roast) based on data collected from a local Coffee Barista.

Age_Group,Coffee_Type,Number_of_Orders
20-30,Light Roast,45
20-30,Medium Roast,60
20-30,Dark Roast,30
31-40,Light Roast,35
31-40,Medium Roast,40
31-40,Dark Roast,55
41-50,Light Roast,45
41-50,Medium Roast,50
41-50,Dark Roast,65
20-30,Light Roast,35
20-30,Medium Roast,49
20-30,Dark Roast,39
31-40,Light Roast,37
31-40,Medium Roast,30
31-40,Dark Roast,32
41-50,Light Roast,49
41-50,Medium Roast,58
41-50,Dark Roast,51


Do age groups and coffee types interact to influence the number of orders?

Conduct an appropriate hypothesis test to determine the interaction effects of 
the relationship at a 5% significance level.
'''

# Ans:
''' Explanation:
Based on the given problem,
we need to analyse the independent effects of two categorical variables 
(coffee types & age groups) on a continuous variable (number of orders) while 
considering their potential interaction. Hence, we perform Two-way ANOVA to test 
the effects of the test.

Based on the given problem, we define our hypotheses as:


Null Hypothesis (H0):

There is no significant difference in the number of orders across different coffee types.
There is no significant difference in the number of orders across different age groups.
There is no significant interaction effect between age group and coffee type on the number 
of orders.


Alternative Hypothesis (H1):

There is a significant difference in the number of orders across different coffee types.
There is a significant difference in the number of orders across different age groups.
There is a significant interaction effect between age group and coffee type on the number 
of orders.
'''

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

link = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/059/220/original/coffee.csv?1702374099"
df= pd.read_csv(link)

# Fit the linear model
model = ols('Number_of_Orders ~ C(Age_Group) * C(Coffee_Type)', data=df).fit()

# Perform two-way ANOVA
anova_table = sm.stats.anova_lm(model, typ=2)

# Print the ANOVA table
print(anova_table)

'''
Based on the ANOVA table, we can analyze the effects of age group, coffee type, and their 
interaction on the number of orders placed at the coffee shop:
Age Group (H0 vs. H1):

F-statistic = 5.104046
p-value = 0.032992
Since the p-value is less than 0.05 (significance level), we reject the null hypothesis (H0).
This indicates a statistically significant difference in the number of orders across 
different age groups.


Coffee Type (H0 vs. H1):

F-statistic = 1.066061
p-value = 0.384141
As the p-value is greater than 0.05, we fail to reject the null hypothesis (H0).
This suggests no statistically significant difference in the number of orders across 
different coffee types.


Interaction (H0 vs. H1):

F-statistic = 1.835260
p-value = 0.206332
With a p-value exceeding 0.05, we fail to reject the null hypothesis (H0).
This implies that the effect of age group on the number of orders does not 
significantly differ across different coffee types.


Conclusion:
The analysis reveals a statistically significant difference in the number of orders 
across different age groups.
This indicates that age plays a role in coffee preferences and ordering behavior.
However, the coffee type does not exhibit a significant difference in the number of 
orders, suggesting that overall preferences might not be heavily influenced by coffee 
type alone.

There is no significant interaction effect exists between age group and coffee type, 
meaning that the effect of age on order numbers does not vary significantly across 
different coffee types.
'''