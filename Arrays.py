# Array vs List
# Arrays store a single data type, lists can have any data type
import array
# the first parameter is a type code, it specifies the data types the array will hold
a = array.array('i', [1,2,3,4,5,6]) # First array is the array of the module, the second array is the name of the constructor

print(a)