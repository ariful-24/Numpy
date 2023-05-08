"""What is Data Distribution?
Data Distribution is a list of all possible values, and how often each value occurs."""

"""Random Distribution
A random distribution is a set of random numbers that follow a certain probability density function."""


"""Example
Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.

The probability for the value to be 3 is set to be 0.1

The probability for the value to be 5 is set to be 0.3

The probability for the value to be 7 is set to be 0.6

The probability for the value to be 9 is set to be 0 """

from numpy import random

x = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0], size=(100))
print(x)


x = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0], size=(3,5))
print(x)
