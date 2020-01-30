# Map-Reduce Functions
# map(): Applies a given function to all the iterables and returns a new list
# filter(): Creates an output list consisting of values for which the function returns true
# reduce(): applies a given function to the iterables and returns a single value

# map: Es un cambio a cada uno de los valores
# filter: es como un condicional
# reduce: como el resultado de una sumatoria de todos los valores

# map function
print('map function within another function')
def new(a):
    return a*a
x = map(new, [1,2,3,4])
print(x)
print(list(x)) # can use tuple, sets, etc
print()
print('map function within another function with 2 parameters')
def new(a,b):
    return a*b
x = map(new, [1,2,3,4], [2,3,4,5])
print(x)
print(tuple(x))
print()
print('map function with lambda')
lst = [1,2,3,4,5]
y = list(map(lambda x: x+3, lst))
print(y)

# filter function
print()
print('filter function within another function')
def new1(i):
    if i>=3:
        return i
j = filter(new1, (1,2,3,4,5,6,7))
print(j)
print(tuple(j))
print('filter function with lambda')

z = filter(lambda x: (x>=3),(1,2,3,4,5,6,7))
print(list(z))

# reduce function
print()
print('reduce function within another function')
from functools import reduce
def a(x,y):
    return x+y
s = reduce(a,[1,3,4,5,6,7,7,8,8])
print(s)
print('reduce function ith lambda')
z = reduce(lambda q,p: q*p, [1,2,3,4,5,6,7,8,9])
print(z)

# filter() within map()
print()
print('filter() within map()')
c = map(lambda x: x+x, filter(lambda x: (x>=4),[2,3,4,5]))
print(tuple(c))

# map() within filter()
print()
print('map() within filter()')
d = filter(lambda x: (x>=4), map(lambda x: x+x, [2,3,4,5,6]))
print(set(d))

# map() and filter() within reduce()
print()
print('map() and filter() within reduce()')
r = reduce(lambda x,y: x+y, map(lambda x: x+x, filter(lambda x: (x<=4), [1,2,3,4,5,6,7])))
print(r)