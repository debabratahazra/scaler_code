import scipy.stats as stats


'''In a factory, the probability of producing a defective bulb is 0.25. A sample 
of 40 bulbs is collected.

What is the probability that exactly 10 bulbs are defective?'''
n=40 # Sample size
p=0.25 # probability of producing a defective bulb
k=10 # exactly 10

binomial = stats.binom.pmf(k,n,p)
print('The probability that exactly 10 bulbs are defective is %1.4f' %binomial)

##################
'''The probability of a person not boarding a cab despite having paid for the seat is 0.4. 
A rideshare app always sells 6 seats in their cabs which can only accommodate 4 people.

What is the probability that everyone who shows up for the ride gets a seat?'''
from scipy.stats import binom

# binomial distribution with n=6, p=0.6 and q = 1-p = 0.4

# probability that the ride is overbooked is P(k=5) + P(k=6)
prob_overbooked = binom.pmf(5,6,0.6)+binom.pmf(6,6,0.6)

# the probability that everyone who shows up gets a seat is 1 - P(overbooked)
print("The probability that everyone who shows up gets a seat is" ,round(1-(prob_overbooked),2))

################

'''A large-scale survey by government automation authority found that 12% of the cars have 
faulty brake lights. Find the probability that in a random sample of 10 cars, less than 4 
cars have faulty brake lights ?'''

# n=10 as the number of cars randomly sampled,
# p=0.12 as the probability that a car has a faulty brake light, and
# q=1−p=0.88 as the probability that a car does not have a faulty brake light.

print(binom.cdf(n=10, k=3, p=0.12))

########
