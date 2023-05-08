
"""Array indexing is the same as accessing an array element.
You can access an array element by referring to its index number."""

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])
print(arr[1])

"""Get third and fourth elements from the following array and add them."""
print(arr[2] + arr[3])



"""To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
Think of 2-D arrays like a table with rows and columns, where the row represents the dimension and the index represents the column."""

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd elemnet of 1st row:',arr[0,1])
print('Last element from 2nd dim: ', arr[1, -1])


"""To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element."""
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0,1,2])

