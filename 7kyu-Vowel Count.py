# DESCRIPTION:
# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

# STRINGS FUNDAMENTALS


def get_count(sentence):

    count=0
    if sentence=="":
        return 0


 
    for item in sentence:
        if item=="a" or item=="e"  or item=="i" or item=="o" or item=="u" :

            count+=1

    return count

