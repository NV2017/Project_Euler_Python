# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# -*- coding: utf-8 -*-

# 015 Lattice paths

# https://projecteuler.net/problem=15

# Starting in the top left corner of a 2×2 grid, 
# and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20 x 20 grid?

# Need to move 20 times right, 20 times down.
# Every sequence of right and down is a unique path.

# So we need number of ways to choose 20 from 40.
# This is 40 C 20

# we can use choose function

import scipy.special

int(scipy.special.comb(40,20))

# Answer is: 137846528820