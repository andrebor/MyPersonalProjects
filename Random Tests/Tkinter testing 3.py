from tkinter import *

root = Tk()

def printName():
    print("Hello my name is Bucky")

button_1 = Button(root, text="Print my name", command=printName)
button_1.pack()

root.mainloop()

# def printName(event):
#     print("Hello my name is Bucky")
#
# button_1 = Button(root, text="Print my name")
# button_1.bind("<Button-1>", printName)
# button_1.pack()
#
# root.mainloop()