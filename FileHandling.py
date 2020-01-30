# Windows support the files for image, text, executable and audio
# Python support binary or text files
# Open a file
# open(filename, mode)
# filename: Any name that you want
# mode: different modes for opneing a file...
# 'r' - Read - Default value. Opens a file for reading. Error if the file does not exist
# 'a'- Append - Opens a file for appending. Creates the file if it does not exist
# 'w' - Write - Opens a file for writing, creates the file if it does not exist.
# 'x' - Create - Creates the specified file, returns an error if the file exists
# In addition you can specifi if the file whould be handled as binary or text mode.
# 't' - Text - Default value. Text mode.
# 'b' - Binary - Binary mode (e.g. images)
# Examples
# Read
print('Read file')

file = open('info.txt', 'w') # When opening with param 'w' it erases the information in the file
file.close()

file = open('info.txt', 'r')
print(file.read()) # When read method is used, it puts the cursor a the end of the file
# print(file.read()) # That's why if you put another file.read() it won't print anythin
file.seek(0) # Puts the cursor at the start of the file
print(file.read(5)) # First 10 characters
file.close()

file = open('info.txt', 'r')
print(file.read(5))
file.close()

# readline and readlines
print()
print('readline')
file = open('info.txt', 'r')
print(file.readline())
print(file.readline())
print(file.readline(2))
file.seek(0) # the last print of the file is where the cursor is
print(file.readlines())
file.close()

# loop for method if you want to have your code be fast and efficient
file = open('info.txt', 'r')
file.seek(0)
for line in file:
    print(file.readlines()) # For some reason it doesn't print the first line
file.close()

# Write file
file = open('info.txt', 'w') # 'w' Overwrites the file
file.write('Hello World!')
file.write('Hello World again')
file.close()

# Create a file
file = open('info2.txt', 'x')
file.write('new file \'info2\'')
file.close()

# Delete a file
# os.remove() function to delete a file
# os.rmdir() function to delete a directory
