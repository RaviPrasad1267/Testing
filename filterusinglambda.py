list3 = ['Manju','Nayana','cha','dharu','san']
def len_check3(n):
    if len(n) > 3:
        return n

res = list(filter(len_check3,list3))
print(res)

lambdares =list(filter(lambda x:len(x)>3,list3))
print(lambdares)

list2 =[2,6,7,12,-1,-4,10,43,14]
def oddnum_fil(n):
    if n%2!=0:
        return  n
oddnum = list(filter(oddnum_fil,list2))
print("Odd number from the list2 with using defination is:",oddnum)

print("Odd number from lambda fun:")
lamodd =list(filter(lambda x:x%2!=0,list2))
print(lamodd)



