import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
label = tk.Label(text="Name")
entry = tk.Entry()
label.pack()
entry.pack()
name = entry.get()
name
print(name)
window = tk.Tk()
