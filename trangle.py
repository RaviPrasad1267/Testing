n = int(input('Enter the value of n:\n'))
for i in range(1,n+1):
    print(i*"*")


print('Using for loop:\n')
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

print('we can do the reverse :\n')
for i in range(n,0,-1):
    print(i*"*")

print('Using the for loop: reverse:\n')
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

