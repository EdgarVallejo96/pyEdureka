# NUMBER
x = 10
print(x)
print(type(x))

# Float
x = 10.15
print(x)
print(type(x))

# Complex
x = 13j
print(x)
print(type(x))

# Boolean
x = 10 > 9
print(x)
print(type(x))

# STRING
x = 'hello'
y = "hello"
# z = input() # User enters a value

name = "Edgar"

print(len(name))

z = 10
print('Here is an example', x, y, z)

print(name[2])
# name[2] = 10 no se puede hacer

print(name[2:4]) # Excluyendo el último valor
print(name[4:2]) # no funciona al revez

print(name.upper())
print(name.lower())

print(name[-2]) # Va de último para lo primero


# LIST
mylist = [10, 20, 30, 40, 'hola', 'hello']

print(mylist)

print(mylist[2:4])

# change a value
mylist[2] = 'edgar'
print(mylist)

# add value
mylist.append(1000) # add value at the end
print(mylist)

mylist.insert(1, 1234) # insert in the index specified
print(mylist)

# reverse list
mylist.reverse()
print(mylist)


# DICTIONARIES
# characteristis: unordered, can be changes, no duplicates present in keys, only in values
print('DICTIONARIES')
courses = { 1: 'python',
            2: 'data science',
            'third': 'machine learning'}
print(courses)
print(courses['third']) # get third value
print(courses[1])
print(courses.get('third')) # same thing

# update value
courses[1] = 'hello bro'
print(courses)

# add value
courses["1"] = 'hello world'
print(courses)


# TUPLE
# characteristics: ordered, cannot be changed, duplicates are present, it is inmutable just like a string
print()
animals = (10, 20, 30, 'tiger', 'lion', 'giraffe', 'tiger')
print(animals)
print(animals[2])
print(animals.count('tiger')) # count the times that the specified word appears in the tuple
print(type(animals))


# SET, unordered, no duplicates entries are present
myset = {10, 20, 30, 40, 40, 30, 'edureka', 'courses'}

# when printed, it doesn't show the values that are repeated
print(myset) # not supports indexing, always shows a random order when the values are printed

# RANGE
range(0,10) # creates a list of values from 0 to 10

# print the range
print(list(range(11)))

a = [1,2,3,4]
b = {4,5,6,4,6}
c = [a, b] # can make list with other data types
print(c)


# TYPE CONVERSION
x = 10
name = 'name'

# int() = this function changes any data type to integer data type
# float() = this function changes any data type to float data type
# tuple() = this function changes any data type to tuple data type
# list() = this function changes any data type to list data type
# set() = this function changes any data type to set data type
# dict() = this function changes any data type to dict data type
# str() = this function changes any data type to string data type

print(str(x) + name)
print(list(b))
x = list(b)
x.append("hola")
print(x)