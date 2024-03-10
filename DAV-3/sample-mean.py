'''
The student hostel office at IIT Madras estimates that each student uses more than 
3.5 buckets of water per day.

In order to verify this claim, the college trustees decide to monitor the water 
consuption over the next 45 days, and it is found that on an average, 3.72 buckets 
of water is consumed by a student, per day.

Assume that the population standard deviation is 0.7 buckets. What is the critical 
sample mean, assuming a critical z-value of 1.28?

Note: The critical sample mean is defined as the mean value for which the z-score is 
equal to the critical value. Also, round off the final answer to three decimal places.
'''

import math

# Given values
population_mean = 3.5
population_std = 0.7
critical_z_value = 1.28
sample_size = 45

# Calculate the critical sample mean
critical_sample_mean = population_mean + (critical_z_value * (population_std / math.sqrt(sample_size)))

# Round off the answer to three decimal places
critical_sample_mean = round(critical_sample_mean, 3)
print("Critical Sample Mean:", critical_sample_mean)
print()

##############################################
############################################

