

"""Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )"""

import numpy as np

arr = np.array([1,2,3,4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

"""We use the array() function to create arrays, this function can take an optional argument: 
dtype that allows us to define the expected data type of the array elements:"""

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)


arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)


"""Converting Data Type on Existing Arrays
The astype() function creates a copy of the array, and allows you to specify the data type as a parameter."""

arr = np.array([1.1,2.1,3.1])
newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)