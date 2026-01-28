# 🟦 4. reduce()?
#     Import:
#         from functools import reduce
#     Syntax: reduce(function, iterable[, initializer])
#     Examples:
#     🟩 1. Example: Sum of List

from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)
print("Sum of list value is:",result)


#     🟩 2. Example: Product of List

numbers1 = [1, 2, 3, 4]

result1 = reduce(lambda x, y: x * y, numbers)
print("Product of list value:",result1)


#     🟦 3.Using Initializer (Optional Third Argument)

# numbers = [1, 2, 3, 4]

result2 = reduce(lambda x, y: x + y, numbers,100)
print("With intial value argument Sum of list value is:",result2)

# 10 + 1 = 11
# 11 + 2 = 13
# 13 + 3 = 16
# 16 + 4= 20   # Final  output


1. csv to csv file validation
2. Csv to Oracle DB Table validation
3. Same DB Two tables validation
4. Source one DB and Target other DB two table validation