c1=int(input("Enter how many numbers you want to enter:"))
c2=[]
for i in range(c1):
    c2.append(int(input(f"Enter {i+1} number:")))
for item in c2:
    while True:
        item+=1
        if str(item)==str(item)[::-1]:
            print(f"The next palindrome number is {item}")
            break
# a=234
# print(str(a)[::-1])