# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
# ARRAYS SORTING ALGORITHMS

def move_zeros(lst):

    list=[]
    for item in lst:
        if item==0:
          list.append(lst.index(item))   

    for object in list:
        lst.remove(0)


    for i in range(len(list)):
        lst.append(0)


    return lst

 

print(move_zeros( [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))