# DESCRIPTION:
# Given the triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

# 1 -->  1
# 2 --> 3 + 5 = 8
# ARRAYSLISTS MATHEMATICS FUNDAMENTALS

def row_sum_odd_numbers(n):    
    sum=0
    for i in range(1,n+1):
            sum+=i

    list1=[]
    for i in range(0,sum):
        list1.append(2*i+1)

    m=n
    a1=(m-1)*(n)+1


    list2=[a1]
    for i in range(n-1):

        list2.append(list2[i]+2)

    sum1=0
    for item in list2:
        sum1+=item

    return sum1



