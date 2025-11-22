str ='  Manjunatha, M, C,   '

print(len(str))
print(str.capitalize())
print(str.lower())
print(str.upper())
print(str.strip())
print(str.replace("M","N"))
print(str.count('M'))
print(str.find("M"))
print(str.index("a"))

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
squared1 = list(map(lambda x: x*x, numbers))
print(squared1)

def sqr(n):
    return n**2

result = list(map(sqr,numbers))
print("Using defination",result)
reult1 =list(map(lambda x:x**2,numbers))
print("Using lambda",reult1)

def printnum(n):
    print("Number is:",n)
    if n==0:
        return 0
    printnum(n-1)

printnum(5)
