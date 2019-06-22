from tkinter import *
from tkinter import messagebox
obj=Tk()
def cmd():
    lab=Label(text='check').pack()
     
def cmdd():
    messagebox.showinfo(obj, title='quit',font=24,message="sure") 

obj.title("message box")
obj.geometry("500x500+100+20")

    

but=Button(text="click me",font=('roman',20,'italic'),command="cmd")
but.pack()
but1=Button(text="quit button",font=('roman',20,'italic'),command="cmdd")
but1.pack()
lab12=Label(text='check').pack()


obj.mainloop()
