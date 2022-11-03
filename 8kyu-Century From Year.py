# DESCRIPTION:
# Introduction
# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

# Task
# Given a year, return the century it is in.

# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20

# FUNDAMENTALS MATHEMATICS

def century(year):

    a=year//100

    message=year%100

    if message==0:
            b=0
    if 0< message<100:
            b=1

    return a+b

