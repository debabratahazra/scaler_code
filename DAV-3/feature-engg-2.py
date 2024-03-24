'''
The below data represents the carbon dioxide emission from vehicles in grams/per km. 
There are a few missing values present in the data.

What will be the imputing strategy that we can use?

'''

import numpy as np
from sklearn.impute import SimpleImputer

data=[50,196,221,136,255,None,230,252,267,212,None,359,328,200,500,624,None,236,289,300,366]
data=np.array(data)

# Since there are 3 outliers present in the data, we should use the median as an 
# impute strategy.

# In the presence of outliers, or extreme values, the median is preferred over the mean.
# The reason for this is that the mean can be “dragged” up or down by extreme values,
# but since the median is just the middle value in a distribution, it is not influenced 
# by the outliers.

imputer = SimpleImputer(strategy = "median")

data1= imputer.fit_transform(data.reshape(-1,1))
print(data1)
print()

#######################################################
#######################################################

'''
For a certain array [0, 1, 2, 3, 4, 5, 10], we decided to plot a boxplot as below:

According to the above plot, calculate the upper limit, median, and lower limit, 
such that, a data point would be considered as an outlier if it is out of those limits.
'''

# Draw boxplot:

import matplotlib.pyplot as plt
import numpy as np

data = np.array([0, 1, 2, 3, 4, 5, 10])
plt.boxplot(data, patch_artist=True)
plt.title('Boxplot')
plt.show()

# Ans:

'''
Explanation:

Here, we can observe from the given boxplot that : Q3 = 4.5 and Q1 = 1.5.
Therefore, IQR = Q3 - Q1 = 3

upper limit = Q3+1.5(IQR) = 4.5+1.5(3) = 9

lower limit = Q1- 1.5(IQR) = 1.5 - 1.5(3) = -3

Any observation greater than upper limit and anything lower than lower limit is 
considered to be an outlier.

Median from the boxplot can easily confirmed as 3.
'''

#################################################
##################################################

'''
Data on the number of text messages sent one weekend by girls and boys in school is 
summarized as follows:

Min: 6
Q1: 14
Median: 45
Q3: 90
Max: 160
Mean: 80
Std Dev: 42.4

A Statistics student checking the calculations finds that the message counts for all the 
students were underreported by 5.

If the numbers are corrected, what are the corrected IQR and standard deviation?
'''

# Ans:
'''
Explanation:

Adding the same constant to every value will increase the Min, Q1, Median, Q3, Max, 
and Mean by that constant.

However, measures of variability, including the IQR and the standard deviation, will 
remain unchanged.

If you add a constant to every value, the distance between values does not change.
As a result, all of the measures of variability (range, interquartile range, standard 
deviation, and variance) remain the same.

On the other hand, suppose you multiply every value by a constant. This has the effect 
of multiplying the range, interquartile range (IQR), and standard deviation by that constant.

Thus, IQR = Q3 - Q1 = 90-14 =76
and standard deviation = 42.4
'''

##############################################
##############################################

'''
You are cleaning up a DataFrame that has almost 5000 observations and you notice that 
one of the categorical columns contains 1512 missing values.

What strategy should you apply to deal with these missing values?
'''

# Ans:
'''
Explanation:

Since the column is categorical we can replace it with the most frequent value.
We cannot drop all the rows which will result in loss of information and we might lose 
some important data.
We cannot replace all the values with randomly selected values either. There is no 
sense of doing this.
We cannot drop the entire column that contains missing values as it may result in a 
huge loss of important data.
'''

##########################################
#########################################

'''
The below data represents the Carbon Dioxide emissions from a vehicle.

Image: co2_em.png

There are 11 features and 1 target column. In the independent variables “Make” 
represents 42 unique car companies.

Which feature engineering technique can be applied to this column?

'''

# Ans:
'''
Explanation:


If we do one hot encoding it will increase the cardinality issue and most of the data 
will be sparse data.
We cannot apply feature scaling or feature engineering / transformation as it is not 
a numeric feature.
We can do feature binning by dividing the 42 unique car companies into 4 categories, 
for example, Luxury, Sports, Premium, and General cars.
'''

# Ans: Feature Binning


# print('Initial column:\n', data['Make'].unique())
# data['Make_Type'] = data['Make'].replace(['BUGATTI', 'PORSCHE', 'MASERATI', 'ASTON MARTIN', 'LAMBORGHINI' 'JAGUAR','SRT'], 'Sports')
# data['Make_Type'] = data['Make_Type'].replace(['ALFA ROMEO', 'AUDI', 'BMW', 'BUICK', 'CADILLAC', 'CHRYSLER', 'DODGE', 'GMC','INFINITI', 'JEEP', 'LAND ROVER', 'LEXUS', 'MERCEDES-BENZ','MINI', 'SMART', 'VOLVO'], 'Premium')
# data['Make_Type'] = data['Make_Type'].replace(['ACURA', 'BENTLEY', 'LINCOLN', 'ROLLS-ROYCE', 'GENESIS'], 'Luxury')
# data['Make_Type'] = data['Make_Type'].replace(['CHEVROLET', 'FIAT', 'FORD', 'KIA', 'HONDA', 'HYUNDAI', 'MAZDA', 'MITSUBISHI','NISSAN', 'RAM', 'SCION', 'SUBARU', 'TOYOTA', 'VOLKSWAGEN'], 'General')
# print('Final column:\n', data['Make_Type'].unique())

'''
Output:

Initial column:
array([‘ACURA’, ‘ALFA ROMEO’, ‘ASTON MARTIN’, ‘AUDI’, ‘BENTLEY’, ‘BMW’, ‘BUICK’, ‘CADILLAC’, 
‘CHEVROLET’, ‘CHRYSLER’, ‘DODGE’, ‘FIAT’,’FORD’, ‘GMC’, ‘HONDA’, ‘HYUNDAI’, ‘INFINITI’, 
‘JAGUAR’, ‘JEEP’,’KIA’, ‘LAMBORGHINI’, ‘LAND ROVER’, ‘LEXUS’, ‘LINCOLN’, ‘MASERATI’,’MAZDA’,
‘MERCEDES-BENZ’, ‘MINI’, ‘MITSUBISHI’, ‘NISSAN’,’PORSCHE’, ‘RAM’, ‘ROLLS-ROYCE’, ‘SCION’, 
‘SMART’, ‘SRT’, ‘SUBARU’,’TOYOTA’, ‘VOLKSWAGEN’, ‘VOLVO’, ‘GENESIS’, ‘BUGATTI’],
dtype=object) - These are 42 unique types.

Final column:
array([‘Sports’, ‘Premium’, ‘Luxury’, ‘General’],dtype=object) - These are 4 unique types
'''

###########################################################
#########################################################

'''
What does the following code snippet do?
'''

# from sklearn.impute
# import SimpleImputer
# imp_mean = SimpleImputer( strategy='mean')
# imp_mean.fit(data)
# imputed_train_df = imp_mean.transform(data)

# Ans:
'''
Explanation:

SimpleImputer() replace missing values using a descriptive statistic 
(e.g. mean, median, or most frequent) along each column or using a constant value.

when strategy=’mean’ is passed inside, it calculates the mean of the non-missing 
values in a column and then replaces the missing values within each column separately
'''

###########################################################
###########################################################

'''
Read below statements regarding two data transformation techniques Standardization and Normalization.

A : Normalization forces all features to come down to same range
B : Standardization computes the z-score of all values which makes the feature mean = 0 

Mark statements A and B as True or False.

'''

# Ans:
'''
Explanation:

Statement A: True.
Normalization is a technique that scales the individual features to have the same range.
It brings the values of different features into a comparable range, often between 0 and 1.


Statement B: True
Standardization (or z-score normalization) scales the features in such a way that they have 
a mean of 0 and a standard deviation of 1.
'''

######################################################
######################################################

'''
Imagine a dataset with two features: 'Age' and 'Salary'.

'Age' has a mean of 30 and a standard deviation of 5, while
'Salary' has a mean of 80,000 and a standard deviation of 20,000.
You decide to apply Standard Scaling to both features.

After applying Standard Scaling, what can be said about the transformed 'Age' and 
'Salary' features?
'''

# Ans:
'''
Explanation:
When you apply Standard Scaling (Standardization) using the Standard Scaler, it 
transforms the data in such a way that the resulting features have a mean of 0 and a 
standard deviation of 1.
This is achieved by subtracting the mean of the feature and dividing by its standard 
deviation for each data point.

In this scenario:

‘Age’ will be transformed to have a mean of 0 and a standard deviation of 1.
‘Salary’ will be transformed to have a mean of 0 and a standard deviation of 1.
The process of standardization does not change the unit of measurement; it scales the 
features to be centered around 0 with a standard deviation of 1, making it easier to 
compare and analyze them.
'''

######################################################
######################################################

'''
Consider a dataset with two features: 'Weight' and 'Height’.

'Weight' values range from 50 to 90, and
'Height' values range from 160 to 190.
Data:

Weight = [70, 80, 60, 90, 50],  
Height = [170, 180, 160, 190, 165]
Which scaler should we choose to preprocess these features for our machine-learning model?

A. Min-Max Scaler for 'Weight' and Standard Scaler for 'Height'
B. Standard Scaler for 'Weight' and Min-Max Scaler for 'Height'
C. Min-Max Scaler for both 'Weight' and 'Height'
D. Standard Scaler for both 'Weight' and 'Height'
'''

# Ans:
'''
Explanation:

Standard Scaler standardizes data by subtracting the mean and dividing by the standard 
deviation. This is generally preferred for machine learning models as it:

Makes all features have zero mean and unit variance, which can improve model performance.
Ensures all features contribute equally to the model, regardless of their original units or 
scales.
Min-Max Scaler scales the data to a specific range, typically between 0 and 1. This may be 
useful in certain cases, but it can be problematic for machine learning models because:

It removes information about the spread of the data (variance), which can be important for 
certain models.

It can amplify the effect of outliers.
In this particular case, both ‘Weight’ and ‘Height’ are continuous features with a 
well-defined range.
Therefore, using Standard Scaler ensures that both features are standardized and contribute 
equally to the machine learning model.


A and B are incorrect because:

Applying different scaling methods to different features can lead to inconsistencies in the 
data and potentially harm the performance of the machine learning model.
In this case, there is no specific reason to choose Min-Max Scaler over Standard Scaler for 
either feature.


C is incorrect because:

While Min-Max Scaler can be useful in certain situations, it is not the best approach for 
this specific case as explained above. Standard Scaler is a more general-purpose scaler and 
is preferred for machine-learning models.

D is correct.
'''

########################################################################
########################################################################

'''
What does the following code snippet do?

from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(strategy='most_frequent')
imp_mean.fit(data)
imputed_train_df = imp_mean.transform(data)
'''

# Ans:
'''
Explanation:

SimpleImputer() replace missing values using a descriptive statistic (e.g. mean, median, 
or most frequent) along each column or using a constant value.

when strategy= 'most_frequent' is passed inside, it calculates the mode of the non-missing 
values in a column and then replaces the missing values within each column separately.
'''

####################################################################
####################################################################

'''
A dataset contains exam scores for students, ranging from 40 to 100. However, 
there are a few outliers with scores exceeding 120.

Which method is more suitable for identifying outliers in this scenario?
'''

# Ans:
'''
Explanation:
IQR method: (Can be detected using this method)

This method identifies outliers based on the quartiles of the data.
It is more resistant to outliers than the mean-based methods like Z-score, making it 
better suited for skewed data like exam scores where a few high scores can significantly 
impact the mean.


Z-score method: (can't be detected using the method)

This method identifies outliers based on their standard deviation from the mean.
However, it can be influenced by outliers itself, leading to inaccurate outlier detection 
when the data is skewed.
In this scenario, the presence of a few high scores can inflate the standard deviation, 
potentially masking other outliers or misidentifying valid data points as outliers.
'''

######################################################
#######################################################

'''
Which of the following statements are true about handling categorical values?


a) One-hot encoding is the most effective approach for handling all categorical data.

b) One-hot encoding increases the dimensionality of the data.

c) Target encoding uses the target variable to estimate the value of each category in a 
categorical variable.

d) Label encoding can be useful for features with a large number of categories.

e) No encoding is also sometimes the best option for handling categorical variables.

f) Label encoding assigns arbitrary numerical values to categories in a categorical variable.
'''

# Ans:
'''
Explanation:

The true statements about handling categorical values are:

b) One-hot encoding increases the dimensionality of the data. This is because every category 
in the original variable is represented by a new binary feature in the one-hot encoded data.

c) Target encoding uses the target variable to estimate the value of each category in a 
categorical variable. This is done by calculating the average target value for each category 
and using that value to represent the category.

f) Label encoding assigns arbitrary numerical values to categories in a categorical variable. 
This is done by assigning a unique integer to each category, but the order of the integers does not necessarily reflect the order of the categories.


The incorrect statements are:

a) One-hot encoding is the most effective approach for handling all categorical data.
- This is not true, as other encoding techniques, such as label encoding and target encoding, 
may be more suitable for certain types of categorical data.

d) Label encoding can be useful for features with a large number of categories.
- This is not true because when there are many categories, label encoding can create a 
large number of features, which can increase the dimensionality of the data and make it 
difficult for the model to learn.

e) No encoding is also sometimes the best option for handling categorical variables:
- Not true.
- Encoding is generally necessary for machine learning models to interpret categorical data 
correctly.
'''