# # Simple print examples
# print("Hello welcome to the python class")
# print('Hello welcome to the python class')
# a=10
# A='Suresh'
# c=100.45
# print(a,A,c)
# print(a,A,c, sep = '\n')
# print(a,A,c, sep = '\n',end='#')
with open("Sample1.txt", "w") as file:
    print("Hello", "Suresh", sep="-", end="!", file=file, flush=True)







