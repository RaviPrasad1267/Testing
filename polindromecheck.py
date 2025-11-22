str = input("Enter the string:\n")
print("Polindrome check using ::-1:")
res1 = str[::-1]
if str == res1:
    print(str,"is polindrome")
else:
    print(str,"Not a polkindrome")

