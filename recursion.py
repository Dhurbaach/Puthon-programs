def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
num = int(input("Enter any number:"))
v=factorial(num)
print("The factorial of given number is:",v)
def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
num=int(input("Enter the value of n:"))
v=fibo(num)
print(v)