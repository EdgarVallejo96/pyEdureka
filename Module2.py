# from Module import divide # This is for only importing the divide function
import Module as md

addition = md.add(10, 15)
print(addition)

# Built in modules
# Are written in C and interpreted using the python interpreter.
import sys
a = sys.builtin_module_names
print(a)

from matplotlib import pyplot
print(dir(pyplot))