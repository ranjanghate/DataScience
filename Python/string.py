#string are squence of character in python characters are encoded in Unicode
string = "Hello"
string = 'Hello'
string = ''' Hello'''

string = """Hello , welcome to python""" # triple quote string extend to multiple lines 

# accesing characters in string 
print(string[6])
print(string[-6])

#slicing a string 
print(string[2:8])

# string are immutable you can delete or change any element

del string 


# concate or repeat string 

str1 = "Hello"
str2 = " Ranjan"
str3=str1*3
print(str1+str2)
print(str3)

#iterating a string 

for letter in str1 :
    print(letter)
    
# check whether a letter in string exist or not

result = 'R' in str2
print(result)    

result = 'x' in str2
print(result)
