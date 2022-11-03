# DESCRIPTION:
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F

# STRINGS FUNDAMENTALS

def abbrev_name(name):

    b=""
    name.split(" ")

   
    for item in (name.split(" ")):

        b+=str(item[0])
                  
    c=""
    c+=b[0].upper()
    c+="."
    c+=b[1].upper()

    return c


name="patrick feeney"

print(abbrev_name(name))

