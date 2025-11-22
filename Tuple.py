    # ✔ Basic tuple

t1=(1,2,3,4,5)
t2=("Suresh",4,6,10.5)
print(t1,t2)



    # ✔ Tuple without parentheses

t3 = 4,7,9
print("t3 values are:",t3)
    # ✔ Single - item tuple(important)
list1=[1]
t4= (4,)
print("Data type of t4 value:",type(t4))


    # 1.Tuple methods
    #     1. count()
    #     2.index()

t5=(4,6,7,8,9,10,"Suresh",2,5,9,9,9)
print("Count of 9 element:",t5.count(9))   #
print(t5.index(4))   #  output 9

    # 2.Nested Tuple

t6=(6,8,9,10,(1,2,3,4,6),9,10)
# print(t6[2])
# print(t6[4])
# print(t6[4][3])

    # 3.Tuple unpacking
a,*b,c,d = t6
print("Value of a is:",a)
print("Value of b is:",b)
print("Value of c is:",c)
print("Value of d is:",d)



    # 4.Tuple operations
    #     1.Concatenation   = +
    #     2.Repetition   = *
    #     3.Membership  in

print("Tuple Repetition values are:",t6*2)
print("Tuple concat values are:",t4+t6)
print("Membership in tuple :",6 in (t6))



    # 5.Accessing Tuples elements