#basic
number = [1,2,3,5,6,7,8]
mixedlist=[1,2.4,'name']
nestedlist = [4,5,number,[1,5,'t']]

#accessing elements from list
print(number[0])
print(number[-1])

#slicing of list
print(number[1:3])

#changing elements 
number[0]=100
print(*number)

number[1:4]=['k','j','i']
print(*number)

#add element to list

odd=[1,3,5]
odd.append(7)
print(*odd)
odd.extend([9,11]) # extends merges two list while append add list element to a list
print(odd[4])

#using operators + *

one = [1,2,3]
two = [4,5,6]
print(one+two) 

three = one*3
print(three)

#insert method  (insert method doesnot replace element)
one.insert(1,9)
print(one)

#deleting items

num = [1,2,3,4,5,6,7,8,9]
del num[4]
print(num)
del num[2:6]
print(num)

# remove method (removing element by its value)

num = [1,2,3,4,5,6,7,8,9]

num.remove(1)
print(num)

#pop method (remove element by its value)
num.pop(5)
print(num)

# copying a list
list1 = [1,2,3]
list2 = list1

print(list2) # this is called aliasing , both the list is pointing to the same list 

list2.pop()
print(list1 , list2 ) # example of aliasing 


# using copy method or slicing to clone a list

list1 = [1,2,3,4,5]
list2 = list1.copy()
list3 = list1[:]

list2[1]="two"
list3[2]="three"
print(list1,list2,list3)

#iterating a list 

fruit = ["apple","mango","banana","orange"]

for x in fruit :
    print(x)
    
    
# nesting a list 

list1 = [1,2,3,[4,5,6]]
print(list1[1])
print(list1[3][2])

list1 = [1,2,3]
list2 = [4,5,6]
list1.append(list2)
print(list1[1])
print(list1[3][2])

# string to list 
string = "Helloo"
list1 = string.split() # list1 = [['H','e','l','l','o','o']]
print(*list1[0][1]) 