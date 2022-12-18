class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.var1="I am in class A's constructor"
        self.classvar1="I am instance variable in class A"
        self.special="Special"
class B(A):
    classvar2="I am in class B"
    def __init__(self):
        super().__init__()
        self.var1="I am in class A's constructor"
        self.classvar1="I am instance variable in class A"
a=A()
b=B()
print(b.special,b.var1)