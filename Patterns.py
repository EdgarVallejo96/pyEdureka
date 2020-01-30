# Patterns
# Star Pattern Programs
# Star Pyramid Pattern
# Hald pyramid pattern
# Triangle pattern
# Hourglass pattern
# Diamond pattern
# Inverted Pyramid patterns

# Pyramid
print('Pyramid pattern')


def pattern(n):
    k = 2 * n - 2 # Can change this values to
    for i in range(0, n):
        for j in range(0, k):
            print(end=' ')
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print('\r') # Commeting this statement gives a different ouput


pattern(5)


# Inverse pyramid
print()
print('Inverse pattern')


def pattern2(n):
    k = 2 * n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


pattern2(10)
