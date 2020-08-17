#open a file 

f = open("text.txt")
#opening using directory f = open("R:\Code\DataScience\Python\text.txt")
print(f)
# mode of file opening 

f = open("text.txt",'w') # write in text mode
f = open("text.txt",'r+b') # read in binary mode

# encoding type
f = open("text.txt",'r',encoding='utf-8') # read in text mode encoded in utf-8

# closing a file

f.close() # not safe

# closing file safely

try :
    f = f.open("text.txt",'w')
    # perform the program
finally :
    f.close()

# closing file using with 

with open("text.txt") as f :
    #perform action

with open("text.txt",'w') as f :
    f.write("First line\n")
    f.write("Second line\n")
    
    