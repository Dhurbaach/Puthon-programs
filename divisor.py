n=int(input("Enter the number of apples that Hari have:"))
mn=int(input("Enter the lower limit:"))
mx=int(input("Enter the upper limit:"))
if mn == mx:
    print("This is not a range")
else:
    for i in range(mn,mx+1,1):
        if n%i==0:
            print(f"{i} is a divisor of {n}")
        else:
            print(f"{i} is not a divisor of {n}")