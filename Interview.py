list1=[10,40,30,20,500,5000]
newlist1=sorted(list1,reverse=True)
newlist2=sorted(list1)
print(newlist1[1])
print(newlist2[1])


s = input("Please enter the value of string: ")
output=""
count=1
for i in range(len(s)):
    if i < len(s)-1 and s[i] == s[i+1]:
        count += 1
    else:
        output += s[i] + str(count)
        count = 1
print(output)



list2=[2,3,3,4,4,4,4,5,5,5,8,9]
distinctele=set([x for x in list2])
distinctelelist=list(distinctele)
print("Distinct elements from the list is:",distinctelelist)
output2=[x for x in list2 if list2.count(x)>1]
print("Duplicate elemenst are:",output2)
Dupdis=set(output2)
Final=list(Dupdis)
print("Distinct duplicate elemesta are:",Final)

