# DESCRIPTION:
# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

# FUNDAMENTALS

def find_short(s):


    c=[]
    for item in s.split(" "):
        c.append(len(item))
        c.sort()
        l=c[0]

    return l 

