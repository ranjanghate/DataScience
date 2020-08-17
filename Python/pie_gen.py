from  random import uniform 

def piegen(n) :
    
    count = 0 
    total = 0
    for i in range(0,n) :
        x=uniform(0,1)
        y=uniform(0,1)
        
        distance = x**2 + y**2
        if distance<=1 :
            count= count+1
        total = total +1 
    
    return (4*count)/total

print(piegen(100))
print(piegen(1000))
print(piegen(10000))