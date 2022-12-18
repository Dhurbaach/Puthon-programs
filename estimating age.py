age=str(input("Enter your age or birthyear:"))
if len(age)==4:
    age=int(age)
    if age<1915:
        print("You are the oldest man alive.")
    elif age > 2022:
        print("You are not born till now.")
    y2=int(input("Enter the year when you want to calculate age:"))
    c=y2-age
    print(f"Your age will be {c} in year {y2}")
    print(f"You will be 100 years in", age + 100)
elif len(age)==2 or len(age)==3 or len(age)==1:
    age=int(age)
    if age > 150:
        print("You are the oldest man alive.")
    elif age < 0:
        print("You are not born till now.")
    a2=int(input("Enter the year when you want to calculate age:"))
    birth=2022-age
    d=a2-birth
    print(f"Your age will be {d} in year {a2}")
    print(f"You will be 100 years in",birth+100)
else:
    print("Invalid input!")
