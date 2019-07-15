# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# coding: utf-8

# # 004 Largest palindrome product
# 
# # A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# # Find the largest palindrome made from the product of two 3-digit numbers.
# 
# ## https://projecteuler.net/problem=4

Largest_Palindrome = 0

for i in range(1000,100,-1):                                            # It's faster to find the largest in this reverse direction
    for j in range(1000,i,-1):                                          # removes many double calculations
        new = i*j
        if new < Largest_Palindrome:                                    # This increases computational efficiency, new answer can't be possible when this condition holds
            break
        if (new > Largest_Palindrome) and (str(new) == str(new)[::-1]): # :: is element wise checking, -1 is in reverse direction
            Largest_Palindrome = new

print(Largest_Palindrome)

# The answer is: 906609