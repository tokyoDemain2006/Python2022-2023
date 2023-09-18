from tkinter import *
#imports Tkinter
import webbrowser
#imports Webbrowser, which is the plugin for opening the CSV after the data has been inputted
import csv
#opens the CSV reader

app = Tk()
app.title("GUI Example 3")
app.geometry('200x250')
#starts and formats the GUI

def copyTextToLabel():
    #opens the function used to save to the file
    f = open("TkinterSchoolSystem.csv", "a")
    #opens the file
    data1 = (v.get())
    data2 = (v2.get())
    data3 = (v3.get())
    data4 = (v4.get())
    #gets the data from the text boxes and saves them into their own variables
    f.write(data4)
    f.write(",")
    f.write(data3)
    f.write(",")
    f.write(data2)
    f.write(",")
    f.write(data1)
    f.write(",")
    f.write("\n")
    #writes the data with formating
    webbrowser.open("TkinterSchoolSystem.csv")
    #opens the csv onto the screen

b1 = Button(app, text="Enter Data", command=copyTextToLabel)
#creates the button to save the data

l1 = Label(app, text="Form ID")
BlankLabel1 = Label(app, text = " ")
#creates some text to show up


v = StringVar()
#creates the variable to store the text box

e1 = Entry(app, textvariable = v)
#creates the text box and links it to the "v" variable

b1.pack(side='bottom')
e1.pack(side='bottom')
l1.pack(side='bottom')
BlankLabel1.pack(side = "bottom")
#packs/formats the buttons


l2 = Label(app, text="Form Tutor")
BlankLabel2 = Label(app, text = " ")

v2 = StringVar()

e2 = Entry(app, textvariable = v2)

e2.pack(side='bottom')
l2.pack(side='bottom')
BlankLabel2.pack(side = "bottom")
#repeat of previous function for a second button

l3 = Label(app, text="Last Name")
BlankLabel3 = Label(app, text = " ")

v3 = StringVar()

e3 = Entry(app, textvariable = v3)

e3.pack(side='bottom')
l3.pack(side='bottom')
BlankLabel3.pack(side = "bottom")
#repeat of previous function for a third button

l4 = Label(app, text="First Name")
BlankLabel4 = Label(app, text = " ")
v4 = StringVar()

e4 = Entry(app, textvariable = v4)

e4.pack(side='bottom')
l4.pack(side='bottom')
BlankLabel4.pack(side = "bottom")
#repeat of previous function to create a fourth button
app.mainloop()
#defines the section of code as the main loop
