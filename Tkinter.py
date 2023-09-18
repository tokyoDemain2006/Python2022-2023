from tkinter import *
def clicked():
    print("clicked")

app = Tk()
app.title("GUI Example 1")
app.geometry("200x200")
button1 = Button(app, text="click here", command = clicked)
button1.pack(side = "bottom")

app.mainloop()
