# Notepad style application that can open, edit, and save text documents. Add syntax highlighting and other features.

from tkinter.filedialog import *
from tkinter.messagebox import *

filename = None


def newFile():
    global filename
    filename = "Untitled"
    text.delete(1.0, END)

def saveFile():
    global filename
    t = text.get(1.0, END)
    f = open(filename, "w")
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfile(mode="w", defaultextension=".txt")
    t = str(text.get(1.0, END))
    if f is None:
        return
    try:
        f.write(t)
    except:
        showerror(title="Oops!", message="Unable to save file...")

def openFile():
    f = askopenfile(mode="r")
    t = f.read()
    text.delete(1.0, END)
    text.insert(1.0, t)

def onClose():
    if askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


root = Tk()
root.title("PythonEDIT")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400)
text.grid(row=0, sticky=E)
text.pack()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0, )
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit())
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.protocol("WM_DELETE_WINDOW", onClose)
root.mainloop()
