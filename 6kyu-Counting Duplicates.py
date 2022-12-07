def duplicate_count(text):
    list1=[]
    message=""
    for item in text:
        message+=item.lower()

    for i in range(len(message)):
        a=message.count(message[i])
        if a>1:
            list1.append(message[i])

    b={}
    for j in range(len(list1)):
        c=list1.count(list1[j])
        b[list1[j]]=c


    return len(b)
        







print(duplicate_count("abcdeaB"))