# TYPE OF OPERATORS IN PYTHON
# Arithmetic
# Assignment
# Comparison
# Logical
# Membership
# Identity
# Bitwise

# Arithmetic operators: Used to perform arithmetic operations between variables
# +, -, *, /, %, **, //
x = 10
y = 20
# Arithmetic Operators
print('Arithmetic Operators')
print(x+y)
print(x-y)
print(x*y)
print(x**y)
print(x/y)
print(x//y) # Shows the int value, taking out the decimals
print(x%y)

# Assignment operators
# Are used to assign values
# Operator | Example
# = | x = 10
# += | x += 10
# -= | x -= 10
# *= | x *= 10
# %= | x %= 10
# **= | x **= 10
# //= | x //= 10
# |= | x |= 10
# ^= | x ^= 10
# &= | x &= 10
print()
print('Assignment operators')
x = 100
x += 10 # Is equal to x = x + 10
a = 5 # Assigning the value '5' to the variable
a += 5
print(a)
a **= 5
print(a)

print()
print('Comparison Operators')
# Comparison operators
# Used to compare two values
# == Equal
# != Not Equal
# >  Greater than
# <  Less than
# >= Greater than or equal
# <= Less than or equal
val = 10
num1 = 20
compare = val == num1
print(compare)

print()
print('Logical Operators')
# Logical Operators
# Used to combine conditional statements
# Conditional statements
print('Conditional statements')
if val == num1:
    print('equal')
elif val > num1:
    print('greater')
else:
    print('smaller')
x = 10
print(x > 10 and x > 5)
print(x > 8 and x > 5)
not(x > 10 and x > 5) # Get the opposite value of the statement

print()
print('Identity Operators')
# Identity Operators
# Used to compare objects
# We have: IS and IS NOT
# IS: Returns true if both variables are same object
# IS NOT: Returns true if both variables are not same object
list1 = [10, 20, 30]
list2 = [10, 20, 30]
x = list1
print(x is list1)
print(list1 is list2) # False because they are not the same object, same type, but not same objects
print(list1 is not list2) # Even though they have the same values, they are not the same object

print()
print('Membership operators')
# Memebership operators
# Used to check if a sequence is present in an object
# We have: IN and NOT IN
# IN: Returns true if a sequence with the specified value is present in the object
# NOT IN: Returns true if a sequence with the specified value is not present in the object
print(x in list1)
print(list1 in list2)
print(10 in list1)
print([10, 20, 30] in list2) # Only recognizes one value in the list of values inside the variable
list1.append('banana')
print('banana' in list1)

list1 = [10, 20, 30]
list2 = [10, 20, 30]
print(list1 == list2)
print(list1 is list2) # False because they are two different objects

print()
print('Bitwise operators')
# Bitwise operators
# Used to compare binary numbers
# & Bitwise AND: Sets each bit to 1 if both bits are 1
# | Bitwise OR: Sets each bit to 1 if one of the bits is 1
# ^ Bitwise XOR: Sets each bit to 1 if only one of the bits is 1
# ~ Bitwise NOT: Inverts all bits
# << Left Shift: Shift left by pushing in zeroes from the right and let the leftmost bits fell off
# >> Right Shift: Shifgt right by pushing copies of the leftmost bit in from the left, and let the rightmost bit fall off
print(10 & 12) # 1010 1100: 1000
print(10 | 12) # 1010 1100: 1110
print("{0:b}".format(8)) # Print parameter as binary
print('right shift')
print(10 >> 2) # We are right shifting 2 bits, so instead of '1010' we have '10'
print('left shift')
print(10 << 2) # It adds two 00 to the right, so instead of '1010' now it is '101000'





