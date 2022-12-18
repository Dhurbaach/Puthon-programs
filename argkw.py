def func(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{key} is a {value}")
lst= ["Rama", "Shyam" , "Hari" , "Nabaraj"]
normal = "This is a normal argument and the students are:"
dic = {"Dhurba": "Programmer", "Govinda": "Monitor", "Harry": "Desktop"}
func(normal, *lst, **dic)
