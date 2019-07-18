# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# 022 Names scores

# https://projecteuler.net/problem=22

# Dependent file: https://projecteuler.net/project/resources/p022_names.txt

# Using names.txt (right click and 'Save Link/Target As...'), 
# a 46K text file containing over five-thousand first names, 
# begin by sorting it into alphabetical order. 
# Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, 
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

import os # And setting proper directory
path=r'C:\Users\Arunabha Sarkar\Documents\QRS\Project Euler\Python'
os.chdir(path)

names_file = open("names.txt", "r")

All_the_names_as_string = names_file.read()

names_file.close()

List_of_names = All_the_names_as_string.replace('"','').split(',')

List_of_names = list(map(lambda x: x.lower(),List_of_names))

List_of_names.sort()

score=[1]*len(List_of_names)

import string
Letters = list(string.ascii_lowercase)

for i in range(len(List_of_names)):
    element_score = 0
    
    for j in range(len(List_of_names[i])):
        element_score = element_score + Letters.index(List_of_names[i][j]) + 1
    
    element_score = (i+1) * element_score
    score[i] = element_score
        
print(sum(score))

# Answer is 871198282


##################################################################
##################################################################

# Alternate beauty:

# Making a lambda function for sum of index of words
score_card = lambda word: sum(ord(letter)-64 for letter in word)

# We use ord function. It's output minus 64 is the letter index
# https://www.geeksforgeeks.org/ord-function-python/

names_from_file = sorted(open('names.txt').read().rstrip().replace('"', '').split(','))

final_answer = sum(Index*score_card(name) for Index, name in enumerate(names_from_file, 1))
# In the above its important to enumerate from '1', not default '0',
# otherwise, (Index + 1) has to be used in lieu of Index

print("Answer: ", final_answer)

# Answer is 871198282
