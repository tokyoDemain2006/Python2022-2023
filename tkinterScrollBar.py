import customtkinter, tkinter

root = customtkinter.CTk()
root.grid_rowconfigure(1, weight = 1)
root.grid_columnconfigure(1, weight = 1)

tk_textbox = tkinter.Text(root, highlightthickness = 1)
tk_textbox.grid(row = 0, column = 0, sticky = "nsew")

ctk_textbox_scrollbar = customtkinter.CTkScrollbar(root, command = tk_textbox.yview)
ctk_textbox_scrollbar.grid(row = 0, column = 1, sticky = "ns")

tk_textbox.configure(yscrollcommand = ctk_textbox_scrollbar.set)

root.mainloop()
