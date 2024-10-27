
def permutations(s):
     
    text=s

    keys_A=[]

    values_A=[]

    for tx in text:
         
         keys_A.append(tx)


    keys_A1=set(keys_A)

    keys_A2=list(keys_A1)



    for i in range (1,len(text)+1):
          
          values_A.append(i)

         
    Alphabet=dict(zip(keys_A2,values_A))
              

    Alphabet_num=dict(zip(values_A,keys_A2))


    Alphabet_value=[]

    numbers=[]

    world_list=[]

    number_1=""


    if len(text)==1:

        world_list.append(text)

        return world_list

    else:

        for item in text:


            Alphabet_value.append(Alphabet[item])


        for i in range(((10**(len(text)-1))-1),(10**(len(text)))):

            i+=1

            numbers.append(i)



    val_set=set(Alphabet_value)


    val_list=list(val_set)



    def check(j,objects):

        lis=[]

        for object in objects:
                
                if str(val_list[j]) in str(object):
                    
                    lis.append(object)

        return lis

            
    lis_F1=[]
    lis_F1.append(check(0,numbers))
    
    for i in range(1,len(val_list)):
         
        lis_F1.append(check(i,lis_F1[i-1]))
         
        

    
    lis_F=lis_F1[-1]


    Num=[]
    for item in lis_F:
        for txt in str(item) :
            b=int(txt)
            if b not in Alphabet_value:
                    Num.append(item)


    Num_01=set(Num)

    Num_02=list(Num_01)


    for num1 in Num_02:
         
         lis_F.remove(num1)


  
    sumation=[]
    lis_F1=[]
    c=sum(Alphabet_value)

    for num2 in lis_F:
        sum_1=0
        for num3 in str(num2):
            sum_1+=int(num3)

        if sum_1==c:

            sumation.append(sum_1)

            lis_F1.append(num2)


    message=""
    for num4  in  lis_F1:
        message=""
        for world in str(num4):
              d=int(world)
              message+=Alphabet_num[d]

        
        world_list.append(message)
              

    return  world_list



print(permutations("abcd"))


     




