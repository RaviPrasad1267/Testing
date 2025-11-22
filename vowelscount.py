str = input("Enter the str:\n")
vowels ='AEIOUaeiou'
cnt =0
for i in str:
    if i in vowels:
        cnt += 1
print(f'Vowels count of the {str} is: {cnt}')