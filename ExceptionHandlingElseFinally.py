# The else Clause
# try: run this code
# except: execute this code when there is an exception
# else: no exceptions? run this code

try:
    # a = 0 / 0 # Try this
    a = 10
except AssertionError as error:
    print(error)
else:
    print('Executing the else clause')
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('This always runs, even with exceptions')

# SUMMARY
# raise: allows you to throw an exception at any time
# assert: enables you to verify if a certain condition is met and throw an exception if it isn't
# try: all statements are executed until an exception is encountered
# except: is used to catch and handle the exception(s) that are encountred in the try clase
# else: lets you code sections that should run only when no exceptions are encountered in the try clause
# finally: enables you to execute sections of code that should always run, with or without any previously encountered exceptions
