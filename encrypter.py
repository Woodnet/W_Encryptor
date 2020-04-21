from cryptography.fernet import Fernet
from tkinter import filedialog as fd
from tkinter import *
import tkinter,os

root = Tk()
root.title("Woodnet-File_Encrypter")
root.geometry("600x600")
root.configure(bg="whitesmoke")
root.maxsize(600, 600)
root.minsize(600, 600)
def encrypt():
    srcfile = root.sourceFile
    keywithoutb = 'RbYgYV6ZsizkqQGGsL7oxLLUMauIxK9vwccOTOUIr_4='
    key = keywithoutb.encode()
    cipher = Fernet(key)
    filename = root.sourceFile
    with open(filename,'rb') as f:
        e_file = f.read()
    encrypted_file = cipher.encrypt(e_file)
    os.remove("%s"%(filename))
    with open(filename,'wb') as ef:
        ef.write(encrypted_file)
    encryptedlabel = Label(root,text="File encrypted!",fg="green",bg="whitesmoke",font="Arial 22")
    encryptedlabel.place(x=150,y=300)

title = Label(root,text="W_Encrypter",fg="black",bg="whitesmoke",font="Arial 33 underline")
title.place(x=150,y=1)
root.sourceFile = filedialog.askopenfilename(parent=root, initialdir= "/",
                                                 title='Please select a directory')
sourcefilelabel = Label(root,text="File %s selected"%(root.sourceFile),font="Arial 15").place(x=1,y=100)
presstoencrypt = Button(root,text="Press to Encrypt File",fg="black",bg="whitesmoke",font="Arial 25",
                        command=encrypt)
presstoencrypt.place(x=150,y=200)
root.mainloop()
