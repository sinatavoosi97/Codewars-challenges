# DESCRIPTION:
# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).

# MATHEMATICS FUNDAMENTALS

def is_triangle(a, b, c):

    if ((a**2)+(b**2)==(c**2)) or (a<c+b and b<c+a and c<a+b) :
        return True
    
    elif a<0 or b<0 or c<0:
        return False
    
    else:
        return False

