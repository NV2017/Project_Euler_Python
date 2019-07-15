# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# coding: utf-8

# # 005 Smallest multiple
# 
# # 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# # What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 
# ## https://projecteuler.net/problem=5


# Notice that 2520 includes the highest power of the primes that is less than 10
# Each number till 10 can be represent as either a prime or some powers of primes
# Multiply all the highest powers of those primes to get the answer, a number divisible by anything till 10

# Done on R, 3 minor differences b/w the two languages are revealed

# This is the most basic Prime number finding algorithm, not very energy efficient
def PrimeNumbers(UpperNumber):
    PrimeList = []
    for i in range(2,UpperNumber+1):    #To find all primes including the UpperNumber
        IsIt = True                     #Assuming it is prime, will falsify later
        for j in range(2,i):            #For primes, divisibility checking starts from 2; also not itself
            if i % j == 0:              #This means the i is divisible, thus not a prime
                IsIt = False
        if IsIt == True:                #Must be a prime as nothing but 1 & itself divides i wholly
            PrimeList.append(i)
    return(PrimeList)


# In[31]:


# Each number till 20 can be represent as either a prime or some powers of primes
# Multiply all the highest powers of those primes to get the answer, a number divisible by anything till 20

Problem5 = PrimeNumbers(20)             #List of prime number till 20, using the function defined above
Problem5Powers = []                     #The highest possible powers of the primes such that they are < 20
for i in range(len(Problem5)):
    j = 1
    while Problem5[i]**j < 20:
        j = j + 1
    Problem5Powers.append(j-1)          #Appending the required power of the primes in the same order as the primes

answer = 1

for k in range(len(Problem5)):
    answer = answer*( (Problem5[k])**(Problem5Powers[k]) )

print (answer)

# The answer is: 232792560