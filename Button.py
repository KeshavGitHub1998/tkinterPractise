from tkinter import *
aobject=Tk()
#creating object from tk class
aobject.title("NewMorning")
aobject.geometry("1000x5000+200+20")
LabA=Label(text="label1",fg='red').grid(row=3,column=2)
#creating a button
Abutton=Button(text="First").grid(row=3,column=0)
#same parameters as label
Bbutton=Button(text="Second",fg='blue').grid(row=1,column=2,sticky='w')




aobject.mainloop()
