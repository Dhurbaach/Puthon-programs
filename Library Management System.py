# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input
class Library:
    def __init__(self,list,name):
        self.list=list
        self.name=name
        self.lenddict={}
    def prin(self):
        print(f"Name of library={self.name}\nName of books=")
        for books in self.list:
            print(books)
    def lendbook(self,user,book):
        #  if book not in dhurba.list:
        #     print("Book is not in the library")
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Book dictionary has been updated")
        else:
            print(f"Book has been already lended by {self.lenddict[book]}")
    def addbook(self,book):
        self.list.append(book)
        print("Book has been added to the booklist")
    def returnbook(self):
        self.lenddict.pop(book)
if __name__ == '__main__':
    dhurba=Library(["Python","cpp","Poor dad rich dad","Mathematics"],"Dhurba's Library")
    cho="y"
    while cho=="y":
        print(f"Welcom to the {dhurba.name}")
        print("Enter your choice to continue")
        print("1.Display Books")
        print("2.Lend book")
        print("3.Add book")
        print("4.Return book")
        ch = int(input())

        if ch==1:
            dhurba.prin()
        elif ch==2:
            book=input("Enter the name of your book you want to lend")
            user=input("Enter your name")
            dhurba.lendbook(user,book)
        elif ch==3:
            book=input("Enter the name of your book you want to add")
            dhurba.addbook(book)
        elif ch==4:
            book=input("Enter the name of your book you want to return")
            dhurba.returnbook()
        else:
            print("Invalid Input!")
        print("Do you want to continue?y. yes n. no")
        cho=input()
        cho=cho.lower()
        # print("Press c.to continue and q. to quit")
        # cho = " "
        # while(cho!="q" and cho!="c"):
        #     cho=input()
        #     cho=cho.upper()
        #     if cho=="q":
        #         exit()
        #     elif cho=="c":
        #         continue

