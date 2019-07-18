# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# 024 Lexicographic permutations

# https://projecteuler.net/problem=24

# A permutation is an ordered arrangement of objects. 
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, 
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the 
# digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# 2**20 is 1048576
# This is more than million, and 2**19 = 524288 is less than million.

# So we can say starting from '0123456789', 
# the 1048576 th iteration will be '9876543210'

# Now, calculating back wards is easier.

# We only have to do this backward calculation 48576 times.

import itertools

Starting_Number = list(range(10))

# itertools.permutations returns all orderings, elements not distinguished for uniqueness
# itertools.slice maintains the entire collection is ascending sequence.

temp = itertools.islice(itertools.permutations(Starting_Number), 999999, None)

print("".join(str(x) for x in next(temp)))

# Answer is 2783915460.





