"""1️⃣ What is filter() in Python?
filter() is a built-in function used to:
Select elements from an iterable
Based on a condition (function returning True/False)
Returns a filter object (iterator)
📌 Important:
filter() does NOT modify data, it only selects elements."""

"""Syntax
filter(function, iterable)
function → returns True / False
iterable → list, tuple, set, etc.
Returns → filter object"""

# 2️⃣ Basic Example
nums = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, nums)
print(list(result))

# 4️⃣ filter() Without Lambda (IMPORTANT)
#
# If function is None, filter() removes falsy values:

data = [0, 1, False, True, "", "Python", None]

print(list(filter(None, data))) # output [1, True, 'Python']

# 5️⃣ filter() with Strings
names = ["Python", "", "Java", None, "C"]
print(list(filter(None, names)))  # Output  ['Python', 'Java', 'C']

# 6️⃣ filter() with Dictionary (Interview)
# Filter dictionary values

d = {"a": 10, "b": 5, "c": 20}

result = dict(filter(lambda item: item[1] > 10, d.items()))
print(result)

# 🔟 Real Interview Question (Combined map + filter)
# Square only even numbers

nums = [1, 2, 3, 4, 5]

result = list(map(lambda x: x*x, filter(lambda x: x % 2 == 0, nums)))
print(result)




