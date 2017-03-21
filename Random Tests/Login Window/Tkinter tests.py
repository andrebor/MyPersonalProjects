from tkinter import *
from passlib.hash import pbkdf2_sha256

window = Tk()
window.title("Window name")

# changes window to a 300x300 pixel window.
# window.geometry("300x300")

# changes window icon to FILENAME.ico
# window.wm_iconbitmap("FILENAME.ico")

def login(event):
    hash = pbkdf2_sha256.hash(ent_2.get())


lbl_1 = Label(window, text="Username")
lbl_2 = Label(window, text="Password")
ent_1 = Entry(window)
ent_2 = Entry(window, show="*")
btn_1 = Button(window, text="Login")
chk_1 = Checkbutton(window, text="Keep me logged in")

ent_1.bind("<Return>", login)
ent_2.bind("<Return>", login)
btn_1.bind("<Button-1>", login)

lbl_1.grid(row=0, sticky=E)
lbl_2.grid(row=1, sticky=E)
ent_1.grid(row=0, column=1)
ent_2.grid(row=1, column=1)
btn_1.grid(row=2,columnspan=2)
chk_1.grid(row=3, columnspan=2, sticky=W)

window.mainloop()