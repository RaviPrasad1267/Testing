""" print syntax is print(*objects,sep="",end="",file=sys.stdout,flush=False)
# Obejects ---are Varibles, string or list,dict anything
# sep ----> This is used to which character need to be there between the each objects
# end  ---> This character shows which character should be there at the end of the file
#  file ---> it say where the output should be there by deafult its sys.stdout (console) screen when
    we want to store file then pass the actuval file name
flush ---->Forcing immidate output  By defualt its false    """
a=10
b=23.4
c=True
print("Hello","how are you")
print("Hello","how are you",sep="-")
print("Hello","how are you",sep=",",end="\n")
print(a,b,c,sep="/" )
for i in range(3):
    print(i,end="\n")
for i in range(3):
    print(i,end=" ")
with open("NewFile.txt",mode="w") as f:
    print("Hello welcome to the python basics class",file=f)
# Interview use case:
# Logging, report generation, debugging



