

"""
What is a Set
A set in mathematics is a collection of unique elements.

Sets are used for operations involving frequent intersection, union and difference operations."""

"""
Create Sets in NumPy
We can use NumPy's unique() method to find unique elements from any array."""

import numpy as np
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr)
print(x)


"""
Finding Union
To find the unique values of two arrays, use the union1d() method."""

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1,arr2)
print(newarr)


"""Finding Intersection
To find only the values that are present in both arrays, use the intersect1d() method."""

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.intersect1d(arr1,arr2, assume_unique=True)
print(newarr)



"""Finding Difference
To find only the values in the first set that is NOT present in the seconds set, use the setdiff1d() method."""

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setdiff1d(set1, set2, assume_unique= True)
print(newarr)

