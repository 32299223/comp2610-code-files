import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom


index = 2
p = 0.20 # probability of producing a 1

all_indexes = []

all_exact = []
all_markov = []
all_chebyshev = []

while (index <= 40):

    k = np.arange(0,index+1) # different possible number of visitors selected in a numpy array i.e. 0 or 5 etc

    binomial = binom.pmf(k=k, n=index, p=p) # SOURCE: https://medium.com/@c_safarli/binomial-distribution-probability-mass-function-cumulative-distribution-function-calculation-5ae74fd3a340
    #print(binomial)

    popper = 0

    while (popper < index/2):
        binomial = np.delete(binomial, 0)
        popper += 1

    #print(binomial)

    bisum = 0

    for elem in binomial:
        bisum += elem

    #print(bisum)
    
    markov = 0.4
    chebyshev = (0.16)/(index * 0.09)

    all_exact.append(bisum)
    all_markov.append(markov)
    all_chebyshev.append(chebyshev)

    all_indexes.append(index)

    index += 2

# Plot Exact Probability
plt.plot(all_indexes, all_exact, label='Exact Probability', color='blue')

# Plot Markov Bound
plt.plot(all_indexes, all_markov, label='Markov Bound', color='red')

# Plot Chebyshev Bound
plt.plot(all_indexes, all_chebyshev, label='Chebyshev Bound', color='green')

# Labels and Legend
plt.title('The Exact Probability, Markov Bound, and Chebyshev Bound of Observing N/2 1s for  N E {2, 4, 6, 8 ... 40}')
plt.xlabel('N (bits generated)')
plt.ylabel('Probability (%)')
plt.legend()
plt.grid()
plt.xticks(ticks=[x for x in range(40) if x%2 == 0]) # SOURCE: https://stackoverflow.com/questions/2184745/even-numbers-in-python