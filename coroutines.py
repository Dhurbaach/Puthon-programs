def searcher():
    with open("words.txt") as f:
        name=f.read()
        while True:
            text = (yield)
            if text in name:
                print("Your name is in the book")
            else:
                print("Your name is not in the book")
search = searcher()
print("search started")
next(search)
print("Next method run")
c=str(input("Enter your word"))
search.send(c)
c=str(input("Enter your word"))
search.send(c)
c=str(input("Enter your word"))
search.send(c)
# search.send("Some")
