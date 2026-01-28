"""🔹 2. Basic if Syntax
if condition:
    statement(s)"""

# Example
if 5>2:
    print("yes")

"""🔹 3. if–else Syntax
if condition:
    statement(s)
else:
    statement(s)"""

# Example
age = 32
if age >= 18:
    print(" Eligibale  for vote")
else:
    print("Not Eligible for vote")

"""
🔹 4. if–elif–else Syntax
if condition1:
    statement(s)
elif condition2:
    statement(s)
elif condition3:
    statement(s)
else:
    statement(s)"""

# example
# 📌 Only ONE block executes, even if multiple conditions are true
marks = 85

if marks >= 90 :
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print(grade)

