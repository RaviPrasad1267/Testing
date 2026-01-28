"""🔹 1. Lambda Functions
    Syntax: lambda arguments: expression
    Examples:
        1.✔ Example 1: Add 10 to a number
        2.✔ Example 2: Multiply two numbers
        3.✔ Example 3: Sorting with lambda
"""

"""1️⃣ What is a Lambda Function in Python?

A lambda function is:
A small anonymous function (no name)
Defined using the keyword lambda
Can have any number of arguments
Can have only ONE expression
Expression result is returned automatically"""

# Q3️⃣ Can lambda have multiple arguments? Yes
# Q4️⃣ Can lambda return multiple values? : ❌ No (only one expression)
# Q5️⃣ Is lambda faster than normal function? ❌ No, ✔ It improves code readability, not performance
# Q6️⃣ Find square of each number
nums = [1, 2, 3, 4]
square = list(map(lambda x: x*x , nums))
print(square)
# Q7️⃣ Find even numbers
evennum = list(filter(lambda x:  x%2==0,nums))
print("Evennumbers:",evennum)
# Q8️⃣ Find maximum of two numbers
maxnum = [lambda a,b:a if a>b else b]
# Q9️⃣ Sort list of tuples by second value
data = [(1, 3), (4, 1), (2, 2)]
print("sorttuple is:",sorted(data, key=lambda x: x[1]))
# Q1️⃣0️⃣ Sort dictionary by values
d = {"a": 3, "b": 1, "c": 2} # output  [('b', 1), ('c', 2), ('a', 3)]
dictvaluessort = sorted(d.items(), key=lambda x: x[1])
print("dict sorted by values:", dictvaluessort)
# when we want output like below
# dict sorted by values: {'b': 1, 'c': 2, 'a': 3}
d = {"a": 3, "b": 1, "c": 2}
dictvaluessort = dict(sorted(d.items(), key=lambda x: x[1]))
print("dict sorted by values:", dictvaluessort)

# # Q1️⃣0️⃣ reverse the string from list
list1 = [1,2,3,"Manju",6,7,"Nayana"]
finaloutput = [i[::-1] if isinstance(i,str) else i for i in list1]
print("Reversed :",finaloutput)



