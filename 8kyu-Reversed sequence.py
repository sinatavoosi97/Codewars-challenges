# DESCRIPTION:
# Build a function that returns an array of integers from n to 1 where n>0.

# Example : n=5 --> [5,4,3,2,1]

# FUNDAMENTALS

def reverse_seq(n):
    list1=[]
    list2=[]

    for i in range(1,n+1):
        list1.append(i)

    for i in range(1,len(list1)):

        list2.append(list1[-i])


    list2.append(1)
    
    return list2



print(reverse_seq(6))

