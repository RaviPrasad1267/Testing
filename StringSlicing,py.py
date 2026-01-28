"""🔹 What is String Slicing in Python?
String slicing is used to extract a part (substring) from a string using indexes.
📌 Strings are immutable, slicing always returns a new string."""

# Syntax : string[start : end : step]
#| Part    | Meaning                          |
#| ------- | -------------------------------- |
#| `start` | Starting index (**inclusive**)   |
#| `end`   | Ending index (**exclusive**)     |
#| `step`  | Interval (optional, default = 1) |

s = "Python Class"
# Want to print only python
print(s[0:6])
# want to print only class
print(s[7:])
# print full string using slicing
print(s[:])
# Reverse the string using
print(s[::-1]) # ssalC nohtyP
print(s[::-2]) # saCnhy
# 5️⃣ Every second character from the string
print(s[0::2]) # output is Pto ls
print(s[0::3])   # skip the n-1 characher from the string 3-1 = every two character skip
# print last character from the string
print(s[-1])
# Remove the last character
print(s[:-1])
# extract class using the negative
print(s[-5:])
# Remove first and last character
print(s[1:-1])
# ❓ Q4: Get alternate characters
print(s[::2])
# ❓ Q8: Get last 3 characters
print(s[-3:])
