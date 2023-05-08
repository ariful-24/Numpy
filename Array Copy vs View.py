

"""The main difference between a copy and a view of an array is that the copy is a new array,
and the view is just a view of the original array."""


"""Make a copy, change the original array, and display both arrays:"""

import numpy as np

arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0]=42

print(arr)
print(x)

"""VIEW:
The view SHOULD be affected by the changes made to the original array."""
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)


"""Check if Array Owns its Data
As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

Every NumPy array has the attribute base that returns None if the array owns the data.

Otherwise, the base  attribute refers to the original object."""

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)