# 🔹 3. filter()
#     Syntax: filter(function, iterable)

#     Examples:
#     1.✔ Example 1: Keep even numbers
list1 = [2,5,10,11,12,13,17,20,30,18,16]
evennumlist= list(filter(lambda x: x%2==0,list1))
oddnnumlist= list(filter(lambda x: x%2!=0,list1))
print("Number number list:",evennumlist)
print("Odd Number List:",oddnnumlist)

#     2.✔ Example 2: Keep strings with length > 3

list2=['Suresh','Ravi Prasad','ABC','God']
finaloutput= list(filter(lambda x: len(x)>3,list2))
print("Words with length > 3:",finaloutput)

#     3.✔ Example 3: Keep positive numbers
list3 = [10,20,-30,-1,45,78]
Positivenum= list(filter(lambda x: x>0,list3))
print("Positive number list:",Positivenum)
