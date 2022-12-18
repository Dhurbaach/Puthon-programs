class Student():
    noleaves=18

    def prindet(self):
        return f"Name is {self.name} and standard is {self.std}"
    pass
harry=Student()
larry=Student()
harry.name="Dhurba"
harry.std=12
larry.name="Dipeka"
larry.std=13
larry.subj=["English","Physics","Chemistry"]
# print(harry.__dict__)
# harry.noleaves=12
# print(harry.__dict__)
# print(larry.subj)
print(larry.prindet())