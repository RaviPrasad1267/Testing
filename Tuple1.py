"""1️⃣ What is a Tuple?
A tuple is an immutable sequence type in Python.
Immutable means: once created, you cannot modify it (no append, remove, etc.).
Tuples can contain heterogeneous data: integers, strings, lists, other tuples, etc."""

# 2️⃣ Tuple Creation
t = (1, 2, 3)
t2 = 1, 2, 3   # parentheses are optional
t3 = ()        # empty tuple
t4 = (5,)      # single element tuple requires a comma
t5=((12,3),(4,5,7)) # Nested Tuple
# Complex Tuples
complex_tuple = (1, "hello", 3.14, (2, 3), [4, 5])

# Can contain nested tuples, lists, other objects.
# Immutable at top-level, but nested lists are mutable.

t = (1, (2, 3), (4, (5, 6)))
print(t[1])      # (2, 3)
print(t[1][0])   # 2
print(t[2][1][1])# 6
print(t[2][0]) # 4

t = (10, 20, 30, 40, 50)
print(t[1:4])     # (20, 30, 40)
print(t[:3])      # (10, 20, 30)
print(t[::2])     # (10, 30, 50)
print(t[::-1])    # (50, 40, 30, 20, 10)  # reverse

# ✅ Tip: Slicing returns a new tuple, original tuple remains unchanged.

"""Tuples have very few methods because they are immutable.
Method	Description
count(x)	Returns the number of times x appears
index(x[, start[, end]])	Returns the first index of x. Raises ValueError if not found"""

"""sequence.index(x[, start[, end]])
✔ sequence → list or tuple
✔ x → element to search
✔ start → optional starting index
✔ end → optional ending index (exclusive)"""

# ✔ Interview Tip: index() raises an exception if element is missing.

tup = (10, 20, 30, 20)
tup.index(20)        # 1
tup.index(20, 2)     # 3
tup.index(20, 2, 4)  # 3

lst = [1, 2, 3, 4, 2]

lst.index(2, -3)      # 4
lst.index(2, -4, -1)  # 1

# 7️⃣ Tuple Packing and Unpacking
# Packing
t = 1, 2, 3, 4
# Unpacking
a, b, c, d = t
print(a, b, c, d)  # 1 2 3 4

# Nested Unpacking
t = (1, (2, 3), 4)
a, (b, c), d = t
print(a, b, c, d)  # 1 2 3 4

# Example 2: Slicing Nested Tuples
matrix = ((1,2,3), (4,5,6), (7,8,9))
print(matrix[0:2])     # ((1,2,3),(4,5,6))
print(matrix[::2])     # ((1,2,3),(7,8,9))


