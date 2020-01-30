# Try except block
# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except:
#     print('Could not open file.log')


try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error) # prints the type of error

# Key takeaways
# A try clause is executed up until the point where the first exception is encountered
# Inside the except clause, or the exception handler, you determine how the program responds to the exception
# You can anticipate multiple exceptions and differentiate how the program should respond to them
# Avoid using bare except clauses