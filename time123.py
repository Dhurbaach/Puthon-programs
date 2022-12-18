import time
# local_time=time.asctime(time.localtime(time.time()))
# print(local_time)
# print(time.time())
# print(time.localtime())
# print(time.asctime())
# k=1
# while k<10:
#     print("Dhurba is a good boy.")
#     time.sleep(2)
#     k+=1
# with open("tme.txt","at") as f:
#     c=time.asctime()
#     f.write(f"Time={c}\n")


from pygame import mixer

mixer.init()
import time


# functions

def getdate():
    return time.asctime(time.localtime(time.time()))


def stWater():
    while True:
        stopWater = str(input("\nEnter \"drank\" to stop music:\n")).lower()

        if stopWater == "drank":
            mixer.music.stop()
            with open("Water.txt", "a") as f:
                f.write(f"{getdate()}\nPani pi liya tha!\n\n")
            print("\n\t\t---------You did it! You are health conscious---------\n")
            print("\t\t\t---------Next reminder is set---------\n")
            break
        else:
            print("\nInvalid input! Enter \"drank\" to stop the music after 5 sec.\n")
            time.sleep(5)
            continue


def stEyes():
    while True:
        stopEyes = str(input("\nEnter \"eydone\" if you done eyes exercise to stop music:\n")).lower()

        if stopEyes == "eydone" or stopEyes == "ey done":
            mixer.music.stop()
            with open("Eyes.txt", "a") as f:
                f.write(f"{getdate()}\nAnkh ka exercise kar liya tha!\n\n")
            print("\n\t\t---------You did it! You are health conscious---------\n")
            print("\t\t\t---------Next reminder is set---------\n")
            break
        else:
            print("\nInvalid input! Enter \"eydone\" if you done eyes exercise to stop the music after 5 sec.\n")
            time.sleep(5)
            continue


def stPhysical():
    while True:
        stopPhysical = str(input("\nEnter \"exdone\" if you done a physical exercise to stop music:\n")).lower()

        if stopPhysical == "exdone" or stopPhysical == "ex done":
            mixer.music.stop()
            with open("Physical.txt", "a") as f:
                f.write(f"{getdate()}\nExercise kar liya tha!\n\n")
            print("\n\t\t---------You did it! You are health conscious---------\n")
            print("\t\t\t---------Next reminder is set---------\n")
            break
        else:
            print("\nInvalid input! Enter \"exdone\" if you done a physical exercise to stop the music after 5 sec.\n")
            time.sleep(5)
            continue


# main program
if __name__ == '__main__':

    init_water = time.time()
    init_eyes = time.time()
    init_phy = time.time()
    init_msg = time.time()

    water = 2400
    eyes = 1800
    phy = 2700
    msg = 20

    print("\n\t\t\t------------Hello! The Healthy Programmer is set------------\n")

    while True:

        if time.time() - init_water > water:
            mixer.music.load("water.mp3")
            mixer.music.play()
            print(f"Time is: {getdate()}")
            stWater()
            init_water = time.time()

        if time.time() - init_eyes > eyes:
            mixer.music.load("eyes.mp3")
            mixer.music.play()
            print(f"Time is: {getdate()}")
            stEyes()
            init_eyes = time.time()

        if time.time() - init_phy > phy:
            mixer.music.load("physical.mp3")
            mixer.music.play()
            print(f"Time is: {getdate()}")
            stPhysical()
            init_phy = time.time()

        if time.time() - init_msg > msg:
            print(f"\nTime: {getdate()}\nThe healthy programmer is working in the background!")
            print("\n\t\t\t   -------------wishing you a good health!-------------\n")
            init_msg = time.time()