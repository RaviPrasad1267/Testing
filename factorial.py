n = int(input("Enter the value of n:\n"))
if n<0:
    print("You entred the negative value")
else:
    fact = 1
    for i in range(1,n+1):
        fact = fact *i
    print(" The fact value is:",fact)

