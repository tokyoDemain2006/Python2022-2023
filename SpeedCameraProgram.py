import time
def SPEED_CAMERA():
    speed = int(input("what was the speed of the car: "))
    if speed >= 75:
        print("Issue Fine")
    elif speed > 70 and speed < 75:
        print("Issue Warning")
    else:
        print("No Action")
    SPEED_CAMERA()


def GAME_LEVEL_INCREASE():
    score = int(input("what score is the player at: "))
    if score > 1000:
        print("level up")
        GAME_LEVEL_INCREASE()
    else:
        GAME_LEVEL_INCREASE()
def WASHING_MACHINE():
    timeRemaining = input("what is the current remaining time: ")
    if timeRemaining == "0":
        while True == True:
            print("BEEP")
    else:
        WASHING_MACHINE()

choice = input("what do you want to do: ")
if choice == "1":
    SPEED_CAMERA()
elif choice == "2":
    WASHING_MACHINE()
else:
    GAME_LEVEL_INCREASE()
