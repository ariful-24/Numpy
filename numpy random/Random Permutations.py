
"""Random Permutations of Elements
A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.

The NumPy Random module provides two methods for this: shuffle() and permutation()."""


"""Shuffling Arrays"""

from numpy import random
import numpy as np

arr = np.array([1,2,3,4,5])

random.shuffle(arr)

print(arr)


arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))
