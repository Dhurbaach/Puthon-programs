# def a_first(a):
#     return a[1]
a=[[1,14],[0,3],[7,8]]
# a.sort(key=a_first)
# print(a)
a.sort(key=lambda a:a[1])
print(a)