#formality
from tkinter import *
obj=Tk()
obj.geometry("500x490+300+0")
obj.title("radio by for loop")
#making of radio button

#function
def disp():
    s=v.get()
    
    lab2=Label(text=s,font=11).pack(anchor=W)

#setting the variable

v=IntVar()

#creating the label
lab1=Label(text="select one option",font=20,padx=25,justify=LEFT).pack(anchor=W)

#using for loop
MainVariable=[('pyhton',1),('c',2),('ruby',3)]

for language,index in MainVariable:
    Radiobutton(obj,text=language,padx=20,variable=v,command=disp,val=index).pack(anchor=W)




obj.mainloop()
