n = int(input('Enter the number for which tables u want:\n'))
i = 1
while i<11:
    print(n,"*",i,"=",n*i)
    i +=1

print('Same we can achive in for loop')
for i in range(1,11):
    print(n,'*',i,'=',n*i)

