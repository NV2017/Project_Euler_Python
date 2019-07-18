# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# 021 Amicable numbers

# https://projecteuler.net/problem=21

# Let d(n) be defined as the sum of proper divisors of n 
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are 
# an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 
# 1, 2, 4, 71 and 142; so d(284) = 220.
#
#Evaluate the sum of all the amicable numbers under 10000.

# Making a function returining list of divisors

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

# Finding sum of divisors and storing them in a dictionary

Limit = 10000

Dictionary_Range_of_Numbers = {i:sum(List_of_Divisors(i)) for i in list(range(1,Limit))}

# Checking for equal sum of divisor 

Exception_list = [] # To avoid duplication of checkting
Amicable_keys = [] # Sum of this is the answer

for key in Dictionary_Range_of_Numbers:
    if key not in Exception_list:
        element = Dictionary_Range_of_Numbers[key]
        if element <= Limit:
            Exception_list.append(key)
            if Dictionary_Range_of_Numbers[element] == key and element != key:
                Amicable_keys.append(key)
        else:
            continue
        
print(sum(Amicable_keys))

# The answer is 31626