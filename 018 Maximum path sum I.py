# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# 018 Maximum path sum I

# https://projecteuler.net/problem=18

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
# the maximum total from top to bottom is 23.

# That is, 3 + 7 + 4 + 9 = 23.
# 
# Find the maximum total from top to bottom of the triangle below:

# This is a beautiful case of dynamic programming: https://en.wikipedia.org/wiki/Dynamic_programming

triangle_of_the_webpage = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# counting number of rows

number_of_rows = triangle_of_the_webpage.count('\n') + 1

# ' + 1 ' at the end because the last row will not have '\n'

## Some theory/insights of mine.... 
# As far as this question is concerned, brute force method will work.
# Convenient are the pmax / pmin function for the same.
# These functions take many vectors as input/output and return max/min of them.

import re
import pandas as pd
triangle_of_the_webpage = re.sub("\n", " ", triangle_of_the_webpage)

triangle_of_the_webpage = list(map(int, triangle_of_the_webpage.split(" ")))

triangle_full = pd.DataFrame(index=range(number_of_rows),columns=range(number_of_rows))
triangle_full = triangle_full.fillna(0) # Not necessary
# creating full triangle matrix

for i in range(number_of_rows):
    
    # We can think along these lines to deduce which elements go to which row
    # Its easiest to figure out the last element of a triangle row
    # The last limit for i'th row sum of 1 + 2 + .... + i
    
    End_limit = sum(range(0,i+2))
    # Now for each End_limit element, the i'th row has i elements
    # So the starting element for this element will be in (i-1) positions before
    # Like for 2:3, the 2nd row, 2 elements are recovered by gap of 1 in range(2,3)
    
    Start_limit = End_limit - (i+1)
    # Filling entire row at one go
    triangle_full.loc[i,:] = triangle_of_the_webpage[Start_limit:End_limit] + [0]*(number_of_rows-len(range(Start_limit,End_limit))) 
    

maximal_path = triangle_full

def parallel_max_of_pair(list_1,list_2):
    
    if len(list_1) == len(list_2):
        output = [0]*len(list_2)
        for k in range(len(list_2)):
            output[k] = max(int(list_1[k]),int(list_2[k]))
        return(output)
    else:
        print('Error in input of function "parallel_max_of_pair"')
        return(None)

# Filling from bottom up
for j in range(number_of_rows-1,0,-1):
    
    # Remember, the 'jth' row has 'j+1' non-zero elements.
  
    # Each of the maximal value of ' j-1 , .. ' element comes from 2 sources
    # From the  right or left element of row# j
    # The positions are : Left_Side & Right_Side
    
    Left_Side = list(maximal_path.iloc[j,0:j] + maximal_path.iloc[j-1,0:j])
  
    Right_Side = [sum(x) for x in zip(list(maximal_path.iloc[j,1:j+1]), list(maximal_path.iloc[j-1,0:j]))]

    # Notice how in the column index, has '2' only in Right_Side part, 
    # this is to pick up the right side element. This is why it ends on 2:i.
  
    # Now,
    # The final input will be the element on top of the triangle
    # This will also be the answer.
  
    # Filling in 1:(i-1) column elements of row# i-1 at once
    # The pamx function gives the max of the vectors of the perpendicular direction!
    # the 'p' in pmax/pmin means 'parallel' !
    pmax_output = parallel_max_of_pair(Left_Side, Right_Side)
    maximal_path.loc[j-1,0:(j-1)] = pmax_output
   
print(maximal_path.iloc[0,0])

# Answer is 1074