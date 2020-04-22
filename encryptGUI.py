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
    encryptedlabel = Label(root,text="Die Datei wurde verschlüsselt!",fg="green",bg="white",font="Arial 25")
    encryptedlabel.place(x=60,y=400)

title = Label(root,text="W-Encrypter",fg="black",bg="whitesmoke",font="Customized 44"
                ,borderwidth=4, relief="groove")
title.place(x=130,y=1)
versionlabel = Label(root,text="Version 1.2.0",fg="black",bg="whitesmoke",font="Arial 22")
versionlabel.place(x=100,y=80)
sourcefilelabel = Label(root,text="User is selecting File..",font="Arial 12").place(x=1,y=130)
root.sourceFile = filedialog.askopenfilename(parent=root, initialdir= "/",
                                            title='Please select a File to encrypt!')
sourcefilelabel = Label(root,text="File %s selected"%(root.sourceFile),font="Arial 15").place(x=1,y=200)
presstoencrypt = Button(root,text="PRESS TO ENCRYPT FILE",fg="black",font="Arial 20",
                        command=encrypt)
presstoencrypt.place(x=100,y=288)
root.mainloop()
