# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# 023 Non-abundant sums

# https://projecteuler.net/problem=23

# A perfect number is a number for which the sum of its proper 
# divisors is exactly equal to the number. For example, 
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
# which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is 
# less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
# the smallest number that can be written as the sum of two 
# abundant numbers is 24. By mathematical analysis, it can be 
# shown that all integers greater than 28123 can be written as the 
# sum of two abundant numbers. However, this upper limit cannot be 
# reduced any further by analysis even though it is known that the 
# greatest number that cannot be expressed as the sum of two 
# abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot 
# be written as the sum of two abundant numbers.

# This is a function returning list of divisors:
def List_of_Divisors(Number):
    if isinstance(Number,int):
        if Number > 0:
            if Number == 1:
                return([Number])
            else:
                Divisor_List = []
                for integer in range(1,int(Number/2)+1):
                    if Number % integer == 0:
                        Divisor_List.append(integer)
                return(Divisor_List)
        else:
            print('Please enter a "positive" integer')
            return(False)
    else:
        print('Please enter an integer')
        return(False)
        
# Using the above, we find abundant number first, till 28123
abundant_number_till_28123 = []

for i in range(1,28124):
    if sum(List_of_Divisors(i)) > i:
        abundant_number_till_28123.append(i)

# Now we have to check which positive numbers cannot be
# sum of any two abundant numbers, up to 28123 (inclusive)
        
# Nice way to code is by removing sum of abundandt numbers from 1 to 28123
Non_Abundant_Numbers = [x for x in range(1,28124)]        

for j in range(len(abundant_number_till_28123)):
    for k in range(i, len(abundant_number_till_28123)):
        Sum_temp = abundant_number_till_28123[j] + abundant_number_till_28123[k]
        if Sum_temp > 28123:
            break
        else:
            if Sum_temp in Non_Abundant_Numbers:
                Non_Abundant_Numbers.remove(Sum_temp)
                
print(sum(Non_Abundant_Numbers))

# Answer is 4179871.

##################################################################
##################################################################

# Way faster alternative using sieving for speeding up sums

from bisect import bisect
from itertools import islice

def Sum_of_all_divisors_below_n(n):
    """
    Trick used here is:
    
    'n' can be factorised as 2^a * 3^b * 5^c ....
    
    Sum of divisors of n can be factorised as:
    (1+2+2^2+2^3+...+2^a)*(1+3+3^2+3^3+...+3^b)*(1+5+5^2+5^3+...+5^a)*....

    """
    output = [1] * n
    for j in range(2, n):
        if output[j] == 1:
            power_of_p, m_last = j, 1
            while power_of_p < n:
                m = m_last + power_of_p
                for i in range(power_of_p, n, power_of_p):
                    output[i] //= m_last
                    output[i] *= m
                m_last = m
                power_of_p *= j
                
    return(output)

def unsums(Limit,abundant,abundant_set):
    for i in range(1, Limit):
        for j in islice(abundant, bisect(abundant, i // 2)):
            if i - j in abundant_set:
                break
        else:
            yield i

def solve_euler(Limit):

    Sum_of_divisors = Sum_of_all_divisors_below_n(Limit)
    abundant = [i for i in range(1, Limit) if Sum_of_divisors[i] > 2 * i]
    abundant_set = set(abundant)

    return(sum(unsums(Limit,abundant,abundant_set)))

solve_euler(Limit=28124)

# Answer is 4179871.