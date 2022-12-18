class A:
    def meth(self):
        print("This is a method in class A")
class B(A):
    def meth(self):
        print("This is a method in class B")
class C(A):
    def meth(self):
        print("This is a method in class C")
class D(C,B):
    def meth(self):
        print("This is a method in class D")
a=A()
b=B()
c=C()
d=D()
d.meth()