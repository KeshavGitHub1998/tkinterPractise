from tkinter import *
#error solver , name error message box not defined
from tkinter import messagebox
#import sys
objmain=Tk()
objmain.title('list format')
objmain.geometry("500x500+100+0")

def mquit():
    messagebox.showinfo("Say hello")
    #mess=messagebox.askyesno(title="quit",message="sure?")
    #if mess==1:
        #objmain.destroy()

#creating list or menu list
mymenu = Menu()
listone=Menu()
listone.add_command(label="new file")
listone.add_command(label="open file")
listone.add_command(label="save file")
listone.add_command(label="quit",command=mquit)

listtwo=Menu()
listtwo.add_command(label="undo")
listtwo.add_command(label="redo")

listthree=Menu()
listthree.add_command(label="font")
listthree.add_command(label="color")



mymenu.add_cascade(label="File",menu=listone)
mymenu.add_cascade(label="Edit",menu=listtwo)
mymenu.add_cascade(label="Format",menu=listthree)
#mymenu.add_cascade(label="Run",menu=listfour)

objmain.config(menu=mymenu)

objmain.mainloop()
