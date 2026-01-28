# lambda arguments: expression
# 1.✔ Example 1: Add 10 to a number

finaloutput= lambda  s: 10+s
print("Output here:",finaloutput(5))

# 2.✔ Example 2: Multiply two numbers

mulval= lambda p,q: p*q
print("Multification of two number value is: ",mulval(8,10))

# 3.✔ Example 3: Sorting with lambda
# **** Important question
pairs = [(2, 10), (70, 5), (68, 1)]
pairs.sort(key=lambda x:x[1])
print("Sorted value based on second element:",pairs)
