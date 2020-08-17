# key(must imutable for ex:- string , number or tuple ) : value pair (any data type)
dict1= {}
dict1 = {1:"apple",2:"boy"}
dict1 = {1:"apple",'two':2,3:[1,2,3]}
dict1 = dict({1:'one',2:'two',3:'three',4:'four'})

# accessing dictionary element 
person = dict({'name':"John",'age':24})

print(person['name'],person['age'])

#using get to access value (get return none if value not exist)
print(person.get('name'),person.get('age'))

#add & change in dictionary

person['salary']=60000
person['age']=25
print(person)

#remove dictionary item

value = person.pop('salary')
print(person)

arbitary_value_removed=person.popitem()
print(arbitary_value_removed)
print(person)

#using del in a dictionary
person = dict({'name':"John",'age':25,'salary':60000})
del person['salary']
print(person)
del person # deletes the whole dictionary 

person = dict({'name':"John",'age':25,'salary':60000})

person.clear() # empty the whole dictionary
print(person)

# iterating through dictionary 
squares  = { 1:1 , 2:4 , 3:9 , 4:16 }

for i in squares : # for key's 
    print(i)

for i in squares.values() :#for vlaues
    print(i)

for i,j in squares.items() :# for both key and value
    print(i,j)
    
# check if key exists (membership test )
print( 1 in squares)
print( 9 in squares) # 9 doesn't as a key so false


