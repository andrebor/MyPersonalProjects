from tkinter import *

root = Tk()     #Window

topFrame = Frame(root)
topFrame.pack(side=TOP)
botFrame = Frame(root)
botFrame.pack(side=BOTTOM)

one = Label(root, text="one", bg="red", fg="white")
one.pack()
two = Label(root, text="one", bg="green", fg="black")
two.pack(fill=X)
three = Label(root, text="one", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(botFrame, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop() #Show window