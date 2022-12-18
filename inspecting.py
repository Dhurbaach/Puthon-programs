class Student:
    namofsch="Pokahra Academy"
    Levelofsch="Secondary"
    def __init__(self,name,clas,rollno,subjects):
        self.name=name
        self.clas=clas
        self.rollno=rollno
        self.subjects=subjects
    def prin(self):
        return (f"The name is {self.name} and Subjects are: {self.subjects}")

    @property
    def dele(self):
        return 0

    @dele.deleter
    def dele(self):
        self.rollno=None
hari=Student("Hari",9,19,["English","Maths","Science"])
ram=Student("Ram",8,1,["Maths","Science"])
print(ram.prin())
del hari.dele
print(ram.rollno)
import inspect
print(inspect.getmembers(Student))
print(inspect.isclass(hari))
print(inspect.isclass(Student))