#formality and basic
from tkinter import *
obj=Tk()
obj.title('radio button 2')
obj.geometry("500x300+110+10")

#new thing known as justify for this also like webd
lab=Label(obj,text="Choose one language",font=10,padx=25,justify=LEFT).pack()

#it is same like entry case where a was the variable
v=IntVar()
#attention on typecasting method like StrVar and now IntVar


#setting the value
v.set(2)

#making the radio buttons
#values need not be in series , can be anythin , use like key 
r1=Radiobutton(obj,text="Python",padx=25,variable=v,value=1).pack(anchor=W)
r2=Radiobutton(obj,text="Ruby",padx=25,variable=v,value=2).pack(anchor=W)
r3=Radiobutton(obj,text="C",padx=25,variable=v,value=3).pack(anchor=W)
r4=Radiobutton(obj,text="C++",padx=25,variable=v,value=4).pack(anchor=W)


#ending mainloop
obj.mainloop()
