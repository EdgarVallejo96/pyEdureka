# Functions
# First-class Object: In python, everything is treated as an object including all the data types, functions too.
# Therefore, a function is also known as a first-class object and can be passed around as arguments
# Inner-function: It is possile to define functions inside a function. That function is called an inner function.
print('First-class Object')
def func1(name):
    return f"Hello{name}"


def func2(name):
    return f"{name}, how you doin?"

def func3(func4):
    return func4('Dear learner')

print(func3(func1))
print(func3(func2))

print()
print('Inner function')
def func():
    print("first function")
    def func1():
        print('first child function')
    def func2():
        print("second child function")

    func2()
    func1()

func()

def functi(n):
    def functi1():
        return 'edgar'
    def functi2():
        return 'python'
    if n == 1:
        return functi1
    else:
        return functi2
a = functi(1)
b = functi(2)
print(a())
print(b())