import random as rd
c1=int(input("Enter the lower range of your number:"))
c2=int(input("Enter the upper range of your number:"))
num=rd.randint(c1,c2)
k1=0
k=0
def player1():
    print("First player's turn")
    global k
    while True:
        ch1=int(input(f"Enter your guess from {c1} to {c2}"))
        k+=1
        if ch1>num:
            print("Wrong! guess a smaller number again")
        elif ch1<num:
            print("Wrong! guess a greater number again")
        else:
            print("Correct guess!")
            print(f"You took {k} trials to guess the number")
            break
    return k
def player2():
    print("Second player's turn")
    global k1
    while True:
        ch2 = int(input(f"Enter your guess from {c1} to {c2}"))
        k1+=1
        if ch2 > num:
            print("Wrong! guess a smaller number again")
            continue
        elif ch2 < num:
            print("Wrong! guess a greater number again")
            continue
        else:
            print("Correct guess!")
            print(f"You took {k1} trials to guess the number")
            break
    return k1
player1()
player2()
if k > k1:
    print("Player 2 wins the game!")
elif k<k1:
    print("Player 1 wins the game!")
else:
    print("Draw!!!")
print(f"The number was {num}")
