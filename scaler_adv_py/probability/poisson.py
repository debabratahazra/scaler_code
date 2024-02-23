import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as se
from scipy.stats import norm
from scipy.stats import poisson, binom

"""
Q1. If electricity power failures occur according to a poisson distribution with an 
average of three failures every 20 weeks, calculate the probability that there will 
not be more than one failure during a week."""

avg_weekly = 3 / 20  # per week
# P[X <= 1] = ?

prob = poisson.cdf(k=1, mu=avg_weekly)
print(prob)


"""
Q2. An observer counts 240 vehicles per hour (3600 seconds) at a specific vehicle arrival 
location on a highway.

Assume that the arrivals follow the poisson distribution, What is the probability of 
one vehicle arriving over a 30-second time interval?"""

vehicle_per_sec = 240 / 3600
vehicle_per_30sec = 30 * vehicle_per_sec
# P[X = 1] = ?
prob = poisson.pmf(k=1, mu=vehicle_per_30sec)
print(prob)

"""
Q3. You go to a party of 500 guests. What is the probability that exactly one other guest 
has the same birthday as you?

Note: Exclude birthdays on February 29."""

# P[X=1] = ?

guest__per_day_birthday = 500 / 365
prob = poisson.pmf(k=1, mu=guest__per_day_birthday)
print(prob)
