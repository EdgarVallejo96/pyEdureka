# Generators
# Functions that return traversable objects
# Produce items one at a time and only when required
# Are run along with 'for' loops
# Advantages
# Easy to implement (implement _iter_(), __next__() automatically)
# Better management and utilization
# Can be used to produce infinite items
# Can also be used to pipeline a number of operations

# Normal functions vs Generators
# Generators functions:
    # Make use of 'yield' keyword
    # Run when 'next()' method is called
    # produce items one at a time and only when required
# normal functions
    # Make use of 'return' keyword
    # Run when name of the method is called
    # Produce all the items at once
print('Generator 1')
def new(dict):
    for x, y in dict.items():
        yield x, y
a = {1: 'hi', 2: 'welcome'}
b = new(a)
print(b)
print(next(b)) # To pass to the first key and value of the dictionary
print(next(b))

print()
print('Generator 2')
def myfunc(i):
    while i<=3:
        yield i
        i+=1
j = myfunc(2)
print(next(j))
print(next(j))

print()
print('Generator 3')
def ex():
    n = 3
    yield n
    n = n*n
    yield n
v = ex()
# print(next(v))
# print(next(v))

# Generators with loops
print()
print('Generators with loops')
for x in v:
    print(x)

# Generator Expressions
# They resemble list comprehensions and like lambda functions
# They create anonymous generator functions
print()
print('Generator Expressions')
f = range(6)
print("List comprehension", end=":")
q = [x+2 for x in f] # List comprehension: From 2 until it has 6 values
print(q)
r = (x+2 for x in f) # Generator expression: From 2 until it has 6 values
print(r)
print(min(r))
for x in r:
    print(x)

# Use cases
# Fibonacci Series
print('Fibonacci')
def fib():
    f, s = 0, 1
    while True:
        yield f
        f, s = s, f+s
for x in fib():
    if x>50:
        break
    print(x, end=" ")

# Number Stream
print()
print('Number Stream')
a = range(100)
b = (x for x in a)
print(b)
for y in b:
    print(y)

print()
print('Number Stream with odd or even values')
a = range(2,100,2)
b = (x for x in a)
print(b)
for y in b:
    print(y)

# Sinewave
print()
print('Sinewave')