# Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#
# Rules
# Pygame module to play audio
from pygame import mixer
mixer.init()
import time

def gettime():
    return time.asctime()

def funcwater():
    while True:
        print("Drink 1 glass of water")
        print("Do you drink?\nY.yes\nN.no")
        cho = (input())
        cho=cho.upper()
        if cho=="Y":
            mixer.music.stop()
            with open("water.txt","at") as f:
                f.write(f"Drank and Time{gettime()}\n")
            break
        else:
            print("Invalid input!\n Stop music after 5 second")
            time.sleep(5)
            continue
def funceyes():
    while True:
        print("Do excercise of eye!")
        print("Do you do excercise of eyes?\nY.yes\nN.no")
        ch=input()
        ch = ch.upper()
        if ch=="Y":
            mixer.music.stop()
            with open("eye.txt","at") as f1:
                f1.write(f"Done and Time{gettime()}\n")
            break
        else:
            print("Invalid input!\n Stop music after 5 second")
            time.sleep(5)
            continue

def funcex():
    while True:
        print("Do physical excercise!")
        print("Do you do excercise?\nY.yes\nN.no")
        ch=input()
        ch = ch.upper()
        if ch == "Y":
            mixer.music.stop()
            with open("exc.txt", "at") as f1:
                f1.write(f"Done and Time{gettime()}\n")
            break
        else:
            print("Invalid input!\n Stop music after 5 second")
            time.sleep(5)
            continue

if __name__ == '__main__':
    init_water=time.time()
    init_eyes=time.time()
    init_phy=time.time()
    water = 2400
    eyes = 1800
    phy = 2700
    print("\n\t\t\t------------Hello! The Healthy Programmer is set------------\n")
    while True:

        if time.time() - init_water > water:
            mixer.music.load("water.mp3")
            mixer.music.play()
            print(f"Time is: {gettime()}")
            funcwater()
            init_water = time.time()

        if time.time() - init_eyes > eyes:
            mixer.music.load("eyes.mp3")
            mixer.music.play()
            print(f"Time is: {gettime()}")
            funceyes()
            init_eyes = time.time()

        if time.time() - init_phy > phy:
            mixer.music.load("physical.mp3")
            mixer.music.play()
            print(f"Time is: {gettime()}")
            funcex()
            init_phy = time.time()






