# Python supports three types of loops: while, for, nested
# While
# Used when you don't know how many iterations are required
print('While')
count = 0
while count < 9:
    print("Number: ", count)
    count = count + 1
print("Good bye")

# Guessing number game
# import random
# n = 20 # Random number generated between 0 to 20
# to_be_guessed = int(n * random.random()) + 1 # Generates a random number between 0 to 20
# guess = 0
# while guess != to_be_guessed:
#     guess = int(input("New number: "))
#     if guess > 0:
#         if guess > to_be_guessed:
#             print("Number too large")
#         elif guess < to_be_guessed:
#             print("Number too small")
#     else:
#         print("Sorry that you're giving up!")
#         break
# else:
#     print("Congratulations. You made it!")

# For loop
# Used when you know the number of iterations that are required
fruits = ['mango', 'grapes', 'apple']
for fruit in fruits:
    print('Current fruit:', fruit)
print("Tschüs")

for i in range(2,11, 2):
    print(i)

# Factorial
num = int(input("Number:"))
factorial = 1

if num < 0:
    print("Must be positive")
elif num == 0:
    print("Factorial = 1")
else:
    for i in range(1, num + 1):
        factorial = factorial*i
print(factorial)

# Nested loops
# 3:33:25 They give an ATM example using nested loops

# Example with pythagorean numbers
# A Pythagorean number satisfies a^2 + b^2 = c^2
from math import sqrt
n = int(input("Maximal Number? "))
for a in range(1, n + 1):
    for b in range(a, n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if((c_square - c**2) == 0):
            print(a, b, c)

# For loop inside a while loop
travelling = input('yes or no:')
while travelling == 'yes':
    num = int(input('number of people travelling:'))
    for num in range(1, num + 1):
        name = input('Name:')
        age = input('Age:')
        sex = input('Male or Female:')
        print(name)
        print(age)
        print(sex)
    travelling = input('Oops! Forgot someone?')