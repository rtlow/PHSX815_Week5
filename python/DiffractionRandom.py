#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from python.Random import Random

# global variables

#default Xlims
Xmin = -5.
Xmax = 5.

random = Random()

def sampleFlat():
    return Xmin + (Xmax - Xmin) * random.rand()

# right now, just a uniform distribution at y = 1/Pi
# need to do this to normalize
def Flat(X):
    return 1/np.pi

# Sine squared divided by x squared
# normalized by dividing by pi
def Sin2(X):

    if X == 0:
        return 1
    else:
        return (1/np.pi) * (np.sin(X) / X) ** 2

# scaling by the bin width for normalization
def PlotSin2(X, bin_width):
    return bin_width * Sin2(X)

# main function
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s -Nsample [no. samples] -range [Xmax]" % sys.argv[0])
        print
        sys.exit(1)

    # default number of samples
    Nsample = 100

    # read the from the command line options (if there)
    if '-Nsample' in sys.argv:
        p = sys.argv.index('-Nsample')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nsample = Ne
    if '-range' in sys.argv:
        p = sys.argv.index('-range')
        Xmax = float(sys.argv[p + 1])
        Xmin = -float(sys.argv[p + 1])

    Ntrial = 0
    i = 0
    accepted_samples = []

    # running the rejection step
    while( i < Nsample ):
        Ntrial += 1

        X = sampleFlat()
        R = Sin2(X)/Flat(X)

        ran = random.rand()
        
        # reject the sample and continue
        if (ran > R):
            continue
        # accept the sample and increment
        else:
            accepted_samples.append(X)
            i += 1

    efficiency = Nsample / Ntrial
    
    print('Efficiecny was {:.3f}'.format(efficiency))

    # normalizing the histogram
    weights = np.ones_like(accepted_samples) / len(accepted_samples)

    # fancy plot formatting
    plt.figure(figsize=[12,7])

    n = plt.hist(accepted_samples, weights=weights, color='r', alpha=0.5, label='samples from f(x)', bins=100)

    bin_width = n[1][1] - n[1][0]
    plt.ylabel('Probability')
    plt.xlabel('X')

    x = np.arange(Xmin, Xmax, 0.001)

    y = [PlotSin2(s, bin_width) for s in x]

    plt.plot(x, y, color='k', label='target f(x)')

    y = np.ones(len(x)) * bin_width * 1/np.pi

    plt.plot(x, y, color='b', label='proposal g(x)')

    plt.title('Density estimation with Monte Carlo')

    plt.legend()

    plt.savefig('RandomDiffraction.pdf')
    plt.show()


    
