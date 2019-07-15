# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# coding: utf-8

# # 007 10001st prime
# 
# # By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# # What is the 10 001st prime number?
# 
# ## https://projecteuler.net/problem=7

# Using numbers of the form 6k±1 is certainly one of the most efficient approaches for an unknown upper limit; 
# that is, continuing through good "prime candidates" until you arrive at the nth prime.

Indexer = 3             # First two prime number 2 & 3 don't follow the 6n +/- 1 theorem. So starting count after them.
NaturalNumber = 1       # Natural number increment, only after checking 6n + 1
switch = True
while (Indexer <= 10001):
    if (switch == True):
        candidate = 6*NaturalNumber -1 # This is Euler's 6n +/- 1 Theorem. i.e. 
        switch = False  # All prime numbers greater than 3 are always of the form 6n - 1 or 6n + 1
    else:               # Also, 6n - 1 < 6n + 1; thus 6n - 1 has to be checked first
        candidate = 6*NaturalNumber +1
        switch = True   # swtich restored
        NaturalNumber = NaturalNumber + 1  # Natural number increment, only after checking 6n + 1
    IsItPrime = True    # Checker of primeness of x
    StartTester = 3     # This coupled with t = t + 2 ensures checking only odd terms
    while (StartTester <= candidate**(0.5)):# Only need to check till 3
        if (candidate%StartTester == 0):  # Divisor test of x for primeness
            IsItPrime = False
        StartTester = StartTester + 2# Skipping even terms
    if (IsItPrime == True):
        Indexer = Indexer + 1# Updating counter only when a prime is found
print(candidate)

# The answer is: 104743