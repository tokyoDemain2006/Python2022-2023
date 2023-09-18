import csv
from csv import writer
def menu():
    choice = input("What would you like to do\n1: Input a new entry\n=================or=================\n2: Read the database\n=================or=================\n3: Exit the program\n")
    if choice == "1":
        newEntry()
    elif choice == "2":
        readDatabase()
    elif choice == "3":
        quit()
    else:
        print("=================\nPlease enter a valid input\n=================")
        menu()

def newEntry():
    speed = input("Enter speed:             ")
    numberPlate = input("Enter Licence Plate:     ")
    if int(speed) <= 70:
        print("driver was not speeding")
        menu()
    list = [speed,numberPlate]
    with open("SpeedingDatabase.csv", "a") as file:
        csvwriter = writer(file)
        csvwriter.writerow(list)
        file.close()
        print("data has been entered")

def readDatabase():
    with open("SpeedingDatabase.csv", "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)
        

menu()
