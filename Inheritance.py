class Car():
    # __init__ is a constructor and initializes the values of the variables
    # self is a reference to the object that is going to be calling this function
    def __init__(self, modelname, yearM, price):
        self.modelName = modelname
        self.yearM = yearM
        self.price = price

    def price_inc(self):
        self.price = int(self.price*1.15)

class SuperCar(Car): # The parameter is the parent class, the class that will inherit from
    def __init__(self, modelname, yearM, price, cc):
        super.__init__(modelname, yearM, price)
        self.cc = cc

honda = SuperCar('City', 2017, 1000000)
tata = Car('Bolt', 2016, 600000)

honda.cc = 1500
print(help(honda)) # 'help()' shows the sequence of operations
print(honda.yearM)
honda.price_inc()
print(honda.price)