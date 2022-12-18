"""list=["harry",1,4,2,6,7,90,46,"a","b","si","/"]
for item in list:
        if str(item).isnumeric() and item>6:
           print(item)"""
i=0
while(True):
    if i<5:
        i=i+1
        continue #returns to while
    if i==45:
        break #stops the loop
    print(i,end=" ")
    i=i+1