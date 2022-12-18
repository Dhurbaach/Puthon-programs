class Studnt:

    def __init__(self,aname,arole,astandard):
        self.name=aname
        self.role=arole
        self.std=astandard

person1 = Studnt("Harry","Teacher",12)
person2 = Studnt("larry","Agent",11)
print(person1.name)