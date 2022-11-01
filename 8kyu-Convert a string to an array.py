# DESCRIPTION:
# Write a function to split a string and convert it into an array of words.

# Examples (Input ==> Output):
# "Robin Singh" ==> ["Robin", "Singh"]

# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]


def string_to_array(s):
    b=[]
    if s=="":
        b.append("")
        return b
    else:
        return s.split()


print(string_to_array("I love arrays they are my favorite"))