# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# coding: utf-8

# # 014 Longest Collatz sequence
# # The following iterative sequence is defined for the set of positive integers:
# 
# # n → n/2 (n is even)
# # n → 3n + 1 (n is odd)
# 
# # Using the rule above and starting with 13, we generate the following sequence:
# 
# # 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# # It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# # Which starting number, under one million, produces the longest chain?
# 
# # NOTE: Once the chain starts the terms are allowed to go above one million.

# Many calculations of part higher terms will be repeat of some lower terms.
# Thus, recording those will speed. This requires checking each new entry with match of a data base
# This can be a list with index as number & values as number of number of terms in the series

# This is not designed to work starting from negative terms

def NextCollatzTerm(n):
    if n % 2 == 0:
        return(int(n/2))
    else:
        return(int(3*n + 1))
    
import numpy as np
# History is to store number of terms in sequence for terms whose Collatz sequence is already done,
# to avoid repetition, without this we get brute force method
History = np.repeat(0, 1000000000) # Numpy is exhibiting error with order greater than this
History[0] = 2 # Reaches in one step
History[1] = 1 # Already there
History[2] = 2 # Two terms till the series reaches 1 starting from 2

Counter = 0
GreatestCounter = 0
BiggestNumber = 0

for i in range(3, 1000001): #i is the number to be checked, not directly index
    Counter = 0
    dummyi = i
    
    while dummyi != 1:
        if dummyi < 1000000000 and History[dummyi] != 0: # dummyi < 1000000000 because numpy repeat set cannot handle bigger list
            Counter = Counter + History[dummyi]
            dummyi = 1
            break
        else:
            dummyi = NextCollatzTerm(dummyi)
            Counter = Counter + 1
    
    History[i] = Counter
    
    if Counter > GreatestCounter:
        GreatestCounter = Counter
        BiggestNumber = i

print('Biggest number is', BiggestNumber, 'with # of terms:', GreatestCounter + 1) #Number of terms in the series is 'GreatestCounter + 1'

# The answer is 837799