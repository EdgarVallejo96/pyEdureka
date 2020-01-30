# Hybrid Inheritance
# Has more than 1 type of inheritance
print('Hybrid Inheritance')

class Parent:
    def func1(self):
        print("this is function 1")

class Parent2(Parent): # Single Inheritance
    def func3(self):
        print('this is function 3')

class Parent3:
    def func4(self):
        print('this is function 4')


class Child(Parent, Parent3): # Multiple inheritance
    def func2(self):
        print('this is function 2')

ob = Child()
ob.func1()
ob.func4() 
