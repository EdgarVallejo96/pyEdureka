# types of inheritance
# Single, multiple, multilevel, hierarchical
# Single: When inheritance involves one child class and one parent class
# Multiple: Involves more than one parent class
# Multilevel: The child class acts as a parent class for another child class
# Hierarchical: More than one type of inheritance

print('Single Inheritance')
class Parent:
    def func1(self):
        print("this is function 1")

class Child(Parent):
    def func2(self):
        print('this is function 2')

ob = Child()
ob.func1()

