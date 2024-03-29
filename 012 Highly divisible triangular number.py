# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# coding: utf-8

# # 012 Highly divisible triangular number
# 
# The sequence of triangle numbers is generated by adding the natural numbers. 
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
# The first ten terms would be:
# 
# # 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# # Let us list the factors of the first seven triangle numbers:
# 
# # 1: 1
# # 3: 1,3
# # 6: 1,2,3,6
# # 10: 1,2,5,10
# # 15: 1,3,5,15
# # 21: 1,3,7,21
# # 28: 1,2,4,7,14,28
# 
# # We can see that 28 is the first triangle number to have over five divisors.
# 
# # What is the value of the first triangle number to have over five hundred divisors?

# returns the nth triangle number; that is, the sum of all the natural numbers less than, or equal to, n
# uses n*(n + 1)/2 as nth triangle number

def TriangleNumber(n):
    return n*(n+1)/2

Nth = 0 # Nth triangle number
NthTriangleNumber = 0 
NumberOfDivisors = 0 # number of divisors for triangle number n

while NumberOfDivisors <= 500:
    NumberOfDivisors = 0 # resets numberOfDivisors because it's now checking a new triangle number
    Nth = Nth + 1 # and also sets n to be the next triangle number
    NthTriangleNumber = TriangleNumber(Nth)

    for i in range(1, 1 + int(NthTriangleNumber**0.5)):
        if NthTriangleNumber % i == 0:
            NumberOfDivisors = NumberOfDivisors + 1
    NumberOfDivisors = NumberOfDivisors * 2 # Total number of divisors till NthTriangleNumber
    #print(NumberOfDivisors, NthTriangleNumber)

print (Nth, 'th triangle number is: ', int(NthTriangleNumber), 'with number of divisors: ', NumberOfDivisors)

# The answer is: 76576500