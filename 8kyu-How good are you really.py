# DESCRIPTION:
# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.

# You receive an array with your peers' test scores. Now calculate the average and compare your score!

# Return True if you're better, else False!

# Note:
# Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!

# FUNDAMENTALS

def better_than_average(class_points,your_points):
    
    sum=0
    for item in class_points:
        sum+=item
    
    average=sum/len(class_points)
    
    if your_points>average:
        message=True
    else:
        message=False

    return message

print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))


