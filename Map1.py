"""1️⃣ What is map() in Python?

map() is a built-in function used to:
Apply a function to each element of an iterable
Return a map object (iterator)
📌 Commonly used with:
lambda
existing functions
multiple iterables"""

"""Syntax
map(function, iterable1, iterable2, ...)
function → function to apply
iterable → list, tuple, set, etc.
Returns → map object"""

nums = [1, 2, 3, 4]

result = map(lambda x: x*x, nums)
print(list(result))

# 4️⃣ map() with Multiple Iterables (VERY IMPORTANT)
# 📌 Stops at shortest iterable in the case not equval list
a = [1, 2, 3]
b = [4, 5, 6]

result = map(lambda x, y: x + y, a, b)
print(list(result))

# 5️⃣ map() with Built-in Functions  change string to int
nums = ["1", "2", "3"]

print(list(map(int, nums)))

# 6️⃣ map() with String Data
names = ["manju", "python"]
print(list(map(str.upper, names)))

# Q3️⃣ Add two lists element-wise

list(map(lambda x, y: x + y, [1,2], [3,4]))

# Q4️⃣ Reverse only strings in a list using map
# Method 1
lst = [1, "Manju", 2, "Python"]

list(map(lambda x: x[::-1] if isinstance(x, str) else x, lst))

# Method 2 List Comphension
result = [i[::-1] if isinstance(i,str) else i for i in lst]
print(result)

# Q5️⃣ Find length of each word

list(map(len, ["Python", "Java"]))

# Q6️⃣ Multiply all numbers by 10
print("Using Map and Lambda",list(map(lambda x: x*10, [1, 2, 3])))
list1=[1,2,3]
finalres = [i*10 for i in list1]
print("Usingg list comphersion", finalres)

# 🔟 map() with Dictionary (IMPORTANT)
# Apply function to values

d = {"a": 1, "b": 2}

list(map(lambda x: x*2, d.values()))







