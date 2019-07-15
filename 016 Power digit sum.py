# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# -*- coding: utf-8 -*-

# https://projecteuler.net/problem=16

# 016 Power digit sum

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26

# What is the sum of the digits of the number 2^1000

Number_as_string = str(2**1000)

answer = 0

for i in range(len(Number_as_string)):
    answer = answer + int(Number_as_string[i])
    
print(answer)

# Answer is 1366