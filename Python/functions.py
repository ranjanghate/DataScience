#basic 
def greet(name):
    print("Hello!",name)

greet("Ranjan")

#two arguments 

def greet(name , msg ) :
    print("Hello!",name,",",msg)
greet("Ranjan" , "kya kr rha h ?")    

#default arguments 

def greet(name , msg="Ohaio"):
    print("Hello!",name,",",msg)

greet("Ranjan","Itadakimasu")
greet("Ranjan")

#keyword arguments 

greet(name="itadakimasu",msg="Ranjan")

#arbitary arguments 

def greet(*names) :
    print(names)

greet("Ranjan","Ghate")


#lambda/anonymous functions

square = lambda x,y:x+y #declare

print(square(5,10)) #call 

