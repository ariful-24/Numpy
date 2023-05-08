

"""Poisson Distribution
Poisson Distribution is a Discrete Distribution.

It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is probability he will eat thrice?

It has two parameters:

lam - rate or known number of occurences e.g. 2 for above problem.

size - The shape of the returned array."""

# from numpy import random
#
# x = random.poisson(lam=2, size=10)
# print(x)


"""Visualization of Poisson Distribution"""

# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# sns.distplot(random.poisson(lam=2, size=1000), kde=False)
#
# plt.show()



"""Difference Between Normal and Poisson Distribution
Normal distribution is continous whereas poisson is discrete."""


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')

plt.show()