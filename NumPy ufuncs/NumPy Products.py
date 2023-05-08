

"""Products
To find the product of the elements in an array, use the prod() function."""

import numpy as np

arr = np.array([1,2,3,4])
x = np.prod(arr)

print(x)


"""Find the product of the elements of two arrays:"""

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1,arr2])
print(x)

"""Product Over an Axis
If you specify axis=1, NumPy will return the product of each array."""

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

newarr1 = np.prod([arr1, arr2], axis=1)
print(newarr1)




"""Cummulative Product
Cummulative product means taking the product partially.

E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]

Perfom partial sum with the cumprod() function."""


arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)

print(newarr)
