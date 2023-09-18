import time
import csv

def login():
    choice = input("Do you allready have a login? Y or N")
    if choice == "y" or "Y":
        next
    elif choice == "n" or "N":
        signup()
    username = input("Username : ")
    password = input("Password : ")
    with open("C:/Users/M2202787/OneDrive - Middlesbrough College/Documents/GitHub/Year-1-T-Level-MbroColl/HotelBookingSystem/LoginDatabase.csv" , "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if username and password in row:
                print("access granted")
                Home()
            else:
                print("user not found")
            

def signup():
    username = input("What do you want to make your username")
    password = input("What do you want to make your password")
    with open("C:/Users/M2202787/OneDrive - Middlesbrough College/Documents/GitHub/Year-1-T-Level-MbroColl/HotelBookingSystem/LoginDatabase.csv" , "a") as file:
        csvwriter = csv.writer
        for row in csvwriter:
            next
        
def Home():
    choice = input("Would you like to\n1: Make a booking\n2: View room info\n3: View restaurant info\n4: View costs\n5: View hotel information\n6: End the program\n")
    if choice == "1":
        Booking()
    elif choice == "2":
        RoomInfo()
    elif choice == "3":
        RestaurantInfo()
    elif choice == "4":
        Payments()
    elif choice == "5":
        HotelRecords()
    elif choice == "6":
        exit()
    else:
        print ("enter a valid value")
        Home()

def dateFunction(date):
    date = input("what date would you like to book on")

def Booking():
    with open("C:/Users/M2202787/OneDrive - Middlesbrough College/Documents/GitHub/Year-1-T-Level-MbroColl/HotelBookingSystem/FreeHotelRooms.csv" , "r") as file:
        csvreader = csv.reader(file)
        print("Room number, Bed number, Floor number, Availability")
        for row in csvreader:
            if "free" in row:
                print(row)
            else:
                next
        choice = str(input("what room do you want to book"))
        count = 0
        for row in csvreader:
            if choice in row:
                print("room can be booked, contact the booking number to book")
                count = count + 1
            else:
                next

    if count == 0:
        print("room cannot be booked")
            

def RoomInfo():
    with open("C:/Users/M2202787/OneDrive - Middlesbrough College/Documents/GitHub/Year-1-T-Level-MbroColl/HotelBookingSystem/FreeHotelRooms.csv" , "r") as file:
        csvreader = csv.reader(file)
        print("Room number, Bed number, Floor number, Availability")
        for row in csvreader:
            print(row)
        else:
            next
    Home()
    

def RestaurantInfo():
    choice = input("Would you like to look at\n1: The menu\nor\n2: The reviews\n")
    if choice == "1":
        print("\n\nAPPETIZERS\nFrench Fries : £1.50\nSoup Of The Day : £2.50\nSourdough Bread : £3.00\nCheese Board : £2.50\n\n")
        print("\n\nMAINS\nFlat Iron Steak : £10.50\nPan Grilled Ribeye : £15.99\nMagerita Pizza : £7.50\nCarbonara : £8.30 \nRavioli : £4.50\nWagu Steak : £23.56\n\n")
        print("\n\nDESERTS\nSticky Toffee Pudding : £4.20\nChocolate Brownie : £2.30 \nIce Cream : £2.50\n")
    elif choice == "2":
        print("✪✪✪✪✪ : Anonomous User : Visited here for my Dads 80th Birthday yesterday, knew it wouldn’t disappoint! Two family members had to drop out late on due to illness which wasn’t a problem for Phil! Food amazing as always, staff attentive, love this place")
        print("✪✪✪✪ : John Doe : Food, service and hospitality were spot on. A chat with the owner about the history of the building and their upcoming plans added to the evening.")
    else:
        print("Please enter a valid input")
        RestaurantInfo()
    Home()

def Payments():
    print("PRICING\n\n1 Bed Room : £10.40 per night\n2 Bed Room : £15.50 per night\n3 Bed Room : £17.90 per night\n4 Bed Room : £22.30 per night\n")
    print("EXEPTIONS\n\nFloor 5 = +£5.00 per night\n\n\n")
    Home()

def HotelRecords():
    print("Artemis Hotel has been a respected hotel and restaurant in the local area and is beggining to spread nation wide. We value ourselves in quality rooms and food for reasonable prices. Artemis Hotel has been serving customers and providing shelter since ~1956 and we pride ourselves in saving customers money and providing the basic right of shelter.")
    
login()
