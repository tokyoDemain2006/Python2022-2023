def MENU():
    selection = input("what do you want to do: ")
    if selection == "1":
        CHALLENGE_5()
    elif selection == "2":
        CHALLENGE_6()
    
def CHALLENGE_5():
    Fname = input("what is your first name: ")
    Sname = input("what is your surname: ")
    print(Fname + " " + Sname + " " + Fname + " " + Sname + " " + Fname + " " + Sname)
    MENU()

def CHALLENGE_6():
    DaysPerWeek = 7
    HoursPerDay = 24
    MinutesPerHour = 60
    MinutesPerWeek = (MinutesPerHour * HoursPerDay * DaysPerWeek)
    print(MinutesPerWeek)
    MENU()

def CHALLENGE_7():
    Name = input("what is your name
    
MENU()
