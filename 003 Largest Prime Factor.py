# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# coding: utf-8

# # 003 Largest Prime Factor
# 
# # The prime factors of 13195 are 5, 7, 13 and 29.
# 
# # What is the largest prime factor of the number 600851475143 ?
# 
# ## https://projecteuler.net/problem=3

# Beautiful demonstration of While Loop
# Every composite number has a prime factor less than or equal to its square root.
number = 600851475143
i = 2
while i * i < number:      # Because, read above; this is upper end for factors
    while number % i == 0: # Dividing the number only when its divisible, as this doesn't effect the largest prime factor
        number = number / i
    i = i + 1
print(int(number))         # Output is whatever number remaining

# The answer is: 6857