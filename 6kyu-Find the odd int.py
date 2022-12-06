def find_it(seq):
    list1=[]
    for item in seq:
        a=seq.count(item)
        list1.append(item)
        list1.append(a)

    for i in range(len(list1)):

        if list1[2*i+1]%2!=0:
            return list1[2*i]


print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))