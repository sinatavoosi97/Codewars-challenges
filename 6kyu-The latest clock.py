def latest_clock(a, b, c, d):

    if a==0 and b==0 and c==0 and d==0:
         
         return f"{0}{0}:{0}{0}"

    numbers=[]

    def make_number(k):

        l=k+59

        for i in range (k,l+1):

            if k < 1000:

                number="0"

                numbers.append(number+f"{i}")

            else:
                numbers.append(f"{i}")



        return numbers


    number_01=[100,200,300,400,500,600,700,800,900,1000,
            1100,1200,1300,1400,1500,1600,1700,1800,
            1900,2000,2100,2200,2300]


    number_02=[]

    for item in number_01:
            for object in (make_number(item)):
                
                number_02.append(object)


    
    
    combination=[f"{c}{d}{a}{b}",f"{c}{d}{b}{a}",f"{c}{a}{d}{b}",f"{c}{a}{b}{d}",
                 
                f"{d}{a}{c}{b}",f"{d}{a}{b}{c}",f"{d}{b}{c}{a}",f"{d}{b}{a}{c}",

                f"{c}{b}{d}{a}",f"{c}{b}{a}{d}",f"{d}{c}{a}{b}",f"{d}{c}{b}{a}",

                f"{a}{c}{d}{b}",f"{a}{c}{b}{d}",f"{a}{d}{c}{b}",f"{a}{d}{b}{c}",

                f"{a}{b}{c}{d}",f"{a}{b}{d}{c}",f"{b}{c}{d}{a}",f"{b}{c}{a}{d}",

                 f"{b}{d}{c}{a}",f"{b}{d}{a}{c}",f"{b}{a}{c}{d}",f"{b}{a}{d}{c}"]


    Num=[]
    for item in  number_02:
         if item in combination:
              
              Num.append(item)



    message=f"{Num[-1][0]}{Num[-1][1]}:{Num[-1][2]}{Num[-1][3]}"


    return message           
                 
                 
          

print(latest_clock(2,4,0,0))








                        
                  

                
            



