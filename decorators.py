def dec1(fun1):
    def now():
        print("Executing now")
        fun1()
        print("Executed")
    return now
def dhurba():
    print("Dhurba is a good boy")
dhurba=dec1(dhurba)
dhurba()