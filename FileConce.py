# File Modes:
# r------->Read
# w------->Write----->Overwrite
# a------->Append
# r+------->read and Write
# w+------>
# a+

f1 = open("Exampleoutput.txt","a+")
f1.write("My name is suresh new line added at the end")
f1.close()

# f2 = open("File2.txt","r")
# content = f2.read()
# print("F2 file content is:",content)

f3 = open("Exampleoutput.txt","r")
content1 = f3.readlines()
print("F3 file content is:",content1)
