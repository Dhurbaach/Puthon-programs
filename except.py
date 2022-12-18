a=input("Enter num1")
b=input("Enter num2")
try:
    print("The sum of these two numbers is:",int(a)+int(b))
except Exception as e:
    print(e)
print("This line is very important")
