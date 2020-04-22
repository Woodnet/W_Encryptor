from cryptography.fernet import Fernet
from cryptography.fernet import Fernet
from tkinter import filedialog as fd
from tkinter import *
import tkinter,os

root = Tk()
root.title("Woodnet-File_Decrypter")
root.geometry("600x600")
root.configure(bg="whitesmoke")
root.maxsize(600, 600)
root.minsize(600, 600)

def decrypt():
    keywithoutb = 'RbYgYV6ZsizkqQGGsL7oxLLUMauIxK9vwccOTOUIr_4='
    key = keywithoutb.encode()
    cipher = Fernet(key)
    filename = root.sourceFile
    with open(filename,'rb') as df:
        encrypted_data = df.read()
    decrypted_file = cipher.decrypt(encrypted_data)
    os.remove(filename)
    with open('%s'%(filename),'wb') as df:
        df.write(decrypted_file)
    decryptedlabel = Label(root,text="Die Datei wurde entschlüsselt!",fg="green",bg="whitesmoke",font="Arial 22")
    decryptedlabel.place(x=150,y=300)

title = Label(root,text="W-Decrypter",fg="black",bg="whitesmoke",font="Customized 44"
                ,borderwidth=4, relief="groove")
title.place(x=130,y=1)
versionlabel = Label(root,text="Version 1.2.0",fg="black",bg="whitesmoke",font="Arial 22")
versionlabel.place(x=100,y=80)
sourcefilelabel = Label(root,text="User is selecting File..",font="Arial 12").place(x=1,y=130)
root.sourceFile = filedialog.askopenfilename(parent=root, initialdir= "/",
                                            title='Please select the encrypted File')
presstoencrypt = Button(root,text="PRESS TO DECRYPT FILE",fg="black",font="Arial 20",
                        command=decrypt)
presstoencrypt.place(x=150,y=200)
sourcefilelabel = Label(root,text="File %s selected"%(root.sourceFile),font="Arial 15")
sourcefilelabel.place(x=1,y=200)
root.mainloop()
