def is_pangram(s):

    list1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    count=0
    list2=[]
    for item in s:
        list2.append(str(item).lower())

    
    list3=list(dict.fromkeys(list2))




    for object in list3:
        if object in list1:
            count+=1



    if count==26:
        return  True
    else:
        return False




print(is_pangram("1bcdefghijklmnopqrstuvwxyz"))

