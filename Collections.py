# COLLECTION DATA TYPES
# Lists, tuples, sets, dictionary

# LISTS
# Declared in square brackets
# Values can be changed
# Stores duplicate values
# Can use indexes

# TUPLES
# Ordered
# Inmutable (can't change values)
# Can have duplicate values

# SET
# Unordered
# Declared in curly brackets {}
# Doesn't have indexes
# Doesn't show duplicate entries

# DICTIONARY
# Has key: value pairs
# Mutable (can change values)
# Use curly brackets to declare a dictionary


# SPECIALISED COLLECTIONS DATA TYPES
# namedtuple(), Chainmap, deque, Counter, OrderedDict, defauldict, UserDict, UserList, UserString4

# NAMEDTUPLE
# Returns a tuple with a named value for each element in the tuple
print('NAMEDTUPLE')
from collections import namedtuple
a = namedtuple('courses', 'name, technology')
s = a('data science', 'python')
print(s)

s = a._make(['artificial intelligence', 'python'])
print(s)

# DEQUE
# Pronounced as 'deck'is an optimised list to perform insertion and deletion easily.
print()
print('DEQUE')
from collections import deque
a = ['e', 'd', 'u', 'r', 'e', 'k', 'a']
d = deque(a)
print(d)
d.append('python')
print(d)

d.appendleft('python')
print(d)

d.pop() # delete last value of the list
print(d)

d.popleft()
print(d)

# CHAINMAP
# Is a dictionary like class for creating a single view of multiple mappings
print()
print('CHAINMAP')
from collections import ChainMap
a = {1: 'edureka', 2: 'python'}
b = {3: 'ML', 4: 'AI'}

a1 = ChainMap(a,b)
print(a1)

# COUNTER
# Is a dictionary subclass for counting hashable objects
print()
print('COUNTER')
from collections import Counter
a = [1,1,2,3,4,4,5,6,4,33,6,7,8,4,2,3]
c = Counter(a)
print(c)

print(list(c.elements())) # returns the list of the elements in certain order

print(c.most_common()) # returns a better visualization of the dictionary

sub = {2:1, 6:1} # Subtract 2 1 time, and subtract 6 1 time
print(c.subtract(sub)) # Subtract function
print(c.most_common())

# ORDEREDDICT
# Is a dictionary subclass which remembers the order in which the entires were done
print()
print('OREDEREDDICT')
from collections import OrderedDict
d = OrderedDict()
d[1] = 'e'
d[2] = 'd'
d[3] = 'u'
d[4] = 'r'
d[5] = 'e'
d[6] = 'k'
d[7] = 'a'
print(d)

print(d.keys())

d[1] = 'p'
print(d)

# DEFAULTDICT
# Is a dictionary subclass which calls a factory function to supply missing values
print()
print('DEFAULTDICT')
from collections import defaultdict
d = defaultdict(int)
d[1] = 'python'
d[2] = 'edureka'
print(d)
print(d[3]) # output with defaultdict

# comparisson with normal dictionary
a = {1: 'python', 2: 'edureka'}
print(a[3]) # this gives an error

# the difference with defaultdict is that it returns a '0' instead of an error

# USERDICT
# Is a wrapper around dictionary objects for easier dictionary sub-classing
# USERLIST
# Is a wrapper around list objects for easier List sub-classing
# USERSTRING
# Is a wrapper around string objects for easier string sub-classing
print()
print('USERDICT')
print('USERSTRING')
print('USERSTRING')

