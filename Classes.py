# class variable: Variable that is shared by all instances of a class
# instance variable: variables unique to each instance
# data member: class variable or instance variable that holds data associated with a class and its objects

class Car():
    # __init__ is a constructor and initializes the values of the variables
    # self is a reference to the object that is going to be calling this function
    def __init__(self, modelname, yearM, price):
        self.modelName = modelname
        self.yearM = yearM
        self.price = price

    def price_inc(self):
        self.price = int(self.price*1.15)

honda = Car('City', 2017, 1000000) # Al quitarle un cero el resultado es 114999, por qué? (Puede que sea porque se pasa de lo que vale un 'int' en python.
tata = Car('Bolt', 2016, 600000)

honda.cc = 1500
print(honda.__dict__) # dictinoary of all the variables of the object
print(tata.__dict__)

print(honda.price)
honda.price_inc()
print(honda.price)