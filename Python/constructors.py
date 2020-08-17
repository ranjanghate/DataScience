class point :
    def __init__(self , x=0 , y=0 ):
        self.x = x 
        self.y = y 
    
    def distance(self) :
        return (self.x**2+self.y**2)**.5

p1 = point(5,5)
dis = p1.distance()
print(dis)

#deleting attributes from an object

del p1.x

#deletinf objects 
del p1 