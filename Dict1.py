"""1. Python Dictionary – Definition
A dictionary (dict) is:
A collection of key : value pairs
Unordered (insertion-ordered from Python 3.7+)
Mutable
Keys must be unique and immutable
Values can be of any data type"""

# Dict Creation
d = {"a": 1, "b": 2}
d = dict(a=1, b=2)
d = dict([("a", 1), ("b", 2)])
keys = ["a", "b"]
values = [1, 2]
d = dict(zip(keys, values))
d = {}
d = dict()

# 4. Complex Dictionary (Nested Dictionary)
student = {
    "name": "Manju",
    "marks": {"math": 90, "science": 85},
    "skills": ["Python", "SQL"]
}

print(student["marks"]["math"]) # 90

# 5. Accessing Dictionary Elements
# Using get method and d["key"]
# 1️⃣ Using Key  ❌ Raises KeyError if key not found
print(student["skills"])  # ["Python", "SQL"]

# 2️⃣ Using get() (Recommended)
print(student.get("marks"))
print(student.get("Id","Key Not Found"))

# Accessing the dict elements using the loop
for i in student:
    print(i)  # We only get the key

for i in student.values():
    print(i)  # We can print only values

for i,j in student.items():
    print(i,j)   # we can access both key and valyes


# Q5: How to reverse a dictionary?
# rev = {v: k for k, v in student.items()}

# 6. Dictionary Methods (ALL with Syntax & Sample Output)
# 1️⃣ get()
print(student.get("marks","Key Not Found"))
# 2️⃣ keys()
print(student.keys())
# 3️⃣ values()
print(student.values())
# 4️⃣ items()
print(student.items())
# 5️⃣ update()
student.update({"Sid":[1,2,4]})
# 6️⃣ pop()
student.pop("name")
# 7️⃣ popitem() --->Removes last inserted item

📌 Key points:

1.Keys must be unique
2.Keys must be immutable (string, number, tuple…)
3.Values can be anything (list, dict, set, etc.)
4.Items are stored as {key: value}

1.1 Accessing Values  d[Keyname] or d.get(KeyValue)
1.2 Adding / Updating  d[NewKey]=Value or d.update({"NewKey": 30})
1.3 Removing Items   # pop(),popitem() del d[] and clear
1.4 How we can iterate Dict





