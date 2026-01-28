# 🔹 2. map()
#     Syntax: map(function, iterable)

#     Examples:
#     1.✔ Example 1: Square each number
list1 = [2,5,6,7,10]
expectedout= list(map(lambda x: x*x,list1))
print(expectedout)


#     2.✔ Example 2: Convert strings to integers
list2=["1","2","50","1000678"]
expectedout2= list(map(float,list2))
print("string converted to int :",expectedout2)

#     3.✔ Example 3: Add items of two lists

list3 = [2,5,6,8]
list4 = [10,6,8,20]
finaloutput = list(map(lambda p,q:p+q,list3,list4))
print("Addtion of two list values are :",finaloutput)

