"""🔹 1. What is a for loop in Python?

A for loop is used to iterate over a sequence:

list
tuple
string
set
dictionary
range
Python for loop works as a for-each loop, not index-based like C/Java."""

# Syntax
#for variable in iterable:
#    statement(s)

# 1. For loop in list
for i in [1,3,4,58,9]:
    print("elements from list:",i)

# Range syntax
# range(start, stop, step)  step by default is 1
# 📌 stop is exclusive
for i in range(1,6):
    print("elements from range with strat and stop ",i)
for i in range(6):
    print("elements from range with only stop",i)
for i in range(0,6,2):
    print("Elements from range with start,stopand step",i)
# for loop in string
s = "Welcome to the python class"
for i in s:
    print(i)

# write a program to find the no of vowel count aeiou
v="aeiou"
count=0
for i in s:
    if i in v:
        count += 1
print("vowels count from string is:",count)

# 2nd method
print("vowels count is:",sum(1 for i in s.lower() if i in "aeiou"))

# program to find the even and odd number from the list
list1 = [1,4,6,7,8,2,3,4,67]
even=[]
odd=[]
for i in list1:
    if i % 2 ==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbes are:",even)
print("Odd Numbers are:",odd)

# Method 2
even1 = [i for i in list1 if i%2==0]
odd1 = [i for i in list1 if i%2!=0]
print(even1,odd1)

# Tuple in for loop
for i in (1,3,4,5,6):
    print("Tuple elements are:",i)

# for loop in set
# (Order not guaranteed)
for i in {1,4,6}:
    print("Set elements are:",i)

# for loop in dict elements
dict = {"Id":[1,2,3],"Name":["Manju","Praveen","Sanju"]}
# print the keys
for i in dict:  # Here we will get only keys not a key valyes
    print("Key value from dict:",i)

# print the values from the dict
for i in dict.values():  # Here we will get only values not a key
    print("Dict values are:",i)

# print both key and value from the dict
for key,value in dict.items(): # Here we will get both  keys and  values
    print("key and values are",key,value)

# Accessing the dict elements
data = {
    "Id": [1, 2, 3],
    "Name": ["Manju", "Praveen"],
    "City": ["BNG", "CHI"]
}
# Q1 output should be Id=1 Id=2 Id=3
# data["Id"] gives the list:[1, 2, 3]
# for i in data["Id"] loops through each value
# print(f"Id={i}") prints each value in the required format
for i in data["Id"]:
    print(f"Id={i}")

# Q2 OutPut is:
#Id = 1 Name= Manju City = BNG
#❓ Why is Id=3 missing when printing Name and City?
#Answer:
#Because zip() stops at the shortest iterable.
# if we observe our dict values Name and City have only have two valyes so zip function will stop at short values
for a,b,c in zip(data["Id"],data["Name"],data["City"]):
    print(f"Id={a},Name={b},City={c} ")

# ✅ 3. Convert dictionary into list of records (rows)
# output is : [{'Id': 1, 'Name': 'Manju', 'City': 'BNG'}, {'Id': 2, 'Name': 'Praveen', 'City': 'CHI'}]
records = []
for a,b,c in zip(data["Id"],data["Name"],data["City"]):
    records.append({"Id":a,"Name":b,"City":c})
print(records)


# ✅ 6. If interviewer asks: “How to handle unequal lengths?”
# Option 1: Use itertools.zip_longest
data1 = {
    "Id": [1, 2, 3,4],
    "Name": ["Manju", "Praveen"],
    "City": ["BNG", "CHI"]
}

from itertools import zip_longest
for a,b,c in zip_longest(data1["Id"],data1["Name"],data1["City"],fillvalue="Unknown"):  # By deafult fillvalue is None
    print(f"Id={a},Name={b},City={c}")


"""🔹 What is a while loop in Python?
A while loop is used to repeat a block of code as long as a condition is True.
It is condition-based, not sequence-based."""

#🔹 Syntax of while loop
# Value assign
#while condition:
#    statement(s)

# Example
i = 1
while i<5:
    print(i)
    i += 1   # If there is no update statment then it will run infinite loops

# print even numbers using the while loop
i = 2
while i<10:
    if i % 2==0:
        print("This is even number",i)
    else:
        print("This is odd Number:",i)
    i += 1
"""break → terminates the loop completely
continue → skips the current iteration and moves to the next one"""

# 1. break (Terminate the loop)
for i in range(1, 6):
    if i == 3:
        break  # stops the loop completely
    print(i)   # output is 1,2

# 2. continue (Skip current iteration)
for i in range(1, 6):
    if i == 3:
        continue  # skip this iteration
    print(i)  # Out put is 1,2,4,5 it will skip the 3rd

