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
    decryptedlabel = Label(root,text="File decrypted!",fg="green",bg="whitesmoke",font="Arial 22")
    decryptedlabel.place(x=150,y=300)
title = Label(root,text="W_Decrypter",fg="black",bg="whitesmoke",font="Arial 33 underline")
title.place(x=150,y=1)
root.sourceFile = filedialog.askopenfilename(parent=root, initialdir= "/",
                                                 title='Please select the encrypted File')
sourcefilelabel = Label(root,text="File %s selected"%(root.sourceFile),font="Arial 15").place(x=1,y=100)
presstoencrypt = Button(root,text="Press to Decrypt File",fg="black",bg="whitesmoke",font="Arial 25",
                        command=decrypt)
presstoencrypt.place(x=150,y=200)
root.mainloop()
