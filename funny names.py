import random as rd
c=int(input("Enter the number of names you want to enter:"))
nam=[]
print(f"Enter the name of your {c} friends:")
for i in range(c):
    nam.append(input())
fname = [name.split()[0] for name in nam]
lname = [name.split(" ", 1)[1] for name in nam]
for _ in nam:
   rand_fnam=rd.choice(fname)
   rand_lnam=rd.choice(lname)
   print(f"The funny names are\n {rand_fnam} {rand_lnam}")
   fname.remove(rand_fnam)
   lname.remove(rand_lnam)