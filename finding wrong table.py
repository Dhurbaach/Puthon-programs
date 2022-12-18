import random as rd
def rohanmult(num):
    li=[]
    a=rd.randint(1,11)
    x=num*a
    print(f"Random number is {x}")
    for i in range(1,11):
        if i!=4:
            li.append(i*num)
        else:
            li.append(x)
    print(f"The multiplication table of {num} is:\n {li}")
    return (li)
def iscorrect(num2,k):
    for i in range(1,11):
        if k[i-1]!=i*num2:
            print(f"The value is incorrect at {i}")
if __name__ == '__main__':
    c=int(input("Enter any number to print table of:"))
    k=rohanmult(c)
    iscorrect(c,k)