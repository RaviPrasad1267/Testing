str = input('Enter the string you want to reverse:\n')
res1 =str[::-1]
print("Reversed string using the ::-1 meth and result is:",res1)

emptstr =""
for i in str:
    emptstr = i + emptstr
print("Reversed string using the coomman empty str and loop is:",emptstr)

res2 = ''.join(reversed(str))
print("reversed string using the built fun and .join is:",res2)