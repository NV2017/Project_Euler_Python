# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# coding: utf-8

# # 010 Summation of primes
# 
# # The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# # Find the sum of all the primes below two million.
# 
# # https://projecteuler.net/problem=10

# In[172]:


def SieveOfEratosthenes(UpperLimit):
    ItemsToReject = set() #unordered and unindexed set of elements, input is a list, not integers
    for i in range(2, UpperLimit+1):
        if i not in ItemsToReject:
            yield i #New and next element added to the set, now gotto delete its multiples.
            # or add its multiples to a list of items to reject
            #Yield can produce a sequence of values. 
            #We can use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.
            ItemsToReject.update(range(i*i, UpperLimit+1, i))
            # Why i * i, and why not i + i, might seems confusing
            # Because: multiples of i+i till i*i have other factors
            # Only beyond i*i can there be numbers that have only i as factors, like i^2 or i^3

#Now sum the primes
sum = 0
Primes = list(SieveOfEratosthenes(2000000))
for x in Primes: #As Primes is a set, there is no indexed order accessibility for x
    sum = sum + int(x) #int(x) is required as set elements are list like by definitionprint(int(x))

print(sum)


# In[148]:


# This is extremely slow, because of usage of while loop

# Strategy - Writing all in one function can make this difficult

# Better strategy is to split into more understandable parts

# First funtion to write is one that inputs a list (and a number to divide is 1st element)
# This should divide all list elements by the number (also first of parent list)
# In case remainder is zero, eliminate
# Then output the remaining numbers to a list
# Also output the 'number' to a list

Prime = []

def InnerLoop(List):
    Prime.append(List[0])
    NewList = []
    for i in range(1,len(List)): #As the 0th element is prime and transferred to 'Prime'
        if List[i] % List[0] != 0:
            NewList.append(List[i])
    #print('Hi',NewList)
    return(NewList)

# For this next part, divide by first element of the list, remove zero elements

Start = [i for i in range(2,2000000)] #Original

while len(Start) != 0:
    Start = InnerLoop(Start)

print(sum(Prime))

# Answer is: 142913828922