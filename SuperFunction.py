# Super Function
# Directly calls the parent class method
class Parent:
    def func1(self):
        print('this is function 1')

class Child(Parent):
    def func2(self):
        super().func1() # Super function
        print('this is function 2')


ob = Child()
ob.func2()