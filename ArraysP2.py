import array as arr
a = arr.array('i', [ 1,2,3,4,5,6])
print(a)

# Accessing elements
print(a[2])
print(a[-2])

# BASIC ARRAY OPERATIONS
# Find length of array
print()
print('Length of array')
print(len(a))

# Adding elments to an array
# append() to add a single element at the end of an array
# extend() to add more than one element at the end of an array
# insert() to add an element at a specific position in an array
print()

# append
print('Append')
a.append(8)
print(a)

# extend
print()
print('Extend')
a.extend([9,8,6,5,4])
print(a)

# insert
print()
print('Insert')
a.insert(2,6) # first param is the index, second param is the value
print(a)

# Removing elements from an array
# pop() Remove an element and return it
# remove() Remove element with a specific value without returning it
print()
print(a)

# pop
print('pop')
print(a.pop()) # removes last element
print(a)
print(a.pop(2))
print(a)
print(a.pop(-1))
print(a)

# remove
print()
print('remove')
print(a.remove(8)) # doesn't return what it removes, it removed the first occurrence of '8'
print(a)

# Array Concatenation
print()
print('Array Concatenation')
b = arr.array('i', [1,2,3,4,5,6,7])
c = arr.array('i', [3,4,2,1,3,5,6,7,8])
d = arr.array('i')
d = b + c
print(d)

# Slicing an Array
print()
print('Slicing an Array') # This means fetching some particular values from an array
print(d)
print(d[0:5]) # Doesn't include the value on the right index
print(d[0:-2])
print(d[::-1]) # Reverse the array, this method is not preferred because it exauhsts the memory

# Looping through an Array
print()
print('Looping through an Array')
print('Using for')
for x in d:
    print(x, end=' ')
print()

for x in d[0:-3]:
    print(x, end=' ')
print()

print('Using while')
temp = 0
while temp < d[2]:
    print(d[temp], end = ' ')
    temp = temp + 1 # Can use temp+=1, it's the same thing

print()
print(a)
tem = 0
while tem < len(a):
    print(a[tem], end=' ')
    tem += 1
print()



