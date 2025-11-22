# list1=[1,10,4,100,5,1000]
# list2=[1,2,10.5,"Sureshk"]
# list3=[]
# print(list2)
# print(list1[0::3])
# print(list1[0:7:])   #output : [1,2,3,4,5,6,7]
# print(list1[2:9:])
# print(list1[-10:-2:])  #output : [1,2,3,4,5,6]

#append
# print(list2)
# list2.append("Ravi")
# print("Append:",list2)
# list2.insert(1,5000)
# print("insert",list2)
# list2.remove(5000)
# print("remove",list2)
# list2.pop(3)
# print("pop",list2)

# Interview question
# method-1
list1=[10,20,40,'abcd',78,60,'manju','ravi']
# Output : [10,20,40,'dcba',78,60]
# str=list1[3]
# print(str)
# reversestr=str[::-1]
# print(reversestr)
# list1.pop(3)
# print(list1)
# list1.insert(3,reversestr)
# print(list1)

expectedoutput=[x[::-1] if isinstance(x,str) else x for x in list1 ]
print("Expected output:",expectedoutput)

list20=[100,5000,40,10,45637,1,5,8,3,5,3,5,3,5,3,5,5,5]
# print("Before sort my list20 values are:",list20)
# list20.sort()
# print("After sort my list20 values are:",list20)
# list20.sort(reverse=True)
# print("After descending sort my list10 values are:",list20)

# print("Before reverse my list20 values are :",list20)
# print("After reverse Using [::-1] list20 values are :",list20[::-1])
# list20.reverse()
# print("After  reverse my list20 values are :",list20)

# print(list20.count(5))
# list30=[1,5,4,"Suresh","Ravi",3.5,100]
# print("Before extend method my list20 valuea are:",list20)
# list20.extend(list30)
# print("After we applied extend method :",list20)
# print(list20)
# print("Before extend method my list30 valuea are :",list30)
# list30.extend(list20)
# print("After we applied extend method :",list30)


# # my_name='Suresh'
# # age=21
# print("My name is:",my_name,"My age is:",age)
#
# print(f"My name is : {my_name}  my age is : {age}")
# print("My name is : {} my age is :{}".format(my_name,age))
# print("My name is : {0} my age is :{1}".format(my_name,age))
# print("My name is : {myname} my age is :{age}".format(myname="Suresh",age=28))
#
# list11=[1,2,3,4,5,6,7,8,9]
# # expectedoutput=[]
# # for i in list11:
# #     print(2*i)
#
# expectedoutput1=[2*i for i in list11]
# print(expectedoutput1)
#
# input=[1,2,3,4,5]
# output=[1,4,27,256,3125]
# output1=[]
#
# # method 1 using for loop
# for i in input:
#     a=i**i
#     output1.append(a)
# print(output1)
#
#
# # Method 2 list comprehension
# # SYNTAX:
#     # [expression for item in iterable]
#
# output2=[i**i for i in input]
# print(output2)

input1=[1,2,3,4,5,6,7,8,9,10]
# Evenlist=[2,4,6,8,10]
# Oddlist=[1,3,5,7,9]


# Method 1 for loop concept
Evenlist=[]
Oddlist=[]
# for i in input1:
#     if i%2==0:
#         Evenlist.append(i)
#     else:
#         Oddlist.append(i)
# print("Even number list is:",Evenlist)
# print("Odd number lis is: ",Oddlist)
# [expression for item in iterable if condition]
# Evenlist = [i for i in input1 if i%2==0]
# Oddlist = [i for i in input1 if i%2!=0]
# print(Evenlist)
# print(Oddlist)

# [expression_if_true if condition else expression_if_false for item in iterable]
expectedoutput1=["Even" if i%2==0 else "Odd" for i in input1]
print("Input:",input1)
print("Output:",expectedoutput1)

# output:["Even","Odd"]
























# expected_output=[x[::-1] if isinstance(x,str) else x for x in list1]
# print(expected_output)



# print function string format



