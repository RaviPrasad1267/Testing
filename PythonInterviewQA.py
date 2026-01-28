# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# ()[]{}
# ([])
# ([)]
# Method 1:

# Q1 print the each vowels count in the given string

text = "ManjunathaM C"
vowels = "aeiouAEIOU"

vowel_count = {v: text.count(v) for v in vowels if v in text}
print(vowel_count)

# Method 2:
filterd = filter(lambda char: char in vowels, text)
for i in set(filterd):
    print(i , ":" , text.count(i))

# Method 3:
from collections import Counter
counter = Counter(text)
print(counter)
for k, v in counter.items():
    if k in vowels:
        print(k , ":" , v)

userstring = input("Please enter your string: ")
print("All characters frequency in the given string:", Counter(userstring))

# Reverse a string.


def reverse_string(s):
    reversed_string = s[::-1]
    print("Reversed string:", reversed_string)

reverse_string("Hello Madam")



# Check if a string is a palindrome.
def is_palindrome(s):
    if s == s[::-1]:
        print("Your string is palindrome")
    else:
        print(" Your string is not a palindrome")

is_palindrome("madam")

# Find the factorial of a number.

num = int(input("Enter a number to find factorial: "))
def factorial(num,result = 1):
    for i in range(1, num + 1):
        result = result * i
    print("Factorial of", num, "is", result)
factorial(num)

# Fibonacci series (using loop & recursion).
n = 10
def fibonacci_loop(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b = b,a+b

fibonacci_loop(7)

# Find the largest / smallest number in a list.
list1 = [34, 12, 5, 67, 23, 89, 2]
def find_largest_smallest(lst):
    big_num = max(lst)
    small_num = min(lst)
    print("Largest number is:",big_num,"Smallest number is:",small_num)
find_largest_smallest(list1)

# Count vowels in a string.
vowels = "aeiouAEIOU"

def vowelscount(s,count = 0):
    for i in s:
        if i in vowels:
            count =+ 1
    print("Total vowels count is:", count)

vowelscount("Hello Welcome to the python class")

# Print each vowels count in the given string.
def each_vowels_count(s):
    vowels_count = {i: s.count(i) for i in vowels if i in s}
    print("Each vowels count in the given string is:", vowels_count)
each_vowels_count("we are into the big world ")

# find the each vowels count using counter method
from collections import Counter
def each_vowels_count_counter(s):
    counter = Counter(s)
    for k,v in counter.items():
        if k in vowels:
            print(k, ":", v)
each_vowels_count_counter("I am learning python programming language")


# Check if a number is prime.

def chech_number_prime(num,count=0):
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

chech_number_prime(6)




# Swap two numbers without using a third variable.

m = 30
n = 50
def swap_numbers(a,b):
    print("Before swapping number is :",a,b)
    a,b = b,a
    print("After swapping number is :",a,b)

swap_numbers(m,n)




# Find duplicate elements in a list.

def find_duplicates(lst):
    duplicates = []
    for i in lst:
            if lst.count(i) > 1:
                duplicates.append(i)
    final_out1=set(duplicates)
    print("Duplicate elemts are :",final_out1)

find_duplicates([10,10,20,30,40,10,20,30])




# Sum of digits of a number.
def sum_of_digits(num,sum=0):
    for i in str(num):
        sum += int(i)
    print("Sum of digits of a number is :",sum)

sum_of_digits(12345)

# 🔹 Strings & Lists

# Remove duplicate characters from a string.
def remove_duplicate_char(s):
    final_res = ""
    for i in s:
        if i not in final_res:
            final_res += i
    print("Your string after removing duplicate characters is :",final_res)

remove_duplicate_char("Manjunatha M C")



# Sort a list without using sort().
def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    print("Sorted list is :",lst)

sort_list([10,100,30,400,1,3,7])

# using sort method
def list_sort_using_sort_method(lst):
    lst.sort()
    print("List ascending sort is :", lst)
    lst.sort(reverse=True)
    print("List descending sort id :", lst)

list_sort_using_sort_method([10,100,30,400,1,3,7])


# Find the second largest element in a list.

def second_largest_num(lst):
    unique_ele = set(lst)
    lst.sort(reverse=True)
    print(lst, "Second largest element from the list is :", lst[1])

second_largest_num([4000,4,7,200,47,5000])

# Count frequency of elements in a list.

def each_element_count(lst):
    each_ele_count = Counter(lst)
    print(lst , "Each element count in the list is :", each_ele_count)

each_element_count([10,40,68,20,10,2,2,2,4,4,5,68,68,68])

# Method 2 using dictionary
def dict_each_ele_count(lst):
    final_res = {i : lst.count(i) for i in lst}
    print(lst , "Each element count in the list is  using dict method:", final_res)

# Reverse words in a sentence.
def word_reverse(str):
    wordlist = str.split()
    reversed_words = ' '.join(reversed(wordlist))
    print(wordlist,"Reversed words in the sentence is :",reversed_words)

word_reverse("Hello welcome to the python programming class")

# Find common elements between two lists.
def common_elements(l1,l2):
    comm_ele = set (l1) & set (l2)
    print("Common elements between two lists are :",comm_ele)

common_elements([10,20,30,40,50],[30,40,50,60,70])


def only_l1_elements_elements(l1, l2):
    only_l1_ele = set(l1) - set(l2)
    print("Only l1 elements are :", only_l1_ele)

only_l1_elements_elements([10, 20, 30, 40, 50], [30, 40, 50, 60, 70])


def only_l2_elements_elements(l1, l2):
    only_l2_ele = set(l2) - set(l1)
    print("Only l2 elements are :", only_l2_ele)

only_l2_elements_elements([10, 20, 30, 40, 50], [30, 40, 50, 60, 70])

# set | operation
def unque_ele_from_both(l1,l2):
    unique_ele = set(l1) | set(l2)
    print("Unique elements from both lists are :", unique_ele)
unque_ele_from_both([10, 20, 30, 40, 50], [30, 40, 50, 60, 70])

# Remove all spaces from a string.
def remove_spaces(s):
    no_space_str = s.replace(" ", "")
    print("String after removing all spaces is :", no_space_str)
remove_spaces("Hello   welcome  to  python  programming")

# Convert a list of strings to uppercase.
def upper_str(str):
    upperstr=str.upper()
    print("String after converting to uppercase is :", upperstr)
upper_str("hello welcome to python programming")


# 🔹 Dictionaries & Sets

# Count occurrences of characters using a dictionary.
def char_count_dict(s):
    char_count = {i: s.count(i) for i in s}
    print("Character occurrences using dictionary is :", char_count)

# Merge two dictionaries.
def merge_dicts(d1,d2):
    merged_dict = {**d1, **d2}
    print("Merged dictionary is :", merged_dict)


# Find key with maximum value in a dictionary.
def key_with_max_value(d):
    max_key = max(d,key=d.get)
    print(d,"Key with maximum value in the dictionary is :", max_key, "with value :", d[max_key])
key_with_max_value({'a': 10, 'b': 25, 'c': 15})

def key_with_min_value(d):
    max_key = min(d,key=d.get)
    print(d,"Key with maximum value in the dictionary is :", max_key, "with value :", d[max_key])
key_with_min_value({'a': 10, 'b': 25, 'c': 15})

# Sort dictionary by values.
def sort_dict_by_values(d):
    dict_sort_by_values = dict(sorted(d.items(),key = lambda i: i[1]))
    print(d,"Dictionary sorted by values is :", dict_sort_by_values)
sort_dict_by_values({'a': 10, 'b': 25, 'c': 15})

def dict_sort_by_key(d):
    dict_sorted_by_key = dict(sorted(d.items(),key = lambda i: i[0]))
    print(d,"Dictionary sorted by keys is :", dict_sorted_by_key)
dict_sort_by_key({'b': 25, 'c': 15,'a': 10})

# Remove duplicate values from a dictionary.
def remove_duplicates_values(d):
    seen = set()
    unique_dict = {}
    for k, v in d.items():
        if v not in seen:
            seen.add(v)
            unique_dict[k] = v
    print("Original dict: ", d , "Unique dict :",unique_dict)

remove_duplicates_values({'a': 10, 'b': 25, 'c': 10, 'd': 30})


# Find intersection of two sets.
def set_intersection(s1,s2):
    intersection = s1 & s2
    print("Intersection of two sets is :", intersection)

set_intersection({1,2,3,4,5},{4,5,6,7,8})



# Check if a key exists in a dictionary.
def check_key_in_dict(d,key):
    if key in d:
        print(f"Key '{key}' exists in the dictionary.")
    else:
        print(f"Key '{key}' does not exist in the dictionary.")

check_key_in_dict({'a':10,'b':1,'c':400},'a')

# Check value is present  in existing dictinary
def value_check_in_dict(d,value1):
    if value1 in d.values():
        print(f"Value {value1} is presnt in dict")
    else:
        print(f"Value {value1} not present in dict")

value_check_in_dict({'a':10,'b':1,'c':400},400)



