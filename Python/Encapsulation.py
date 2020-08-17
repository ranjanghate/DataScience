class com :
    def __init__(self) :
        self.__maxprice = 900 # maxprice is a private element 
        
    def sell(self) :
        print("Selling price : {}".format(self.__maxprice))
    
    def setmax(self,price) :
        self.__maxprice= price 
        
c = com()
c.sell()

c.__maxprice=1000 # data encapsulation
c.sell()

c.setmax(1000)
c.sell()