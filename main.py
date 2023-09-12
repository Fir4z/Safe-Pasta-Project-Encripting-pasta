from PIL import ImageTk
from tkinter import *
import PIL.Image

import os

def encrypytf():
    os.system("unlock.bat")

def dencrypytf():
    os.system("pass.bat")

def open():
    os.system("open.bat")



window = Tk()

def submit():
    Password = password.get()
    if Password == "b":
        crypt_b.config(state=NORMAL)
        decrypt_b.config(state=NORMAL)
        open_b.config(state=NORMAL)
    else:
        password.config(state=DISABLED)
def delete():
    password.delete(0,END)



window.title("Password")
window.config(background="#2e292c")

image = PIL.Image.open("img.png")
res = image.resize((100, 100))
photo = ImageTk.PhotoImage(res)


icon =  PhotoImage(file="img.png")
window.iconphoto(True,icon)



label = Label(window,
              text="Enter a Password",
              font=("Arial",20,"bold"),
              fg="#c9c7c9",
              bg="#2e292c",
              relief=RAISED,
              bd=10,
              padx= 10,
              pady=10,
              image= photo,
              compound="left")





label.pack()

password = Entry(window,
                 font=("Arial", 20, "bold"),
                 fg="#c9c7c9",
                 bg="#2e292c",
                 relief=RAISED,
                 bd=10,
                 show="*")

password.pack()

open_b = Button(window,
                text="Open!",
                font=("Arial", 20, "bold"),
                fg="#c9c7c9",
                bg="#2e292c",
                relief=RAISED,
                bd=10,
                padx=10,
                pady=10,
                command=open,
                state= DISABLED)
open_b.pack()


decrypt_b = Button(window,
                text="Decrypt!",
                font=("Arial", 20, "bold"),
                fg="#c9c7c9",
                bg="#2e292c",
                relief=RAISED,
                bd=10,
                padx=10,
                pady=10,
                command=dencrypytf,
                state= DISABLED)
decrypt_b.pack()

crypt_b = Button(window,
                text="Crypt!",
                font=("Arial", 20, "bold"),
                fg="#c9c7c9",
                bg="#2e292c",
                relief=RAISED,
                bd=10,
                padx=10,
                pady=10,
                command=encrypytf,
                state= DISABLED)
crypt_b.pack()


submit_b = Button(window,
                text="Submit!",
                font=("Arial", 20, "bold"),
                fg="#c9c7c9",
                bg="#2e292c",
                relief=RAISED,
                bd=10,
                padx=10,
                pady=10,
                command=submit)
submit_b.pack()

delete_b = Button(window,
                text="Delete!",
                font=("Arial", 20, "bold"),
                fg="#c9c7c9",
                bg="#2e292c",
                relief=RAISED,
                bd=10,
                padx=10,
                pady=10,
                command=delete)

delete_b.pack()
window.mainloop()