# import time
# from functools import lru_cache
#
# @lru_cache(maxsize=3)
# def some(n):
#     time.sleep(n)
#     return n
# if __name__ == '__main__':
#     print("Now running some work")
#     some(3)
#     print("Done...calling again")
#     some(3)
#     print("Called again")

from functools import lru_cache
@lru_cache(maxsize=2)
def pirrn(n):
    if n%2==0:
        print(f"{n} is even number")
    else:
        print(f"{n} is odd number")
if __name__ == '__main__':
    c = int(input("Enter any number:"))
    pirrn(c)
    # print("HEllO")
    pirrn(c)
    pirrn(c)
    pirrn(c)
