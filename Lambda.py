# Lambda functions
# Anonymous or namesless functions
# 'lambda' is a keyword
# Why are used
# One-time use: Also known as throw-away functions as they are needed just once
# I/O of other functions: They are also passed as inputs or returned as outputs of other higher-order functions
# The body of lambda functions is written in a single line
x = lambda a: a*a
print(x(3))

def new(a):
    return a*a
print(new(4))

# Anonymouse functions within user defined functions
print('Lambda within user-defined functions')
def func(x):
    return lambda y: x+y
t = func(4)
print(t(8))

def func(x):
    return lambda y: x+y
t = func(4)
print(t(8))
u = func(7)
print(u(5))

# Using lambda functions within filter(), map(), reduce()
print()
print('Using lambda within filter, map and reduce')

# filter(): Used to fitler the given iterables (lists, sets, etc)
# reduce(function, iterables)
# with the help of another function passed as an argument to test all the elements to be true or false
print('Using filter')
myList = [1,2,3,4,5,6]
newList = list(filter(lambda a:(a/3)==2, myList)) # SYNTAX: filter(function, iterables)
print(newList)

# map()
# map(function, iterables)
# Applies a given function to all the iterables and returns a new list
print()
print('Using lambda with map()')
myList = [1,2,3,4,5,6]
p = list(map(lambda a:(a/3!=2), myList))
print(p)

# reduce()
# reduce(function, sequence
# Applies som other function to a list of elements that are passed as a parameter to it and finally returns a single value
print()
print('Using lambda with reduce()')
from functools import reduce
x = reduce(lambda a,b: a+b, [23,56,43,98,1]) # Stars with the sum of the first two numbers, then sum with the third one, and so on
print(x)

# Solving algebraic expressions using lambda
print()
print('Lambda for Algebra')
print('Linear equations')
s = lambda a: a*a
print(s(4))
# 3x + 4y
d = lambda x,y: 3*x+4*y
print(4,7)
print('Quadratic equation')
# (a+b)^2
x = lambda x, y: (x+y)**2
print(x(4,4))