li=[]
while True:
   c=input("Enter items in your list:")
   li.append(c)
   ch=int(input("Press 1 if done any if not:"))
   if ch==1:
       break

x=len(li)
l1=li[::-1]
l2=li[:]
l2.reverse()
l3=li[:]
# print(l3)
for i in range(x//2):
    l3[i],l3[x-i-1]=l3[x-i-1],l3[i]
print(f"The reverse of {li} is\n {l1}\n {l2}\n {l3}")
if l1==l2 and l2==l3:
    print("All types are same ")