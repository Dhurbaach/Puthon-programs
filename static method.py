class Studnt:
    noleaves=10
    def __init__(self,aname,arole,astandard):
        self.name=aname
        self.role=arole
        self.std=astandard
    @classmethod
    def any(cls,newleaves):
        cls.noleaves=newleaves
    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def printgood(str):
        print("This is good "+str)
newleaves=12
person1 = Studnt("Harry","Teacher",12)
person2 = Studnt("larry","Agent",11)
karan=Studnt.from_str("Karan-Student-14")
# person2.any(34)
# print(Studnt.noleaves)
# print(karan.name)
karan.printgood("Dhurba")