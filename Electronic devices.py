class Electronics:
    sourc="Alternating Current"
    movable="Maybe or Not"
    var=1
    def __init__(self,name,company):
        self.name=name
        self.company=company

    def printx(self):
        return(f"This is {self.name} from {self.company} company")
class Pocketdevices(Electronics):
    source="Direct current"
    movable = "Yes Portable"
class Phone(Pocketdevices):
    processor="11 ghz"
    source="Direct Current"
mobile=Phone("Iphone","Apple")
Earpod=Pocketdevices("Ipod","Android")
laptop=Electronics("Television","Samsung")
print(mobile.printx())
print(mobile.var)

