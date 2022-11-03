# DESCRIPTION:
# Simple, remove the spaces from the string, then return the resultant string.

# FUNDAMENTALS STRINGS

def no_space(x):

    c=""
    for item in x.split(" "):

        if not item=="":
            c+=item
    
    return c

