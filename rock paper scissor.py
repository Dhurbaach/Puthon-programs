import random as rd
list1=["Rock","Paper","Scissor"]
print("You will have 10 chances\n")
pc=0
ph=0
chance=10
ch=1
while chance>0:
    comp = str(rd.choice(list1))
    print("Enter your choice?\nR for rock:\nP for paper:\nS for scissor:")
    cho = str(input())
    d = cho.upper()
    if d=="R" and comp=="Rock":
        print("Draw")
        print(f"You:{cho}")
        print(f"Computer:{comp}")
        pc=pc+0
        ph=ph+0
        chance=chance -1
        print(f"You have {chance} chance left")
    elif d =="R" and comp=="Paper":
        print("You Lose!!!")
        print(f"You:{cho}")
        print(f"Computer:{comp}")
        pc=pc+1
        ph=ph+0
        chance = chance - 1
        print(f"You have {chance} chance left")
    elif d=="R" and comp=="Scissor":
        print("You Win!!!")
        print(f"You:{cho}")
        print(f"Computer:{comp}")
        pc = pc + 0
        ph = ph + 1
        chance = chance - 1
        print(f"You have {chance} chance left")
    elif d=="P" and comp=="Paper":
        print("Draw!!!")
        print(f"You:{cho}")
        print(f"Computer:{comp}")
        pc = pc + 0
        ph = ph + 0
        chance = chance - 1
        print(f"You have {chance} chance left")
    elif d=="P" and comp=="Scissor":
        print("You Lose!!!")
        print(f"You:{cho}")
        print(f"Computer:{comp}")
        pc = pc + 1
        ph = ph + 0
        chance = chance - 1
        print(f"You have {chance} chance left")
    elif d=="P" and comp=="Rock":
        print("You Win!!!")
        print(f"You:{cho}")
        print(f"Computer:{comp}")
        pc = pc + 0
        ph = ph + 1
        chance = chance - 1
        print(f"You have {chance} chance left")
    elif d=="S" and comp=="Rock":
        print("You Lose!!!")
        print(f"You:{cho}")
        print(f"Computer:{comp}")
        pc = pc + 1
        ph = ph + 0
        chance = chance - 1
        print(f"You have {chance} chance left")
    elif d=="S" and comp=="Paper":
        print("You Win!!!")
        print(f"You:{cho}")
        print(f"Computer:{comp}")
        pc = pc + 0
        ph = ph + 1
        chance = chance - 1
        print(f"You have {chance} chance left")
    elif d=="S" and comp=="Scissor":
        print("Draw!!!")
        print(f"You:{cho}")
        print(f"Computer:{comp}")
        pc = pc + 0
        ph = ph + 0
        chance = chance - 1
        print(f"You have {chance} chance left")
    else:
        print("Please enter valid input!")
        chance = chance - 1
        print(f"You have {chance} chance left")
if ph<pc:
    print(f"Computer wins! ")
elif pc<ph:
    print(f"Human wins!")
else:
    print("!!!Draw!!!")
print(f"Computer have {pc} points")
print(f"Human have {ph} points")
print("!Thank You!")

