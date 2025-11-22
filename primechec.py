n = int(input('Enter the value of n:\n'))
cnt = 0

# Checking for factors from 1 to n
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1

# A prime number has exactly two factors: 1 and itself
if cnt == 2:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
