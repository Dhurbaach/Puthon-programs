c=[]
while True:
    c.append(int(input("Enter the numbers in the list:")))
    c1=int(input("Enter 1 to if done:"))
    if c1==1:
        break
c2=[]
for item in c:
    if item<=10:
        c2.append(item)
    elif item>10:
        while True:
            item=item+1
            if str(item)==str(item)[::-1]:
                c2.append(item)
                break
    else:
        print("Invalid input!")
print(c2)