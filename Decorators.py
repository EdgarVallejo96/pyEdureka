# Decorators
# Modify the behavior of a function without modifying it permanently.
# It basically wraps another function and since both functions are callable,
# it returns a callable.
print('First way of doing decorators')
def function1(function):
    def wrapper():
        print("hello")
        function()
        print("welcome to python edureka tutorial")
    return wrapper
def function2():
    print("pythonista")
function2 = function1(function2)
function2()

print()
print("Second way of doing decorators")
def function1(function):
    def wrapper():
        print("hello")
        function()
        print("welcome to python edureka tutorial")
    return wrapper
@function1
def function2():
    print("pythonista")
function2()


# Arguments
# The special syntax, *args and **kwargs in function definitions is used to pass a variable number of arguments to a function.
# The single asterisk form (*args) is used to pass a non-keyworded, variable-length argument list,
# and the double asterisk form is used to pass a keyworded, variable-length argument list.
# https://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/

def function(function):
    def wrapper(*args, **kwargs):
        print('hello')
        function(*args, **kwargs)
        print('welcome to edureka python tutorial')
    return wrapper

@function1
def function2(name):
    print(f"{name}")

function2('waseem')