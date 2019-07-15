# Solution Author: Arunabha Sarkar, https://github.com/NV2017

# 019 Counting Sundays

# https://projecteuler.net/problem=19

# You are given the following information, 
# but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, 
# but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century 
# (1 Jan 1901 to 31 Dec 2000)?

# Given: 1/1/1900 is Monday

# Coding logic can be found in my R repositoy
# Here, we utilise library of date to find the answer
# But for this answer, "Given: 1/1/1900 is Monday" should be correct
# Luckily we find it is

import datetime

answer = sum(1
		for year in range(1901, 2001)
		for month in range(1, 13)
        if datetime.date(year, month, 1).weekday() == 6)
# Monday == 0 & Sunday == 6
print(answer)

# Answer is 171