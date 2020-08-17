#write a file 

with open("test.txt",'w',encoding='utf-8') as f :
    f.write("HaHaHaHaHa\n")
    f.write("HoHoHoHoHo\n")

# reading a file 

x = open("test.txt",'r',encoding='utf-8') 
print(x.read(4))
print(x.read())

# seek and tell function

print(x.tell())
x.seek(0)
print(x.read(4))
x.seek(0)

# read file line by line
for z in x :
    print(z,end='')
    
#readline method 

x.seek(0)
print(x.readline())
print(x.readline())
