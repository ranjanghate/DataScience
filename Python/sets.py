# set is an unordered and sorted collection of items with no duplicate

sets = {1,2,3}
sets = {1,"two",3.00,(2,3)}

list1 = [1,4,5,1,4,5]
sets = set(list1)
print(list1,sets)

# create a empty set
sets = {}#its a dictionary
sets = set() # we use set function to create a empty set

# Add and update in set (index has not meaning in set because they are unordered)
sets = set(list1)
sets.add(2)
print(*sets)
sets.update([3,6,7]) # update() take input as list , tuple ,string or set
print(*sets)

# removing elements from sets

sets.discard(5)
print(*sets)
sets.remove(6)
print(*sets)

# pop and clear 

sets.pop() # removes an random element from set
print(*sets)
sets.clear()# delete all element from set 
print(*sets)


# python set operations 

A = {1,2,3}
B = {2,3,4,5}

print(A|B,A.union(B),B.union(A)) #union
print(A&B,A.intersection(B),B.intersection(A)) #intersection
print(A^B,B^A,A.symmetric_difference(B),B.symmetric_difference(A)) # symetric difference
print(A-B,B-A,A.difference(B),B.difference(A)) # difference 

# set iteration
for em in A :
    print(em)
    
# check if element exist in set or not 

print(1 in A)
print('1' in A)
