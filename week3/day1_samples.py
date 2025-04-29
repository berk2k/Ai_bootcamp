from itertools import product

#sample space of a dice roll
sample_space = list(range(1,7))

# probability of rolling an even number
even_numbers = [2,4,6]
P_even = len(even_numbers) / len(sample_space)
print("P(even): ",P_even)

import numpy as np 

outcomes = np.array([1,2,3,4,5,6])
probabilities = np.array([1/6]*6)

expectation = np.sum(outcomes * probabilities)


print("expectation (mean): ",expectation)

# variance and sd

variance = np.sum((outcomes - expectation)**2 * probabilities)
std_dev = np.sqrt(variance)


# simulating 10,000 dice rolls
rolls = np.random.randint(1,7,size=10000)

P_even = np.sum(rolls % 2 == 0) / len(rolls)
P_greater_than_4 = np.sum(rolls > 4) / len(rolls)

import matplotlib.pyplot as plt 
from scipy.stats import uniform

outcomes = [1,2,3,4,5,6]
probabilities = [1/6]*6
plt.bar(outcomes,probabilities,color="blue",alpha=0.7)




