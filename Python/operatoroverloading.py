class point :
    def __init__(self , x , y ) :
        self.x = x 
        self.y = y 
        
    def __str__(self) : # special function 
        return "({0},{1})".format(self.x,self.y)
    
    def __add__(self,other) : # operator overloading 
        x = self.x + other.x
        y = self.y + other.y
        return point(x,y)

p1 = point(5,3)
p2 = point(8,2)

print(p1+p2)

