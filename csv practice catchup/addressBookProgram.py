def menu():
    choice = input("would you like to\n==============================\n1: Search for contacts\n==============================\n2: Add a new contact\n")
    if choice == "1":
        searchFunction()
    else:
        newContact()
def searchFunction():
    file = open("addressBookProgram.csv", "r")
    line = file.readline()
    search = input("what would you like to search by\n==============================\n1: Name\n==============================\n2: Address\n==============================\n3:City\n==============================\n4: Phone number\n")

    if search == "1":
        name = input("what name do you want to search: ")
        while(line):
            data = line.split(",")
            if data[0] == name:
                print(line)
                line = file.readline()
            else:
                line = file.readline()

    if search == "2":
        address = input("what address do you want to search: ")
        while(line):
            data = line.split(",")
            if data[1] == address:
                print(line)
                line = file.readline()
            else:
                line = file.readline()

    if search == "3":
        city = input("what city do you want to search: ")
        while(line):
            data = line.split(",")
            if data[2] == city:
                print(line)
                line = file.readline()
            else:
                line = file.readline()

    if search == "4":
        number = input("what Phone Number do you want to search: ")
        while(line):
            data = line.split(",")
            if data[3] == number:
                print(line)
                line = file.readline()
            else:
                line = file.readline()

def newContact():
    file = open("addressBookProgram", "w")
    newName = ("what is the name of the user you want to enter")
    newAddress = ("what is the address of the user you want to enter")
    newCity = ("what is the city of the user you want to enter")
    newPhoneNumber = ("what is the phone number of the user you want to enter")
    tempList = [newName,newAddress,newCity,newPhoneNumber]
    file.write(tempList)

menu()
