# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# 020 Factorial digit sum

# https://projecteuler.net/problem=20

# n! means n x (n − 1) x... x 3 x 2 x 1
# 
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# 
# Find the sum of the digits in the number 100!

import math

print(sum(int(c) for c in str(math.factorial(100))))

# Answer is 648.