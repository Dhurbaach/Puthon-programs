# Health management system
# Clients-Harry,Rohan,Ram
def fundiet():
    print("Enter your diet:")
    d = input()
    return d


def funexe():
    print("Enter your exercise:")
    e = input()
    return e


def getdate():
    import datetime
    return datetime.datetime.now()


print("!!!WELCOME TO HEALTH MANAGEMENT SYSSTEM!!!")
print("Press 1 to continue:\n Press 0 to exit:")
cho = int(input())
while cho == 1:
    print("Do you want to \n1.store data or \n2.retrive data?")
    a = int(input())
    print("Whose?\n 1.Harry\n 2.Rohan\n 3.Ram")
    b = int(input())
    if a == 1 and b == 1:
        print("Which?\n 1.Excercise\n 2.Diet")
        c = int(input())
        if c == 1:
            with open("Harryexer.txt", "at") as f:
                f.write(funexe())
                f.write(str(getdate()))
        else:
            with open("Harrydiet.txt", "at") as f1:
                f1.write(fundiet())
                f1.write(str(getdate()))
    elif a == 1 and b == 2:
        print("Which?\n 1.Excercise\n 2.Diet")
        c = int(input())
        if c == 1:
            with open("Rohanexer.txt", "at") as f2:
                f2.write(funexe())
                f2.write(str(getdate()))
        else:
            with open("Rohandiet.txt", "at") as f3:
                f3.write(fundiet())
                f3.write(str(getdate()))
    elif a == 1 and b == 3:
        print("Which?\n 1.Excercise\n 2.Diet")
        c = int(input())
        if c == 1:
            with open("Ramexer.txt", "at") as f4:
                f4.write(funexe())
                f4.write(str(getdate()))
        else:
            with open("Ramdiet.txt", "at") as f5:
                f5.write(fundiet())
                f5.write(str(getdate()))
    elif a == 2 and b == 1:
        print("Which?\n 1.Excercise\n 2.Diet")
        c = int(input())
        if c == 1:
            with open("Harryexer.txt", "rt") as f:
                print(f.readlines())
        else:
            with open("Harrydiet.txt", "rt") as f1:
                print(f1.readlines())
    elif a == 2 and b == 2:
        print("Which?\n 1.Excercise\n 2.Diet")
        c = int(input())
        if c == 1:
            with open("Rohanexer.txt", "rt") as f2:
                print(f2.readlines())
        else:
            with open("Rohandiet.txt", "rt") as f3:
                print(f3.readlines())
    elif a == 2 and b == 3:
        print("Which?\n 1.Excercise\n 2.Diet")
        c = int(input())
        if c == 1:
            with open("Ramexer.txt", "rt") as f4:
                print(f4.readlines())
        else:
            with open("Ramdiet.txt", "rt") as f5:
                print(f5.readlines())
    else:
        print("Invalid input!")
    print("Do you want to?\n1.Continue\n2. Exit")
    cho = int(input())
