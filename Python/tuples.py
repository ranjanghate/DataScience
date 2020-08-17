#tuples are same as list but they are not mutable
tple = ()
tple1 =(1,2,3)
tple2 = (1,"Hello",3.14)
tple3 = (1,[1,2],45.45) # tuple containing list

tple4 = 3,4.6 , "dog" # creatingg tuple without parantheses

# creating tuple with one item 
tple = ("Hello" ,) 
tple2 = "Hello" , # need comma at the end without comma it will be considered as a  string 

# accesing tuple elments 
tple = ('a','b','c','d')
print(tple[1],tple[3],tple[-1])

# Slicing 
python = ('p','y','t','h','o','n')
print(python[2:4])
print(python[0:-3])
print(python[-1:6])

# changing tupple elements 
 #you cannot change a tuple element but if tupple contain mutable element it can be changed
 
# using + and * operator 

tple1 = (1,2,3)
tple2 = (4,5,6)
print(tple1+tple2)
tple3 = tple1*3
print(tple3)

# deleteing a Tuple 

del tple # you can remove a single element from tuple 

# count and index
tple1 = ('a','b','c')
print(tple1.count(2)) # count returns the  frequency of 'x' in tuple 
print(tple1.index('b')) # index returns the index of value 'x'