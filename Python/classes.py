#define
class newclass :
    a = 10
    def fun(self):
        print("hello")

# creating  a object
ob =newclass()
ob1 = newclass()
ob.fun()
print(ob.a)
ob.a=1 
ob1.a=100
print(ob.a)
print(ob1.a)

#object of same class name is also created

print(newclass.a)
newclass.a=5
ob2 = newclass()
print(ob2.a)