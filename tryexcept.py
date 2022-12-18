f1=open("Harrydiet.exe")
try:
    f=open("ANy.txt")
except Exception as e:
    print(e)
else:
    print("This will run only if except is not runing")
finally:
    print("run this anyway....")
    f1.close()
print("Important Stuff")