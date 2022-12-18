#Pattern printing
row=4
print("Enter 0 or 1")
c=int(input())
d=bool(c)
if d == True:
    for i in range(row):
        for j in range(i+1):
            print("*",end="")
        print("")
else:
    for i in range(row):
        for j in range(4-i):
            print("*",end="")
        print("")