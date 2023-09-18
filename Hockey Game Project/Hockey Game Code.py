import pandas as pd
import time as time

def GAME_SELECT():
    gameType = input("do you want to play\n1:The Computer\n2:2 Player")
    if gameType == "1":
        ONE_PLAYER_GAME()
    elif gameType == "2":
        TWO_PLAYER_GAME()
    else:
        print("input a valid value")
        GAME_SELECT()

def ONE_PLAYER_GAME():
    print("***Team 1***")
    T1 = pd.read_csv("Hockey Game Team 1.csv")
    print(T1)
    print("***Team 2***")
    T2 = pd.read_csv("Hockey Game Team 2.csv")
    print(T2)
    print("***Team 3***")
    T3 = pd.read_csv("Hockey Game Team 3.csv")
    print(T3) ae
    teamSelect = input("\n\n***What team do you want to play as***\n\n")
    if teamSelect == "1":
        TEAM_ONE()
    elif teamSelect == "2":
        TEAM_TWO()
    elif teamSelect == "3":
        TEAM_THREE()
    else:
        print("Enter a valid input")
        ONE_PLAYER_GAME()
            

def TEAM_ONE():
    count = 0
    playersUsed = []
    T1 = pd.read_csv("
    while count = <= 6:
        playerSelect = input("\n\n***What Player Do You Want To Play As***\n\n")
        if playerSelect not in playersUsed:
            
    

GAME_SELECT()
