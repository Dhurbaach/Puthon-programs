#Dictionary is nothing but key value
d1={}
print(type(d1))
d2={"Amrit":"Student","Rohan":"Teacher","Harry":"Programmer","Sunil":{"Mor":"Running","Noon":"Football","Evening":"Dieting"}}
print(d2["Sunil"]["Mor"])
d2["Alok"]="Junk food"#can also use update function
print(d2)
del d2["Rohan"]
print(d2)
d3=d2.copy()
del(d3['Harry'])
print(d2.keys())
