c=input("Enter your name:")
try:
    print(a);
except Exception as e:
    if c=="Dhurba":
        raise ValueError("Dhurba is blocked he is not allowed")
    print('Exception handeled')

a=[1,2,"33"]
b=[1,2,"33"]
print(b is a)
print(b ==a)