# CREATING DICTIONARIES
# First Method: Using curly braces
print('Curly braces')
myDict = {'Dave': '001', 'Eva': '002', 'Joe': '003'}
print(myDict)
print(type(myDict))

newDict = dict()
print(newDict)
print(type(newDict))

newDict = dict(Dave='001', Ava='002')
print(newDict)

# Nested Dictionaries
print()
print('Nested Dictionaries')
empDetails = {'Employee':{'Dave':{'ID':'001','Salary':'2000','Designation':'Team Lead'},
                          'Ava':{'ID':'002', 'Salary': '1000', 'Designation':'Associate'}}}
print(empDetails)

# Performing Operations on Hash Tables
print()
print('Performing Operations on Hash Tables')
print('Accesing Items')
print(myDict['Dave'])
print(myDict)
print(myDict.keys())
print(empDetails.keys())
print(myDict.values())
print(empDetails.values())
print(myDict.get('Eva'))
print('Using for loop')
# Retrieve all keys
print('Retrieve all Keys')
for x in myDict:
    print(x)
# Retrieve all  values
print('Retrieve all values')
for x in myDict.values():
    print(x)
# Retrieve all keys and values
print('Retrieve all keys and values')
for x, y in myDict.items():
    print(x,y )

# Updating
print()
print('Updating')
myDict['Dave'] = '004'
myDict['Chris'] = '003'
print(myDict)

# Deleting
print()
print('Deleting')
print(myDict)
print(myDict.pop('Eva')) # Deletes specific
print(myDict)
print(myDict.popitem()) # Deletes last item and returns it
print(myDict)
del myDict['Dave'] # deletes specific key value pair
print(myDict)

# Dicionary to Dataframe
print()
print('Dictionary to dataframe')
import pandas as pd
dataFrame = pd.DataFrame(empDetails['Employee'])
print(dataFrame)