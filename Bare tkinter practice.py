from tkinter import *
#use "pip install tk" to use tkinter
import customtkinter
#use "pip install customtkinter" to use custom tkinter
import webbrowser
import csv

def dialogBox():
    dialog = customtkinter.CTkInputDialog(text = "what website do you want to go to", title = "go to website")
    webbrowser.open_new_tab(dialog.get_input())

def openYoutube():
    webbrowser.open_new_tab("youtube.com")

def openTwitch():
    webbrowser.open_new_tab("twitch.com")

def openTeams():
    webbrowser.open_new_tab("teams.microsoft.com")

def comboBox_Callback(choice):
    if choice == "Middlesbro collage website":
        webbrowser.open_new_tab("https://www.mbro.ac.uk/")
    else:
        dialogBox()
    

root = customtkinter.CTk()
root.geometry("300x200")
customtkinter.set_appearance_mode("system")
root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 1)
combobox_var = customtkinter.StringVar(value = "option 1")
CustomURL = customtkinter.CTkButton(master = root, text = "Custom URL", command = dialogBox)
Youtube = customtkinter.CTkButton(master = root, text = "Open Youtube", command = openYoutube)
Twitch = customtkinter.CTkButton(master = root, text = "Open Twitch", command = openTwitch)
Teams = customtkinter.CTkButton(master = root, text = "Open Teams", command = openTeams)
combobox = customtkinter.CTkComboBox(master = root, values = ["Middlesbro collage website", "Enter custom url"], command = comboBox_Callback)
CustomURL.place(relx = 0.5, rely = 0.3, anchor = CENTER)
Youtube.place(relx = 0.75, rely = 0.5, anchor = CENTER)
Twitch.place(relx = 0.25, rely = 0.5, anchor = CENTER)
Teams.place(relx = 0.5, rely = 0.7, anchor = CENTER)
combobox.place(relx = 0.5, rely = 0.1, anchor = CENTER)
combobox.set("Choose Option")
root.mainloop()
