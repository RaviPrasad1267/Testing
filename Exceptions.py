# 2. Try–Except Blocks
# try:
#     # Code that may cause an error
# except ExceptionType:
#     # Code that runs if the error occurs
#
#
# 3. Multiple Exception Handling
#
# Syntax 1: Multiple except blocks
# try:
#     # risky code
# except ValueError:
#     # handle ValueError
# except TypeError:
#     # handle TypeError
#
# Syntax 2: Multiple exceptions in one block
# try:
#     # risky code
# except (ValueError, TypeError):
#     # handle both
#
# 4. Finally Block
# The finally block runs whether or not an exception occurs, often used
# for cleanup (closing files, releasing resources, etc.)
#
# Syntax:
# try:
#     # risky code
# except SomeError:
#     # handle error
# finally:
#     # code that always runs
#
# 5. Common Exceptions
# (a) ValueError:Occurs when a function receives an argument of correct type but invalid value.
# (b) TypeError: Occurs when an operation is applied to an object of inappropriate type.
# (c) ZeroDivisionError: Occurs when dividing a number by zero.
# (d) IndexError : Occurs when accessing an invalid list index.
# (e) KeyError : Occurs when accessing a non-existing dictionary key.
# (f) FileNotFoundError : 2. Try–Except Blocks
# try:
#     # Code that may cause an error
# except ExceptionType:
#     # Code that runs if the error occurs
#
#
# 3. Multiple Exception Handling
#
# Syntax 1: Multiple except blocks
# try:
#     # risky code
# except ValueError:
#     # handle ValueError
# except TypeError:
#     # handle TypeError
#
# Syntax 2: Multiple exceptions in one block
# try:
#     # risky code
# except (ValueError, TypeError):
#     # handle both
#
# 4. Finally Block
# The finally block runs whether or not an exception occurs, often used
# for cleanup (closing files, releasing resources, etc.)
#
# Syntax:
# try:
#     # risky code
# except SomeError:
#     # handle error
# finally:
#     # code that always runs
#
# 5. Common Exceptions
# (a) ValueError:Occurs when a function receives an argument of correct type but invalid value.
# (b) TypeError: Occurs when an operation is applied to an object of inappropriate type.
# (c) ZeroDivisionError: Occurs when dividing a number by zero.
# (d) IndexError : Occurs when accessing an invalid list index.
# (e) KeyError : Occurs when accessing a non-existing dictionary key.
# (f) FileNotFoundError : Occurs when attempting to open a non-existent file.



try:
    num = int(10.5)       # ValueError
except ValueError :
    print("ValueError: Invalid input!")
try:
    result = 100 / 5     # TypeError
except TypeError:
    print("TypeError: Wrong data type!")
try:
    result = 100 / 0     # TypeError
except ZeroDivisionError:
    print("ZeroDivisionError: Wrong divi!")

finally:
    print("Hello I am doing good")


# excel
# sql
# Any other programing


