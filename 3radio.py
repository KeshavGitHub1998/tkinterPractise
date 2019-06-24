#formality
from tkinter import *
q=Tk()
q.title("radio with function")
q.geometry=("500x500+100+10")

#function
def disp():
    a=v.get()
    if (a==1):
        print("you chose python")
    elif (a==2):
        print("Perl")
    else:
        print("sorry choose a good language")

    
v=IntVar()

#label
lab1=Label(text="Choose a programming language",padx=20,justify=LEFT).pack(anchor=W)

#making radio button
r1=Radiobutton(text="Python",padx=20,command=disp,variable=v,value=1).pack(anchor=W)
r2=Radiobutton(text="Perl",padx=20,command=disp,variable=v,value=2).pack(anchor=W)
r3=Radiobutton(text="Ruby",padx=20,command=disp,variable=v,value=3).pack(anchor=W)
r4=Radiobutton(text="Java",padx=20,command=disp,variable=v,value=4).pack(anchor=W)






#ending
q.mainloop()
