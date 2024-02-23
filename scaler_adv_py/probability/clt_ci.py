import numpy as np
import pandas as pd
import math as m
import matplotlib.pylab as plt
import seaborn as sn
from scipy.stats import norm

"""You are working for the Department of Endangered Species. Along with your team, 
you have bred a certain species of endangered fish in your pond.
On taking a sample of 100 fishes, the calculated average length of this species 
came out to be 24cm. It is known that the population standard deviation in the 
length of these fishes is 8cm.
Estimate the mean length confidence interval of the fishes in the pond with a 
confidence of 95 percent.
Note: z-multiplier for 95% is 1.96."""

mu = 24
std = 8
n = 100

se = std / m.sqrt(n)

z1 = norm.ppf(2.5 / 100)
z2 = norm.ppf(97.5 / 100)

x1 = mu + (z1 * se)
x2 = mu + (z2 * se)
print(x1, x2)
