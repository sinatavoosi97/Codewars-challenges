
import math 
def find_next_square(sq):
    
    num1=(math.sqrt(sq))
    
    if int(str(num1)[-1])==0:
        
        num2=num1+1
        sq2=(num2**2)
        
        return int(sq2)
    
    else:
        return -1


print(find_next_square(319225))