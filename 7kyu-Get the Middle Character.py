# DESCRIPTION:
# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

# #Examples:

# Kata.getMiddle("test") should return "es"

# Kata.getMiddle("testing") should return "t"

# Kata.getMiddle("middle") should return "dd"

# Kata.getMiddle("A") should return "A"
# #Input

# A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.

# #Output

# The middle character(s) of the word represented as a string.

# FUNDAMENTALS STRINGS

def get_middle(s):


   
        list1=[]
        for item in s:
                list1.append(item)

        message=''
        if len(list1)%2==0:

                a=len(list1)/2
                a=int(a)
                message+=list1[a-1]
                message+=list1[a]

        elif not len(list1)%2==0:

                b=len(list1)/2
                b=int(b)
                message+=list1[b]
        

        return message

