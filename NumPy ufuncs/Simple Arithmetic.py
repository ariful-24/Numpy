
"""Simple Arithmetic
You could use arithmetic operators + - * / directly between NumPy arrays, but this section discusses an extension of the same where we have functions
that can take any array-like objects e.g. lists, tuples etc. and perform arithmetic conditionally."""


"""Addition
The add() function sums the content of two arrays, and return the results in a new array."""


import numpy as np

arr1 = np.array([10,11,12,13,14,15])
arr2 = np.array([20,21,22,23,24,25])

newarr = np.add(arr1,arr2)
print(newarr)

newarr = np.subtract(arr1,arr2)
print(newarr)

newarr = np.multiply(arr1, arr2)
print(newarr)

newarr = np.divide(arr1, arr2)
print(newarr)

newarr = np.power(arr1, arr2)
print(newarr)


"""Remainder
Both the mod() and the remainder() functions return the remainder of the values in the first array corresponding to the values in the second array, 
and return the results in a new array."""

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.mod(arr1, arr2)
print(newarr)

newarr = np.remainder(arr1, arr2)
print(newarr)

"""Absolute Values
Both the absolute() and the abs() functions do the same absolute operation element-wise but we should use absolute() to avoid confusion with python's inbuilt math.abs()"""

arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr)
print(newarr)