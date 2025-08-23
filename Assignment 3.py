#Task1
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter a number: "))
print(factorial(num))
#Task2
import math
num=int(input("Enter a number: "))
square_root=math.sqrt(num)
log=math.log(num)
sine=math.sin(log)
print("square root:",square_root)
print("log:",log)
print("sin:",sine)