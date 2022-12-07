def count(string):
    b={}
    for i in range(len(string)):
        a=string.count(string[i])
        b[string[i]]=a


    return b






print(count('aba'))