from tkinter import *
objmain=Tk()
objmain.title("functioning of the menu")
objmain.geometry("500x600+100+0")

#defining the functions needed
def newfile():
    labfile=Label(text="clicked on new file",font=10).pack()
    return("")

lab1=Label(text='label1',font=20,bg='red',fg='black').pack()

#creating menu
#new object for menu
menuobj=Menu()


#list objects in menu
list1=Menu()
list1.add_command(label="New file",command=newfile)
list1.add_command(label="Open file")
list1.add_command(label="Save file")

list2=Menu()
list2.add_command(label="redo")
list2.add_command(label="undo")
 
list3=Menu()
list3.add_command(label="")
list3.add_command(label="")

#cascading the list
#pass (something) on to a succession of others.
menuobj.add_cascade(label='File',menu=list1)
menuobj.add_cascade(label='Edit',menu=list2)
menuobj.add_cascade(label='Format',menu=list3)

objmain.config(menu=menuobj)
objmain.mainloop()
