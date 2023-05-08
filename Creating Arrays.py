

"""NumPy is used to work with arrays. The array object in NumPy is called ndarray.

We can create a NumPy ndarray object by using the array() function."""

import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
#
# print(arr)
#
# print(type(arr))


"""To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:"""
# arr = np.array((1,2,3,4,5))
# print(arr)


"""1-D Arrays
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array."""

arr=np.array([1,2,3,4,5])
print(arr)

"""2-D Arrays
An array that has 1-D arrays as its elements is called a 2-D array."""

arr= np.array([[1,2,3],[4,5,6]])
print(arr)

"""3-D arrays
An array that has 2-D arrays (matrices) as its elements is called 3-D array."""

arr= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)

"""NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have."""
a= np.array(42)
b=np.array([1,2,3,4,5])
c= np.array([[1,2,3],[4,5,6]])
d= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)



"""An array can have any number of dimensions.

When the array is created, you can define the number of dimensions by using the ndmin argument"""
arr = np.array([1,2,3,4], ndmin=5)
print(arr)
print('number of dimnension:', arr.ndim)

