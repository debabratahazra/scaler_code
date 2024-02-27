import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as se
from scipy.stats import geom, expon

"""You are hired as a data scientist for the company SellMart.

Your first task is to analyze the durations of customer support call.

On an average, a customer care executive takes about 5 minutes to solve 
the issue of any customer. It is known that the time taken follows an exponential distribution.

Find the probability that an executive spends 4 to 5 minutes with any randomly selected customer."""
mu = 5
x1 = 4
x2 = 5

e1 = expon.cdf(scale=mu, x=x1)
e2 = expon.cdf(scale=mu, x=x2)

# So P[4<X<5] = ?
ans = e2 - e1
print(round(ans * 100, 2), "%")

################################

"""For a certain railway agency, the number of days people book their rail ticket 
in advance can be modeled by an exponential distribution, with the average amount of time 
to be 4 days. Based on this data, how many days in advance do 75% of all travelers book tickets?
#####################

Explanation:
Given μ = 4 days
So, λ = 1/4 = 0.25


We need to find the number of days that 75% of people book their ticket in advance. So basically, we need to find the 75th percentile value of the given distribution.

Another way of looking at this is that for k days, P(X < k) = 0.75
Hence, we can apply the CDF formula for Exponential distribution to calculate the value of k

Using CDF of exponential distribution,
P(X < k) = 1 - e(-k / μ)
=> 0.75 = 1 - e(-k/4)
=> e(-0.25k) = 1-0.75 = 0.25
=> ln(e(-0.25k)) = ln(0.25)
=> -0.25k = -1.386
=> k = 1.386/0.25
=> k = 5.5

Hence, 75% of all travelers book tickets 5.5 days in advance"""
######################################
"""Suppose that the lifespan of an electronic gadget (in years) follows an exponential distribution. 
The average life span of an Electronic Gadget is known to be 2 years.

Find the probability that :

i) It will work for at least 6 years.

ii) It will work for at most 6 years.

Note: Round the output up to 2 decimal places."""

mu = 2
k = 6

e1 = 1 - expon.cdf(x=6, scale=mu)
e2 = expon.cdf(x=6, scale=mu)
print(e1, e2)

#############################################
"""The amount of money customers spend in one trip to the supermarket follows an exponential
distribution with a mean amount of Rs 1000.

If a customer has Rs 600 in the wallet, what is the probability that the customer will need 
more money?

Note: Round the output up to 2 decimal places."""

mu = 1000
x = 600
e = 1 - (expon.cdf(x=x, scale=mu))
print(round(e, 2), "is the probability that the customer will need more money.")

#########################

"""A new pair of running shoes of Brank X are known to last 6 months, on an average, assuming that they are used every day.

It is known that the duration of their lifespan follows exponential distributed.

If a pair has already lasted 5 months, find the probability that it will last a total of over 9 months."""

mu = 6
x1 = 5
x2 = 9

e1 = 1 - (expon.cdf(x=x1, scale=mu))
e2 = 1 - (expon.cdf(x=x2, scale=mu))
print(round((e2 / e1), 2))

# or ##
mu = 6
x1 = 5
x2 = 9
x3 = x2 - x1

# Probability that it will last a total of over 9 months

e = 1 - (expon.cdf(x=x3, scale=mu))
print("The probability that it will last a total of over 9 months:", round(e, 2))
