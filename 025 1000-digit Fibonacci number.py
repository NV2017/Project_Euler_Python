# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# 025 1000-digit Fibonacci number

# https://projecteuler.net/problem=25

#The Fibonacci sequence is defined by the recurrence relation:
#
#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#
#The 12th term, F12, is the first term to contain three digits.
#
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

Fibonacci_List = [1,1]
counter = 2
while len(str(Fibonacci_List[-1])) < 1000:
    Fibonacci_List.append(Fibonacci_List[-1]+Fibonacci_List[-2])
    counter += 1

print(counter)

# Answer is 4782.
