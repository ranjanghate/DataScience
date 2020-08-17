class polygon :
    def __init__(self , no_of_sides) :
        self.n = no_of_sides 
        self.sides=[]
        for i in range(no_of_sides) :
            self.sides.append(0)    
    def input_sides(self) :
        for i in range(self.n) :
            self.sides[i]=float(input("Enter side"+str(i+1)+" "))
    
    def display_side(self) :
        print(self.sides)

class triangle(polygon) :
    def __init__(self):
        polygon.__init__(self,3)
    def area(self) :
        a,b,c = self.sides
        s = (a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c))**0.5

tri = triangle()
tri.input_sides()
print(tri.area())