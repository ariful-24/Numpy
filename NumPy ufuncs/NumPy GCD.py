

"""Finding GCD (Greatest Common Denominator)
The GCD (Greatest Common Denominator), also known as HCF (Highest Common Factor) is the biggest number that is a common factor of both of the numbers."""


#Find the HCF of the following two numbers:

import numpy as np
num1 = 6
num2 = 9

x = np.gcd(num1,num2)
print(x)

"""Finding GCD in Arrays
To find the Highest Common Factor of all values in an array, you can use the reduce() method."""

arr = np.array([20, 8, 32, 36, 16])

x = np.gcd.reduce(arr)

print(x)

