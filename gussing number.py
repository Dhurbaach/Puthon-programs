num=12
chance=10
count=0
while chance>0:
    print("Enter your guess:")
    guess=int(input())
    if guess > num:
        chance = chance - 1
        count=count+1
        print("Less than this")
        print("Number of chances left:", chance)
        continue
    elif guess<num:
        chance = chance - 1
        count = count + 1
        print("Greater than this")
        print("Number of chances left:", chance)
        continue
    else:
        chance=chance-1
        count = count + 1
        print("Congraluations! Your guess is correct")
        print("No of guesses required=",count)
        break
if chance==0:
    print("Game Over!")