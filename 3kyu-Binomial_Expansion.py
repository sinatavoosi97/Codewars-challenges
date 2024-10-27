

def expand(expr):


    Mazareb=[]

    b_list=[]

    X_list=[]

    x=[]

    y=[]

    expr_list=[]


    for tex in expr:

        expr_list.append (tex)

    e=0

    for tex_b in expr_list:


        if tex_b==")":
              
              x.append(e)


        if tex_b=="+" or tex_b=="-" :
             
             y.append(e)

        e+=1



    
    len_b=max(x)-max(y)


    b=""

    for k in range(max(y),max(x)):

         b+=(expr[k])


    def factoriel(N):

            N_factoriel=1

            for i in range(N,1,-1):

                N_factoriel*=i

            return N_factoriel


    K_factoriel_list=[]

    for i in range(0,int(expr[-1])+1,+1):

        K_factoriel_list.append(factoriel(i))

        b_list.append(int(b)**i)


    NK_factoriel_list=[]

    for j in range(0,int(expr[-1])+1):
        
        NK_factoriel_list.append(factoriel(int(expr[-1])-j))

 
        if  j < int(expr[-1]) :

            if (int(expr[-1])-j)==1:

                
                X_list.append(expr[max(y)-1])

            else:
                
                X_list.append(f"{expr[max(y)-1]}^{(int(expr[-1])-j)}")


    for p in range(int(expr[-1])+1):
        
        Mazareb.append((factoriel(int(expr[-1])))/((K_factoriel_list[p])*(NK_factoriel_list[p])))



        
    e_a=0

    x_a,y_a=[],[]

  
    for tex_a in expr_list:


        if tex_a=="(":
              
              x_a.append(e_a)


        if tex_a=="+" or tex_a=="-" :
             
             y_a.append(e_a)

        e_a+=1

        
    len_a=(max(y_a)-2)-(max(x_a))


    a1=""

    if (max(x_a))+1==(max(y_a)-2)+1:
         
         a1+="1"

    else:

        for k1 in range((max(x_a))+1,(max(y_a)-2)+1):

                a1+=(expr[k1])





    a_list=[]

    if a1=='-':
        
        a=-1
    else:
        a=int(a1)



    for l in range(0,int(expr[-1])+1):
        
            if  l < int(expr[-1])+1 :

                a_list.append(a**(int(expr[-1])-l))


    Mazareb_finall=[]

    for t in range (int(expr[-1])+1):
        
        Mazareb_finall.append(a_list[t]*b_list[t]*Mazareb[t])


    txt=""

    text=""

    message1=[]

    message2=""

    if int(expr[-1])==0:

        txt+="1"

    elif  int(expr[-1])==1:

        txt+=expr[1:-3]

    else:

        if int(Mazareb_finall[0])==1:

            for q in range(len(Mazareb_finall)-1):
                
                if q==0:
                
                        message1.append(""+str(X_list[q]))

                else:
                        message1.append(str(int(Mazareb_finall[q]))+str(X_list[q]))

        elif int(Mazareb_finall[0])==-1:

            for q in range(len(Mazareb_finall)-1):
                
                if q==0:
                
                        message1.append("-"+str(X_list[q]))

                else:
                        message1.append(str(int(Mazareb_finall[q]))+str(X_list[q]))

        else:
             
            for q in range(len(Mazareb_finall)-1):
                
                    message1.append(str(int(Mazareb_finall[q]))+str(X_list[q]))


        message1.append(str(int(Mazareb_finall[-1])))


        message2=[]

        for y in range(int(expr[-1])):

            if  int(Mazareb_finall[y+1]) > 0:
                 
                message1[y]+="+"

                message2.append(message1[y])

            else:
                 
                 message2.append(message1[y])

            
        message2.append(message1[-1])



        for object in message2:
             
             txt+=object

            
    return  txt



print(expand("(-w-16)^5"))


