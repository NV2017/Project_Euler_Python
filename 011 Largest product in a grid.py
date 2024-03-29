# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# coding: utf-8

# # 011 Largest product in a grid
# 
# # In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
# 
# ## 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# ## 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# ## 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# ## 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# ## 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# ## 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# ## 32 98 81 28 64 23 67 10 <font color='red'>26</font> 38 40 67 59 54 70 66 18 38 64 70
# ## 67 26 20 68 02 62 12 20 95 <font color='red'>63</font> 94 39 63 08 40 91 66 49 94 21
# ## 24 55 58 05 66 73 99 26 97 17 <font color='red'>78</font> 78 96 83 14 88 34 89 63 72
# ## 21 36 23 09 75 00 76 44 20 45 35 <font color='red'>14</font> 00 61 33 97 34 31 33 95
# ## 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# ## 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# ## 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# ## 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# ## 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# ## 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# ## 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# ## 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# ## 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# ## 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
# 
# # The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
# 
# # What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
# 
# # https://projecteuler.net/problem=11

# In[170]:


# Note: Input is not row by row, but all at once, so that this can be scaled for bigger datasets

import numpy as np

PrimaryData = '''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''
type(PrimaryData)
SecondaryData = PrimaryData.split('\n')
SecondaryData
SecondaryData[-1]
len(SecondaryData)


# In[169]:


Rows={}
for x in range(len(SecondaryData)):
        Rows["string{0}".format(x)] = SecondaryData[x]
Rows
Rows["string1"]


# In[105]:


#Calling element of the dictionary using custom name
name = 'string'+str(1)
name
Rows[name]
type(Rows[name])
ListOfRow1 = Rows[name].split(' ')
ListOfRow1
type(ListOfRow1)
ListOfRow1[0]


# In[165]:


# Converting list elements to numbers in a new array

ArrayData = np.empty((20,20))
for i in range(len(ArrayData)):
    #print(i)
    name = 'string'+str(i)
    #print(Rows[name].split(' '),type(Rows[name].split(' ')))
    #print(np.asarray(Rows[name].split(' ')))
    ArrayData[i,0:20] = np.asarray(Rows[name].split(' '))
print(ArrayData)

#Now this numpy array can be used for 


# # Now to answer the question:
# # What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
# 
# # Five loops doing these 5 different tasks and comparing greatest output should do the job.

# In[172]:


#DiagonalSlash

#np.shape(ArrayData)
#np.shape(ArrayData)[0]
#int(np.shape(ArrayData)[0])
Greatest = 0
for i in range(np.shape(ArrayData)[0]-3):
    for j in range(np.shape(ArrayData)[0]-3):
        GreatestTemporary = 1
        GreatestTemporary = GreatestTemporary*ArrayData[i,j]*ArrayData[i+1,j+1]*ArrayData[i+2,j+2]*ArrayData[i+3,j+3]
        if GreatestTemporary > Greatest:
            Greatest = GreatestTemporary
            print(i,j,ArrayData[i,j],ArrayData[i+1,j+1],ArrayData[i+2,j+2],ArrayData[i+3,j+3])

DiagonalSlash = int(Greatest)
print(DiagonalSlash)


# In[163]:


#DiagonalBackSlash

#np.shape(ArrayData)
#np.shape(ArrayData)[0]
#int(np.shape(ArrayData)[0])
Greatest = 0
for i in range(np.shape(ArrayData)[0]-3):
    for j in range(3,np.shape(ArrayData)[0]):
        GreatestTemporary = 1
        GreatestTemporary = GreatestTemporary*ArrayData[i,j]*ArrayData[i+1,j-1]*ArrayData[i+2,j-2]*ArrayData[i+3,j-3]
        if GreatestTemporary > Greatest:
            Greatest = GreatestTemporary
            print(i,j,ArrayData[i,j],ArrayData[i,j],ArrayData[i+1,j-1],ArrayData[i+2,j-2],ArrayData[i+3,j-3])

DiagonalBackSlash = int(Greatest)
print(DiagonalBackSlash)


# In[155]:


#Down            # Same as up theoretically

#np.shape(ArrayData)
#np.shape(ArrayData)[0]
#int(np.shape(ArrayData)[0])
Greatest = 0
for i in range(np.shape(ArrayData)[0]-3):
    for j in range(np.shape(ArrayData)[0]):
        GreatestTemporary = 1
        GreatestTemporary = GreatestTemporary*ArrayData[i,j]*ArrayData[i+1,j]*ArrayData[i+2,j]*ArrayData[i+3,j]
        if GreatestTemporary > Greatest:
            Greatest = GreatestTemporary
            print(i,j,ArrayData[i,j],ArrayData[i+1,j],ArrayData[i+2,j],ArrayData[i+3,j])

GreatestDown = int(Greatest)
print(GreatestDown)


# In[156]:


#Right            # Same as up left

#np.shape(ArrayData)
#np.shape(ArrayData)[0]
#int(np.shape(ArrayData)[0])
Greatest = 0
for i in range(np.shape(ArrayData)[0]):
    for j in range(np.shape(ArrayData)[0]-3):
        GreatestTemporary = 1
        GreatestTemporary = GreatestTemporary*ArrayData[i,j]*ArrayData[i,j+1]*ArrayData[i,j+2]*ArrayData[i,j+3]
        if GreatestTemporary > Greatest:
            Greatest = GreatestTemporary
            print(i,j,ArrayData[i,j],ArrayData[i,j+1],ArrayData[i,j+2],ArrayData[i,j+3])

GreatestRight = int(Greatest)
print(GreatestRight)


# In[164]:


print(max(GreatestRight,GreatestDown,DiagonalBackSlash,DiagonalSlash))

# Answer is 70600674