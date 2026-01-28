"""1. Python Set – Definition
1. Python Set – Definition
A set in Python is:
An unordered collection of unique elements
Mutable (you can add/remove elements)
Does not allow duplicates
Elements must be immutable (hashable)"""

# Set creation
s = {1, 2, 3}
s = set([1, 2, 3])
s = set()     # correct
s = {}        # ❌ creates dictionary
s = {"Manjunatha M C"}
print(s)
s1 = set("banana") # {'Manjunatha M C'}
print(s1)   #  {'b', 'n', 'a'}

"""4. Complex Set Explained
Allowed Elements

✔ int
✔ float
✔ str
✔ tuple
✔ frozenset

Not Allowed

❌ list
❌ set
❌ dict"""

s = {1, (2, 3), "python"}

# 5. Accessing Elements from Set
# ❌ Indexing NOT allowed
# s[0]   # TypeError

set1 = {1,3,6,"Manju","Hello",6,7}
# 1️⃣ add() ---->Adds single element
set1.add(5000)
# 2️⃣ update()-----> Adds multiple elements
set1.update([10,20])
# 3️⃣ remove() --------->Removes element (ERROR if not found)
set1.remove(1)
# 4️⃣ discard() ------->Removes element (NO error)
set1.discard(1)
# 5️⃣ pop() ----->Removes random element
set1.pop()
# 6️⃣ clear() ------->Removes all elements
# shallow copy
set2 = set1.copy()


# Set Operations 1.union  = | 2. intersection + &  3. difference  + - 4.Symmetric difference =
set_1 = {1,2,3,4}
set_2 = {3,4,7,9}
print("After union is:",set_1.union(set_2))  # Combines sets selmets remove the duplicates elements
print("After union is:",set_1 | (set_2))

print("After Intersection is:",set_1.intersection(set_2))  # Common elements elements
print("After Intersection is:",set_1 & (set_2))

print("After difference is:",set_1.difference(set_2))  # Elements in s1 not in s2
print("After difference is:",set_1 - (set_2))

print("After symmetricdiff is:",set_1.symmetric_difference(set_2))  # Not comman elements
print("After symmetricdiff is:",set_1 ^ (set_2))

# 1️⃣2️⃣ intersection_update() ----->Updates original set
set_1.intersection_update(set_2)
print("intersection_update:",set_1)

"""1️⃣ What is a Frozen Set?
A frozen set in Python is like a regular set, but immutable:
You cannot add or remove elements once it’s created.
It cannot be changed, which makes it hashable.
Being hashable means it can be used as a key in a dictionary or an element of another set.
Regular sets cannot do this because they are mutable."""

# 2️⃣ Creating a Frozen Set
# Create a frozen set
fs = frozenset([1, 2, 3, 4])

print(fs)         # Output: frozenset({1, 2, 3, 4})
print(type(fs))   # Output: <class 'frozenset'>















