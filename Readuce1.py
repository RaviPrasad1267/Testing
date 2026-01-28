"""🔷 What is reduce() in Python?

reduce() is used to:
Apply a function cumulatively to elements of an iterable
Reduce the iterable to a single value
📌 reduce() is not built-in — it must be imported."""

from functools import reduce

"""🔹 Syntax
reduce(function, iterable[, initializer])
Parameters:
function → takes two arguments
iterable → list, tuple, etc.
initializer (optional) → starting value"""

#🔹 How reduce() Works (Very Important)

#Example:

nums = [1, 2, 3, 4]
reduce(lambda a, b: a + b, nums)

#Step-by-step execution:
#Step 1: a=1, b=2 → 3
#Step 2: a=3, b=3 → 6
#Step 3: a=6, b=4 → 10

#Final Output:
#10


# 🔹 Basic Examples
from functools import reduce

nums = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b, nums))

#Product of list
reduce(lambda a, b: a * b, [1, 2, 3, 4])


#🔹 reduce() with Initializer
reduce(lambda a, b: a + b, [1, 2, 3], 10)

#Execution:
#10 + 1 → 11
#11 + 2 → 13
#13 + 3 → 16

#🔹 reduce() with Built-in Functions
# 📌 Interview-preferred (cleaner than lambda)
from functools import reduce
import operator

reduce(operator.add, [1, 2, 3, 4])
reduce(operator.mul, [1, 2, 3, 4])


#🔹 Most Asked Interview Coding Questions
#Q1️⃣ Sum of all elements
reduce(lambda x, y: x + y, [1, 2, 3])


# Q2️⃣ Find maximum number
reduce(lambda a, b: a if a > b else b, [10, 20, 5])


# Q3️⃣ Find minimum number
reduce(lambda a, b: a if a < b else b, [10, 20, 5])


# Q5️⃣ Concatenate strings
reduce(lambda a, b: a + b, ["Py", "thon"])

# Q7️⃣ Find factorial
reduce(lambda a, b: a * b, range(1, 6))

#🔹 Real Interview Combined Question
#Square only even numbers and find sum
nums = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a + b,map(lambda x: x*x, filter(lambda x: x % 2 == 0, nums)))

print(result)



