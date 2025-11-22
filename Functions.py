# 1. Defining and Calling Functions (def)
# 2. Arguments and Return Values
# 3. Default Arguments
# 4. Keyword Arguments
# 5. *args (Variable-Length Positional Arguments)
# 6. **kwargs (Variable-Length Keyword Arguments)
# 7. Using *args and **kwargs Together


# 1. Defining and Calling Functions (def)


def add():
    a=2
    b=4
    c=a+b
    print("add fun Two number sum is:",c)

add()


# 2. Arguments and Return Values

def add1(a,b):      # Parameters
    c=a+b
    return  c

v1=add1(100,58)    # Arguments
print("Value 1 is:",v1)
v2=add1(5000,6000000)
print("Value 2 is:",v2)
v3=add1(50,20)
print("Value 3 is:",v3)

# 3. Default Arguments
def defun(name="Suresh"):
    print("My name is:",name)

defun()
defun("Ravi")


# 4. Keyword Arguments

def keywordfun(name,age):
    print(f"My name is {name} and my age is:{age}")

keywordfun(name="Suresh",age=28)
keywordfun(age=87,name="jordan")




# 5. *args (Variable-Length Positional Arguments)

def VLPAfun(*args):
    print("My args values are:",args)
    print(args[0])

VLPAfun(1,2,4)
VLPAfun(1,2)
VLPAfun(1)
VLPAfun(1,4,5,6,7,8,9,10000)

# 6. **kwargs (Variable-Length Keyword Arguments)
def kwargsfun(**kwargs):
    print(kwargs)


kwargsfun(name="Suresh",age=32)
kwargsfun(name="jordan",age=56,Location="UK")
kwargsfun(name="Ravi Kiran",age=22,Location="HYD",sal=500000)

# 7. Using *args and **kwargs Together

def argskwargs(a,b,*args,**kwargs):
    print('Value of a and b is:',a,b)
    print('Values of args is:',args)
    print('Values of kwargs is:',kwargs)

argskwargs(8,10,50000,40000,x="Suresh",y="Hello",Age=29)



