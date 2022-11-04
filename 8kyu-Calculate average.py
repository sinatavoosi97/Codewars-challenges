# DESCRIPTION:
# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.

# FUNDAMENTALS ARRAYS


def find_average(numbers):

    sum=0
    for item in numbers:
        if item==None:
            sum=0
        else:
            sum+=item
    
    average=sum/len(numbers)
    
    return average

print(find_average([1,2,3]))


