# file io basis
# f=open("dhurba.txt","r")
"""content=f.read()
print(content)
#for line in f
#print(line)
#print(f.readline())
f.close()
f=open("dhurba.txt","a")
a=f.write("\nDhurba plays football")
print(a)
f.close()"""
f=open("dhurba.txt","r+")
print(f.read())
f.write("Thank you!")