class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{self.fname}{self.lname}@gmail.com"
    def explain(self):
        return(f"This is {self.fname} {self.lname}")
    @property
    def prinem(self):
        if self.fname==None or self.lname==None:
            return ("Email is not set")
        return f"{self.fname}{self.lname}@gmail.com"
    @prinem.setter
    def prinem(self,string):
        print("Setting Now")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]
    @prinem.deleter
    def prinem(self):
        self.fname=None
        self.lname=None
nabbu=Employee("Nabaraj","Acharya")
amrit=Employee("Amrit","Acharya")
nabbu.fname="Indian"
print(nabbu.prinem)
nabbu.prinem="This.that.codewithme@.com"
# print(nabbu.prinem)
del nabbu.prinem
print(nabbu.prinem)