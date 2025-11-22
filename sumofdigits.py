n = int(input('Enter the value of n:\n'))
sumval =0
while n !=0:
    digit = n%10
    sumval +=digit
    n =int(n/10)
print('The sum of the digits is:',sumval)