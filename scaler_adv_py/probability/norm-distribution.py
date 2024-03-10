

from scipy.stats import norm

'''Suppose you reside in a city with a large population. The weight of people living 
in your city follows a Gaussian distribution with a mean of 60 kgs with a standard deviation of 10 kgs.

You weigh 65 kg. What is the probability that a randomly selected person in your city 
is heavier than you?'''
prob = 1 - norm.cdf(0.5)

print("Probability that a person is heavire than you is",round(prob,4))

##########

'''A packaging plant fills bags with cement.

The weight of the cement bags can be modelled by a normal distribution with a mean of 
50kg and a standard deviation of 2 kg.

Find the weight x that is exceeded by 99% of the bags.'''

#μ = 50
# σ = 2
print("Z value:", round(norm.ppf(0.01),3))
# z = (x - μ) / σ
# -2.326 = (x - 50) / 2
# -4.652 = x - 50
# -4.652 + 50 = x
# x = 45.348 kgs.

###############################

z1 = (13-27)/7
z2 = (20-27)/7

val = norm.cdf(z2) - norm.cdf(z1)
print(val*10000)