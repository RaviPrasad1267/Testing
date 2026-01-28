"""1️⃣ What is a List?
1. What is a List in Python?
A list is:
An ordered
Mutable (changeable)
Indexed
Can store duplicate values
Can hold multiple data types"""

my_list = [1, "apple", 3.5, True]
lst = [1, 2, 3]
lst1 = list((1, 2, 3)) # Using list() Constructor
# 3. Empty List
lst = []
lst = list()
# 4. From String
lst = list("python") #  output ['p', 'y', 't', 'h', 'o', 'n']
# 5. Using range()
lst = list(range(1, 6))  # output [1, 2, 3, 4, 5]
# 6. Nested List
lst = [[1, 2], [3, 4]]
# 4. List Slicing (VERY IMPORTANT)
# list_name[start : stop : step]
# start → inclusive
# stop → exclusive
# step → jump value

my_list = [1,3,5,6,"Manju","Hello",4,7,8]
# print frist and last element from the list
print(my_list[0:-1])
# print the last three elements from list
print(my_list[-3:])

# List Methods
# 1. append() ---->Adds element at the end
my_list.append(9)
# 2. extend() -------->Adds multiple elements
# 3. insert() ---->Adds element at specific index
# lst.insert(index, element)
# 4. remove() ----> Removes first occurrence of element
# lst.remove(element)
# 5. pop() ---->Removes element using index (default last)
# lst.pop()
# lst.pop(index)
# 6. clear() ---->Removes all elements
# lst.clear()
# 7. index() --->Returns index of element
# lst.index(element)
# lst.index(element, start, end)
# 8. count() ----->Returns number of occurrences
# 9. sort() --->Sorts list
# lst.sort()
# lst.sort(reverse=True)
# lst.sort(key=function)
# 10. reverse() ---->Reverses list
# 11. copy() --->Creates shallow copy
# new_list = lst.copy()
# Method 1
list1 = [1, 2, 3, 4, 5, 2, 3, 45, 12, 3, 4]
# OutPut : {1: 1, 2: 2, 3: 3, 4: 2, 5: 1, 45: 1, 12: 1}

result = {}
for item in list1:
    result[item] = result.get(item, 0) + 1

print(result)

# Method 2

from collections import Counter

list1 = [1, 2, 3, 4, 5, 2, 3, 45, 12, 3, 4]
result = dict(Counter(list1))

print(result)

# Method 3
result3 = {}
for i in set(list1):
    result3[i] = list1.count(i)
print(result3)

# 6. Difference: append() vs extend() (Interview Favorite)
lst1 = [1, 2]
lst1.append([3, 4])
# [1, 2, [3, 4]]

lst2 = [1, 2]
lst2.extend([3, 4])
# [1, 2, 3, 4]

"""List comprehension is a compact and readable way to create a new list 
by applying an expression to each item in an iterable, optionally with conditions."""
# It is faster and cleaner than using a traditional for loop.
# 1️⃣ Basic form : [expression for item in iterable]
numbers = [1, 2, 3, 4]
squares = [x * x for x in numbers]
print(squares)

# 🧱 With if condition (filtering) : [expression for item in iterable if condition]
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens)

# 🧱 With if–else (conditional expression) :[expression_if_true if condition else expression_if_false for item in iterable]
numbers = [1, 2, 3, 4]
result = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(result)  # ['odd', 'even', 'odd', 'even']

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Retrieve all even numbers
even_num = [num for row in matrix for num in row if num%2==0 ]
print(even_num)

# Flatten the matrix
flat_matrix = [num for row in matrix for num in row]
print(flat_matrix)

# ❓ Retrieve all elements greater than 2
data = [[1, 2], [3, 4, 5], [6]]

morethan_two = [num for row in data for num in row if num>2]
print(morethan_two)

# 🔹 3. Nested List with Strings
# ❓ Retrieve words with length > 3
words = [["apple", "bat"], ["cat", "dog"], ["elephant"]]
morethan_three = [word for row in words for word in row if len(word)>3]
print(morethan_three)

employees = [
    {"name": "A", "salary": 5000},
    {"name": "B", "salary": 7000},
    {"name": "C", "salary": 4000}
]

# ❓ Retrieve names with salary > 5000
Names = [emp["name"] for emp in employees if emp["salary"]>5000]
print(Names)


# Retrive the duplicate elements from the given list
list10 = [1, 2, 3, 1, 2, 3, 4, 5, 4, 5, 67, 8, 9]

# Method 1
from collections import Counter

list10 = [1, 2, 3, 1, 2, 3, 4, 5, 4, 5, 67, 8, 9]

# Count occurrences
count = Counter(list10)

# Keep only duplicates (count > 1)
duplicates = [item for item, freq in count.items() if freq > 1]

print(duplicates)


# method 2
list10 = [1, 2, 3, 1, 2, 3, 4, 5, 4, 5, 67, 8, 9]
seen = set()
duplicates = set()

for x in list10:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)

print(list(duplicates))

#method 3
lst = [1, 2, 2, 3]
duplicates = set([x for x in lst if lst.count(x) > 1])

# Q5: Find second largest element
lst = [10, 20, 4, 45, 99]
lst = list(set(lst))
lst.sort()
print(lst[-2])

# Interview question
list100 = [1,2,3,"Manju",4,"Hello"]  # output : [1,2,3,"ujnaM",4,"olleH"]
set100 = {1,2,3,"Manju",4,"Hello"}  # output : {1,2,3,"ujnaM",4,"olleH"}

finaloutput = []
for i in list100:
    if isinstance(i,str):
        finaloutput.append(i[::-1])
    else:
        finaloutput.append(i)
print("Final OutPut is using normal method:",finaloutput)

#Method 2 list compehensrion
finaloutput1 = [i[::-1] if isinstance(i,str) else i for i in list100]
print("Using the list Comphensrion :",finaloutput1)

setfinaloutput = set()
for i in set100:
    if isinstance(i,str):
        setfinaloutput.add(i[::-1])
    else:
        setfinaloutput.add(i)
print("Final OutPut is using normal method:",setfinaloutput)

#Method 2 list compehensrion
setfinaloutput1 = {i[::-1] if isinstance(i,str) else i for i in set100}
print("Using the list Comphensrion :",setfinaloutput1)










