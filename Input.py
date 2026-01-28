""" 1️⃣ What is input() in Python?
input() is a built-in function used to read user input from standard input (keyboard).
# data alwas read as string even if we enter the value when we want then needs to change to particular data tyep"""
a = input("Enter the value of a:")
print(type(a))
A = int(input("Enter the value of A:"))
print(type(A))
B = float(input("Enter the value of B:"))
print(type(B))
# Reading more than one numbers and coverting as int
c,d = map(int,input("Enter the two numbers c  d").split())
print(c,d)