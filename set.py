# Set:
# 1.Definition
#
# A list is an ordered, mutable, collection of  elements.
# A tuple is an ordered, nonmutable, collection of  elements.
# A set is an unordered, mutable, collection of unique elements.
# A dictionary is a mutable, unordered collection of key–value pairs.
#
#
# Syntax:
s1={1,2,3,4,4}
s3={}
print(type(s3))
s2=()  #empty set         single element tuple = (1,)  for empty set s4=()
#



#
# 2.Set Methods:
#     2.1 Add

s4= {2,4,6,8,"Suresh",10.5}
s4.add("Python class")
s4.add("Hello Man")
print("S4 value after adding a element:",s4)

#     2.2 Update
s4.update({5,6})
print("After update s4 value then s4 set values are:",s4)

#     2.3 Remove
s4.remove("Suresh")
print("After we removed then tuple is:",s4)

#     2.4 Discard
s4.discard("Ravi")
print("After we discard then tuple is:",s4)


#     2.5 Pop
value1=s4.pop()
value2=s4.pop()
print("pop value:",value1)
print("pop value:",value2)

print("Enter s4 is now:",s4)

#     2.6 Clear

s4.clear()              #
print("After we cleared the s4 values :",s4)



#     2.7 Copy

s6=s4.copy()
print("s6 values are same as s4:",s6)
s6.clear()
print("After s6 clear:",s6)

s9={1,2,3}
s10={3,4,5}

# 3.Set Operations
#     🔶 1. Union (| or .union())
print("Uinon using union method:",s9.union(s10))
print("Union is using the | symbol",s9 | s10)

#     🔶 2. Intersection (& or .intersection())

print("intersection using union method:",s9.intersection(s10))
print("intersection is using the | symbol",s9 & s10)


#     🔶 3. Difference (- or .difference())

print("difference using union method:",s9.difference(s10))
print("difference is using the | symbol",s9 - s10)

#     🔶 4. Symmetric Difference (^ or .symmetric_difference())

print("symmetric_difference using union method:",s9.symmetric_difference(s10))
print("symmetric_difference is using the | symbol",s9 ^ s10)


list1=[1,2,2,3,4,5,5,6]   # INput:
# OUTPUT1:[2,2,5,5]
# OUTPUT:[1,2,3,4,5,6]

output2=list[set(list1)]
print("Unique element from the list1 is:",output2)




