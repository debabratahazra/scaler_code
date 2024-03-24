'''
The loan.csv: https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/018/746/original/loan.csv?1666170299
data shows that graduate unmarried men are in a different income group 
than both married and unmarried graduate women.

To prove this, would a t-test be more appropriate or a chi-square test?

Carry out the test on the 'ApplicantIncome' column for the two groups and report the 
p-value. Also report your interpretation.

Note: Assume a confidence level of 95% and round off the p-value to 2 decimal places.
'''

# Ans:
'''Explanation:

We will perform a t-test since the incomes are a continuous variable.

Nulll hypothesis (H0) : The incomes of both groups are similar.
Alternate hypothesis (Ha) : The incomes of both groups are different.
'''

import pandas as pd
from scipy.stats import ttest_ind

# Load the data
link = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/018/746/original/loan.csv?1666170299"
data = pd.read_csv(link)

# Load the Income data for graduate unmarried men
unmarried_graduate_men = data[(data["Gender"] == "Male") & (data["Married"] == "No") & (data["Education"] == "Graduate")]["ApplicantIncome"]
unmarried_graduate_men = unmarried_graduate_men.dropna()
print("Number of unmarried graduate men datapoints: ", len(unmarried_graduate_men))

# Load the data for graduate women
graduate_women = data[(data["Gender"] == "Female") & (data["Education"] == "Graduate")]["ApplicantIncome"]
graduate_women = graduate_women.dropna()
print("Number of graduate women datapoints: ", len(graduate_women))

# Perform a t-test since the incomes are a continuous variable.
p_value = ttest_ind(unmarried_graduate_men, graduate_women)[1]
print("p_value :" ,round(p_value,2))

if p_value > 0.05:
 print('Since p_value > 0.05 we fail to reject the null hypothesis.')
 print("implying that the incomes are similar")
else:
 print('Since p_value < 0.05 we reject the null hypothesis.')
 print("implying that the incomes are different")
print()

#########################################################
#########################################################

# Notes:
'''
Box plot for continuous variable
Bar plot for categorical variable
Histogram for continuous variable
Q-Q plot specifically for outliers in Continuous variable.
'''

# Sample of Q-Q Plot:
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Generate random data from a normal distribution
np.random.seed(0)  # Set seed for reproducibility
data = np.random.normal(loc=0, scale=1, size=1000)

# Create a Q-Q plot
stats.probplot(data, dist="norm", plot=plt)
plt.title('Q-Q plot of the data')
plt.xlabel('Theoretical quantiles')
plt.ylabel('Sample quantiles')
plt.show()

############################################################
#############################################################

'''
Data distributions can be named based on the kurtosis value. Specifically, for given 
kurtosis k :

If k = 3, it is called a Mesokurtic distribution and has kurtosis statistics 
similar to a normal distribution.

For k > 3, it is called a Leptokurtic distribution (has a profound number of outliers)

And for k < 3, it is called a Platykurtic distribution (shows lack of outliers).

Based on this information, given a data sample [4, 6, 2, 18, 7, 2], 
what would be this kind of distribution called?
'''
# Explanation :
# In order to determine kurtosis, we can plot the data for a better understanding.

import pandas as pd
import seaborn as sns

data = pd.Series([4, 6, 2, 18, 7, 2])

sns.histplot(data, kde=True)
plt.show()

'''
This plot is not enough to help us determine which distribution is followed, 
as the data size is very small.

We can however, utilise the pd.kurt() function, to get a value of kurtosis in 
this data.
'''

import pandas as pd

data = pd.Series([4, 6, 2, 18, 7, 2])
print("Value of kurtosis:", data.kurt())
print()

# Note: Since this is greater than 3, we conclude that the data follows 
# Leptokurtic distribution.
###################################################
#####################################################

'''
The following list contains data about the age of visitors, in a mall.

data=[38,36,31,30,20,28,25,26,19,21,19,21,20,21,21,20,21,24,32,35,38,38]

Based on the given data, decide the distribution of data.
'''

# Ans:
'''
Approach 1:

For a negatively skewed distribution, mean<median<mode
For distribution with no skewness(Normal), mean=median=mode
For a positively skewed distribution, mean>median>mode

Code to print the mean, median and mode are:
'''

import numpy as np
data=np.array([38,36,31,30,20,28,25,26,19,21,19,21,20,21,21,20,21,24,32,35,38,38])
mean = data.mean()
median = np.median(data)

#there is no direct method to determine the mode.
vals,counts = np.unique(data, return_counts=True)
index = np.argmax(counts)
mode = vals[index]

print(f"mean:",mean,"\nmedian:",median,"\nmode:",mode)
print()

# Note: we can clearly observe that mean > median > mode, which is a 
# case of right-skewed distribution.

'''
Approach 2:

To plot the distribution of given data, we can use the following python code:
'''

import seaborn as sns
import matplotlib.pyplot as plt
sns.histplot(data, kde=True)
# sns.kdeplot(data, shade=True)
# sns.distplot(a=data)
plt.show()

# Note: We can clearly observe from the above density plot that the distribution
# is rightly skewed.

#############################################################
#############################################################

''' Note:
Kurtosis gives us the measure of tailedness and outliers in the distribution of the data. 
It does not give us the measure of the peak.

The Q-Q plot between the log-normal distribution and normal distribution won’t 
be a straight line. For getting a straight line we will first have to take the 
log of each value in the log-normal distribution and then the Q-Q plot of 
these logarithmically transformed values from the log-normal distribution and 
normal distribution will be a straight line.

For a data distribution like the one in the picture shown below also we can get a 
good Spearman correlation score but with that, we cannot assume that the relationship 
between the data is linear.
'''

##############################################################
###############################################################

'''
We have been given a dataset containing the details of the people applied for loan.

dataset: loan.csv : https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/018/746/original/loan.csv?1666170299

We wish to create a new feature called 'NewFeature' using a linear combination of the 
features ApplicantIncome, LoanAmount and Credit_History, with weights 1, 3 and 7000,

i.e., data['NewFeature'] = (data["ApplicantIncome"]) + (3 * data["LoanAmount"]) + 
(7000 * data["Credit_History"]).

Since 'NewFeature' is a numerical feature, convert it to a categorical feature by 
checking whether 'NewFeature' is greater than 0.25 times the mean of 'NewFeature'.
Call this feature 'Separator'.

Perform a chi-square test on the contingency table formed by the features 'Loan_Status' 
and 'Separator' and report the p-value. Also report your interpretation.

Note: Drop all the rows having 'na' values before performing any operation on the 
data and assume the significance level to be 5%. Also, round off the p-value to 
four decimal places.
'''

# Explanation:
# Based on the given question, we define our hypothesis as:

# H0: The features Separator and Loan_Status are independent.
# Ha: The features Separator and Loan_Status are dependent on each other.
# We can perform Chi squared test on this data using the following code:

import pandas as pd
from scipy.stats import chi2_contingency

# Read data
link = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/018/746/original/loan.csv?1666170299"
data = pd.read_csv(link)

# Add a column indicating that the entry contains graduate and married men
data = data.dropna()
data['NewFeature'] = (data["ApplicantIncome"]) + (3 * data["LoanAmount"]) + (7000 * data["Credit_History"])
data['Separator'] = data['NewFeature'] > (data['NewFeature'].mean()*0.25)

# Perform a chi-square test since the incomes are a continuous variable.
contingency = pd.crosstab(data['Separator'], data['Loan_Status'])
print(contingency)

# p-value calculation
p_value = chi2_contingency(contingency)[1]
print('p-value:',round(p_value,4))

if(p_value < 0.05):
  print("Since p-value < 0.05, the two features 'Separator' and 'Loan_Status' are dependent.")
else:
  print("Since p-value > 0.05, the two features 'Separator' and 'Loan_Status' are independent.")
print()

###################################################
####################################################

'''
We have been given a dataset containing the details of the people applied for loan.

dataset: loan.csv : https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/018/746/original/loan.csv?1666170299

Which of the following features can be converted from a numerical feature to a 
categorical feature simply by renaming the values?
'''

# Explanation:

# Since the Credit_History contains the values that are either 0.0 or 1.0, which can 
# be relabeled as False and True, respectively.

# Therefore,it can be converted from a numerical feature to a categorical feature 
# simply by renaming the values.

#################################################################
#################################################################

'''
In the loan.csv : https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/018/746/original/loan.csv?1666170299
dataset, we wish to test the hypothesis that among all loan 
applicants who were rejected for a loan, applicants with a credit history of 1 
are more likely to be female.

Use a chi-square test to verify this claim (Ensure that you drop all nan rows), 
and report your interpretation.

Note: Use a significance level of 5%.
'''

# Explanation:

# Null hypothesis (H0): the features are independent.
# Alternate hypothesis (Ha) : the features are dependent.

# The below given code performs the chi2 test and the p-value comes out to 
# be 0.961.

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# Load the data
link = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/018/746/original/loan.csv?1666170299"
data = pd.read_csv(link)

# data of all the rejected applicants
chn = data[(data["Loan_Status"] == "N")]

#dropping na values
chn = chn.dropna()

#contingency table
contingency = pd.crosstab(chn['Gender'], chn['Credit_History'])
print(contingency)

#p-value
p_value = round(chi2_contingency(contingency)[1],3)
print('p-value:', p_value)

if p_value > 0.05:
 print('Since p_value > 0.05, we fail to reject the null hypothesis.')
else:
 print('Since p_value < 0.05, we reject the null hypothesis.')
print()
