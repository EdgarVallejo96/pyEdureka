# ENCAPSULATION
# Binds the data and code together as a single unit
# Securing data by hiding the implementation details to user

# ABSTRACTION
# Hides the implementation details and only provides the functionality to the user
# Can be used with abstract classes and interfaces
# Helps users just focus on the main functionality, doesn't know what happens inside the car, just knows how to turn it on, use pedals and wheel
# They cannot be instantiated
# It can only be inherited

from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def price_inc(self):
        pass


class SuperCar(Car): # The parameter is the parent class, the class that will inherit from
    def __init__(self, modelname, yearM, price, cc):
        super.__init__(modelname, yearM, price)
        self.cc = cc

    def price_inc(self):
        self.price = int(self.price*2 )

honda = SuperCar('City', 2017, 1000000)
tata = Car('Bolt', 2016, 600000)

honda.cc = 1500
print(help(honda)) # 'help()' shows the sequence of operations
print(honda.yearM)
honda.price_inc()
print(honda.price)