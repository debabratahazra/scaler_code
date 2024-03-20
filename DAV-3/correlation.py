# Covariance?

# Ans:
'''
Explanation :

When the values of the data is doubled, the data only scales up 
in the size. And because of this the variance will also change, 
but the relationship between the features will always be the same.

Covariance is not a parameter to define how good the line of best 
fit is, and thus it also cannot tell how close the data points are
to the line of best fit.

Covariance cannot tell if the line of best fit is steep or not steep,
Though it does tell us whether the slope of best fit is positive or 
negative.

If the covariance is compared for the data with the same scales the 
option D holds true. But, when the scale of the same data is changed, 
it is not mandatory that the covariance will have a higher value.
'''

##########################################################
##########################################################

# Rank based on Spearman's rank correlation:
# image: corr_1.png
 
# Ans: C,A,B,D

#####################################################
#####################################################

'''
Child development researchers studying growth patterns of children 
collect data on the height of fathers and sons.

Analyse the correlation between the father's height and their son's 
height using the given data

Father Height = [169.39, 161.91, 159.23, 161.72, 167.52, 152.13, 
169.64, 162.56, 154.92, 158.57, 153.17, 159.56, 153.77, 168.02, 
157.75, 157.42, 160.65, 160.09, 151.4, 151.05, 136.94, 163.56, 
160.39, 146.92, 171.66, 150.48, 158.12, 157.83, 163.99, 164.95]  

Son Height = [187.35, 177.8, 181.85, 190.69, 188.07, 168.16, 181.65, 
173.94, 174.28, 177.87, 176.01, 185.18, 180.33, 175.85, 178.11, 
177.34, 185.46, 173.56, 177.19, 169.02, 157.13, 179.58, 181.05, 
169.8, 190.89, 164.82, 175.32, 173.69, 185.73, 185.29]
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
Father_Height = [169.39, 161.91, 159.23, 161.72, 167.52, 152.13, 169.64, 162.56, 154.92, 158.57, 153.17, 159.56, 153.77, 168.02, 157.75, 157.42, 160.65, 160.09, 151.4, 151.05, 136.94, 163.56, 160.39, 146.92, 171.66, 150.48, 158.12, 157.83, 163.99, 164.95]
Son_Height = [187.35, 177.8, 181.85, 190.69, 188.07, 168.16, 181.65, 173.94, 174.28, 177.87, 176.01, 185.18, 180.33, 175.85, 178.11, 177.34, 185.46, 173.56, 177.19, 169.02, 157.13, 179.58, 181.05, 169.8, 190.89, 164.82, 175.32, 173.69, 185.73, 185.29]

data = {'Father Height': Father_Height, 'Son Height': Son_Height}

# Create the DataFrame
df = pd.DataFrame(data)
print(df.corr())

# Plot father heights vs. son heights

plt.figure(figsize=(6,4))
plt.scatter(Father_Height,Son_Height, color='b')
plt.title("Father Heights vs. Son Heights")
plt.xlabel("Father Height (cm)")
plt.ylabel("Son Height (cm)")
plt.grid(True)
plt.show()

''' Conclusion:
Positive correlation means if one variable increases, then the other increases as well.
- Now, if the father is tall then it's highly likely the son is also tall. i.e. there's 
some positive correlation between them.

Negative correlation means if one variable increases, the other decreases.
- In terms of father-son height, it means if the father is tall then the son 
would be short; which is quite rare or outlier.

We already know that correlation coef. ranges from -1 to 1. Hence it can't be greater than 1.
''' 

########################################################################
##########################################################################

'''
Suppose we have mRNA data with features as Gene ‘X’ and Gene ‘Y’. You get 
to know that there is a correlation between these features. Based on the 
correlation type, what conclusion can you make?

Image: genere-corr.png
'''
# Ans:
'''
Explanation :

If there is a positive correlation, then based on the trend one can assume/deduce that 
if the value of one feature is high, then the other also will be high-valued.

Negative correlation describes when two variables tend to move in the opposite 
direction from one another, such that when one increases the other variable decreases.

If there is no correlation between two features, one cannot assume/deduce anything as 
the points will be scattered all over the plot and will follow no 
trend(positive or negative).
'''
######################################################################
#######################################################################

'''
A researcher is analyzing the relationship between the number of hours students spend 
studying and their exam scores. He collects data from 10 students:

study_hours = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55])  
exam_scores = np.array([60, 65, 70, 75, 80, 85, 90, 95, 100, 105])

Calculate the Pearson correlation coefficient between these variables.

'''

import seaborn as sns

study_hours = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
exam_scores = np.array([60, 65, 70, 75, 80, 85, 90, 95, 100, 105])

plt.title("Study hours vs. Exam score")
plt.xlabel("Study hour")
plt.ylabel("Exam score")
plt.grid(True)
sns.scatterplot(x=study_hours, y=exam_scores)
plt.show()

# Hence, Pearson Correlation is applicable. There are two approaches to 
# calculating the Pearson correlation.




# Approach 1 Code: Using the scipy built-in function

import numpy as np
from scipy.stats import pearsonr

study_hours = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
exam_scores = np.array([60, 65, 70, 75, 80, 85, 90, 95, 100, 105])

corr, pval = pearsonr(study_hours, exam_scores)

print("Pearson Correlation Coefficient: ", corr)
print()



# Approach 2 Code: Calculating correlation from scratch

import numpy as np

study_hours = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
exam_scores = np.array([60, 65, 70, 75, 80, 85, 90, 95, 100, 105])

# Calculate mean of these variables
mean_study_hours = np.mean(study_hours)
mean_exam_scores = np.mean(exam_scores)

# Calculate the numerator and denominators for Pearson correlation
numerator = np.sum((study_hours - mean_study_hours) * (exam_scores - mean_exam_scores))
denominator_x = np.sqrt(np.sum((study_hours - mean_study_hours)**2))
denominator_y = np.sqrt(np.sum((exam_scores - mean_exam_scores)**2))

# Calculate Pearson correlation coefficient
correlation_coefficient = numerator / (denominator_x * denominator_y)

print("correlation coefficient:", correlation_coefficient)
print()

####################################################################
####################################################################

'''
Compute the pearson and spearman correlation between two variables a and b .

a = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]

b = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
'''

# Ans:
''' Explanation:
We can find the Pearson and Spearman correlation using pearsonr() and spearmanr() 
functions of scipy.stats
'''
import numpy as np
from scipy.stats import pearsonr, spearmanr

a = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
b = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

print(pearsonr(a,b))
print(spearmanr(a,b))
print()

######################################################################
######################################################################

'''
A biologist is studying the relationship between the height of plants and the amount 
of sunlight they receive.

The biologist collects data from 8 different plants, measuring their heights 
(in centimeters) and ranking them based on the amount of sunlight they receive.


plant_heights = np.array([15, 20, 25, 18, 22, 30, 28, 35])

sunlight_rankings = np.array([4, 7, 3, 6, 5, 8, 2, 1])

Calculate the Spearman correlation between these variables.
'''

# Ans:

# Explanation:
# We can use the spearmanr() function of scipy.stats to calculate the Spearman 
# Correlation coefficient.


import numpy as np
from scipy.stats import spearmanr

plant_heights = np.array([15, 20, 25, 18, 22, 30, 28, 35])
sunlight_rankings = np.array([4, 7, 3, 6, 5, 8, 2, 1])

corr, pval = spearmanr(plant_heights, sunlight_rankings)

print("Spearman Correlation Coefficient: ", corr)
print()


#########################################################################################
########################################################################################
'''
Pearson Correlation Coefficient and Spearman Rank Correlation Coefficient
'''

# Ans:
'''
Explanation :

Pearson test tells us the about the slope of the line of best fit. Other than that, 
Pearson gives a measure of the strength of linear association between two variables 
whereas Spearman gives a measure of the strength of monotonicity between two variables,

Pearson coefficient is calculated from the raw value of data points whereas Spearman 
depends on the rank. It assesses how well the relationship between two variables can
be described using a monotonic function.

Both techniques cannot be used with nominal (unranked) data as the data must be 
ordinal (ranked) in Spearman.

The Spearman test does not tell us about the slope of the line of best fit, it 
tells us how closely our data fit on a line, so two datasets with the same 
correlation coefficient can have very different slopes.
'''