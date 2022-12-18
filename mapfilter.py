# # # list=["johncena","Khali","Randywortern","Dhamaka"]
# # # a=" , ".join(list)
# # # print(a)
# # num=["1","2","23","45","48","7"]
# # num=list(map(int,num))
# # num[1]=num[1]+2
# # # print(num)
# # sqr=lambda x:x*x
# # square=list(map(sqr,num))
# # print(square)
# num=["1","2","23","45","48","7"]
# num=list(map(int,num))
# a=lambda x:x*x
# b=lambda x:x+10
# fun=[a,b]
# for i in range(5) :
#     c=list(map(lambda x:x(i),fun))
#     print(c)
# nu=[1,2,3,4,5,6,7,8,9,0]
# def gr5(x):
#     return x<5
# c=list(filter(gr5,nu))
# print(c)

from functools import reduce
nu=[1,2,3,4,5,6,7,8,9]
a=reduce(lambda x,y:x+y,nu)
print(a)