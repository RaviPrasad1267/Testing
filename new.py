# Sample list with duplicates
original_list = [1, 2, 3, 1, 4, 2, 5, 6, 3]

# Remove duplicates using set and maintain order
unique_list = list(set(original_list))

# Print the result
print("Original List:", original_list)
print("List with Duplicates Removed:", unique_list)



uniquelist = []
duplicateslist = []

for i in original_list:
    if i not in uniquelist:
        uniquelist.append(i)
    else:
        duplicateslist.append(i)

print("Unique list is:", uniquelist)
print("Duplicate list elements are:", duplicateslist)

list1 =[1,4,6,8,9]
list2 =[6,8,9]

print(list1 + list2)
print(list1*2)
print(1 in list1)
