# # Register with username and password, and print hashed PW to file.
# from tkinter import *
# from passlib.hash import pbkdf2_sha256
#
# window = Tk()
# window.title("Register Information")
#
#
# # changes window to a 300x300 pixel window.
# # window.geometry("300x300")
#
# # changes window icon to FILENAME.ico
# # window.wm_iconbitmap("FILENAME.ico")
#
# var = IntVar()
# showPW = "*"
# def login(event):
#     hash = pbkdf2_sha256.hash(ent_2.get())
#
# def switch():
#     if var.get():
#         showPW = str("")
#     else:
#         showPW = str("*")
#     return showPW
# print(showPW)
#
#
# lbl_1 = Label(window, text="Username:")
# lbl_2 = Label(window, text="Password:")
# ent_1 = Entry(window)
# ent_2 = Entry(window, show=showPW)
# btn_1 = Button(window, text="Register")
# chk_1 = Checkbutton(window, text="Show Password", variable=var, command=switch)
#
# ent_1.bind("<Return>", login)
# ent_2.bind("<Return>", login)
# btn_1.bind("<Button-1>", login)
#
# lbl_1.grid(row=0, sticky=E, padx=5, pady=5)
# lbl_2.grid(row=1, sticky=E, padx=5, pady=5)
# ent_1.grid(row=0, column=1, pady=5)
# ent_2.grid(row=1, column=1)
# btn_1.grid(row=3, column=0, pady=10)
# chk_1.grid(row=3, column=1, sticky=W, pady=10)
#
# window.mainloop()


from tkinter import Frame, Label, Entry, Button, Tk, E
from passlib.hash import pbkdf2_sha256
from os.path import isfile

class Reginfo(Frame):
    '''An application to register Username and Password'''
    def __init__(self, master):
        '''Start Frame'''
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()



    def create_widgets(self):
        # Labels
        Label(self, text="Username:").grid(row=0, sticky=E, padx=5, pady=5)
        Label(self, text="Password:").grid(row=1, sticky=E, padx=5, pady=5)

        # Text Entry
        global usn
        usn = Entry(self)
        usn.grid(row=0, column=1, pady=5)
        # self.hoho = Entry(self, show="*").grid(row=1, column=1)
        global pwd
        pwd = Entry(self, show="*")
        pwd.grid(row=1, column=1)

        # Register Button
        Button(self, text="Register", command=self.collectprint).grid(row=3, column=0, pady=10)

        # # Show PW checkbox
        # self.secure = BooleanVar()
        # Checkbutton(self, text="Show Password", variable=self.secure,
        # command=self.switch).grid(row=3, column=1, sticky=W, pady=10)


    # def switch(self):
    #
    #     if self.secure.get():
    #         self.hoho.config(show="")
    #     else:
    #         self.hoho.config(show="*")
    ## UNFINISHED, cant get show password to update entry settings.
    def collectprint(self):
        passhash = pbkdf2_sha256.hash(pwd.get())
        #if isfile()




root = Tk()
root.title("Register Information")
app = Reginfo(root)

root.mainloop()
